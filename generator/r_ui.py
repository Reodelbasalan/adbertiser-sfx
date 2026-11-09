"""Pops, UI clicks/blips, dings, social, money, typing, timers, alerts."""
from functools import partial
from dsp import *

P = 'pop'


def pop(f0=900, f1=500, d=0.12, k=38, nz=0.25, kp=60):
    f = f1 + (f0 - f1) * np.exp(-T(d) * kp)
    return sine(f, d) * dec(d, k, 0.0015) + nz * bp(white(d), f0 * 2, 1.5) * dec(d, 250)


for i, (f0, f1, k) in enumerate([(900, 480, 38), (1200, 650, 42), (700, 380, 34), (1500, 900, 50)], 1):
    add(P, f'pop_{i}', 'Clean pop for text and stickers', ['pop', 'sticker', 'text'], partial(pop, f0, f1, 0.13, k))
for i, (f0, f1) in enumerate([(300, 1200), (450, 1500), (250, 900)], 1):
    add(P, f'pop_bubble_{i}', 'Bubble pop (rising chirp)', ['bubble', 'pop', 'cute'],
        partial(pop, f0, f1, 0.12, 32, 0.1, 45))


@sfx(P, 'pop_cork', 'Cork / bottle pop', ['cork', 'bottle', 'pop'])
def _():
    d = 0.25
    return mix(bp(white(d), 900, 1.5) * dec(d, 120) * 1.2, sine(geo(420, 160, d), d) * dec(d, 22, 0.001))


for i, (f0, f1) in enumerate([(600, 350), (800, 450)], 1):
    add(P, f'pop_soft_{i}', 'Soft muted pop', ['soft', 'pop', 'subtle'],
        lambda f0=f0, f1=f1: lp(pop(f0, f1, 0.14, 30, 0.1), 1600))
add(P, 'pop_high', 'High, bright pop', ['high', 'bright', 'pop'], partial(pop, 2600, 1800, 0.09, 55, 0.2))
for i, (f0, f1, d) in enumerate([(200, 700, 0.2), (260, 900, 0.16)], 1):
    add(P, f'bloop_{i}', 'Watery bloop', ['bloop', 'water', 'cute'],
        lambda f0=f0, f1=f1, d=d: sine(geo(f0, f1, d), d) * swell(d, 0.25, 1, 1.5))


@sfx(P, 'pop_mouth', 'Mouth / lip pop', ['mouth', 'lip', 'pop'])
def _():
    d = 0.07
    return lp(white(d), 2200) * dec(d, 140) * 0.6 + sine(geo(420, 240, d), d) * dec(d, 50)


@sfx(P, 'pop_double', 'Two quick pops', ['double', 'pop'])
def _():
    return mixat([(0, pop(900, 500)), (0.09, pop(1300, 700), 0.85)])


UI = 'ui'
for i, (f, k) in enumerate([(3200, 260), (2200, 220), (4500, 320), (1600, 200)], 1):
    add(UI, f'click_{i}', 'Crisp UI click', ['click', 'ui', 'button'], partial(click, f, 0.05, k))
for i, f in enumerate([1800, 1300], 1):
    add(UI, f'click_soft_{i}', 'Soft muted click', ['click', 'soft', 'ui'], lambda f=f: lp(click(f, 0.06, 140), 2500))


@sfx(UI, 'click_mouse', 'Mouse click (press + release)', ['mouse', 'click', 'computer'])
def _():
    return mixat([(0, click(3000, 0.04, 300)), (0.075, click(3600, 0.03, 380), 0.55)])


for i, f in enumerate([1200, 800, 2000], 1):
    add(UI, f'tap_{i}', 'Finger tap on glass', ['tap', 'touch', 'phone'],
        lambda f=f: sine(f, 0.08) * dec(0.08, 60, 0.0005) + 0.3 * bp(white(0.08), f * 2, 2) * dec(0.08, 200))


def toggle(up=True):
    a, b = (800, 1250) if up else (1250, 800)
    return mixat([(0, click(2600, 0.03, 300), 0.6), (0.0, beep(a, 0.045, 'tri') * dec(0.045, 30)),
                  (0.05, beep(b, 0.07, 'tri') * dec(0.07, 30))])


add(UI, 'toggle_on', 'Switch on (up blip)', ['toggle', 'on', 'switch'], partial(toggle, True))
add(UI, 'toggle_off', 'Switch off (down blip)', ['toggle', 'off', 'switch'], partial(toggle, False))
for i, f in enumerate([1000, 1500, 2100], 1):
    add(UI, f'blip_{i}', 'Short digital blip', ['blip', 'beep', 'ui'],
        lambda f=f: fm(f, f * 2, 0.6, 0.08) * dec(0.08, 35, 0.002))
add(UI, 'blip_up', 'Blip sliding up', ['blip', 'up'], lambda: sine(geo(600, 1500, 0.09), 0.09) * gate(0.09, 0.002, 0.03))
add(UI, 'blip_down', 'Blip sliding down', ['blip', 'down'], lambda: sine(geo(1500, 600, 0.09), 0.09) * gate(0.09, 0.002, 0.03))
add(UI, 'blip_retro_1', 'Square-wave retro blip', ['retro', 'blip', 'square'], lambda: lp(sq(880, 0.07, 0.25), 5000) * gate(0.07, 0.001, 0.02))
add(UI, 'blip_retro_2', 'Two-note retro blip', ['retro', 'blip', 'square'], lambda: chip([('A5', 0.04), ('E6', 0.07)], duty=0.25))
add(UI, 'ui_select', 'Pleasant select tone', ['select', 'menu', 'ui'], lambda: mel([(0, 'E6', 0.12), (0.06, 'B6', 0.18)], marimba))
add(UI, 'ui_back', 'Back / close tone', ['back', 'close', 'ui'], lambda: mel([(0, 'B5', 0.12), (0.06, 'E5', 0.18)], marimba))
add(UI, 'ui_hover', 'Very soft hover tick', ['hover', 'soft', 'ui'], lambda: lp(sine(3200, 0.035) * dec(0.035, 90, 0.002), 4000))
add(UI, 'ui_confirm', 'Three-note confirm', ['confirm', 'ok', 'ui'], lambda: mel([(0, 'C6', 0.15), (0.06, 'E6', 0.15), (0.12, 'G6', 0.3)], marimba))
add(UI, 'ui_cancel', 'Low two-note cancel', ['cancel', 'no', 'ui'],
    lambda: chip([('E4', 0.07), ('C4', 0.12)], 'tri') * 0.9)

D = 'ding'
for i, f in enumerate([1320, 1760, 1046], 1):
    add(D, f'ding_{i}', 'Clean bell ding', ['ding', 'bell', 'notification'], lambda f=f: verb(bell(f, 1.3), 0.7, 0.15))
add(D, 'ding_success', 'Two-note success ding', ['success', 'ding', 'correct'],
    lambda: verb(mel([(0, 'C6', 1.0), (0.12, 'G6', 1.3)], partial(bell, k=3.5)), 0.8, 0.18))
for i, root in enumerate(['C5', 'G5'], 1):
    def _chime(root=root, up=True):
        m = nf(root)
        notes = [(j * 0.09, m * r, 1.4) for j, r in enumerate([1, 1.26, 1.5, 2])]
        return verb(mel(notes, partial(bell, k=2.8)), 1.2, 0.25)
    add(D, f'chime_up_{i}', 'Rising bell arpeggio', ['chime', 'up', 'magic'], _chime)
add(D, 'chime_down', 'Falling bell arpeggio', ['chime', 'down'],
    lambda: verb(mel([(j * 0.09, nf('C6') * r, 1.4) for j, r in enumerate([2, 1.5, 1.26, 1])], partial(bell, k=2.8)), 1.2, 0.25))
for i, f in enumerate([2650, 3300], 1):
    add(D, f'bell_small_{i}', 'Desk / service bell', ['bell', 'desk', 'service'],
        lambda f=f: verb(mix(bell(f, 2.0, (1, 2.32, 4.25, 6.63), (1, .5, .3, .15), 1.6, 1.2), 0.3 * click(5000, 0.02, 400)), 0.6, 0.12))
NOTIFS = [[(0, 'E6', .3), (0.1, 'B6', .5)], [(0, 'G5', .3), (0.09, 'D6', .3), (0.18, 'G6', .5)], [(0, 'A6', .25), (0.08, 'A6', .4)]]
for i, n in enumerate(NOTIFS, 1):
    add(D, f'notif_{i}', 'Phone-style notification', ['notification', 'alert', 'phone'], lambda n=n: verb(mel(n, marimba), 0.6, 0.15))
for i, (a, b) in enumerate([(700, 1400), (900, 1600)], 1):
    def _msg(a=a, b=b):
        d = 0.09
        return mixat([(0, sine(geo(a, a * 1.4, d), d) * gate(d, 0.002, 0.03)), (0.1, sine(geo(b * 0.8, b, d), d) * gate(d, 0.002, 0.03))])
    add(D, f'notif_message_{i}', 'New message bubble', ['message', 'chat', 'notification'], _msg)
for i, root in enumerate(['C5', 'F5'], 1):
    def _lvl(root=root):
        m = nf(root)
        steps = [1, 1.26, 1.5, 2, 2.52, 3, 4]
        x = chip([(m * s, 0.05) for s in steps[:-1]] + [(m * 4, 0.3)], 'sq', 0.25)
        return verb(x * 0.8, 0.6, 0.2)
    add(D, f'level_up_{i}', 'Fast level-up arpeggio', ['level', 'up', 'win', 'game'], _lvl)

SO = 'social'
add(SO, 'like_pop', 'Like / heart tap', ['like', 'heart', 'social'],
    lambda: mixat([(0, pop(800, 1300, 0.12, 34, 0.1, 45)), (0.05, bell(2640, 0.6, k=6), 0.25)]))
add(SO, 'heart_pop', 'Heart burst with sparkle', ['heart', 'love', 'social'],
    lambda: verb(mixat([(0, pop(400, 1400, 0.14, 30, 0.1, 40))] + [(0.06 + j * 0.05, bell(nf(n), 0.5, k=7), 0.25) for j, n in enumerate(['E7', 'G7', 'B7'])]), 0.6, 0.2))
add(SO, 'follow_ding', 'Follow / subscribe ding', ['follow', 'subscribe', 'social'],
    lambda: verb(mel([(0, 'A5', .6), (0.08, 'E6', .9)], partial(bell, k=4)), 0.7, 0.15))
add(SO, 'comment_blip', 'New comment double blip', ['comment', 'blip', 'social'],
    lambda: mixat([(0, sine(1400, 0.05) * gate(0.05)), (0.07, sine(1900, 0.06) * gate(0.06))]))
add(SO, 'share_swoosh', 'Share: swoosh + blip', ['share', 'send', 'social'],
    lambda: mixat([(0, sweep(white(0.25), 'bp', geo(1200, 5000, 0.25), 1.3) * swell(0.25, 0.7, 2, 1)), (0.2, sine(geo(1200, 1800, 0.07), 0.07) * gate(0.07), 0.6)]))
add(SO, 'message_sent', 'Message sent "whoop"', ['sent', 'message', 'chat'],
    lambda: mix(sine(geo(500, 1800, 0.16), 0.16) * swell(0.16, 0.4, 1, 1.5), 0.4 * sweep(white(0.16), 'bp', geo(1500, 6000, 0.16), 1.5) * swell(0.16, 0.6)))
add(SO, 'message_received', 'Message received pluck', ['received', 'message', 'chat'],
    lambda: verb(mel([(0, 'D6', .35), (0.09, 'A6', .45)], marimba), 0.5, 0.12))


def vibrate(pattern):
    ev = []
    for t, d in pattern:
        x = lp(sq(160 + rnd(-4, 4), d, 0.3), 900) * (0.6 + 0.4 * (wander(d, 40, 0, 1) > 0.3)) * gate(d, 0.01, 0.03)
        ev.append((t, x + 0.2 * bp(white(d), 3000, 2) * gate(d, 0.01, 0.03)))
    return mixat(ev)


add(SO, 'vibrate_1', 'Phone vibration buzz-buzz', ['vibrate', 'phone', 'buzz'], partial(vibrate, [(0, 0.4), (0.55, 0.4)]))
add(SO, 'vibrate_2', 'Short single vibration', ['vibrate', 'phone', 'short'], partial(vibrate, [(0, 0.25)]))


@sfx(SO, 'ringtone', 'Original marimba ringtone', ['ringtone', 'phone', 'call'])
def _():
    line = ['E5', 'G5', 'D6', 'B5', 'G5', 'A5', 'D6', 'G6']
    return verb(mel([(i * 0.15, n, 0.5) for i, n in enumerate(line)] * 1 + [(1.35 + i * 0.15, n, 0.5) for i, n in enumerate(line)], marimba), 0.6, 0.15)


@sfx(SO, 'notification_stack', 'Several notifications in a row', ['notification', 'many', 'viral'])
def _():
    return mixat([(t, mel([(0, n1, .3), (0.08, n2, .4)], marimba), g) for t, n1, n2, g in
                  [(0, 'E6', 'B6', 1), (0.22, 'G5', 'D6', 0.8), (0.4, 'A5', 'E6', 0.9), (0.55, 'C6', 'G6', 0.8)]])


M = 'money'


def coinping(f=3600, d=0.6):
    return mix(metal(f, d, 6.0, 5, 0.3) * 0.8, 0.2 * click(f * 1.5, 0.02, 400))


def jingle(d=0.5, n=10, f=(2800, 5200)):
    return mixat([(rnd(0, d * 0.6), pan(coinping(rnd(*f), 0.4), rnd(-0.7, 0.7)), rnd(0.3, 0.9)) for _ in range(n)])


def register(two=False):
    ev = [(0, kick(0.25, 140, 60, 40, 20, 0.6), 0.6), (0.0, pulses(np.arange(0, 0.12, 0.012), hp(white(0.004), 2000), 0.15), 0.6)]
    b = bell(2350, 1.4, (1, 1.52, 2.43, 3.6), (1, .6, .4, .2), 2.2, 0.8)
    ev += [(0.12, b, 1.0)] + ([(0.03, bell(1900, 0.5, (1, 1.52, 2.43), (1, .5, .3), 7), 0.6)] if two else [])
    ev.append((0.18, jingle(0.6, 12), 0.5))
    return verb(mixat(ev), 0.5, 0.12)


add(M, 'cash_register_1', 'Cash register "ka-ching"', ['cash', 'register', 'sale', 'money'], partial(register, False))
add(M, 'cash_register_2', 'Cash register with double bell', ['cash', 'register', 'sale', 'money'], partial(register, True))
add(M, 'coin_1', 'Single coin ping', ['coin', 'money', 'ping'], lambda: coinping(3600, 0.7))


@sfx(M, 'coin_2', 'Coin dropping on a table', ['coin', 'drop', 'table'])
def _():
    ts, t, g = [], 0.0, []
    for k in range(9):
        ts.append(t)
        g.append(0.85 ** k)
        t += 0.13 * 0.72 ** k
    return mixat([(tt, coinping(3400, 0.25) * gg) for tt, gg in zip(ts, g)])


add(M, 'coin_3', 'Bright coin collect', ['coin', 'collect', 'reward'],
    lambda: verb(mixat([(0, coinping(2700, 0.4)), (0.07, coinping(4000, 0.8))]), 0.5, 0.15))
for i, (d, n) in enumerate([(0.8, 25), (1.2, 50)], 1):
    add(M, f'coins_drop_{i}', 'Pile of coins pouring', ['coins', 'pour', 'money'],
        lambda d=d, n=n: mixat([(min(rnd(0, 1) ** 1.5 * d, d), pan(coinping(rnd(2600, 5400), 0.35), rnd(-0.8, 0.8)), rnd(0.3, 1)) for _ in range(n)]))


def counter(d=1.5, end=False):
    ts = np.arange(0, d, 0.032)
    ev = [(t, click(2400 + 1200 * t / d, 0.02, 400), 0.7) for t in ts]
    if end:
        ev.append((d, verb(bell(1760, 1.0), 0.6, 0.15)))
    return mixat(ev)


add(M, 'counter_roll_1', 'Number counter rolling up', ['counter', 'numbers', 'count'], partial(counter, 1.5, False))
add(M, 'counter_roll_2', 'Counter rolling then ding', ['counter', 'numbers', 'ding'], partial(counter, 1.2, True))
add(M, 'cha_ching', 'Bright two-bell cha-ching', ['cha-ching', 'money', 'win'],
    lambda: verb(mixat([(0, bell(1800, 0.4, k=8), 0.7), (0.1, bell(2700, 1.4, (1, 1.52, 2.43), (1, .6, .4), 2.4)), (0.12, jingle(0.4, 8), 0.4)]), 0.6, 0.15))
add(M, 'money_counter', 'Bills flicking through a counter', ['bills', 'cash', 'counting'],
    lambda: mixat([(t, bp(white(0.03), 3500, 1.2) * dec(0.03, 90), rnd(0.6, 1)) for t in np.arange(0, 1.2, 0.035)]))

TY = 'typing'


def key(thock=180, cf=3200, soft=0.0):
    d = 0.07
    x = bp(white(d), cf * rnd(0.85, 1.15), 1.6) * dec(d, 170) + 0.6 * sine(thock * geo(1.3, 1, d) * rnd(0.9, 1.1), d) * dec(d, 70)
    return lp(x, 6000 - 4000 * soft)


def typing(d=1.6, gap=(0.06, 0.14), thock=180, cf=3200, soft=0.0):
    ts, t = [], 0.0
    while t < d:
        ts.append(t)
        t += rnd(*gap)
    return mixat([(t, key(thock, cf, soft), rnd(0.6, 1)) for t in ts])


add(TY, 'typing_1', 'Mechanical keyboard typing', ['typing', 'keyboard', 'mechanical'], partial(typing, 1.6))
add(TY, 'typing_2', 'Soft laptop typing', ['typing', 'laptop', 'soft'], partial(typing, 1.6, (0.07, 0.16), 260, 2400, 0.6))
add(TY, 'typing_3', 'Clicky keyboard typing', ['typing', 'clicky'], partial(typing, 1.6, (0.06, 0.13), 150, 4200))
add(TY, 'typing_fast', 'Very fast typing burst', ['typing', 'fast', 'hacker'], partial(typing, 1.4, (0.035, 0.07)))
add(TY, 'key_single_1', 'Single key press', ['key', 'press'], partial(key, 180, 3200))
add(TY, 'key_single_2', 'Soft single key press', ['key', 'soft'], partial(key, 260, 2400, 0.6))
add(TY, 'key_enter', 'Big enter / spacebar press', ['enter', 'spacebar', 'key'],
    lambda: mixat([(0, key(120, 2200)), (0.012, bp(white(0.06), 1800, 2) * dec(0.06, 80), 0.6), (0.09, key(160, 2800), 0.5)]))


@sfx(TY, 'typewriter_bell', 'Typewriter clacks, bell and carriage return', ['typewriter', 'retro', 'bell'])
def _():
    clack = lambda: mix(click(2200, 0.06, 120) * 1.2, kick(0.08, 300, 150, 60, 50, 0)) * rnd(0.7, 1)
    ev = [(t, clack()) for t in (0, 0.15, 0.27, 0.42)]
    ev.append((0.6, bell(2900, 1.0, (1, 2.7, 5.1), (1, .4, .2), 3.5)))
    d = 0.45
    ev.append((0.8, bp(white(d), 2500, 1) * trem(d, 45, 0.7) * swell(d, 0.3, 1, 1), 0.6))
    return mixat(ev)


add(TY, 'typewriter_keys', 'Typewriter typing', ['typewriter', 'typing', 'retro'],
    lambda: mixat([(t, mix(click(2200, 0.06, 120), kick(0.08, 300, 150, 60, 50, 0)) * rnd(0.6, 1)) for t in np.cumsum(rnd(0.09, 0.2, 10))]))

TM = 'timer'
add(TM, 'tick_1', 'Clock tick', ['tick', 'clock'], lambda: click(2600, 0.04, 300) + 0.4 * sine(1200, 0.04) * dec(0.04, 120))
add(TM, 'tick_2', 'Woody tick', ['tick', 'wood'], lambda: mix(sine(1700, 0.05) * dec(0.05, 90), 0.3 * click(4000, 0.03, 400)))
add(TM, 'clock_tick', 'Tick-tock clock (2.5 s)', ['clock', 'tick', 'tock', 'waiting'],
    lambda: mixat([(i * 0.5, click(2600 if i % 2 == 0 else 1900, 0.05, 260)) for i in range(5)]))


def countdown(step=1.0, f=880):
    ev = [(i * step, beep(f, 0.15, 'sine') * 0.9) for i in range(3)]
    ev.append((3 * step, beep(f * 2, 0.6, 'sine') * dec(0.6, 2)))
    return mixat(ev)


add(TM, 'countdown_beep_1', '3-2-1-GO race beeps', ['countdown', 'start', 'race'], partial(countdown, 1.0))
add(TM, 'countdown_beep_2', 'Fast 3-2-1 beeps', ['countdown', 'fast'], partial(countdown, 0.5, 1046))
add(TM, 'timer_done', 'Digital timer alarm', ['timer', 'alarm', 'done'],
    lambda: mixat([(g * 0.6 + i * 0.1, lp(sq(2000, 0.06), 6000) * gate(0.06, 0.001, 0.005), 0.5) for g in range(2) for i in range(4)]))
add(TM, 'stopwatch', 'Stopwatch start click and ticking', ['stopwatch', 'timer', 'tick'],
    lambda: mixat([(0, click(3000, 0.05, 200))] + [(0.2 + i * 0.125, click(4200, 0.02, 500), 0.4) for i in range(12)]))
add(TM, 'metronome', 'Four metronome clicks (120 bpm)', ['metronome', 'beat', 'count'],
    lambda: mixat([(i * 0.5, sine(1800 if i == 0 else 1200, 0.05) * dec(0.05, 80), 1 if i == 0 else 0.8) for i in range(4)]))

AL = 'alert'
add(AL, 'error_1', 'Two-tone error', ['error', 'wrong', 'fail'],
    lambda: chip([(380, 0.12), (280, 0.22)], 'sq', 0.5, 0.03) * 0.6)
add(AL, 'error_2', 'Triple low error beep', ['error', 'denied'],
    lambda: mixat([(i * 0.12, lp(sq(220, 0.09), 1800) * gate(0.09), 0.6) for i in range(3)]))
add(AL, 'error_buzz', 'Harsh error buzz', ['buzz', 'error', 'harsh'],
    lambda: drive(lp(saw(110, 0.5) + sq(111.5, 0.5), 2500) * gate(0.5, 0.005, 0.05), 2.5) * 0.6)
add(AL, 'wrong_buzzer', 'Game-show wrong-answer buzzer', ['wrong', 'buzzer', 'quiz'],
    lambda: drive(lp(saw(150, 0.8) + saw(157, 0.8) + saw(75, 0.8), 2200) * gate(0.8, 0.01, 0.1), 2.0) * 0.5)
add(AL, 'correct_1', 'Correct-answer chime', ['correct', 'right', 'quiz'],
    lambda: verb(mel([(0, 'C6', .5), (0.1, 'E6', .5), (0.2, 'G6', .9)], lambda f, d: (sine(f, d) + 0.3 * tri(f, d)) * dec(d, 5, 0.003)), 0.6, 0.18))
add(AL, 'correct_2', 'Bright two-note correct', ['correct', 'yes', 'quiz'],
    lambda: verb(mel([(0, 'G5', .4), (0.12, 'D6', .9)], lambda f, d: (sine(f, d) + 0.4 * sq(f, d, 0.25) * 0.3) * dec(d, 4.5, 0.003)), 0.6, 0.15))
add(AL, 'alarm_beep_1', 'Four urgent beeps', ['alarm', 'beep', 'urgent'],
    lambda: mixat([(i * 0.18, lp(sq(2400, 0.1), 7000) * gate(0.1, 0.001, 0.01), 0.5) for i in range(4)]))
add(AL, 'alarm_beep_2', 'Hi-lo alarm', ['alarm', 'hi-lo', 'warning'],
    lambda: mixat([(i * 0.25, lp(saw(960 if i % 2 == 0 else 720, 0.24), 3000) * gate(0.24, 0.005, 0.01), 0.5) for i in range(6)]))
add(AL, 'censor_beep', 'Censor bleep (1 kHz)', ['censor', 'bleep', 'beep'], lambda: sine(1000, 0.6) * gate(0.6, 0.004, 0.004) * 0.5)
add(AL, 'warning_siren', 'Siren sweep up and down', ['siren', 'warning', 'emergency'],
    lambda: lp(saw(800 + 400 * np.sin(ph(1.0, 2.0) - np.pi / 2), 2.0), 3500) * gate(2.0, 0.05, 0.2) * 0.5)
add(AL, 'attention_ping', 'Sonar-like attention ping', ['ping', 'sonar', 'attention'],
    lambda: verb(sine(1500, 0.6) * dec(0.6, 6, 0.004), 1.6, 0.4))
add(AL, 'beep_short', 'Short beep', ['beep', 'short'], lambda: beep(1200, 0.12) * 0.8)
