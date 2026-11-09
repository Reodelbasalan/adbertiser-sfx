"""Batch 3: festive, horror, sports, food, extra UI."""
from functools import partial
from dsp import *
from r_motion import whoosh, cymbal
from r_ui import pop, coinping
from r_more import voice, claps

FE = 'festive'


@sfx(FE, 'jingle_bells', 'Sleigh / jingle bells shaking (2 s)', ['jingle', 'christmas', 'bells', 'pasko'])
def _():
    ev = []
    for b in range(8):
        t0 = b * 0.25
        for _ in range(7):
            ev.append((t0 + rnd(0, 0.05), pan(coinping(rnd(3500, 6500), 0.35), rnd(-0.6, 0.6)), rnd(0.3, 1) * (1 if b % 2 == 0 else 0.7)))
    return verb(mixat(ev), 0.6, 0.15)


def reed(f, d, nasal=1000):
    s = drive(sq(f, d, 0.35) + 0.6 * saw(f * 1.002, d), 2.5) * (0.85 + 0.15 * wander(d, 25, 0, 1))
    return mix(bp(s, nasal, 1.0), 0.6 * bp(s, nasal * 2.4, 2.0), 0.15 * bp(white(d), 2500, 1))


add(FE, 'party_horn_1', 'Party horn / torotot blow', ['torotot', 'party horn', 'new year', 'bagong taon'],
    lambda: reed(ramp(300, 330, 0.9), 0.9) * gate(0.9, 0.04, 0.1))
add(FE, 'party_horn_2', 'Party blowout toot', ['party', 'blowout', 'birthday'],
    lambda: mixat([(0, reed(geo(380, 520, 0.35), 0.35, 1400) * gate(0.35, 0.02, 0.05)), (0.05, crackle(0.3, 0.3, 2000, 8000), 0.4)]))
add(FE, 'confetti_popper', 'Confetti popper bang + falling confetti', ['confetti', 'popper', 'celebration'],
    lambda: verb(mixat([(0, mix(bp(white(0.08), 1500, 0.8) * dec(0.08, 45), 0.5 * pop(600, 250, 0.1, 30, 0))), (0.05, crackle(1.2, 0.08, 2500, 9000) * dec(1.2, 2), 0.5)]), 0.7, 0.15))


def airhorn(d=1.0):
    s = sum(saw(f * (1 + k * 0.004), d) for f in (440, 554, 659) for k in (-1, 1)) / 6
    return drive(lp(s, 3500), 3) * gate(d, 0.015, 0.06)


add(FE, 'air_horn_1', 'Air horn blast', ['air horn', 'hype', 'party'], lambda: verb(airhorn(1.0), 0.6, 0.15))
add(FE, 'air_horn_2', 'Air horn x3 (short-short-long)', ['air horn', 'hype', 'triple'],
    lambda: verb(mixat([(0, airhorn(0.16)), (0.22, airhorn(0.16)), (0.44, airhorn(0.8))]), 0.6, 0.15))


@sfx(FE, 'firecracker_string', 'String of firecrackers (2.5 s)', ['firecracker', 'paputok', 'new year'])
def _():
    ts, t = [], 0.0
    while t < 2.4:
        ts.append(t)
        t += rnd(0.025, 0.09)
    bang = lambda: mix(hp(white(0.05), 400) * dec(0.05, 70), 0.5 * lp(kick(0.08, 180, 90, 40, 40, 0), 800))
    return verb(mixat([(t, pan(bang(), rnd(-0.7, 0.7)), rnd(0.4, 1)) for t in ts]), 1.2, 0.25, 5000)


HO = 'horror'
add(HO, 'music_box_creepy', 'Out-of-tune creepy music box', ['music box', 'creepy', 'horror'],
    lambda: verb(mixat([(i * 0.32, mix(pluck(nf(n) * rnd(0.985, 1.0), 1.2, 0.997, 0.9), 0.3 * bell(nf(n) * 2, 0.6, k=6)), 0.8) for i, n in enumerate(['A5', 'C6', 'E6', 'D#6', 'C6', 'A5', 'G#5', 'B5', 'A5'])]), 1.8, 0.35))


def jump_scare(pre=False):
    d = 1.4
    stab = lp(sum(saw(nf(n) * (1 + k * 0.006), d) for n in ('C3', 'C#4', 'G4', 'F#5') for k in (-1, 1)), 5000) * dec(d, 2.5, 0.003) * 0.25
    screech = sum(sine(f * (1 + 0.02 * np.sin(ph(rnd(7, 12), d))), d) for f in (2300, 2410, 3150)) * dec(d, 3, 0.003) * 0.25
    hit = mix(kick(0.8, 110, 40, 20, 5, 0.6), 0.6 * hp(white(0.15), 800) * dec(0.15, 25))
    x = verb(mix(stab, screech, hit), 1.8, 0.3)
    if pre:
        return mixat([(0, rev(verb(hp(white(0.6), 2000) * dec(0.6, 6), 0.8, 0.5)), 0.5), (0.85, x)])
    return x


add(HO, 'jump_scare_1', 'Sudden jump-scare stab', ['jump scare', 'scary', 'horror'], partial(jump_scare, False))
add(HO, 'jump_scare_2', 'Reverse swell into a scare', ['jump scare', 'scary', 'horror'], partial(jump_scare, True))
add(HO, 'ghost_whoosh', 'Ghostly moaning whoosh', ['ghost', 'spooky', 'whoosh'],
    lambda: verb(mix(pan(voice(1.8, 160, 1 + 0.3 * np.sin(np.pi * U(1.8)) + 0.05 * np.sin(ph(3, 1.8)), 'u') * swell(1.8, 0.5, 1.5, 1.5), ramp(-0.6, 0.6, 1.8)),
                     0.6 * whoosh(1.8, 300, 1500, 400, 1.0, 0.5)), 2.5, 0.45))
add(HO, 'dun_dun_dunnn', 'Dramatic "dun dun DUNNN"', ['dramatic', 'reveal', 'shock'],
    lambda: verb(mixat([(t, mix(brass(nf(n), d, 2200, 0.005, 0.02 if d > 1 else 0), 0.7 * lp(kick(0.8, 100, 70, 6, 4, 0.2), 500))) for t, n, d in ((0, 'A2', 0.3), (0.42, 'C3', 0.3), (0.84, 'D#3', 1.6))]), 1.8, 0.3))
add(HO, 'creak_long', 'Long creepy creak', ['creak', 'door', 'haunted'],
    lambda: bp(pulses(np.cumsum(1 / wander(1.8, 6, 50, 190)[::N(0.004)]), bp(white(0.004), 1200, 3), 1.8), 1300, 1.5) * gate(1.8, 0.1, 0.2))

SP = 'sports'


@sfx(SP, 'basketball_bounce', 'Basketball dribble', ['basketball', 'bounce', 'ball'])
def _():
    ts, t, g = [], 0.0, 1.0
    for k in range(5):
        ts.append((t, g))
        t += 0.42 * 0.82 ** k
        g *= 0.85
    b = lambda: mix(sine(geo(150, 90, 0.15), 0.15) * dec(0.15, 25, 0.0005), 0.5 * bp(white(0.06), 500, 1) * dec(0.06, 60), 0.15 * sine(420, 0.15) * dec(0.15, 30))
    return verb(mixat([(t, b(), g) for t, g in ts]), 0.9, 0.2)


add(SP, 'boxing_bell', 'Boxing ring bell ding-ding-ding', ['boxing', 'bell', 'round', 'fight'],
    lambda: verb(mixat([(i * 0.22, metal(1150, 1.6, 1.8, 7, 0.2)) for i in range(3)]), 1.0, 0.2))
add(SP, 'stadium_horn', 'Big stadium horn', ['stadium', 'horn', 'goal'],
    lambda: verb(drive(lp(sum(saw(f * (1 + k * 0.003), 1.6) for f in (110, 220, 277) for k in (-1, 1)) / 6, 2200), 2.5) * gate(1.6, 0.06, 0.25), 2.2, 0.3))
add(SP, 'ball_kick', 'Ball kick', ['kick', 'ball', 'football'],
    lambda: mix(lp(kick(0.2, 200, 90, 40, 18, 0), 1200), 0.6 * bp(white(0.05), 1500, 1) * dec(0.05, 80)))
add(SP, 'racket_hit', 'Tennis / badminton racket hit', ['tennis', 'racket', 'hit'],
    lambda: mix(sine(700, 0.2) * dec(0.2, 40, 0.0005), 0.4 * sine(1850, 0.3) * dec(0.3, 18), 0.4 * click(3000, 0.02, 300)))

FD = 'food'
add(FD, 'sizzle', 'Frying / sizzling pan (4 s)', ['sizzle', 'frying', 'cooking', 'prito'],
    lambda: mix(np.stack([crackle(4.0, 0.25, 2500, 11000) for _ in range(2)]), 0.25 * hp(white(4.0), 4000) * wander(4.0, 3, 0.6, 1)) * gate(4.0, 0.15, 0.3))


def crunch(d=0.25):
    return mix(crackle(d, 0.55, 1200, 9000) * dec(d, 9, 0.002), 0.5 * lp(kick(0.12, 140, 80, 40, 25, 0), 500))


add(FD, 'crunch_1', 'Crunchy chip bite', ['crunch', 'chips', 'bite', 'snack'], partial(crunch, 0.25))
add(FD, 'crunch_2', 'Crunchy chewing', ['crunch', 'chewing', 'snack'],
    lambda: mixat([(t, crunch(0.2), g) for t, g in ((0, 1), (0.32, 0.7), (0.6, 0.55), (0.86, 0.4))]))
add(FD, 'can_open_fizz', 'Soda can open + fizz', ['soda', 'can', 'fizz', 'drink'],
    lambda: mixat([(0, click(2500, 0.04, 200)), (0.03, hp(white(0.25), 2500) * dec(0.25, 12, 0.005), 0.8), (0.1, crackle(1.5, 0.12, 4000, 12000) * dec(1.5, 1.8), 0.5)]))
add(FD, 'pour', 'Pouring a drink into a glass', ['pour', 'drink', 'glass', 'water'],
    lambda: (sweep(pink(2.0), 'bp', geo(450, 1700, 2.0), 4) * (0.6 + 0.4 * wander(2.0, 20, 0, 1)) + 0.1 * crackle(2.0, 0.05, 2000, 7000)) * gate(2.0, 0.08, 0.2))
add(FD, 'splash', 'Water splash', ['splash', 'water', 'pool'],
    lambda: verb(mixat([(0, lp(white(0.6), 5000) * dec(0.6, 7, 0.004)), (0, lp(kick(0.2, 150, 70, 30, 15, 0), 600), 0.5)] +
                       [(rnd(0.05, 0.6), pan(sine(geo(f, f * 2, 0.04), 0.04) * swell(0.04, 0.3), rnd(-0.7, 0.7)), rnd(0.2, 0.6)) for f in rnd(400, 1500, 18)]), 0.6, 0.15))
add(FD, 'chopping', 'Knife chopping on a board', ['chopping', 'knife', 'kitchen'],
    lambda: mixat([(i * 0.21, mix(sine(geo(500, 380, 0.08), 0.08) * dec(0.08, 50), 0.5 * click(3500, 0.03, 300), 0.3 * lp(white(0.05), 2000) * dec(0.05, 80)), rnd(0.7, 1)) for i in range(6)]))

UI = 'ui'
add(UI, 'lock', 'Lock (click + clunk)', ['lock', 'secure', 'ui'],
    lambda: mixat([(0, click(2200, 0.04, 220)), (0.06, lp(kick(0.12, 260, 140, 50, 30, 0), 1200), 0.7)]))
add(UI, 'unlock', 'Unlock (clunk + up blip)', ['unlock', 'open', 'ui'],
    lambda: mixat([(0, lp(kick(0.12, 260, 140, 50, 30, 0), 1200), 0.7), (0.05, click(2600, 0.04, 250)), (0.1, sine(geo(900, 1500, 0.08), 0.08) * gate(0.08), 0.5)]))
add(UI, 'download_complete', 'Download complete', ['download', 'done', 'complete'],
    lambda: verb(mixat([(0, mel([(0, 'C6', .2), (0.07, 'E6', .2), (0.14, 'G6', .2)], marimba), 0.6), (0.22, bell(nf('C7'), 1.0, k=4))]), 0.6, 0.15))
add(UI, 'delete_trash', 'Delete: crumple into the trash', ['delete', 'trash', 'remove'],
    lambda: mixat([(0, crackle(0.25, 0.4, 1500, 8000) * swell(0.25, 0.5), 0.8), (0.2, sweep(white(0.2), 'bp', geo(3000, 600, 0.2), 1.2) * swell(0.2, 0.3), 0.6), (0.4, lp(kick(0.12, 180, 100, 40, 25, 0), 900), 0.6)]))
add(UI, 'upload_whoosh', 'Upload / send whoosh with blip', ['upload', 'send', 'whoosh'],
    lambda: mixat([(0, whoosh(0.35, 600, 4000, 4500, 1.2, 0.85, 2, 0.6), 0.8), (0.32, sine(geo(1300, 2000, 0.07), 0.07) * gate(0.07), 0.5)]))
