"""Whooshes, swishes, transitions, risers."""
from functools import partial
from dsp import *


def whoosh(d=0.5, f0=500, fpk=2500, f1=700, q=1.2, peak=0.55, p1=2.2, p2=1.6, low=0.0,
           st=0.35, panf=None, rt=0.0, wet=0.0, tone=0.0):
    u = U(d)
    fc = np.where(u < peak, f0 * (fpk / f0) ** (u / peak), fpk * (f1 / fpk) ** ((u - peak) / (1 - peak)))
    n0 = white(d)
    nz = np.stack([n0 * (1 - st) + white(d) * st, n0 * (1 - st) + white(d) * st])
    x = sweep(sweep(nz, 'bp', fc, q), 'lp', fc * 2.5, 0.7) * swell(d, peak, p1, p2)
    if tone:
        x = x + tone * sine(fc * 0.5, d) * swell(d, peak, p1, p2)
    if low:
        x = mix(x, low * lp(brown(d), 220) * swell(d, peak, 2, 1.4))
    if panf:
        x = pan(x, ramp(panf[0], panf[1], d))
    if wet:
        x = verb(x, rt, wet)
    return x


W = 'whoosh'
for i, (d, f0, fpk, f1, q) in enumerate([(0.3, 600, 3200, 900, 1.3), (0.34, 500, 3800, 800, 1.1),
                                          (0.38, 700, 2600, 700, 1.5), (0.25, 900, 4600, 1200, 1.2)], 1):
    add(W, f'whoosh_fast_{i}', 'Quick air pass for fast cuts', ['fast', 'cut', 'transition'],
        partial(whoosh, d, f0, fpk, f1, q))
for i, (d, fpk, pk) in enumerate([(0.7, 1300, 0.55), (0.85, 950, 0.6), (0.6, 1700, 0.5)], 1):
    add(W, f'whoosh_soft_{i}', 'Gentle, smooth whoosh', ['soft', 'smooth', 'calm'],
        partial(whoosh, d, 300, fpk, 400, 0.8, pk, 2.0, 1.8))
for i, (d, fpk, rt) in enumerate([(0.9, 1900, 1.2), (1.1, 1500, 1.5), (1.3, 2300, 1.8)], 1):
    add(W, f'whoosh_big_{i}', 'Heavy, wide whoosh with low end and tail', ['big', 'heavy', 'cinematic'],
        partial(whoosh, d, 250, fpk, 300, 1.0, 0.6, 2.4, 1.3, 0.8, 0.5, None, rt, 0.25))
for i, d in enumerate([0.8, 1.0], 1):
    add(W, f'whoosh_low_{i}', 'Deep rumbling pass', ['low', 'deep', 'bass'],
        partial(whoosh, d, 120, 520, 140, 1.1, 0.55, 2, 1.6, 1.0, 0.3, None, 0.8, 0.15))
for i, (d, fpk) in enumerate([(0.5, 6500), (0.6, 5200)], 1):
    add(W, f'whoosh_air_{i}', 'Bright airy whoosh', ['air', 'bright', 'light'],
        partial(whoosh, d, 1500, fpk, 2000, 0.7, 0.5, 2, 2))
for i, pf in enumerate([(-1, 1), (1, -1)], 1):
    add(W, f'whoosh_flyby_{i}', 'Fly-by that pans across the stereo field', ['flyby', 'pan', 'pass'],
        partial(whoosh, 0.95, 1400, 3200, 450, 1.3, 0.45, 2.0, 1.4, 0.3, 0.0, pf, 0.6, 0.12, 0.25))


@sfx(W, 'whoosh_double', 'Two quick passes back to back', ['double', 'fast'])
def _():
    return mixat([(0, whoosh(0.28, 700, 3400, 900, 1.3)), (0.17, whoosh(0.3, 600, 2800, 800, 1.3), 0.9)])


def whoosh_reverse(d=1.0, fpk=2600, rt=1.2):
    x = verb(whoosh(d * 0.5, 400, fpk, 700, 1.0, 0.3, 1.5, 2.5, 0.3), rt, 0.6)
    return rev(x)


for i, (d, fpk, rt) in enumerate([(0.9, 2600, 1.0), (1.2, 1800, 1.6)], 1):
    add(W, f'whoosh_reverse_{i}', 'Reverse swell that sucks into the cut', ['reverse', 'swell', 'build'],
        partial(whoosh_reverse, d, fpk, rt))


@sfx(W, 'whoosh_sweep_up', 'Whoosh that rises in pitch', ['rise', 'up'])
def _():
    return whoosh(0.7, 300, 5000, 6000, 1.6, 0.8, 1.6, 1.0, 0.0, 0.3, None, 0.5, 0.15, 0.2)


S = 'swish'
for i, (d, f0, f1) in enumerate([(0.14, 1500, 6000), (0.17, 1200, 5000), (0.12, 2000, 7500)], 1):
    def _whip(d=d, f0=f0, f1=f1, i=i):
        x = sweep(white(d), 'bp', geo(f0, f1, d), 1.6) * swell(d, 0.75, 3, 0.8)
        if i == 3:
            x = mixat([(0, x), (d * 0.9, click(4200, 0.03, 300), 0.8)])
        return x
    add(S, f'swish_whip_{i}', 'Very fast whip swish', ['whip', 'fast', 'snap'], _whip)
for i, d in enumerate([0.35, 0.5], 1):
    def _cloth(d=d):
        return lp(hp(white(d), 300), 3500) * trem(d, wander(d, 6, 15, 40), 0.5) * swell(d, 0.45, 1.5, 1.5)
    add(S, f'swish_cloth_{i}', 'Fabric / jacket swish', ['cloth', 'fabric', 'foley'], _cloth)
for i in (1, 2):
    def _sword(i=i):
        d = 0.32
        x = sweep(white(d), 'bp', np.where(U(d) < 0.6, geo(1800, 5200, d), 5200 * (1 - 0.4 * U(d))), 7) * swell(d, 0.6, 2.5, 1.2)
        if i == 2:
            ring = metal(2600, 1.2, 2.5)
            return mixat([(0, x), (0.18, ring, 0.35)])
        return x
    add(S, f'swish_sword_{i}', 'Sharp blade slice' + (' with metal ring' if i == 2 else ''), ['sword', 'slice', 'blade'], _sword)


@sfx(S, 'swish_stick', 'Thin stick swing with a whistle', ['stick', 'swing', 'whistle'])
def _():
    d = 0.3
    f = geo(400, 950, d)
    return (sweep(white(d), 'bp', f * 3, 4) + 0.3 * sine(f * 2, d)) * swell(d, 0.6, 2, 1.2)


TR = 'transition'
for i, (pf, f1) in enumerate([((-0.8, 0.8), 5000), ((0.8, -0.8), 4200), ((0, 0), 6500)], 1):
    def _swipe(pf=pf, f1=f1):
        d = 0.2
        x = sweep(white(d), 'bp', geo(1800, f1, d), 1.4) * swell(d, 0.6, 2, 1.5)
        return pan(x, ramp(pf[0], pf[1], d))
    add(TR, f'swipe_{i}', 'Phone-style screen swipe', ['swipe', 'ui', 'phone'], _swipe)


def slide(up=True):
    d = 0.38
    f = geo(320, 950, d) if up else geo(950, 320, d)
    return mix(0.5 * (sine(f, d) + 0.3 * tri(f * 2, d)) * swell(d, 0.5, 1.5, 1.5),
               whoosh(d, 500, 2200, 600, 1.0, 0.5) * 0.7)


add(TR, 'slide_in', 'Smooth slide in (rising)', ['slide', 'in', 'ui'], partial(slide, True))
add(TR, 'slide_out', 'Smooth slide out (falling)', ['slide', 'out', 'ui'], partial(slide, False))


def zoom(up=True, d=0.55, k=0):
    f = geo(150, 1600, d) if up else geo(1600, 120, d)
    s = lp(saw(f, d) + saw(f * 1.007, d), 2500) * 0.35
    n = sweep(white(d), 'bp', f * 2.5, 1.2)
    env = swell(d, 0.85 if up else 0.12, 2.2, 1.0 if up else 0.6, ) if True else 1
    x = (s + n) * env
    if k:
        x = mixat([(0, x), (d * (0.92 if up else 0.0), click(2400, 0.05, 160), 0.5)])
    return verb(x, 0.6, 0.15)


add(TR, 'zoom_in_1', 'Rising zoom-in sweep', ['zoom', 'in', 'rise'], partial(zoom, True, 0.55, 0))
add(TR, 'zoom_in_2', 'Zoom-in sweep that ends on a click', ['zoom', 'in', 'click'], partial(zoom, True, 0.4, 1))
add(TR, 'zoom_out_1', 'Falling zoom-out sweep', ['zoom', 'out', 'fall'], partial(zoom, False, 0.55, 0))
add(TR, 'zoom_out_2', 'Short zoom-out sweep', ['zoom', 'out'], partial(zoom, False, 0.35, 1))


def whoosh_hit(d=0.35, f0=120, heavy=1.0):
    w = whoosh(d, 500, 3000, 2500, 1.1, 0.95, 2.2, 0.5)
    h = mix(kick(0.8, f0, 40, 25, 6, 0.5) * heavy, 0.4 * nburst(0.3, 300, 5000, 25))
    return verb(mixat([(0, w, 0.8), (d * 0.95, h)]), 1.0, 0.2)


for i, (d, f0, hv) in enumerate([(0.35, 130, 1.0), (0.5, 100, 1.3), (0.25, 160, 0.8)], 1):
    add(TR, f'whoosh_hit_{i}', 'Whoosh that lands on a hit', ['whoosh', 'hit', 'impact', 'transition'],
        partial(whoosh_hit, d, f0, hv))


def glide(up=True):
    d = 0.6
    f = geo(400, 1200, d) if up else geo(1200, 400, d)
    x = (sine(f, d) + sine(f * 1.005, d) + 0.3 * tri(f * 2, d)) * swell(d, 0.5, 1.4, 1.6)
    return verb(x, 0.8, 0.25)


add(TR, 'glide_up', 'Soft tonal glide up', ['glide', 'up', 'smooth'], partial(glide, True))
add(TR, 'glide_down', 'Soft tonal glide down', ['glide', 'down', 'smooth'], partial(glide, False))


@sfx(TR, 'warp', 'Jet / flanger warp transition', ['warp', 'jet', 'flanger'])
def _():
    d = 1.0
    x = comb(comb(white(d), ramp(0.008, 0.0006, d, 0.7), 0.9), ramp(0.004, 0.0003, d, 0.7), 0.9)
    return verb(pan(lp(x, 7000) * swell(d, 0.6, 1.6, 1.4), ramp(-0.5, 0.5, d)), 0.7, 0.15)


@sfx(TR, 'spin', 'Spinning whoosh with a rotating flutter', ['spin', 'rotate', 'flutter'])
def _():
    d = 0.8
    x = whoosh(d, 400, 2400, 600, 1.0, 0.5).mean(0) * trem(d, ramp(8, 22, d), 0.8)
    return pan(x, 0.7 * np.sin(ph(ramp(3, 8, d), d)))


@sfx(TR, 'swoosh_tape', 'Tape-stop style downward swoosh', ['tape', 'stop', 'down'])
def _():
    d = 0.6
    f = 220 * (1 - U(d)) ** 1.5 + 20
    return lp(saw(f, d) + saw(f * 1.5, d) * 0.5, 2500) * swell(d, 0.05, 1, 0.8) * 0.5 + 0.0


@sfx(TR, 'swoosh_rise', 'Short rising swoosh into the next shot', ['rise', 'swoosh', 'up'])
def _():
    return whoosh(0.5, 300, 4500, 4500, 1.2, 0.92, 2.5, 0.5)


R = 'riser'


def riser(d=1.2, f0=200, f1=900, nz=0.7, tone=0.35, tr=(0, 0), rt=0.0):
    u = U(d)
    n = sweep(sweep(wide(white, d), 'hp', geo(300, 6000, d), 0.8), 'bp', geo(600, 9000, d), 0.7)
    f = geo(f0, f1, d)
    t = sweep(saw(f, d) + saw(f * 1.005, d) + 0.6 * saw(f * 1.5, d), 'lp', 400 + 6000 * u ** 2, 0.7) * 0.4
    x = mix(nz * n, tone * t) * u ** 2
    if tr[1]:
        x = x * trem(d, ramp(tr[0], tr[1], d), 0.6)
    return verb(x, rt, 0.2) if rt else x


add(R, 'riser_short_1', 'One-second build into a cut', ['riser', 'build', 'short'], partial(riser, 1.0))
add(R, 'riser_short_2', '1.5 s build with pulse', ['riser', 'build', 'pulse'], partial(riser, 1.5, 250, 1100, 0.6, 0.45, (4, 16)))
add(R, 'riser_long_1', 'Three-second tension build', ['riser', 'long', 'tension'], partial(riser, 3.0, 110, 880, 0.6, 0.5, (2, 18), 1.2))
add(R, 'riser_long_2', 'Four-second big build', ['riser', 'long', 'epic'], partial(riser, 4.0, 80, 1000, 0.7, 0.55, (1, 24), 1.5))
for i, d in enumerate([2.0, 3.0], 1):
    add(R, f'riser_noise_{i}', 'Pure white-noise sweep up', ['riser', 'noise', 'sweep'],
        lambda d=d: verb(sweep(wide(white, d), 'bp', geo(400, 9000, d), 1.0) * U(d) ** 1.8, 1.0, 0.2))


def riser_tonal(d=2.0, root=220):
    f = geo(1, 2, d)
    x = sum((sine(root * r * f * (1 + 0.004 * U(d) * np.sin(ph(ramp(4, 9, d), d))), d) + 0.4 * tri(root * r * f, d)) for r in (1, 1.25, 1.5))
    return verb(x * U(d) ** 1.6, 1.0, 0.3)


add(R, 'riser_tonal_1', 'Major chord rising an octave', ['riser', 'tonal', 'chord'], partial(riser_tonal, 2.0, 220))
add(R, 'riser_tonal_2', 'Bright tonal rise', ['riser', 'tonal', 'bright'], partial(riser_tonal, 1.5, 330))


def cymbal(d=2.0):
    return hp(mix(lp(white(d), 12000) * 0.7, metal(420, d, 1.0, 8, 0.6) * 0.5), 2500) * dec(d, 2.0, 0.002)


for i, d in enumerate([1.5, 2.5], 1):
    add(R, f'swell_reverse_{i}', 'Reverse cymbal swell', ['reverse', 'cymbal', 'swell'],
        lambda d=d: rev(verb(cymbal(d), d * 0.5, 0.35)))


def downlifter(d=1.5):
    n = sweep(wide(white, d), 'lp', geo(9000, 200, d), 0.9)
    s = sine(geo(700, 50, d), d) * 0.5
    return verb(mix(n, s) * dec(d, 2.5 / d, 0.005), 1.2, 0.25)


add(R, 'downlifter_1', 'Falling sweep after a drop', ['downlifter', 'fall', 'down'], partial(downlifter, 1.5))
add(R, 'downlifter_2', 'Long falling sweep', ['downlifter', 'fall', 'long'], partial(downlifter, 2.5))
