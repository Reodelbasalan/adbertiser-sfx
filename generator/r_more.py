"""Batch 2: crowd, household foley, scratches, cartoon extras."""
from functools import partial
from scipy import signal as _sig
from dsp import *
from r_motion import whoosh
from r_fx import impact, explosion
from r_ui import pop, coinping
from r_world import crackle

CR = 'crowd'


def claps(d=4.0, rate=60, swell_pk=0.35, rt=1.2):
    ch = []
    for _ in range(2):
        out = np.zeros(N(d) + N(0.05))
        for k in range(8):
            ker = bp(white(0.03), rnd(900, 2300), 1.2) * dec(0.03, rnd(80, 170))
            n_ev = int(rate * d / 8)
            imp = np.zeros(N(d))
            imp[(rnd(0, d, n_ev) * SR).astype(int).clip(0, N(d) - 1)] = rnd(0.3, 1, n_ev)
            out[:N(d) + len(ker) - 1] += _sig.fftconvolve(imp, ker)
        ch.append(out)
    x = np.stack(ch)
    env = np.pad(swell(d, swell_pk, 0.5, 1.2), (0, x.shape[1] - N(d)))
    return verb(x * env, rt, 0.25, 6000)


add(CR, 'applause_1', 'Small group applause (4 s)', ['applause', 'clap', 'audience'], partial(claps, 4.0, 60))
add(CR, 'applause_2', 'Big audience applause (5 s)', ['applause', 'big', 'audience'], partial(claps, 5.0, 260, 0.3, 1.8))
add(CR, 'applause_short', 'Short burst of applause (2 s)', ['applause', 'short'], partial(claps, 2.0, 120, 0.15, 1.0))

VOW = dict(a=(730, 1090, 2440), o=(300, 870, 2240), aw=(570, 840, 2410), eh=(530, 1840, 2480), u=(325, 700, 2530))


def voice(d, f0, contour, vowel, f1=None):
    """One synthetic voice: buzzy source through 3 formants; vowel may glide to f1."""
    f = f0 * contour * (1 + 0.012 * np.sin(ph(rnd(4.5, 6.5), d) + rnd(0, 6)))
    src = saw(f, d) + 0.3 * white(d)
    F = VOW[vowel]
    G = VOW[f1] if f1 else F
    out = np.zeros(N(d))
    for a, b, g in zip(F, G, (1, 0.6, 0.25)):
        out += g * sweep(src, 'bp', ramp(a, b, d), 6)
    return out


def crowd(d, vowel, cont, n=24, to=None, rt=1.2):
    ev = []
    for _ in range(n):
        dd = d * rnd(0.8, 1.0)
        c = cont(dd) * rnd(0.97, 1.03)
        v = voice(dd, rnd(105, 260), c, vowel, to) * swell(dd, rnd(0.25, 0.45), 1.2, 1.4)
        ev.append((rnd(0, d * 0.12), pan(v, rnd(-0.85, 0.85)), rnd(0.5, 1)))
    return verb(mixat(ev), rt, 0.35, 5000)


add(CR, 'crowd_ooh', 'Impressed crowd "ooooh"', ['ooh', 'crowd', 'impressed'],
    partial(crowd, 1.8, 'o', lambda d: 1 + 0.25 * np.sin(np.pi * U(d) ** 0.8)))
add(CR, 'crowd_aww', 'Sympathetic crowd "awww"', ['aww', 'crowd', 'cute'],
    partial(crowd, 1.8, 'aw', lambda d: 1.25 - 0.3 * U(d) ** 0.7))
add(CR, 'crowd_wow', 'Crowd "woooow"', ['wow', 'crowd', 'amazed'],
    partial(crowd, 1.6, 'u', lambda d: 1 + 0.35 * np.sin(np.pi * U(d)), 24, 'a'))


@sfx(CR, 'cheer', 'Crowd cheer with applause and whistles', ['cheer', 'crowd', 'celebrate', 'win'])
def _():
    d = 3.5
    yay = crowd(d, 'eh', lambda dd: 1 + 0.3 * U(dd) ** 0.3, 30, 'a', 1.4)
    wh = mixat([(rnd(0.3, 2.2), pan(finger_whistle(0.6), rnd(-0.7, 0.7)), 0.35) for _ in range(3)])
    return mix(yay, claps(d, 220, 0.3, 1.4) * 0.8, wh)


def finger_whistle(d=0.8):
    u = U(d)
    f = 2900 - 1100 * (1 - np.clip(u / 0.2, 0, 1)) ** 2 - 500 * np.clip((u - 0.6) / 0.4, 0, 1) ** 2
    f = f * (1 + 0.01 * np.sin(ph(7, d)))
    return (sine(f, d) + 0.12 * bp(white(d), 2800, 2)) * gate(d, 0.04, 0.12)


add(CR, 'finger_whistle', 'Loud finger whistle', ['whistle', 'crowd', 'hype'], partial(finger_whistle, 0.8))
add(CR, 'whistle_wolf', 'Two-part "wheet-whew" whistle', ['whistle', 'wow', 'flirt'],
    lambda: mixat([(0, sine(geo(1200, 2800, 0.35), 0.35) * gate(0.35, 0.03, 0.05)), (0.45, sine(geo(2900, 1100, 0.6), 0.6) * gate(0.6, 0.03, 0.15))]))

FO = 'foley'
add(FO, 'doorbell', 'Ding-dong doorbell', ['doorbell', 'ding-dong', 'visitor'],
    lambda: verb(mel([(0, 'E5', 1.6), (0.55, 'C5', 2.0)], partial(bell, ratios=(1, 2.76, 5.4), amps=(1, .35, .15), k=1.4)), 1.0, 0.2))
add(FO, 'school_bell', 'Electric school bell (2 s)', ['bell', 'school', 'ring'],
    lambda: verb(metal(1600, 2.0, 0.4, 6, 0.3) * (0.4 + 0.6 * (0.5 + 0.5 * sq(24, 2.0))) * gate(2.0, 0.005, 0.15), 0.8, 0.2))
add(FO, 'bike_bell', 'Bicycle bell ring-ring', ['bike', 'bell', 'ring'],
    lambda: mixat([(t, bell(3800, 0.8, (1, 1.48, 2.1, 2.9), (1, .7, .4, .2), 4) * trem(0.8, 30, 0.4)) for t in (0, 0.14)]))


def horn(times, d=0.45):
    tone = lambda dd: drive(lp(saw(415, dd) + saw(520, dd) + 0.5 * sq(207, dd), 3200), 2.2) * gate(dd, 0.01, 0.04)
    return verb(mixat([(t, tone(dd)) for t, dd in times]), 0.5, 0.1)


add(FO, 'car_horn_1', 'Car horn honk', ['car', 'horn', 'honk', 'traffic'], partial(horn, [(0, 0.55)]))
add(FO, 'car_horn_2', 'Double car honk', ['car', 'horn', 'beep beep'], partial(horn, [(0, 0.14), (0.22, 0.3)]))
add(FO, 'elevator_ding', 'Elevator arrival ding', ['elevator', 'ding', 'arrive'],
    lambda: verb(bell(nf('E6'), 2.0, (1, 2.0, 3.0, 4.2), (1, .3, .15, .05), 1.6, 1.0), 1.2, 0.25))
add(FO, 'referee_whistle', 'Referee whistle', ['whistle', 'referee', 'stop'],
    lambda: mixat([(t, (sine(2900, d) * (0.65 + 0.35 * np.sin(ph(42, d))) + 0.15 * bp(white(d), 3000, 2)) * gate(d, 0.01, 0.05)) for t, d in ((0, 0.18), (0.28, 0.7))]))
add(FO, 'kiss', 'Kiss / smooch', ['kiss', 'smooch', 'love'],
    lambda: mixat([(0, lp(white(0.12), 3000) * swell(0.12, 0.6, 2, 1) * 0.3), (0.1, pop(500, 1300, 0.08, 45, 0.4, 70))]))
add(FO, 'slap', 'Face slap', ['slap', 'hit', 'funny'],
    lambda: verb(mix(hp(white(0.15), 600) * dec(0.15, 45, 0.0005), 0.5 * lp(kick(0.12, 220, 120, 50, 30, 0), 800)), 0.4, 0.15))
add(FO, 'bubble_wrap', 'Bubble wrap popping', ['bubble wrap', 'pop', 'satisfying'],
    lambda: mixat([(t, hp(pop(rnd(1400, 2400), rnd(900, 1400), 0.05, 80, 0.8), 600), rnd(0.5, 1)) for t in np.sort(rnd(0, 1.2, 12))]))
add(FO, 'alarm_clock', 'Mechanical alarm clock ringing', ['alarm', 'clock', 'wake up'],
    lambda: mixat([(i / 16, metal(2400 if i % 2 else 2700, 0.12, 25, 5), 1) for i in range(40)]))


@sfx(FO, 'glass_break', 'Glass breaking', ['glass', 'break', 'shatter'])
def _():
    crash = hp(white(0.3), 2500) * dec(0.3, 18)
    shards = mixat([(rnd(0, 0.9) ** 1.6, pan(metal(rnd(3000, 7000), 0.3, 12, 4), rnd(-0.8, 0.8)), rnd(0.2, 0.8)) for _ in range(40)])
    return verb(mixat([(0, crash), (0, lp(kick(0.15, 300, 150, 40, 30, 0), 1500), 0.4), (0.01, shards, 0.7)]), 0.7, 0.2)


add(FO, 'door_slam', 'Door slam', ['door', 'slam', 'angry'],
    lambda: verb(mix(lp(kick(0.4, 110, 55, 35, 9, 0), 600), 0.6 * bp(white(0.2), 700, 1) * dec(0.2, 30), 0.3 * click(1500, 0.05, 120)), 0.9, 0.3, 4000))
add(FO, 'keys_jingle', 'Keys jingling', ['keys', 'jingle', 'metal'],
    lambda: mixat([(b * 0.25 + rnd(0, 0.12), pan(coinping(rnd(4500, 8500), 0.18), rnd(-0.6, 0.6)), rnd(0.3, 0.9)) for b in range(3) for _ in range(10)]))
DTMF = {'1': (697, 1209), '2': (697, 1336), '3': (697, 1477), '4': (770, 1209), '5': (770, 1336), '6': (770, 1477),
        '7': (852, 1209), '8': (852, 1336), '9': (852, 1477), '0': (941, 1336)}
add(FO, 'phone_dial', 'Phone keypad dialing tones', ['phone', 'dial', 'keypad'],
    lambda: mixat([(i * 0.16, (sine(DTMF[c][0], 0.1) + sine(DTMF[c][1], 0.1)) * gate(0.1, 0.003, 0.01) * 0.5) for i, c in enumerate('2468135')]))
add(FO, 'phone_busy', 'Busy / hang-up tone', ['phone', 'busy', 'hang up'],
    lambda: mixat([(i * 1.0, (sine(480, 0.5) + sine(620, 0.5)) * gate(0.5, 0.005, 0.01) * 0.5) for i in range(3)]))
add(FO, 'vinyl_crackle', 'Vinyl record crackle (4 s)', ['vinyl', 'crackle', 'retro', 'lofi'],
    lambda: mix(np.stack([crackle(4.0, 0.03, 800, 6000) for _ in range(2)]) * 1.5, 0.05 * lp(white(4.0), 4000), 0.1 * lp(brown(4.0), 120)) * gate(4.0, 0.2, 0.3))
add(FO, 'receipt_print', 'Receipt printer', ['printer', 'receipt', 'pos'],
    lambda: mixat([(i * 0.09, bp(sq(rnd(900, 1300), 0.07, 0.3) + 0.4 * white(0.07), 2000, 1) * gate(0.07, 0.002, 0.01), 0.7) for i in range(12)] + [(1.15, crackle(0.15, 0.6, 2500, 9000), 0.8)]))
add(FO, 'body_fall', 'Body falling to the floor', ['fall', 'thud', 'body'],
    lambda: verb(mixat([(0, lp(white(0.2), 2500) * swell(0.2, 0.6), 0.3), (0.18, lp(kick(0.4, 100, 50, 30, 10, 0), 600)), (0.18, bp(white(0.1), 400, 1) * dec(0.1, 40), 0.6), (0.42, lp(kick(0.2, 90, 50, 30, 18, 0), 500), 0.4)]), 0.6, 0.2))

TR = 'transition'


def scratch(pos_fn, d):
    src_d = 1.2
    src = lp(saw(110, src_d) + saw(165, src_d) + 0.7 * saw(220, src_d) + 0.4 * white(src_d), 5000)
    t = T(d)
    pos = pos_fn(t)
    x = np.interp(pos * SR, np.arange(len(src)), src)
    speed = np.abs(np.gradient(pos) * SR)
    needle = hp(white(d), 2000) * np.clip(speed, 0, 3) * 0.15
    return lp((x + needle) * np.clip(speed, 0, 1.5) / 1.5, 9000) * gate(d, 0.003, 0.02)


add(TR, 'record_scratch_1', 'DJ record scratch (wikka)', ['scratch', 'dj', 'record'],
    lambda: scratch(lambda t: 0.35 + 0.09 * np.sin(2 * np.pi * 3.2 * t) + 0.0 * t, 0.5))
add(TR, 'record_scratch_2', 'Record-stop scratch', ['scratch', 'stop', 'record', 'awkward'],
    lambda: scratch(lambda t: 0.25 + 0.4 * t - 0.25 * np.clip((t - 0.12) / 0.18, 0, 1) ** 1.5, 0.4))


def tape(direction=-1, d=1.4):
    src_d = 3.0
    m = [nf(n) for n in ('C4', 'E4', 'G4', 'A4', 'F4', 'D4', 'G4', 'C5')]
    src = mixat([(i * 0.37, pluck(f, 0.6, 0.99)) for i, f in enumerate(m)])
    src = np.pad(src, (0, max(0, N(src_d) - len(src))))
    sp = ramp(1, 7, d, 0.7)
    pos = np.cumsum(sp) / SR
    pos = (src_d - 0.05 - pos) if direction < 0 else pos
    pos = np.mod(pos, src_d - 0.05)
    x = np.interp(pos * SR, np.arange(len(src)), src)
    return lp(x + 0.05 * hp(white(d), 3000), 10000) * gate(d, 0.01, 0.05) * (1 + 0.15 * np.sin(ph(13, d)))


add(TR, 'rewind', 'Tape rewind (speeding up backwards)', ['rewind', 'tape', 'back'], partial(tape, -1))
add(TR, 'fast_forward', 'Fast-forward (speeding up)', ['fast forward', 'tape', 'skip'], partial(tape, 1))

TM = 'timer'


@sfx(TM, 'ticking_bomb', 'Ticking bomb countdown', ['bomb', 'tick', 'countdown', 'tension'])
def _():
    ts, t, step = [], 0.0, 0.32
    while t < 2.6:
        ts.append(t)
        t += step
        step = max(0.07, step * 0.88)
    ev = [(t, mix(click(2600, 0.04, 260), 0.4 * beep(1800, 0.05)), 1) for t in ts]
    ev.append((t + 0.05, beep(1800, 0.6) * 0.7))
    return mixat(ev)


CT = 'cartoon'
add(CT, 'slip', 'Banana slip and fall', ['slip', 'fall', 'funny'],
    lambda: mixat([(0, sine(geo(400, 2400, 0.25), 0.25) * gate(0.25, 0.005, 0.03) * 0.7), (0.3, lp(kick(0.35, 120, 55, 30, 10, 0), 700)), (0.3, bp(white(0.1), 500, 1) * dec(0.1, 40), 0.5)]))


@sfx(CT, 'dizzy', 'Dizzy circling stars', ['dizzy', 'stars', 'knocked out'])
def _():
    d = 1.6
    notes = ['E7', 'C7', 'A6', 'C7'] * 4
    ev = [(i * 0.1, bell(nf(n), 0.35, k=9), 0.6) for i, n in enumerate(notes)]
    x = mixat(ev).astype(float)
    return verb(pan(x, 0.8 * np.sin(ph(1.5, len(x) / SR))), 0.6, 0.2)


def honk(d=0.28):
    f = 330 * ramp(0.95, 1.05, d)
    s = drive(saw(f, d) * (0.7 + 0.3 * sq(60, d)), 2)
    return (bp(s, 1000, 1.2) + 0.5 * bp(s, 2400, 2)) * gate(d, 0.01, 0.05)


add(CT, 'honk_toy', 'Clown horn honk-honk', ['honk', 'clown', 'horn', 'funny'], lambda: mixat([(0, honk(0.22)), (0.3, honk(0.32))]))
add(CT, 'splat', 'Wet splat', ['splat', 'wet', 'gross'],
    lambda: verb(mix(lp(white(0.35), 1800) * dec(0.35, 14, 0.002) * (0.6 + 0.4 * np.abs(np.sin(ph(30, 0.35)))), 0.6 * sine(geo(260, 70, 0.3), 0.3) * dec(0.3, 15)), 0.4, 0.12))

MO = 'money'
add(MO, 'payment_success', 'Payment received chime', ['payment', 'success', 'paid'],
    lambda: verb(mixat([(0, sine(geo(500, 1100, 0.12), 0.12) * swell(0.12, 0.5) * 0.5), (0.12, mel([(0, 'G5', 1.2), (0, 'D6', 1.2), (0.09, 'G6', 1.4)], partial(bell, k=2.6)))]), 0.8, 0.2))

DI = 'ding'
add(DI, 'notif_4', 'Soft three-note notification', ['notification', 'soft', 'phone'],
    lambda: verb(mel([(0, 'C6', .3), (0.09, 'A5', .3), (0.18, 'F6', .5)], marimba), 0.6, 0.15))
add(DI, 'notif_5', 'Plucky notification', ['notification', 'pluck', 'phone'],
    lambda: verb(mixat([(0, pluck(nf('D5'), 0.8, 0.995)), (0.1, pluck(nf('A5'), 1.0, 0.995))]), 0.6, 0.15))

CA = 'camera'
add(CA, 'lens_zoom', 'Lens zoom motor', ['lens', 'zoom', 'motor'],
    lambda: mix(lp(saw(ramp(170, 230, 0.8), 0.8), 1400) * gate(0.8, 0.04, 0.08) * 0.5, pulses(np.arange(0, 0.8, 0.018), click(4000, 0.006, 900), 0.8) * 0.3))
