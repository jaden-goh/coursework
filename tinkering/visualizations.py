
from __future__ import annotations

import os
import math
from dataclasses import dataclass
from typing import Callable, Dict, Tuple, Optional, List, Sequence


import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio


# -----------------------------
# 1) Color palettes
# -----------------------------
def make_palette(name: str = "viridis", n: int = 5) -> np.ndarray:
    """
    Returns an (n,4) RGBA palette sampled from a matplotlib colormap.
    """
    cmap = plt.get_cmap(name)
    xs = np.linspace(0.1, 0.95, n)
    return cmap(xs)

PALETTE_LIBRARY: Dict[str, Callable[[int], np.ndarray]] = {
    # matplotlib colormaps (sampled)
    "viridis": lambda n: make_palette("viridis", n),
    "plasma": lambda n: make_palette("plasma", n),
    "magma": lambda n: make_palette("magma", n),
    "inferno": lambda n: make_palette("inferno", n),
    "cividis": lambda n: make_palette("cividis", n),
    "turbo": lambda n: make_palette("turbo", n),
    "twilight": lambda n: make_palette("twilight", n),
    "hsv": lambda n: make_palette("hsv", n),
    "Spectral": lambda n: make_palette("Spectral", n),
    "coolwarm": lambda n: make_palette("coolwarm", n),
    "cubehelix": lambda n: make_palette("cubehelix", n),

    # custom palettes (hand-picked RGBA)
    "neon_cmyk": lambda n: np.array([
        (0.00, 0.90, 1.00, 1.0),  # cyan
        (1.00, 0.00, 0.80, 1.0),  # magenta-ish
        (1.00, 0.95, 0.00, 1.0),  # yellow
        (1.00, 0.40, 0.00, 1.0),  # orange
        (0.60, 0.00, 1.00, 1.0),  # purple
    ][:n] if n <= 5 else make_palette("hsv", n)),

    "electric": lambda n: np.array([
        (0.05, 0.80, 1.00, 1.0),
        (0.10, 1.00, 0.60, 1.0),
        (0.95, 1.00, 0.10, 1.0),
        (1.00, 0.45, 0.10, 1.0),
        (0.95, 0.10, 0.90, 1.0),
        (0.65, 0.15, 1.00, 1.0),
    ][:n] if n <= 6 else make_palette("turbo", n)),

    "sunset": lambda n: np.array([
        (0.10, 0.05, 0.30, 1.0),
        (0.45, 0.10, 0.55, 1.0),
        (0.85, 0.25, 0.30, 1.0),
        (1.00, 0.55, 0.15, 1.0),
        (1.00, 0.85, 0.25, 1.0),
    ][:n] if n <= 5 else make_palette("magma", n)),

    "mintberry": lambda n: np.array([
        (0.10, 0.95, 0.75, 1.0),
        (0.15, 0.70, 1.00, 1.0),
        (0.35, 0.35, 1.00, 1.0),
        (0.85, 0.25, 0.90, 1.0),
        (1.00, 0.40, 0.35, 1.0),
    ][:n] if n <= 5 else make_palette("Spectral", n)),
}

def get_palette_names() -> List[str]:
    return list(PALETTE_LIBRARY.keys())

def pick_random_palette_name(rng: np.random.Generator, exclude: Sequence[str] = ()) -> str:
    names = [n for n in get_palette_names() if n not in set(exclude)]
    if not names:
        names = get_palette_names()
    return names[int(rng.integers(0, len(names)))]

def make_palette_from_library(name: str, bins: int) -> np.ndarray:
    if name not in PALETTE_LIBRARY:
        # fallback to matplotlib colormap lookup
        return make_palette(name, bins)
    pal = PALETTE_LIBRARY[name](bins)
    # Ensure shape is (bins, 4)
    if pal.shape[0] != bins:
        # if a custom palette has fewer colors, resample via hsv fallback
        pal = make_palette("hsv", bins)
    if pal.shape[1] != 4:
        # add alpha
        alpha = np.ones((pal.shape[0], 1), dtype=pal.dtype)
        pal = np.concatenate([pal, alpha], axis=1)
    return pal

# -----------------------------
# 2) Input functions
# -----------------------------
DotFunc = Callable[[np.random.Generator, int, float], Tuple[np.ndarray, np.ndarray, np.ndarray]]

def preset_superellipse(a=1.0, b=1.0, m=4.0, noise=0.02, wobble=0.35) -> DotFunc:
    """
    Superellipse (squircle-ish). m=2 -> ellipse, m>2 -> squarer.
    """
    def f(rng: np.random.Generator, N: int, t: float):
        th = rng.uniform(0, 2*np.pi, N)
        # Oscillate exponent to get "breathing" square/circle feel
        mm = m + wobble * math.sin(2*np.pi*t)
        ct, st = np.cos(th), np.sin(th)

        x = a * np.sign(ct) * (np.abs(ct) ** (2.0 / mm))
        y = b * np.sign(st) * (np.abs(st) ** (2.0 / mm))

        x += rng.normal(0, noise, N)
        y += rng.normal(0, noise, N)

        # Color by angle + time
        c = (th / (2*np.pi) + t) % 1.0
        return x, y, c
    return f

def preset_lissajous(ax=1.0, ay=1.0, fx=3, fy=2, phase=0.0, noise=0.02, wobble=0.8) -> DotFunc:
    """
    Lissajous curve (looping figure). Great for "oval" motifs.
    """
    def f(rng: np.random.Generator, N: int, t: float):
        u = rng.uniform(0, 2*np.pi, N)
        ph = phase + wobble * math.sin(2*np.pi*t)
        x = ax * np.sin(fx*u + ph)
        y = ay * np.sin(fy*u)
        x += rng.normal(0, noise, N)
        y += rng.normal(0, noise, N)
        c = (u/(2*np.pi) + 0.5*t) % 1.0
        return x, y, c
    return f

def preset_line(angle=0.0, length=1.6, thickness=0.02, noise=0.01, spin=1.0) -> DotFunc:
    """
    A rotating line segment (like the diagonal sticks in your image).
    """
    def f(rng: np.random.Generator, N: int, t: float):
        ang = angle + 2*np.pi*spin*t
        s = rng.uniform(-length/2, length/2, N)
        # thickness around the line
        off = rng.normal(0, thickness, N)

        ca, sa = math.cos(ang), math.sin(ang)
        # base point on line + perpendicular offset
        x = s*ca - off*sa
        y = s*sa + off*ca

        x += rng.normal(0, noise, N)
        y += rng.normal(0, noise, N)

        c = (s/length + 0.5 + t) % 1.0
        return x, y, c
    return f

def preset_ring(r=1.0, thickness=0.06, noise=0.01, wobble=0.15) -> DotFunc:
    """
    Noisy ring / donut (like the circles/ovals).
    """
    def f(rng: np.random.Generator, N: int, t: float):
        th = rng.uniform(0, 2*np.pi, N)
        rr = r + wobble*math.sin(2*np.pi*t) + rng.normal(0, thickness, N)
        x = rr*np.cos(th)
        y = 0.75*rr*np.sin(th)  # squash -> oval
        x += rng.normal(0, noise, N)
        y += rng.normal(0, noise, N)
        c = (th/(2*np.pi) + 0.25*t) % 1.0
        return x, y, c
    return f

def make_animation(
    dot_func: DotFunc,
    *,
    out_dir: str = "frames",
    gif_path: str = "oscillation.gif",
    frames: int = 120,
    loop: bool = True,
    seed: int = 0,
    fps: int = 30,
    palette_name: str = "viridis",      # can be "random"
    palette_bins: int = 6,
    palette_exclude: Sequence[str] = (),
    **render_kwargs,
) -> None:
    os.makedirs(out_dir, exist_ok=True)

    # Pick ONE palette for this entire gif
    if palette_name == "random":
        prng = np.random.default_rng(seed ^ (id(dot_func) & 0xFFFFFFFF))
        chosen_palette = pick_random_palette_name(prng, exclude=palette_exclude)
    else:
        chosen_palette = palette_name

    print(f"[{gif_path}] using palette: {chosen_palette}")

    ts = np.linspace(0, 1, frames, endpoint=False)
    png_paths = []

    for i, t in enumerate(ts):
        png_path = os.path.join(out_dir, f"frame_{i:04d}.png")

        render_frame(
            dot_func,
            float(t),
            seed=seed + i,                 # randomness can drift for dots
            out_path=png_path,
            palette_name=chosen_palette,   # <-- constant across frames
            palette_bins=palette_bins,
            **render_kwargs,
        )
        png_paths.append(png_path)

    imgs = [imageio.imread(p) for p in png_paths]
    if loop:
        imgs = imgs + imgs[::-1][1:-1]

    imageio.mimsave(gif_path, imgs, fps=fps)
    print(f"Saved {len(png_paths)} PNG frames to '{out_dir}/' and GIF to '{gif_path}'")

def render_frame(
    dot_func: DotFunc,
    t: float,
    *,
    seed: int,
    N: int = 2200,
    palette_name: str = "viridis",   # now always a concrete name
    palette_bins: int = 5,
    out_path: Optional[str] = None,
    dpi: int = 200,
    size_px: int = 900,
    dot_size: float = 2.0,
    alpha: float = 0.9,
    background: str = "black",
    xlim: Tuple[float, float] = (-1.35, 1.35),
    ylim: Tuple[float, float] = (-1.0, 1.0),
) -> None:
    if out_path is None:
        raise ValueError("render_frame requires out_path (a PNG filename).")

    rng = np.random.default_rng(seed)

    x, y, c = dot_func(rng, N, t)

    palette = make_palette_from_library(palette_name, palette_bins)
    idx = np.floor((c % 1.0) * palette_bins).astype(int)
    idx = np.clip(idx, 0, palette_bins - 1)
    colors = palette[idx]

    fig = plt.figure(figsize=(size_px / dpi, size_px / dpi), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    fig.patch.set_facecolor(background)
    ax.set_facecolor(background)

    ax.scatter(x, y, s=dot_size, c=colors, alpha=alpha, linewidths=0)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

    fig.savefig(out_path, dpi=dpi, facecolor=background, bbox_inches="tight", pad_inches=0)
    plt.close(fig)

def preset_spirograph(
    R: float = 1.0,
    r: float = 0.33,
    d: float = 0.75,
    noise: float = 0.01,
    wobble: float = 0.15,
) -> DotFunc:
    """
    Hypotrochoid / spirograph-like curves.
    Animate by wobbling parameters with time.
    """
    def f(rng, N, t):
        u = rng.uniform(0, 2*np.pi, N)
        rr = r + wobble * math.sin(2*np.pi*t)
        dd = d + 0.25*wobble * math.cos(2*np.pi*t)

        k = (R - rr) / rr
        x = (R - rr) * np.cos(u) + dd * np.cos(k * u)
        y = (R - rr) * np.sin(u) - dd * np.sin(k * u)

        # scale to about [-1,1]
        s = np.percentile(np.sqrt(x*x + y*y), 99)
        x = x / (s + 1e-9)
        y = y / (s + 1e-9)

        x += rng.normal(0, noise, N)
        y += rng.normal(0, noise, N)

        c = (u/(2*np.pi) + t) % 1.0
        return x, y, c
    return f

def preset_phyllotaxis(
    turns: float = 8.0,
    jitter: float = 0.01,
    spin: float = 1.0,
    golden: bool = True,
) -> DotFunc:
    """
    Sunflower / phyllotaxis spiral.
    Looks amazing with rotation + color by radius.
    """
    def f(rng, N, t):
        i = np.arange(N, dtype=np.float32)
        if golden:
            angle = i * (np.pi * (3 - np.sqrt(5)))  # golden angle
        else:
            angle = i * (2*np.pi/turns)

        r = np.sqrt(i / (N + 1e-9))
        # rotate over time
        ang = angle + 2*np.pi*spin*t

        x = r * np.cos(ang)
        y = r * np.sin(ang)

        x += rng.normal(0, jitter, N)
        y += rng.normal(0, jitter, N)

        c = (r + 0.5*t) % 1.0
        return x, y, c
    return f

def preset_interference(
    k1: float = 9.0,
    k2: float = 13.0,
    k3: float = 17.0,
    threshold: float = 0.25,
    noise: float = 0.004,
    drift: float = 1.0,
) -> DotFunc:
    """
    Moiré / interference “field thresholding”.
    We sample random points and keep those near a level set.
    Creates floating cellular / wave patterns.
    """
    def f(rng, N, t):
        # oversample then filter
        M = int(N * 3.5)
        x = rng.uniform(-1.2, 1.2, M)
        y = rng.uniform(-1.2, 1.2, M)

        phase = 2*np.pi*drift*t
        val = (
            np.sin(k1*x + phase) +
            np.sin(k2*y - 0.7*phase) +
            np.sin(k3*(x+y) + 0.3*phase)
        ) / 3.0

        # keep points close to 0 level set (like contour dots)
        keep = np.abs(val) < threshold
        x, y, val = x[keep], y[keep], val[keep]

        if len(x) < N:
            # if too strict, relax a bit
            idx = np.argsort(np.abs(val))[:N]
        else:
            idx = rng.choice(len(x), size=N, replace=False)

        x, y, val = x[idx], y[idx], val[idx]
        x += rng.normal(0, noise, N)
        y += rng.normal(0, noise, N)

        # color by val
        c = (val - val.min()) / (val.max() - val.min() + 1e-9)
        return x, y, c
    return f

def preset_kaleidoscope_rosette(
    petals: int = 7,
    rings: int = 3,
    noise: float = 0.01,
    pulse: float = 0.25,
    spin: float = 0.6,
) -> DotFunc:
    """
    Symmetric rosette via polar mapping + kaleidoscope fold.
    Very "pattern tile" friendly.
    """
    def f(rng, N, t):
        th = rng.uniform(0, 2*np.pi, N)
        rr = rng.uniform(0.0, 1.0, N)

        # fold angle into a wedge then mirror -> kaleidoscope
        wedge = 2*np.pi / petals
        th_fold = np.mod(th, wedge)
        mirror = (np.floor(th / wedge) % 2).astype(bool)
        th_k = np.where(mirror, wedge - th_fold, th_fold)

        # rosette radius modulation
        rr2 = rr * (0.6 + 0.4*np.sin(rings*th_k + 2*np.pi*spin*t))
        rr2 *= 1.0 + pulse * np.sin(2*np.pi*t)

        x = rr2 * np.cos(th_k)
        y = rr2 * np.sin(th_k)

        x += rng.normal(0, noise, N)
        y += rng.normal(0, noise, N)

        c = (th_k / wedge + t) % 1.0
        return x, y, c
    return f

def preset_torus_projection(
    R: float = 1.0,
    r: float = 0.35,
    spin_u: float = 1.0,
    spin_v: float = 0.7,
    tilt: float = 0.9,
    noise: float = 0.004,
) -> DotFunc:
    """
    TRUE 3D surface (torus) sampled in 3D, then projected to 2D with a rotating camera.
    This is a real 3D object -> 2D projection.
    """
    def f(rng, N, t):
        u = rng.uniform(0, 2*np.pi, N)
        v = rng.uniform(0, 2*np.pi, N)

        # torus in 3D
        x3 = (R + r*np.cos(v)) * np.cos(u)
        y3 = (R + r*np.cos(v)) * np.sin(u)
        z3 = r*np.sin(v)

        # rotate camera over time
        au = 2*np.pi*spin_u*t
        av = 2*np.pi*spin_v*t
        cu, su = np.cos(au), np.sin(au)
        cv, sv = np.cos(av), np.sin(av)

        # rotate around z (u-spin)
        x1 = x3*cu - y3*su
        y1 = x3*su + y3*cu
        z1 = z3

        # rotate around x (v-spin)
        y2 = y1*cv - z1*sv
        z2 = y1*sv + z1*cv
        x2 = x1

        # tilt around y
        ct, st = np.cos(tilt), np.sin(tilt)
        x3r = x2*ct + z2*st
        z3r = -x2*st + z2*ct
        y3r = y2

        # perspective projection
        dist = 3.0
        px = x3r / (dist - z3r)
        py = y3r / (dist - z3r)

        # normalize scale
        s = np.percentile(np.sqrt(px*px + py*py), 99)
        px = px / (s + 1e-9)
        py = py / (s + 1e-9)

        px += rng.normal(0, noise, N)
        py += rng.normal(0, noise, N)

        # color by depth (z)
        c = (z3r - z3r.min()) / (z3r.max() - z3r.min() + 1e-9)
        return px, py, c
    return f

def preset_mandelbrot_edge(
    max_iter: int = 80,
    edge_band: Tuple[float, float] = (0.45, 0.55),
    zoom: float = 1.0,
    pan_x: float = -0.5,
    pan_y: float = 0.0,
    drift: float = 0.6,
    noise: float = 0.003,
) -> DotFunc:
    """
    Dotty Mandelbrot "edge" sampler:
    - sample points in the complex plane
    - keep those whose normalized escape iteration is within edge_band
    Great for a shimmering fractal boundary.
    """
    def f(rng, N, t):
        M = int(N * 5.0)
        # animate zoom slightly (gentle breathing)
        zf = zoom * (0.9 + 0.2*np.sin(2*np.pi*drift*t))
        x = rng.uniform(-2.2, 1.2, M) / zf + pan_x
        y = rng.uniform(-1.6, 1.6, M) / zf + pan_y

        cplx = x + 1j*y
        z = np.zeros_like(cplx)
        esc = np.zeros(M, dtype=np.float32)

        mask = np.ones(M, dtype=bool)
        for k in range(max_iter):
            z[mask] = z[mask]*z[mask] + cplx[mask]
            escaped = np.abs(z) > 2.0
            newly = escaped & mask
            esc[newly] = k
            mask &= ~escaped
            if not mask.any():
                break

        esc = esc / max_iter
        lo, hi = edge_band
        keep = (esc >= lo) & (esc <= hi)

        xk, yk, ek = x[keep], y[keep], esc[keep]
        if len(xk) < N:
            # relax if too few
            idx = np.argsort(np.abs(ek - 0.5))[:N]
        else:
            idx = rng.choice(len(xk), size=N, replace=False)

        xk, yk, ek = xk[idx], yk[idx], ek[idx]

        # map to view coords ~[-1,1]
        # (these bounds match the sampling ranges)
        x2 = (xk - pan_x) * zf / 1.7
        y2 = (yk - pan_y) * zf / 1.7

        x2 += rng.normal(0, noise, N)
        y2 += rng.normal(0, noise, N)

        c = (ek + t) % 1.0
        return x2, y2, c
    return f

def preset_lorenz(
    sigma: float = 10.0,
    rho: float = 28.0,
    beta: float = 8.0 / 3.0,
    dt: float = 0.005,
    warmup_steps: int = 5000,
    # how much the "window" slides through the attractor over time:
    slide: int = 800,
    # how many steps between sampled points (controls density / "stringiness")
    stride: int = 2,
    noise: float = 0.002,
    wobble: float = 2.0,
) -> DotFunc:
    """
    Lorenz attractor dots:
    - Precomputes a long Lorenz trajectory.
    - Each frame picks a moving window (based on t) of points from that trajectory.
    - Colors by normalized z (height), which looks very 'grokking-y'.

    Tip: increase stride for more separated dots, decrease for smoother ribbons.
    """

    def rk4_step(x, y, z, sig, r, b, h):
        # dx/dt = sigma (y - x)
        # dy/dt = x (rho - z) - y
        # dz/dt = x y - beta z
        def f(xx, yy, zz):
            dx = sig * (yy - xx)
            dy = xx * (r - zz) - yy
            dz = xx * yy - b * zz
            return dx, dy, dz

        k1 = f(x, y, z)
        k2 = f(x + 0.5*h*k1[0], y + 0.5*h*k1[1], z + 0.5*h*k1[2])
        k3 = f(x + 0.5*h*k2[0], y + 0.5*h*k2[1], z + 0.5*h*k2[2])
        k4 = f(x + h*k3[0],     y + h*k3[1],     z + h*k3[2])

        x2 = x + (h/6.0)*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
        y2 = y + (h/6.0)*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
        z2 = z + (h/6.0)*(k1[2] + 2*k2[2] + 2*k3[2] + k4[2])
        return x2, y2, z2

    # Precompute trajectory ONCE (closure state)
    # We'll compute enough points to support sliding windows.
    # N points requested per frame -> we need at least warmup + frames*slide + N*stride,
    # but we don't know frames here. So we compute a generous buffer.
    base_len = 250000  # you can raise if you make very long gifs
    traj = np.zeros((base_len, 3), dtype=np.float32)

    # initial condition (non-zero so it moves)
    x, y, z = 0.1, 0.0, 0.0

    # warmup to get onto the attractor
    for _ in range(warmup_steps):
        x, y, z = rk4_step(x, y, z, sigma, rho, beta, dt)

    for i in range(base_len):
        # wobble rho over time to create gentle "breathing" changes
        # (still Lorenz-like but adds life)
        rr = rho + wobble * math.sin(2 * math.pi * (i / base_len))
        x, y, z = rk4_step(x, y, z, sigma, rr, beta, dt)
        traj[i] = (x, y, z)

    # Normalize for plotting nicely (Lorenz is not naturally in [-1,1])
    # We'll scale x/y using robust percentiles so outliers don't dominate.
    xs, ys, zs = traj[:, 0], traj[:, 1], traj[:, 2]
    sx = np.percentile(np.abs(xs), 99)
    sy = np.percentile(np.abs(ys), 99)
    # z is for color; keep range for normalization
    zmin, zmax = np.percentile(zs, 1), np.percentile(zs, 99)

    def f(rng: np.random.Generator, N: int, t: float):
        # sliding window start index
        start = int((t % 1.0) * (len(traj) - (N * stride) - 1))
        start = max(0, min(start, len(traj) - (N * stride) - 1))

        idx = start + np.arange(N) * stride
        pts = traj[idx]

        # project to 2D: (x, y) (classic butterfly), then scale to ~[-1,1]
        x2 = pts[:, 0] / (sx + 1e-9)
        y2 = pts[:, 1] / (sy + 1e-9)

        # small jitter so it looks like "confetti dots"
        x2 += rng.normal(0, noise, N)
        y2 += rng.normal(0, noise, N)

        # color by normalized z
        c = (pts[:, 2] - zmin) / (zmax - zmin + 1e-9)
        c = np.clip(c, 0.0, 1.0)

        return x2, y2, c

    return f

def preset_clifford(
    a: float = -1.4,
    b: float = 1.6,
    c: float = 1.0,
    d: float = 0.7,
    warmup: int = 500,
    stride: int = 2,
    jitter: float = 0.0015,
    wobble: float = 0.15,
    rotate: float = 1.0,
) -> DotFunc:
    """
    Clifford (strange) attractor.
    It's technically a 2D map, but it *feels* very 3D when you rotate the 2D projection over time
    and color by a "pseudo-depth" signal.

    Map:
      x_{n+1} = sin(a*y_n) + c*cos(a*x_n)
      y_{n+1} = sin(b*x_n) + d*cos(b*y_n)

    We:
    - iterate a long trajectory,
    - take a sliding window for each frame,
    - rotate the points as a function of time,
    - color by a pseudo-depth = x*cos(phi)+y*sin(phi).
    """
    base_len = 250000
    traj = np.zeros((base_len, 2), dtype=np.float32)

    x, y = 0.1, 0.1

    # warmup
    for _ in range(warmup):
        x, y = math.sin(a * y) + c * math.cos(a * x), math.sin(b * x) + d * math.cos(b * y)

    # precompute (with gentle parameter wobble across the whole stored trajectory)
    for i in range(base_len):
        tt = i / base_len
        aa = a + wobble * math.sin(2 * math.pi * tt)
        bb = b + wobble * math.cos(2 * math.pi * tt)
        x, y = math.sin(aa * y) + c * math.cos(aa * x), math.sin(bb * x) + d * math.cos(bb * y)
        traj[i] = (x, y)

    # robust scale to ~[-1,1]
    xs, ys = traj[:, 0], traj[:, 1]
    sx = np.percentile(np.abs(xs), 99)
    sy = np.percentile(np.abs(ys), 99)

    def f(rng: np.random.Generator, N: int, t: float):
        start = int((t % 1.0) * (len(traj) - (N * stride) - 1))
        start = max(0, min(start, len(traj) - (N * stride) - 1))

        idx = start + np.arange(N) * stride
        pts = traj[idx].astype(np.float32)

        x2 = pts[:, 0] / (sx + 1e-9)
        y2 = pts[:, 1] / (sy + 1e-9)

        # rotate projection over time (gives a strong "3D orbiting" vibe)
        ang = 2 * math.pi * rotate * t
        ca, sa = math.cos(ang), math.sin(ang)
        xr = x2 * ca - y2 * sa
        yr = x2 * sa + y2 * ca

        # pseudo-depth for coloring (before jitter)
        depth = (x2 * ca + y2 * sa)
        depth = (depth - depth.min()) / (depth.max() - depth.min() + 1e-9)

        # add tiny jitter for that dotty texture
        xr += rng.normal(0, jitter, N)
        yr += rng.normal(0, jitter, N)

        return xr, yr, depth

    return f


PRESETS: Dict[str, DotFunc] = {
    "squircle": preset_superellipse(m=5.0),
    "ellipse": preset_superellipse(m=2.0, b=0.7),
    "lissajous": preset_lissajous(fx=3, fy=2),
    "ring": preset_ring(),
    "line": preset_line(angle=np.pi/6),
    "clifford": preset_clifford(),
    "lorenz": preset_lorenz(),
    "spirograph": preset_spirograph(),
    "phyllotaxis": preset_phyllotaxis(),
    "interference": preset_interference(),
    "rosette": preset_kaleidoscope_rosette(),
    "torus3d": preset_torus_projection(),
    "mandelbrot_edge": preset_mandelbrot_edge(),
}

# -----------------------------
# 5) Example usage
# -----------------------------
if __name__ == "__main__":
    RUN = {
        "clifford": True,
        "torus3d": True,
        "interference": True,
        "phyllotaxis": True,
        "spirograph": True,
        "rosette": True,
        "mandelbrot_edge": True,
    }

    common = dict(
        N=2600,
        palette_name="random",     # <-- randomize palette
        palette_bins=6,
        # palette_per_frame=True,  # <-- uncomment for chaos mode (palette changes every frame)
        dot_size=2.0,
        alpha=0.95,
        size_px=900,
        dpi=200,
        xlim=(-1.35, 1.35),
        ylim=(-1.05, 1.05),
    )

    for name, on in RUN.items():
        if not on:
            continue
        make_animation(
            PRESETS[name],
            out_dir=f"frames_{name}",
            gif_path=f"{name}.gif",
            frames=120,
            fps=30,
            seed=10,
            **common,
        )