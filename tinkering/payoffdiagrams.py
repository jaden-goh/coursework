import numpy as np
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Options Payoff Visualizer", layout="wide")

# ----------------------------
# Payoff helpers (at expiry)
# ----------------------------
def call_payoff(S, K, premium):
    return np.maximum(S - K, 0.0) - premium

def put_payoff(S, K, premium):
    return np.maximum(K - S, 0.0) - premium

def make_price_grid(center, width_frac=0.6, n=800):
    lo = max(0.01, center * (1.0 - width_frac))
    hi = center * (1.0 + width_frac)
    return np.linspace(lo, hi, n)

def find_breakevens(S, payoff, tol=1e-6):
    # Find sign changes and approximate roots by linear interpolation
    y = payoff
    sign = np.sign(y)
    sign[np.abs(y) < tol] = 0

    idx = np.where(sign[:-1] * sign[1:] < 0)[0]  # sign change
    bes = []
    for i in idx:
        x0, x1 = S[i], S[i+1]
        y0, y1 = y[i], y[i+1]
        if y1 == y0:
            continue
        x_root = x0 - y0 * (x1 - x0) / (y1 - y0)
        bes.append(float(x_root))

    # Also include points where payoff is ~0 exactly
    near0 = np.where(np.abs(y) < tol)[0]
    for i in near0:
        bes.append(float(S[i]))

    # Deduplicate (within small epsilon) and sort
    bes = sorted(bes)
    cleaned = []
    for b in bes:
        if not cleaned or abs(b - cleaned[-1]) > 1e-3:
            cleaned.append(b)
    return cleaned

def max_gain_loss(payoff):
    max_gain = np.max(payoff)
    max_loss = np.min(payoff)
    return float(max_gain), float(max_loss)

def format_money(x):
    return f"{x:,.2f}"

# ----------------------------
# UI
# ----------------------------
st.title("Local Options Payoff Visualizer (Expiry)")

left, right = st.columns([0.38, 0.62], gap="large")

with left:
    st.subheader("Position Builder")

    option_type = st.selectbox(
        "Strategy",
        ["Single", "Straddle", "Strangle", "Vertical Spread", "Butterfly"],
        index=0,
    )

    side = st.radio("Side", ["Buy (Long)", "Sell (Short)"], horizontal=True)
    side_mult = 1.0 if side.startswith("Buy") else -1.0

    st.divider()

    # Common inputs
    spot = st.number_input("Reference spot price (for chart range)", min_value=0.01, value=100.0, step=1.0)
    width = st.slider("Chart width (% around spot)", min_value=10, max_value=200, value=60, step=5)
    S = make_price_grid(spot, width_frac=width/100.0, n=900)

    st.divider()
    st.caption("Premiums are per 1 contract/share unit (keep consistent).")

    legs = []  # each leg: (type, K, premium, qty)

    if option_type == "Single":
        cp = st.selectbox("Option", ["Call", "Put"])
        K = st.slider("Strike K", min_value=1.0, max_value=float(max(2.0, spot*2)), value=float(spot), step=0.5)
        premium = st.number_input("Premium", min_value=0.0, value=2.0, step=0.1)
        qty = st.number_input("Quantity", value=1, step=1)

        legs.append((cp, K, premium, qty))

    elif option_type == "Straddle":
        # Long/Short straddle: call + put same strike
        K = st.slider("Strike K", min_value=1.0, max_value=float(max(2.0, spot*2)), value=float(spot), step=0.5)
        call_prem = st.number_input("Call premium", min_value=0.0, value=2.0, step=0.1)
        put_prem = st.number_input("Put premium", min_value=0.0, value=2.0, step=0.1)
        qty = st.number_input("Quantity (per leg)", value=1, step=1)

        legs += [("Call", K, call_prem, qty), ("Put", K, put_prem, qty)]

    elif option_type == "Strangle":
        K_put = st.slider("Put strike Kp", min_value=1.0, max_value=float(max(2.0, spot*2)), value=float(spot*0.95), step=0.5)
        K_call = st.slider("Call strike Kc", min_value=1.0, max_value=float(max(2.0, spot*2)), value=float(spot*1.05), step=0.5)

        put_prem = st.number_input("Put premium", min_value=0.0, value=2.0, step=0.1)
        call_prem = st.number_input("Call premium", min_value=0.0, value=2.0, step=0.1)
        qty = st.number_input("Quantity (per leg)", value=1, step=1)

        legs += [("Put", K_put, put_prem, qty), ("Call", K_call, call_prem, qty)]

    elif option_type == "Vertical Spread":
        spread_kind = st.selectbox("Spread kind", ["Bull Call (debit)", "Bear Put (debit)"])
        qty = st.number_input("Quantity (per leg)", value=1, step=1)

        if spread_kind.startswith("Bull Call"):
            K1 = st.slider("Lower strike K1 (buy call)", min_value=1.0, max_value=float(max(2.0, spot*2)), value=float(spot*0.95), step=0.5)
            K2 = st.slider("Higher strike K2 (sell call)", min_value=1.0, max_value=float(max(2.0, spot*2)), value=float(spot*1.05), step=0.5)
            prem1 = st.number_input("Premium for buy call (K1)", min_value=0.0, value=3.0, step=0.1)
            prem2 = st.number_input("Premium for sell call (K2)", min_value=0.0, value=1.5, step=0.1)

            # base structure = long call K1, short call K2
            legs += [("Call", K1, prem1, +qty), ("Call", K2, prem2, -qty)]

        else:
            K1 = st.slider("Higher strike K1 (buy put)", min_value=1.0, max_value=float(max(2.0, spot*2)), value=float(spot*1.05), step=0.5)
            K2 = st.slider("Lower strike K2 (sell put)", min_value=1.0, max_value=float(max(2.0, spot*2)), value=float(spot*0.95), step=0.5)
            prem1 = st.number_input("Premium for buy put (K1)", min_value=0.0, value=3.0, step=0.1)
            prem2 = st.number_input("Premium for sell put (K2)", min_value=0.0, value=1.5, step=0.1)

            # base structure = long put K1, short put K2
            legs += [("Put", K1, prem1, +qty), ("Put", K2, prem2, -qty)]

    elif option_type == "Butterfly":
        # Default: call butterfly (debit): +1 K1 call, -2 K2 call, +1 K3 call
        butterfly_kind = st.selectbox("Butterfly kind", ["Call Butterfly", "Put Butterfly"])
        qty = st.number_input("Quantity (base unit)", value=1, step=1)

        K2 = st.slider("Middle strike K2", min_value=1.0, max_value=float(max(2.0, spot*2)), value=float(spot), step=0.5)
        wing = st.slider("Wing width (K2±wing)", min_value=0.5, max_value=float(max(1.0, spot)), value=5.0, step=0.5)
        K1, K3 = K2 - wing, K2 + wing

        prem1 = st.number_input("Premium @ K1", min_value=0.0, value=4.0, step=0.1)
        prem2 = st.number_input("Premium @ K2", min_value=0.0, value=2.5, step=0.1)
        prem3 = st.number_input("Premium @ K3", min_value=0.0, value=1.2, step=0.1)

        opt = "Call" if butterfly_kind.startswith("Call") else "Put"
        legs += [(opt, K1, prem1, +qty), (opt, K2, prem2, -2*qty), (opt, K3, prem3, +qty)]

# ----------------------------
# Compute total payoff
# ----------------------------
total = np.zeros_like(S)
for opt_type, K, prem, q in legs:
    if opt_type == "Call":
        total += q * call_payoff(S, K, prem)
    else:
        total += q * put_payoff(S, K, prem)

# Apply Buy/Sell switch to the whole structure
total *= side_mult

# Breakevens + max gain/loss
bes = find_breakevens(S, total)
mg, ml = max_gain_loss(total)

# Detect "infinite" cases (very basic heuristic):
# if payoff keeps increasing at right edge => infinite gain; decreasing => infinite loss, similarly left edge.
right_slope = total[-1] - total[-50]
left_slope = total[50] - total[0]
inf_gain = False
inf_loss = False

# If strongly trending at edge, call it infinite
if right_slope > 1e-3:
    inf_gain = True
if right_slope < -1e-3:
    inf_loss = True
if left_slope < -1e-3:
    inf_gain = True  # for puts on left tail
if left_slope > 1e-3:
    inf_loss = True

# For many common strategies this works fine; you can refine later by analyzing legs.
max_gain_str = "∞" if inf_gain else format_money(mg)
max_loss_str = "∞" if inf_loss else format_money(ml)

# ----------------------------
# Plot
# ----------------------------
with right:
    st.subheader("Payoff Diagram")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=S, y=total, mode="lines", name="Payoff"))

    # Zero line
    fig.add_hline(y=0, line_dash="dash")

    # Breakeven lines
    for b in bes[:6]:  # keep it tidy
        fig.add_vline(x=b, line_dash="dot")

    fig.update_layout(
        height=520,
        xaxis_title="Underlying Price at Expiry",
        yaxis_title="Profit / Loss",
        margin=dict(l=30, r=30, t=40, b=30),
        hovermode="x unified",
    )

    st.plotly_chart(fig, use_container_width=True)

    # Stats
    st.markdown("### Key Metrics")
    c1, c2, c3 = st.columns(3)

    c1.metric("Max Gain", max_gain_str)
    c2.metric("Max Loss", max_loss_str)
    if bes:
        c3.write("**Breakeven(s):**")
        c3.write(", ".join([format_money(x) for x in bes[:6]]))
        if len(bes) > 6:
            c3.write("(more omitted)")
    else:
        c3.write("**Breakeven(s):** none in chart range")

    # Show legs
    st.markdown("### Legs")
    for opt_type, K, prem, q in legs:
        signed_q = q * side_mult
        direction = "Long" if signed_q > 0 else "Short"
        st.write(f"- {direction} {abs(int(signed_q))}× {opt_type} @ K={format_money(K)} (premium={format_money(prem)})")
