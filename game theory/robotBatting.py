"""
For Jane Street's Oct 2025 Puzzle
"""

import numpy as np
import pandas as pd

# ---------- Helpers ----------

def terminal_value(b, s):
    if b >= 4:   # walk
        return 1.0
    if s >= 3:   # strikeout
        return 0.0
    return None

def solve_2x2(a, b, c, d):
    """
    Payoff matrix for batter:
        [[a, b],   # row = Ball
         [c, d]]   # row = Strike
    Columns: Wait, Swing
    Returns: (value, pitcher_strike_prob, batter_swing_prob)
    """
    denom = a - b - c + d

    # Pure-strategy saddle check
    min_col1 = min(a, c)
    min_col2 = min(b, d)
    v_batter = max(min_col1, min_col2)
    max_row1 = max(a, b)
    max_row2 = max(c, d)
    v_pitcher = min(max_row1, max_row2)

    if v_batter >= v_pitcher:
        # Saddle in pure strategies
        if min_col1 >= min_col2:
            return min_col1, 0.0, 0.0   # pitcher: Ball, batter: Wait
        else:
            return min_col2, 0.0, 1.0   # pitcher: Ball, batter: Swing

    # Mixed strategy
    if abs(denom) < 1e-12:
        return v_pitcher, 0.0, 0.0
    p_ball = (d - c) / denom
    q_wait = (d - b) / denom
    if 0 <= p_ball <= 1 and 0 <= q_wait <= 1:
        val = (a*d - b*c) / denom
        return val, 1 - p_ball, 1 - q_wait  # return strike prob, swing prob
    return v_pitcher, 0.0, 0.0

# ---------- Dynamic Equilibrium ----------

def compute_equilibrium(p):
    V = np.zeros((5,4))
    x_strike = np.zeros((5,4))  # pitcher strike prob
    y_swing = np.zeros((5,4))   # batter swing prob

    for b in reversed(range(5)):
        for s in reversed(range(4)):
            t = terminal_value(b,s)
            if t is not None:
                V[b,s] = t
                continue

            # Payoff entries
            a = V[b+1,s]              # (Ball, Wait)
            b_ = V[b, s+1]            # (Ball, Swing)
            c = V[b, s+1]             # (Strike, Wait)
            d = p*4 + (1-p)*V[b,s+1]  # (Strike, Swing)

            val, x, y = solve_2x2(a, b_, c, d)
            V[b,s] = val
            x_strike[b,s] = x
            y_swing[b,s] = y
    return V, x_strike, y_swing

# ---------- Full-count probability ----------

def compute_F(p, xS, yH):
    F = np.zeros((5,4))
    for b in reversed(range(5)):
        for s in reversed(range(4)):
            if (b,s) == (3,2):
                F[b,s]=1; continue
            if b>=4 or s>=3:
                F[b,s]=0; continue
            x = xS[b,s]
            y = yH[b,s]
            # (B,W)
            F[b,s] += (1-x)*(1-y)*F[b+1,s]
            # (S,W)
            F[b,s] += x*(1-y)*(1 if (b,s+1)==(3,2) else F[b,s+1])
            # (B,H)
            F[b,s] += (1-x)*y*(1 if (b,s+1)==(3,2) else F[b,s+1])
            # (S,H) miss
            F[b,s] += x*y*(1-p)*(1 if (b,s+1)==(3,2) else F[b,s+1])
    return F

def q_of_p(p):
    V, xS, yH = compute_equilibrium(p)
    F = compute_F(p, xS, yH)
    return F[0,0]

# ---------- Main ----------

if __name__ == "__main__":
    # Sweep p
    ps = np.linspace(0.001, 0.999, 500)
    qs = [q_of_p(p) for p in ps]
    idx = int(np.argmax(qs))
    p_star, q_star = ps[idx], qs[idx]

    print(f"Optimal p ≈ {p_star:.6f}, Max q ≈ {q_star:.10f}")

    # Show strategies table at optimal p
    V, xS, yH = compute_equilibrium(p_star)
    F = compute_F(p_star, xS, yH)

    rows=[]
    for b in range(4):
        for s in range(3):
            rows.append({
                "State (b,s)": f"({b},{s})",
                "Pitcher Pr(Strike)": round(xS[b,s],4),
                "Batter Pr(Swing)": round(yH[b,s],4),
                "Value V(b,s)": round(V[b,s],4),
                "Full-count prob from (b,s)": round(F[b,s],4)
            })

    df = pd.DataFrame(rows)
    print("\nEquilibrium strategies at optimal p:")
    print(df.to_string(index=False))
