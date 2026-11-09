"""Glitch, tech/sci-fi, impacts, cinematic, camera, magic."""
from functools import partial
from dsp import *
from r_motion import whoosh, cymbal, riser

G = 'glitch'


def glitch(d=0.45, seg=(0.012, 0.045), gaps=0.15):
    t, ev = 0.0, []
    while t < d:
        L = rnd(*seg)
        k = rint(0, 6)
        if k == 0:
            s = white(L)
        elif k == 1:
            s = sq(rnd(80, 2000), L)
        elif k == 2:
            s = saw(geo(rnd(100, 3000), rnd(100, 3000), L), L)
        elif k == 3:
            s = np.tile(white(0.003), N(L) // N(0.003) + 1)[:N(L)]
        elif k == 4:
            s = fm(rnd(200, 1500), rnd(30, 400), rnd(2, 12), L)
        else:
            s = np.zeros(N(L)) if rnd() < gaps * 3 else white(L) * 0.5
        s = crush(s, rint(3, 7), rint(2, 24)) * rnd(0.4, 1)
        ev.append((t, pan(s, rnd(-0.7, 0.7))))
        t += L
    return lp(mixat(ev), 12000)


for i, d in enumerate([0.45, 0.35, 0.6, 0.5, 0.4], 1):
    add(G, f'glitch_{i}', 'Digital glitch burst', ['glitch', 'digital', 'error'], partial(glitch, d))
for i, d in enumerate([0.14, 0.18, 0.12], 1):
    add(G, f'glitch_short_{i}', 'Tiny glitch for quick cuts', ['glitch', 'short', 'cut'], partial(glitch, d, (0.008, 0.03)))


def stutter(src_d=0.06, reps=8):
    src = mix(fm(rnd(300, 800), rnd(50, 200), 5, src_d), 0.5 * white(src_d))
    ev, t = [], 0.0
    for r in range(reps):
        L = max(0.012, src_d * (1 - r / reps))
        ev.append((t, src[:N(L)] * gate(L, 0.001, 0.003)))
        t += L
    return crush(mixat(ev), 6, 3)


add(G, 'glitch_stutter_1', 'Buffer stutter that shrinks', ['stutter', 'glitch', 'repeat'], partial(stutter, 0.06, 8))
add(G, 'glitch_stutter_2', 'Long buffer stutter', ['stutter', 'glitch', 'repeat'], partial(stutter, 0.09, 12))
for i, hum in enumerate([0, 1], 1):
    def _static(hum=hum):
        d = 0.7
        x = crush(bp(white(d), 3000, 0.5), 5, 3) * (0.4 + 0.6 * (wander(d, 30, 0, 1) > 0.4))
        if hum:
            x = x + 0.4 * lp(saw(60, d), 600)
        return x * gate(d, 0.003, 0.06)
    add(G, f'static_burst_{i}', 'TV static burst' + (' with hum' if hum else ''), ['static', 'tv', 'noise'], _static)
for i, d in enumerate([0.6, 1.0], 1):
    add(G, f'data_chirp_{i}', 'Modem-like data chirps', ['data', 'modem', 'computer'],
        lambda d=d: mixat([(j * 0.03, lp(sq(rnd(600, 3200), 0.028), 6000) * gate(0.028, 0.001, 0.003), rnd(0.3, 0.7)) for j in range(int(d / 0.03))]))
add(G, 'power_up', 'Electric power-up', ['power', 'up', 'start'],
    lambda: verb(mix(lp(saw(geo(60, 900, 1.2), 1.2), 3000) * trem(1.2, ramp(6, 30, 1.2), 0.5) * U(1.2) ** 0.7, 0.3 * sine(geo(200, 2400, 1.2), 1.2)) * gate(1.2, 0.05, 0.02), 0.6, 0.15))
add(G, 'power_down', 'Electric power-down', ['power', 'down', 'shutdown'],
    lambda: crush(lp(saw(geo(900, 35, 1.2), 1.2), 3000) * trem(1.2, ramp(30, 4, 1.2), 0.5) * (1 - U(1.2)) ** 0.8, 8, 2))

TE = 'tech'
for i, (f0, f1, d) in enumerate([(2600, 280, 0.22), (1800, 200, 0.3), (3200, 600, 0.45)], 1):
    add(TE, f'laser_{i}', 'Sci-fi laser shot', ['laser', 'pew', 'sci-fi'],
        lambda f0=f0, f1=f1, d=d, i=i: verb(fm(geo(f0, f1, d), geo(f0, f1, d) * 0.5, 2 + i, d) * dec(d, 6 / d, 0.001), 0.4, 0.12))
add(TE, 'scanner', 'Scanner sweeping back and forth', ['scan', 'scanner', 'sci-fi'],
    lambda: lp(saw(1800 + 1200 * np.sin(ph(2.0, 1.5)), 1.5), 5000) * trem(1.5, 18, 0.6) * gate(1.5, 0.05, 0.1) * 0.5)
add(TE, 'hologram', 'Shimmering hologram', ['hologram', 'shimmer', 'sci-fi'],
    lambda: verb(sum(sine(f * (1 + 0.003 * np.sin(ph(rnd(3, 7), 1.6))), 1.6) for f in (880, 1320, 1760, 2640)) * trem(1.6, 9, 0.6) * swell(1.6, 0.3, 1, 1), 1.0, 0.3))
add(TE, 'beam_up', 'Teleport beam rising', ['beam', 'teleport', 'rise'],
    lambda: verb(sum(sine(geo(f, f * 3, 1.8), 1.8) for f in (300, 450, 600)) * trem(1.8, 25, 0.5) * swell(1.8, 0.7, 1.5, 1), 1.0, 0.3))
for i, n in enumerate([10, 16], 1):
    add(TE, f'computer_beeps_{i}', 'Sci-fi computer beeps', ['computer', 'beeps', 'sci-fi'],
        lambda n=n: mixat([(j * 0.08, beep(rnd(800, 2400), 0.06), rnd(0.4, 0.8)) for j in range(n)]))
add(TE, 'robot_blips', 'Robot talking blips', ['robot', 'blips', 'voice'],
    lambda: mixat([(j * 0.07, fm(rnd(200, 600), rnd(80, 300), rnd(3, 9), 0.06) * gate(0.06), rnd(0.5, 0.9)) for j in range(12)]))
add(TE, 'teleport', 'Teleport phase-out', ['teleport', 'warp', 'sci-fi'],
    lambda: verb(mix(comb(white(1.0), ramp(0.004, 0.0004, 1.0), 0.9) * swell(1.0, 0.3, 1, 1.5) * 0.4, sine(geo(2000, 200, 1.0), 1.0) * trem(1.0, 20, 0.7) * 0.5), 0.8, 0.25))
add(TE, 'charge_up', 'Energy charge-up whine', ['charge', 'energy', 'power'],
    lambda: mixat([(0, mix(sine(geo(200, 4000, 1.2), 1.2), 0.3 * sine(geo(200, 4000, 1.2) * 1.01, 1.2)) * U(1.2) ** 1.5 * 0.7), (1.2, click(3000, 0.04, 200))]))
add(TE, 'shield', 'Energy shield hum', ['shield', 'force', 'sci-fi'],
    lambda: verb(mix(fm(110, 55, 3, 1.0) * 0.5, sweep(white(1.0), 'bp', geo(400, 3000, 1.0), 2) * 0.4) * swell(1.0, 0.2, 1, 1.2), 0.8, 0.2))
add(TE, 'ui_hud', 'Futuristic HUD pop-up', ['hud', 'interface', 'sci-fi'],
    lambda: verb(mixat([(0, sine(geo(800, 2400, 0.08), 0.08) * gate(0.08)), (0.07, beep(2400, 0.05), 0.6), (0.12, beep(3200, 0.08), 0.5)]), 0.4, 0.2))

IM = 'impact'


def impact(d=1.2, f0=120, f1=38, kp=18, ka=4, crack=0.5, cf=3000, dist=1.5, rt=1.0, wet=0.25, body=0.4):
    sub = sine(f1 + (f0 - f1) * np.exp(-T(d) * kp), d) * dec(d, ka, 0.002)
    cr = crack * lp(hp(white(d), cf * 0.3), cf * 2) * dec(d, 35, 0.0005)
    bo = body * lp(brown(d), 400) * dec(d, 9, 0.002)
    mid = 0.45 * bp(white(d), 220, 0.7) * dec(d, 11, 0.001) + 0.3 * sine(f0 * 1.9, d) * dec(d, ka * 2.5, 0.001)
    x = drive(sub + cr + bo + mid, dist)
    return verb(x, rt, wet) if wet else x


for i, (f0, crk, rt) in enumerate([(120, 0.5, 1.0), (150, 0.7, 0.8), (100, 0.4, 1.4)], 1):
    add(IM, f'impact_{i}', 'Solid impact hit', ['impact', 'hit', 'punch'], partial(impact, 1.2, f0, 38, 18, 4, crk, 3000, 1.5, rt))
for i, (f0, dist) in enumerate([(140, 3.0), (110, 4.0)], 1):
    add(IM, f'impact_hard_{i}', 'Hard distorted impact', ['impact', 'hard', 'heavy'], partial(impact, 1.4, f0, 35, 16, 3.5, 0.9, 4000, dist, 1.2, 0.3, 0.6))
for i, d in enumerate([2.0, 2.6], 1):
    add(IM, f'boom_{i}', 'Deep boom', ['boom', 'bass', 'big'], partial(impact, d, 70, 30, 6, 1.6, 0.3, 1500, 1.8, 1.8, 0.3, 0.8))
for i, (f0, f1) in enumerate([(55, 30), (65, 34)], 1):
    add(IM, f'boom_sub_{i}', 'Sub-bass boom (use good speakers)', ['sub', 'bass', 'boom'],
        lambda f0=f0, f1=f1: drive(sine(geo(f0, f1, 1.8), 1.8) * dec(1.8, 1.8, 0.004), 2.0))
for i, d in enumerate([1.5, 2.2], 1):
    add(IM, f'bass_drop_{i}', 'Bass drop glide', ['drop', 'bass', 'edm'],
        lambda d=d: drive(sine(geo(140, 28, d), d) + 0.3 * saw(geo(140, 28, d), d), 2.5) * swell(d, 0.03, 1, 1.0) * 0.8)
for i, (f0, pre) in enumerate([(160, 0), (130, 0), (150, 1)], 1):
    def _punch(f0=f0, pre=pre):
        h = mix(kick(0.25, f0, 60, 35, 14, 0.2), 0.5 * bp(white(0.12), 1200, 1.0) * dec(0.12, 40))
        if pre:
            return mixat([(0, whoosh(0.18, 800, 3500, 2000, 1.3, 0.9, 2.5, 0.4), 0.6), (0.17, h)])
        return h
    add(IM, f'punch_{i}', 'Body punch' + (' with swing' if pre else ''), ['punch', 'fight', 'hit'], _punch)
for i, f0 in enumerate([90, 70], 1):
    add(IM, f'thud_{i}', 'Dull low thud', ['thud', 'drop', 'low'], lambda f0=f0: lp(kick(0.4, f0, 45, 30, 12, 0) + 0.3 * brown(0.4) * dec(0.4, 20), 500))
for i, f in enumerate([320, 540], 1):
    add(IM, f'hit_metal_{i}', 'Metal clang', ['metal', 'clang', 'hit'],
        lambda f=f: verb(mix(metal(f, 1.6, 2.2, 8, 0.4), 0.5 * nburst(0.1, 1000, 9000, 60)), 0.8, 0.2))


def hit_cine(d=3.0, f0=90):
    x = mixat([(0, impact(d, f0, 32, 10, 1.6, 0.8, 3500, 2.0, 0, 0, 0.7)), (0, metal(180, d, 1.4, 8, 0.6), 0.25),
               (0, hp(white(d), 3000) * dec(d, 3), 0.15)])
    return verb(x, 2.5, 0.35, 5000)


add(IM, 'hit_cinematic_1', 'Big trailer-style hit', ['cinematic', 'trailer', 'hit'], partial(hit_cine, 3.0, 90))
add(IM, 'hit_cinematic_2', 'Darker cinematic hit', ['cinematic', 'dark', 'hit'], partial(hit_cine, 3.5, 65))


def explosion(d=2.5, bright=900):
    body = lp(brown(d), bright) * dec(d, 2.2, 0.004) * wander(d, 8, 0.6, 1)
    cr = hp(white(0.08), 1000) * dec(0.08, 50)
    return verb(drive(mixat([(0, body), (0, cr, 0.7), (0, kick(1.5, 90, 30, 8, 2.5, 0), 0.8)]), 1.8), 1.8, 0.25, 4000)


add(IM, 'explosion_1', 'Explosion', ['explosion', 'blast', 'boom'], partial(explosion, 2.5, 900))
add(IM, 'explosion_2', 'Distant explosion', ['explosion', 'distant'], lambda: lp(explosion(3.0, 500), 1500))

CI = 'cinematic'


def braam(d=2.5, notes=('C2', 'G2', 'C3', 'Eb3')):
    s = sum(saw(nf(n) * (1 + k * 0.003), d) for n in notes for k in (-1, 0, 1)) / (3 * len(notes))
    cut = 200 + 2200 * (1 - np.exp(-T(d) * 12)) * np.exp(-T(d) * 1.2)
    return verb(drive(sweep(s, 'lp', cut, 1.1), 2.5) * gate(d, 0.02, 0.5), 2.0, 0.3, 4000)


add(CI, 'braam_1', 'Big brassy BRAAM', ['braam', 'trailer', 'epic'], partial(braam))
add(CI, 'braam_2', 'Dark low BRAAM', ['braam', 'dark', 'epic'], partial(braam, 3.0, ('A1', 'E2', 'A2', 'C3')))
for i, d in enumerate([1.0, 1.4], 1):
    add(CI, f'trailer_hit_{i}', 'Reverse swell into a trailer hit', ['trailer', 'whoosh', 'hit'],
        lambda d=d: mixat([(0, rev(verb(cymbal(d), d * 0.4, 0.3)), 0.6), (d, hit_cine(2.5, 80))]))


def drone(d=4.0, root=55):
    s = sum(saw(f * (1 + 0.002 * np.sin(ph(rnd(0.1, 0.3), d))), d) for f in (root, root * 1.06, root * 1.5, root * 2.12)) / 4
    return verb(lp(s, wander(d, 0.6, 250, 700).mean()) * swell(d, 0.4, 1.2, 1.0) + 0.1 * lp(pink(d), 300), 2.0, 0.3)


add(CI, 'tension_drone_1', 'Dark tension drone (4 s)', ['drone', 'tension', 'suspense'], partial(drone, 4.0, 55))
add(CI, 'tension_drone_2', 'Uneasy higher drone (4 s)', ['drone', 'tension', 'horror'], partial(drone, 4.0, 82.4))


@sfx(CI, 'heartbeat', 'Heartbeat (lub-dub x3)', ['heartbeat', 'suspense', 'pulse'])
def _():
    lub = lambda g: lp(kick(0.25, 70, 40, 25, 14, 0), 220) * g
    return mixat([(b * 0.85 + o, lub(g)) for b in range(3) for o, g in ((0, 1.0), (0.2, 0.7))])


add(CI, 'suspense_sting', 'Sudden high string-like sting', ['sting', 'suspense', 'scare'],
    lambda: verb(lp(sum(saw(nf(n) * (1 + k * 0.004), 1.5) for n in ('C6', 'C#6', 'F#6') for k in (-1, 1)), 4000) * dec(1.5, 2.5, 0.01) * 0.15, 2.0, 0.4))
add(CI, 'tail_reverb', 'Impact with long reverb tail', ['tail', 'reverb', 'impact'],
    lambda: verb(impact(0.6, 110, 40, 18, 6, 0.6, 3000, 1.5, 0, 0), 3.0, 0.6, 5000))
add(CI, 'rumble', 'Low rumble (3 s)', ['rumble', 'earthquake', 'low'],
    lambda: lp(brown(3.0), 150) * wander(3.0, 4, 0.3, 1) * swell(3.0, 0.3, 1, 1) + 0.3 * sine(38, 3.0) * swell(3.0, 0.3, 1, 1))
add(CI, 'slow_motion', 'Slow-motion whoosh down', ['slowmo', 'slow', 'down'],
    lambda: verb(mix(sweep(white(1.5), 'lp', geo(4000, 200, 1.5), 1.2), 0.5 * sine(geo(400, 60, 1.5), 1.5)) * swell(1.5, 0.15, 1, 1.2), 1.5, 0.3))

CA = 'camera'


def shutter(heavy=False):
    c1 = click(2800 if not heavy else 1800, 0.05, 220 if not heavy else 150, 1.5)
    whirr = bp(white(0.05), 2000, 1.5) * swell(0.05, 0.5) * 0.3
    c2 = click(3400 if not heavy else 2200, 0.05, 260, 1.5)
    ev = [(0, c1), (0.02, whirr), (0.075 if not heavy else 0.095, c2, 0.8)]
    if heavy:
        ev.append((0, lp(kick(0.08, 220, 120, 60, 40, 0), 800), 0.4))
    return mixat(ev)


add(CA, 'shutter_1', 'Camera shutter', ['shutter', 'camera', 'photo'], partial(shutter, False))
add(CA, 'shutter_2', 'DSLR shutter with mirror slap', ['shutter', 'dslr', 'photo'], partial(shutter, True))
add(CA, 'shutter_quick', 'Phone camera snap', ['shutter', 'phone', 'snap'],
    lambda: mixat([(0, click(3500, 0.03, 350)), (0.035, click(4200, 0.03, 400), 0.7)]))
add(CA, 'shutter_burst', 'Burst mode (5 shots)', ['burst', 'shutter', 'photos'], lambda: mixat([(i * 0.1, shutter(False)) for i in range(5)]))
add(CA, 'flash_charge', 'Flash charging whine + ready beep', ['flash', 'charge', 'camera'],
    lambda: mixat([(0, sine(geo(1000, 7000, 1.2), 1.2) * U(1.2) ** 0.5 * 0.25), (1.25, beep(2800, 0.08), 0.6)]))
add(CA, 'film_wind', 'Film advance ratchet', ['film', 'wind', 'ratchet'],
    lambda: pulses(np.arange(0, 0.8, 0.04), click(3000, 0.015, 600), 0.85) + 0.15 * bp(white(0.85), 2500, 1) * gate(0.85, 0.02, 0.05))
add(CA, 'focus_beep', 'Autofocus bip-bip', ['focus', 'beep', 'camera'], lambda: mixat([(0, beep(3200, 0.05)), (0.08, beep(3200, 0.05))]))
add(CA, 'polaroid', 'Instant camera shot + motor', ['polaroid', 'instant', 'print'],
    lambda: mixat([(0, shutter(True)), (0.2, lp(sq(120, 1.0), 1500) * 0.25 * gate(1.0, 0.05, 0.1) + 0.1 * bp(white(1.0), 1800, 1) * gate(1.0, 0.05, 0.1))]))

MG = 'magic'


def sparkle(d=1.2, n=26, lo=2500, hi=8000, rt=0.9):
    ev = [(rnd(0, d * 0.7) * (1 - rnd() * 0.3), pan(sine(rnd(lo, hi), 0.25) * dec(0.25, rnd(15, 30), 0.001), rnd(-0.8, 0.8)), rnd(0.2, 0.8)) for _ in range(n)]
    return verb(mixat(ev), rt, 0.35)


for i, (d, n, lo, hi) in enumerate([(1.2, 26, 2500, 8000), (1.0, 18, 3500, 9000), (1.6, 40, 2000, 6000)], 1):
    add(MG, f'sparkle_{i}', 'Magic sparkle twinkles', ['sparkle', 'magic', 'shine'], partial(sparkle, d, n, lo, hi))


def wand(d=1.2):
    g = sine(geo(600, 2400, d * 0.6), d * 0.6) * swell(d * 0.6, 0.6, 1.5, 1.5) * 0.5
    return mixat([(0, verb(g, 1.0, 0.3)), (0.3, sparkle(d, 20))])


add(MG, 'magic_wand_1', 'Wand swish + sparkles', ['wand', 'magic', 'spell'], partial(wand, 1.2))
add(MG, 'magic_wand_2', 'Longer wand spell', ['wand', 'magic', 'spell'], partial(wand, 1.8))
for i, base in enumerate([2000, 3000], 1):
    add(MG, f'shimmer_{i}', 'Soft shimmer', ['shimmer', 'glow', 'soft'],
        lambda base=base: verb(sum(sine(base * r, 2.0) * trem(2.0, rnd(5, 11), 0.8) for r in (1, 1.25, 1.5, 2)) * swell(2.0, 0.3, 1.2, 1.4) * 0.3, 1.5, 0.4))
add(MG, 'twinkle', 'Quick twinkle run', ['twinkle', 'star', 'cute'],
    lambda: verb(mel([(j * 0.06, nf(n), 0.4) for j, n in enumerate(['E7', 'C7', 'G6', 'E7', 'G7'])], partial(bell, k=8)), 0.9, 0.3))
add(MG, 'fairy_rise', 'Harp-like rising glissando', ['harp', 'fairy', 'rise', 'dream'],
    lambda: verb(mixat([(j * 0.035, pluck(nf('C5') * 2 ** (s / 12), 1.0, 0.995), 0.6) for j, s in enumerate([0, 2, 4, 7, 9, 12, 14, 16, 19, 21, 24, 26, 28])]), 1.5, 0.35))
for i, ch in enumerate([('C4', 'E4', 'G4', 'B4', 'D5'), ('A3', 'E4', 'A4', 'C#5', 'E5')], 1):
    add(MG, f'reveal_glow_{i}', 'Glowing reveal swell', ['reveal', 'glow', 'swell'],
        lambda ch=ch: mixat([(0, verb(pad([nf(n) for n in ch], 2.2, 2200), 1.5, 0.3)), (0.9, sparkle(1.2, 16), 0.5)]))
add(MG, 'chime_tree', 'Wind-chime glissando', ['chimes', 'glissando', 'dream'],
    lambda: verb(mixat([(j * 0.05, bell(nf('C6') * 2 ** (-s / 12) * 1.5, 1.2, k=4), 0.5) for j, s in enumerate(range(0, 26, 2))]), 1.2, 0.3))
add(MG, 'poof', 'Magic poof (disappear)', ['poof', 'smoke', 'disappear'],
    lambda: mixat([(0, verb(lp(white(0.5), 3000) * swell(0.5, 0.1, 1, 2), 0.8, 0.3)), (0.05, sparkle(0.8, 12), 0.5)]))
