"""Paper, nature/ambience, foley."""
from functools import partial
from dsp import *
from r_fx import explosion

PA = 'paper'
for i, (d, dens) in enumerate([(0.5, 0.12), (0.8, 0.2)], 1):
    add(PA, f'paper_{i}', 'Paper crinkle', ['paper', 'crinkle', 'foley'], lambda d=d, dens=dens: crackle(d, dens, 1500, 7000) * swell(d, 0.3, 1, 1))
for i, d in enumerate([0.45, 0.8], 1):
    add(PA, f'rip_{i}', 'Paper rip / tear', ['rip', 'tear', 'paper'],
        lambda d=d: lp(hp(white(d), 900), 7000) * (0.45 + 0.55 * np.abs(np.sin(ph(wander(d, 8, 25, 55), d)))) * swell(d, 0.25, 0.6, 0.7))
for i, (d, r) in enumerate([(0.8, 5), (1.2, 7)], 1):
    add(PA, f'scribble_{i}', 'Pen / marker scribble', ['scribble', 'pen', 'writing'],
        lambda d=d, r=r: bp(white(d), 3500, 1.5) * (0.3 + 0.7 * np.abs(np.sin(ph(wander(d, 3, r * 0.6, r * 1.4), d)))) * gate(d, 0.02, 0.05))
for i, d in enumerate([0.35, 0.5], 1):
    add(PA, f'page_flip_{i}', 'Page flip', ['page', 'flip', 'book'],
        lambda d=d: mixat([(0, sweep(white(d), 'bp', geo(400, 1500, d), 1) * swell(d, 0.5, 1.5, 1.5), 0.7), (0, crackle(d, 0.08, 2000, 8000), 0.5),
                           (d * 0.85, lp(white(0.04), 3000) * dec(0.04, 90), 0.8)]))
add(PA, 'stamp', 'Rubber stamp', ['stamp', 'approved', 'office'],
    lambda: mixat([(0, lp(kick(0.2, 140, 70, 40, 20, 0), 900)), (0, hp(white(0.05), 800) * dec(0.05, 80), 0.6), (0.25, click(1500, 0.04, 150), 0.3)]))
add(PA, 'crumple', 'Paper crumpled into a ball', ['crumple', 'paper', 'trash'],
    lambda: crackle(1.2, 0.35, 1200, 8000) * wander(1.2, 6, 0.2, 1) * gate(1.2, 0.02, 0.1))
add(PA, 'sticky_note', 'Sticky note peel and slap', ['sticky', 'note', 'peel'],
    lambda: mixat([(0, crackle(0.25, 0.4, 2500, 9000) * swell(0.25, 0.7, 1, 1)), (0.3, lp(white(0.03), 2500) * dec(0.03, 100), 0.8)]))

NA = 'nature'


def wind(d=5.0, lo=250, hi=900):
    ch = []
    for _ in range(2):
        x = sweep(pink(d), 'bp', wander(d, 0.8, lo, hi), 1.4) * wander(d, 0.6, 0.25, 1)
        ch.append(hp(x, 80))
    return np.stack(ch) * gate(d, 0.4, 0.6)


add(NA, 'wind_1', 'Wind (5 s)', ['wind', 'air', 'ambience'], partial(wind, 5.0))
add(NA, 'wind_2', 'Howling high wind (5 s)', ['wind', 'storm', 'howl'], partial(wind, 5.0, 500, 1600))


@sfx(NA, 'rain', 'Rain (5 s)', ['rain', 'weather', 'ambience'])
def _():
    d = 5.0
    hiss = np.stack([lp(hp(white(d), 900), 7000) for _ in range(2)]) * 0.25
    drop = lambda: sine(geo(rnd(2000, 4500), rnd(4000, 7000), 0.006), 0.006) * dec(0.006, 600)
    ev = [(rnd(0, d - 0.01), pan(drop(), rnd(-0.9, 0.9)), rnd(0.1, 0.6)) for _ in range(900)]
    return mix(hiss, mixat(ev)) * gate(d, 0.3, 0.5)


@sfx(NA, 'thunder', 'Thunder crack and roll', ['thunder', 'storm', 'weather'])
def _():
    d = 4.5
    roll = lp(brown(d), 260) * wander(d, 5, 0.2, 1) * dec(d, 0.9, 0.05)
    crack = hp(white(0.2), 600) * dec(0.2, 25)
    return verb(mixat([(0, crack, 0.8), (0.05, roll)]), 2.5, 0.35, 3000)


for i, (a, b, rt) in enumerate([(900, 2200, 0.5), (600, 1500, 1.8)], 1):
    add(NA, f'water_drop_{i}', 'Water drop' + (' in a cave' if i == 2 else ''), ['water', 'drop', 'drip'],
        lambda a=a, b=b, rt=rt, i=i: verb(sine(geo(a, b, 0.05), 0.05) * dec(0.05, 50, 0.001), rt, 0.25 if i == 1 else 0.4))
add(NA, 'bubbles', 'Bubbles rising', ['bubbles', 'water', 'underwater'],
    lambda: mixat([(rnd(0, 1.8), pan(sine(geo(f, f * 2.5, 0.05), 0.05) * swell(0.05, 0.3), rnd(-0.6, 0.6)), rnd(0.3, 1)) for f in rnd(250, 900, 30)]))


@sfx(NA, 'fire_crackle', 'Campfire crackle (4 s)', ['fire', 'crackle', 'campfire'])
def _():
    d = 4.0
    roar = np.stack([lp(brown(d), 500) * wander(d, 2, 0.4, 1) for _ in range(2)]) * 0.5
    cr = mixat([(rnd(0, d - 0.01), pan(hp(white(0.004), 1500) * dec(0.004, 900), rnd(-0.8, 0.8)), rnd(0.2, 1)) for _ in range(160)])
    return mix(roar, cr) * gate(d, 0.3, 0.4)


@sfx(NA, 'wave', 'Ocean wave (5 s)', ['ocean', 'wave', 'beach'])
def _():
    d = 5.0
    env = swell(d, 0.45, 1.5, 1.2)
    ch = [sweep(pink(d), 'lp', 300 + 3200 * env, 0.7) * env + 0.3 * hp(white(d), 3000) * env ** 3 for _ in range(2)]
    return np.stack(ch)


@sfx(NA, 'stream', 'Babbling stream (4 s)', ['stream', 'water', 'river'])
def _():
    d = 4.0
    base = np.stack([bp(pink(d), 1100, 0.8) * wander(d, 3, 0.5, 1) for _ in range(2)]) * 0.5
    bub = mixat([(rnd(0, d - 0.05), pan(sine(geo(f, f * 1.8, 0.03), 0.03) * swell(0.03, 0.3), rnd(-0.8, 0.8)), rnd(0.1, 0.5)) for f in rnd(500, 1800, 160)])
    return mix(base, bub) * gate(d, 0.3, 0.4)


@sfx(NA, 'birds', 'Birds chirping (3 s)', ['birds', 'morning', 'nature'])
def _():
    def chirp():
        d = rnd(0.05, 0.12)
        f0 = rnd(2500, 4500)
        return sine(f0 * (1 + 0.3 * np.sin(np.pi * U(d))) * (1 + 0.05 * np.sin(ph(rnd(30, 60), d))), d) * swell(d, 0.3)
    ev = []
    for _ in range(8):
        t0, p = rnd(0, 2.6), rnd(-0.8, 0.8)
        for k in range(rint(2, 5)):
            ev.append((t0 + k * rnd(0.1, 0.16), pan(chirp(), p), rnd(0.4, 1)))
    return verb(mixat(ev), 0.8, 0.15)


@sfx(NA, 'crickets', 'Night crickets (4 s)', ['crickets', 'night', 'ambience'])
def _():
    d = 4.0
    ev = []
    for _ in range(5):
        f, p, rate = rnd(4200, 5200), rnd(-0.8, 0.8), rnd(0.5, 0.9)
        for t in np.arange(rnd(0, 0.5), d - 0.2, rate):
            s = sine(f, 0.15) * (0.5 + 0.5 * np.sin(ph(60, 0.15))) * swell(0.15, 0.4)
            ev.append((t, pan(s, p), rnd(0.2, 0.6)))
    return mixat(ev)

FO = 'foley'


@sfx(FO, 'zipper', 'Zipper pull', ['zipper', 'zip', 'clothes'])
def _():
    d = 0.6
    ts = np.cumsum(1 / ramp(120, 300, d)[::N(0.003)] * 1.0)
    ts = ts[ts < d]
    return bp(pulses(ts, hp(white(0.002), 1500), d), 3000, 0.7) * swell(d, 0.5, 0.8, 0.8)


def knock(times):
    k = lambda: mix(sine(220 * rnd(0.95, 1.05), 0.12) * dec(0.12, 40), 0.4 * sine(590, 0.12) * dec(0.12, 70), 0.5 * lp(white(0.12), 1500) * dec(0.12, 90))
    return verb(mixat([(t, k()) for t in times]), 0.4, 0.15)


add(FO, 'knock_1', 'Door knock x3', ['knock', 'door', 'wood'], partial(knock, [0, 0.18, 0.36]))
add(FO, 'knock_2', 'Door knock x2', ['knock', 'door'], partial(knock, [0, 0.22]))
add(FO, 'glass_clink', 'Glass clink / cheers', ['glass', 'clink', 'cheers'],
    lambda: verb(mixat([(0, bell(3100, 1.0, (1, 2.32, 4.1, 5.9), (1, .6, .4, .2), 5, 0.8)), (0.06, bell(3500, 0.8, (1, 2.32, 4.1), (1, .5, .3), 6, 0.8), 0.6)]), 0.6, 0.15))
add(FO, 'pen_click', 'Ballpoint pen click', ['pen', 'click', 'office'], lambda: mixat([(0, click(3800, 0.03, 380)), (0.12, click(3200, 0.03, 380), 0.8)]))
add(FO, 'light_switch', 'Light switch', ['switch', 'light', 'click'],
    lambda: mix(click(2000, 0.04, 260), 0.5 * sine(1200, 0.04) * dec(0.04, 120), 0.5 * lp(kick(0.06, 160, 100, 60, 50, 0), 600)))
add(FO, 'spray', 'Spray can', ['spray', 'aerosol', 'hiss'], lambda: hp(white(0.9), 2500) * gate(0.9, 0.03, 0.15) * (0.85 + 0.15 * wander(0.9, 10, 0, 1)))


@sfx(FO, 'fireworks', 'Firework whistle, bang and crackle', ['fireworks', 'celebration', 'new year'])
def _():
    d = 1.2
    whistle = (sine(geo(1200, 2700, d) * (1 + 0.01 * np.sin(ph(9, d))), d) * 0.5 + 0.2 * hp(white(d), 3000)) * swell(d, 0.8, 1, 0.5)
    cr = mixat([(rnd(0, 1.4), pan(hp(white(0.004), 2000) * dec(0.004, 700), rnd(-0.9, 0.9)), rnd(0.2, 0.8)) for _ in range(90)])
    return mixat([(0, whistle, 0.6), (1.2, explosion(1.5, 1200), 0.9), (1.45, verb(cr, 1.0, 0.3), 0.5)])


add(FO, 'footsteps', 'Footsteps on a hard floor', ['footsteps', 'walk', 'steps'],
    lambda: verb(mixat([(j * 0.45, mix(lp(kick(0.1, 120, 70, 50, 30, 0), 700), 0.4 * bp(white(0.06), 2500, 1.2) * dec(0.06, 70))) for j in range(5)]), 0.5, 0.15))
add(FO, 'door_open', 'Door handle and creak', ['door', 'creak', 'open'],
    lambda: mixat([(0, click(1800, 0.05, 150)), (0.12, lp(saw(ramp(90, 140, 0.8) * (1 + 0.04 * wander(0.8, 12, -1, 1)), 0.8), 1800) * swell(0.8, 0.4, 1, 1) * 0.4)]))
add(FO, 'cup_set_down', 'Cup set down on a table', ['cup', 'table', 'kitchen'],
    lambda: mix(bell(2100, 0.4, (1, 2.5, 4.4), (1, .5, .2), 9), 0.6 * lp(kick(0.1, 220, 120, 50, 30, 0), 900)))
