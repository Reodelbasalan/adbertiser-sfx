"""Tiny DSP kit for the Adbertiser SFX pack: pure numpy/scipy synthesis, no samples."""
import numpy as np
from scipy import signal
from scipy.ndimage import uniform_filter1d

SR = 48000
REG = []
_r = np.random.default_rng(0)


def reseed(n):
    global _r
    _r = np.random.default_rng(n)


def rnd(a=0.0, b=1.0, size=None):
    return _r.uniform(a, b, size)


def rint(a, b):
    return int(_r.integers(a, b))


def add(cat, name, desc, tags, fn, **kw):
    REG.append(dict(cat=cat, name=name, desc=desc, tags=list(tags), fn=fn, kw=kw))


def sfx(cat, name, desc, tags=()):
    def deco(fn):
        add(cat, name, desc, tags, fn)
        return fn
    return deco


# ---------- time + pitch ----------
def N(d):
    return max(1, int(round(d * SR)))


def T(d):
    return np.arange(N(d)) / SR


def U(d):  # 0..1 across the sound
    return np.arange(N(d)) / N(d)


def ramp(a, b, d, p=1.0):
    return a + (b - a) * U(d) ** p


def geo(a, b, d):
    return a * (b / a) ** U(d)


def mf(m):
    return 440.0 * 2 ** ((m - 69) / 12)


_NOTE = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}


def nf(s):
    k, i = _NOTE[s[0]], 1
    if s[1] in '#b':
        k += 1 if s[1] == '#' else -1
        i = 2
    return mf(12 * (int(s[i:]) + 1) + k)


def _arr(v, n):
    v = np.asarray(v, float)
    return np.full(n, float(v)) if v.ndim == 0 else np.resize(v, n)


def _f(f, d):
    return _arr(f, N(d))


# ---------- sources ----------
def white(d):
    return _r.uniform(-1, 1, N(d))


def colored(d, slope):
    n = N(d)
    X = np.fft.rfft(_r.standard_normal(n))
    f = np.fft.rfftfreq(n, 1 / SR)
    f = np.maximum(f, 30.0)  # flat below 30 Hz so energy stays audible
    x = np.fft.irfft(X / f ** (slope / 2), n)
    return x / (np.max(np.abs(x)) + 1e-12)


def pink(d):
    return colored(d, 1)


def brown(d):
    return colored(d, 2)


def ph(f, d):
    return 2 * np.pi * np.cumsum(_f(f, d)) / SR


def sine(f, d, p0=0.0):
    return np.sin(ph(f, d) + p0)


def tri(f, d):
    p = (ph(f, d) / (2 * np.pi)) % 1
    return 2 * np.abs(2 * p - 1) - 1


def saw(f, d):
    p = (ph(f, d) / (2 * np.pi)) % 1
    return 2 * p - 1


def sq(f, d, duty=0.5):
    p = (ph(f, d) / (2 * np.pi)) % 1
    return np.where(p < duty, 1.0, -1.0)


def fm(fc, fmod, idx, d):
    return np.sin(ph(fc, d) + _f(idx, d) * np.sin(ph(fmod, d)))


OSC = dict(sine=sine, tri=tri, saw=saw, sq=sq)


# ---------- envelopes ----------
def dec(d, k, a=0.0):
    t = T(d)
    e = np.exp(-k * np.maximum(t - a, 0))
    if a > 0:
        e *= np.clip(t / a, 0, 1)
    return e


def swell(d, peak=0.5, p1=2.0, p2=2.0):
    u = U(d)
    return np.where(u < peak, (u / peak) ** p1, np.clip((1 - u) / (1 - peak), 0, 1) ** p2)


def gate(d, a=0.003, r=0.02):
    n = N(d)
    e = np.ones(n)
    na, nr = min(N(a), n), min(N(r), n)
    e[:na] *= np.linspace(0, 1, na)
    e[n - nr:] *= np.linspace(1, 0, nr)
    return e


def trem(d, rate, depth=1.0):
    return 1 - depth * (0.5 + 0.5 * np.sin(ph(rate, d)))


def wander(d, rate, lo, hi):
    n = N(d)
    k = max(3, int(d * rate) + 3)
    pts = _r.uniform(lo, hi, k)
    xs = np.linspace(0, n, k)
    y = np.interp(np.arange(n), xs, pts)
    w = max(1, N(0.5 / max(rate, 0.1)))
    return uniform_filter1d(y, w, mode='nearest') if w < n else y


# ---------- filters ----------
def _sos(x, sos):
    return signal.sosfilt(sos, x, axis=-1)


def lp(x, f, o=2):
    return _sos(x, signal.butter(o, min(f, SR * 0.45), 'low', fs=SR, output='sos'))


def hp(x, f, o=2):
    return _sos(x, signal.butter(o, max(f, 10), 'high', fs=SR, output='sos'))


def bp(x, f, q=1.0, o=2):
    bw = f / q
    lo, hi = max(15, f - bw / 2), min(SR * 0.45, f + bw / 2)
    return _sos(x, signal.butter(o, [lo, hi], 'band', fs=SR, output='sos'))


def sweep(x, kind, f, q=0.8, blk=128):
    """Time-varying RBJ biquad (lp/hp/bp), coefficients updated every blk samples."""
    if x.ndim == 2:
        return np.stack([sweep(c, kind, f, q, blk) for c in x])
    n = len(x)
    f, q = _arr(f, n), _arr(q, n)
    y, zi = np.empty(n), np.zeros(2)
    for i in range(0, n, blk):
        w = 2 * np.pi * min(max(f[i], 20), SR * 0.45) / SR
        c, s = np.cos(w), np.sin(w)
        al = s / (2 * q[i])
        if kind == 'lp':
            b = [(1 - c) / 2, 1 - c, (1 - c) / 2]
        elif kind == 'hp':
            b = [(1 + c) / 2, -(1 + c), (1 + c) / 2]
        else:
            b = [al, 0, -al]
        a0 = 1 + al
        y[i:i + blk], zi = signal.lfilter(np.array(b) / a0, np.array([a0, -2 * c, 1 - al]) / a0, x[i:i + blk], zi=zi)
    return y


def comb(x, delay_s, amt=0.8):
    n = len(x)
    idx = np.arange(n) - _arr(delay_s, n) * SR
    return x + amt * np.interp(idx, np.arange(n), x, left=0)


# ---------- effects ----------
def drive(x, a):
    return np.tanh(a * x) / np.tanh(a)


def crush(x, bits=6, ds=8):
    y = np.repeat(x[..., ::ds], ds, axis=-1)[..., :x.shape[-1]]
    q = 2 ** (bits - 1)
    return np.round(y * q) / q


def stereo(x):
    return x if x.ndim == 2 else np.stack([x, x])


def pan(x, p):
    if x.ndim == 2:
        x = x.mean(0)
    a = (_arr(p, len(x)) + 1) * np.pi / 4
    return np.stack([x * np.cos(a), x * np.sin(a)]) * 1.4142


def wide(fn, *a, **k):
    """Call a noise-based generator twice (different random draws) for a wide stereo pair."""
    return np.stack([fn(*a, **k), fn(*a, **k)])


def verb(x, rt=1.0, mix=0.25, bright=7000, pre=0.012):
    x = stereo(x)
    n = N(rt * 1.3)
    t = np.arange(n) / SR
    wet = []
    for c in x:
        ir = _r.standard_normal(n) * np.exp(-6.9 * t / rt)
        ir[:N(pre)] = 0
        ir = lp(ir, bright)
        ir /= np.sqrt(np.sum(ir ** 2)) + 1e-12
        wet.append(signal.fftconvolve(c, ir))
    wet = np.stack(wet)
    dry = np.pad(x, ((0, 0), (0, wet.shape[1] - x.shape[1])))
    return dry + mix * wet


def rev(x):
    return x[..., ::-1].copy()


def mixat(ev):
    """ev: list of (t_seconds, signal[, gain]); mono+stereo mixed -> stereo."""
    ev = [(e[0], e[1], e[2] if len(e) > 2 else 1.0) for e in ev]
    st = any(s.ndim == 2 for _, s, _ in ev)
    n = max(int(round(t * SR)) + s.shape[-1] for t, s, _ in ev)
    out = np.zeros((2, n)) if st else np.zeros(n)
    for t, s, g in ev:
        s = stereo(s) if st else s
        i = int(round(t * SR))
        out[..., i:i + s.shape[-1]] += g * s
    return out


def mix(*sigs):
    return mixat([(0, s) for s in sigs])


def echo(x, t=0.18, fb=0.45, n=4, pp=True):
    ev = [(0, x)]
    for i in range(1, n + 1):
        s = x * fb ** i
        ev.append((t * i, pan(s, 0.6 if i % 2 else -0.6) if pp else s))
    return mixat(ev)


def seq(x, times, gains=None, jitter=0.0):
    return mixat([(t + (rnd(-jitter, jitter) if jitter else 0), x if not callable(x) else x(),
                   1 if gains is None else gains[i]) for i, t in enumerate(times)])


# ---------- instruments ----------
def beep(f, d, w='sine', a=0.003, r=0.015):
    return OSC[w](f, d) * gate(d, a, r)


def bell(f, d=1.2, ratios=(1, 2.76, 5.4, 8.93), amps=(1, .45, .25, .12), k=3.0, ks=1.8):
    s = np.zeros(N(d))
    for i, (r, a) in enumerate(zip(ratios, amps)):
        if f * r < SR * 0.45:
            s += a * sine(f * r, d) * dec(d, k * (1 + ks * i), 0.0008)
    return s


def marimba(f, d=0.5, k=7):
    return sine(f, d) * dec(d, k, 0.002) + 0.25 * sine(4 * f, d) * dec(d, k * 3.5, 0.001) \
        + 0.08 * sine(min(9.9 * f, 20000), d) * dec(d, 60)


def pluck(f, d=1.0, damp=0.996, bright=0.6):
    n, L = N(d), max(2, int(SR / f))
    x = np.zeros(n)
    x[:L] = lp(_r.uniform(-1, 1, L), 1500 + bright * 10000)
    a = np.zeros(L + 2)
    a[0], a[L], a[L + 1] = 1, -damp / 2, -damp / 2
    return signal.lfilter([1], a, x)


def metal(f, d=1.0, k=3.0, n=6, spread=0.15):
    base = [1, 1.47, 2.09, 2.56, 3.37, 4.18, 5.21, 6.4][:n]
    s = np.zeros(N(d))
    for i, r in enumerate(base):
        fr = f * r * (1 + rnd(-spread, spread) * 0.1)
        if fr < SR * 0.45:
            s += (0.85 ** i) * sine(fr, d, rnd(0, 6.28)) * dec(d, k * (1 + 0.35 * i), 0.0005)
    return s


def nburst(d, lo=200, hi=8000, k=30, a=0.0):
    return lp(hp(white(d), lo), hi) * dec(d, k, a)


def click(f=3000, d=0.04, k=250, q=2.0):
    return bp(white(d), f, q) * dec(d, k) + 0.4 * sine(f, d) * dec(d, k * 1.4)


def kick(d=0.5, f0=150, f1=45, kp=30, ka=7, clk=0.3):
    f = f1 + (f0 - f1) * np.exp(-T(d) * kp)
    return sine(f, d) * dec(d, ka, 0.001) + clk * hp(white(d), 2500) * dec(d, 300)


def snare(d=0.35, f=190, tone=0.5, k=14, bright=5000):
    return tone * sine(geo(f * 1.3, f, d), d) * dec(d, k * 1.6, 0.001) + bp(white(d), bright, 0.8) * dec(d, k, 0.0008)


def clap(d=0.4, f=1300, k=18):
    ev = [(i * 0.011, bp(white(0.02), f, 1.2) * dec(0.02, 160)) for i in range(3)]
    ev.append((0.033, bp(white(d), f, 1.0) * dec(d, k)))
    return mixat(ev)


def hat(d=0.08, k=60, f=8000):
    r = [205.3, 304.4, 369.6, 522.7, 540.0, 800.0]
    s = sum(sq(x * 1.6, d) for x in r) / 6
    return hp(bp(s + 0.5 * white(d), f, 0.9), 6000) * dec(d, k, 0.0005)


def brass(f, d, bright=3000, det=0.004, vib=0.0):
    fr = _f(f, d) * (1 + vib * np.sin(ph(5.5, d)) * np.clip(T(d) / 0.3, 0, 1))
    s = (saw(fr, d) + saw(fr * (1 + det), d) + saw(fr * (1 - det), d)) / 3
    cut = 300 + bright * (1 - np.exp(-T(d) * 25)) * (0.6 + 0.4 * np.exp(-T(d) * 3))
    return drive(sweep(s, 'lp', cut, 0.9), 1.5) * gate(d, 0.02, 0.08)


def pad(freqs, d, cut=1400, det=0.006):
    s = np.zeros(N(d))
    for f in freqs:
        for k in (-1, 0, 1):
            s += saw(f * (1 + k * det), d, ) / (3 * len(freqs))
    return lp(s, cut) * swell(d, 0.35, 1.5, 1.2)


def chip(notes, w='sq', duty=0.5, gap=0.0, k=0.0):
    """notes: list of (freq_or_name, dur). 8-bit melody."""
    ev, t = [], 0.0
    for f, d in notes:
        f = nf(f) if isinstance(f, str) else f
        s = (sq(f, d, duty) if w == 'sq' else OSC[w](f, d)) * gate(d, 0.001, 0.008)
        if k:
            s *= dec(d, k)
        ev.append((t, s))
        t += d + gap
    return lp(mixat(ev), 9000)


def mel(notes, inst, step=None):
    """notes: list of (t, freq_or_name, dur)."""
    return mixat([(t, inst(nf(f) if isinstance(f, str) else f, d)) for t, f, d in notes])


def crackle(d, dens=0.15, lo=1500, hi=7000, blk=0.0015):
    nb = max(1, int(d / blk))
    m = (rnd(0, 1, nb) < dens) * rnd(0.2, 1, nb)
    m = np.repeat(m, N(blk))[:N(d)]
    m = np.pad(m, (0, N(d) - len(m)))
    return lp(hp(white(d) * m, lo), hi)


def pulses(times, kernel, d):
    x = np.zeros(N(d) + len(kernel))
    for t in times:
        i = int(t * SR)
        if i < N(d):
            x[i:i + len(kernel)] += kernel * rnd(0.6, 1)
    return x[:N(d)]
