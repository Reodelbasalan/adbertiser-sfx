"""Cartoon, retro 8-bit, stingers/jingles, drums."""
from functools import partial
from dsp import *
from r_motion import whoosh, riser, cymbal
from r_fx import impact, sparkle

CT = 'cartoon'


def boing(f0=220, vr=12, d=0.8, depth=0.5, rise=1.0):
    t = T(d)
    f = f0 * ramp(1, rise, d) * (1 + depth * np.exp(-t * 4) * np.sin(2 * np.pi * vr * t))
    x = sweep(tri(f, d) + 0.4 * saw(f, d), 'lp', f * 5, 1.5)
    return x * dec(d, 3.5, 0.002)


for i, (f0, vr) in enumerate([(220, 12), (160, 9), (300, 16)], 1):
    add(CT, f'boing_{i}', 'Cartoon boing', ['boing', 'bounce', 'funny'], partial(boing, f0, vr))
add(CT, 'spring', 'Springy sproing', ['spring', 'sproing', 'funny'],
    lambda: mix(boing(500, 18, 0.7, 0.35, 1.6), 0.25 * sine(2200, 0.7) * dec(0.7, 6)))


def slide_whistle(up=True, d=0.8):
    f = geo(500, 1800, d) if up else geo(1800, 500, d)
    f = f * (1 + 0.012 * np.sin(ph(6, d)))
    return (sine(f, d) + 0.15 * bp(white(d), 1500, 1)) * gate(d, 0.03, 0.08)


add(CT, 'slide_whistle_up', 'Slide whistle up', ['whistle', 'up', 'funny'], partial(slide_whistle, True))
add(CT, 'slide_whistle_down', 'Slide whistle down (falling)', ['whistle', 'down', 'fall'], partial(slide_whistle, False))
add(CT, 'bonk_1', 'Wood-block bonk', ['bonk', 'wood', 'hit'],
    lambda: mix(sine(900, 0.25) * dec(0.25, 30, 0.0005) + 0.5 * sine(2350, 0.25) * dec(0.25, 55), 0.3 * click(3000, 0.02, 400)))
add(CT, 'bonk_2', 'Head bonk', ['bonk', 'head', 'hit', 'funny'],
    lambda: mix(sine(geo(650, 330, 0.35), 0.35) * dec(0.35, 14, 0.001), 0.6 * lp(kick(0.2, 200, 90, 40, 20, 0), 900), 0.25 * sine(1650, 0.35) * dec(0.35, 20)))
for i, (rate, d) in enumerate([(6, 1.0), ((3, 14), 1.2)], 1):
    def _wob(rate=rate, d=d):
        r = ramp(rate[0], rate[1], d) if isinstance(rate, tuple) else rate
        cut = 300 + 2200 * (0.5 + 0.5 * np.sin(ph(r, d)))
        return sweep(saw(110, d) + saw(110.6, d), 'lp', cut, 3) * gate(d, 0.02, 0.1) * 0.5
    add(CT, f'wobble_{i}', 'Wah-wah wobble', ['wobble', 'wah', 'funny'], _wob)
add(CT, 'zip_1', 'Zip away (up)', ['zip', 'fast', 'away'], lambda: (sine(geo(300, 3000, 0.15), 0.15) + 0.3 * sq(geo(300, 3000, 0.15), 0.15)) * gate(0.15, 0.003, 0.03) * 0.7)
add(CT, 'zip_2', 'Zip down', ['zip', 'fast', 'down'], lambda: (sine(geo(3000, 300, 0.15), 0.15) + 0.3 * sq(geo(3000, 300, 0.15), 0.15)) * gate(0.15, 0.003, 0.03) * 0.7)
for i, (f, d) in enumerate([(1600, 0.25), (1200, 0.35)], 1):
    def _sq(f=f, d=d):
        fr = f * (1 + 0.25 * np.sin(np.pi * U(d)) - 0.1 * U(d))
        return (lp(sq(fr, d, 0.3), 5000) * 0.4 + sine(fr, d) + 0.2 * bp(white(d), 2200, 2)) * swell(d, 0.3, 1, 1)
    add(CT, f'squeak_{i}', 'Rubber toy squeak', ['squeak', 'toy', 'cute'], _sq)


@sfx(CT, 'wah_wah_fail', 'Sad descending "wah wah wah wahhh"', ['fail', 'sad', 'trombone', 'funny'])
def _():
    ev = []
    for j, (n, d) in enumerate([('Bb3', 0.42), ('A3', 0.42), ('Ab3', 0.42), ('G3', 1.3)]):
        s = brass(nf(n), d, 1600, 0.004, 0.03 if j == 3 else 0.0)
        s = sweep(s, 'lp', 300 + 1500 * swell(d, 0.25, 1, 1.5), 2)
        ev.append((j * 0.45, s))
    return verb(mixat(ev), 0.8, 0.15)


add(CT, 'tiptoe', 'Sneaky pizzicato tiptoe', ['tiptoe', 'sneak', 'pizzicato'],
    lambda: mixat([(j * 0.2, pluck(nf(n), 0.4, 0.98, 0.3)) for j, n in enumerate(['E4', 'B4', 'F4', 'C5', 'F#4', 'C#5', 'G4', 'D5'])]))
add(CT, 'run_away', 'Run-away blips + zoom', ['run', 'escape', 'fast'],
    lambda: mixat([(j * 0.03, beep(400 * 1.1 ** j, 0.028, 'tri'), 0.5) for j in range(16)] + [(0.45, whoosh(0.3, 800, 3500, 1500, 1.3, 0.5), 0.8)]))
add(CT, 'pop_eyes', 'Eyes-pop "boink"', ['surprise', 'eyes', 'boink'],
    lambda: mixat([(0, sine(geo(300, 1400, 0.08), 0.08) * gate(0.08)), (0.08, boing(700, 20, 0.4, 0.3), 0.6)]))
add(CT, 'drum_hit_fail', 'Comedy ba-dum-tss', ['rimshot', 'joke', 'funny'],
    lambda: mixat([(0, mix(snare(0.2), 0.5 * kick(0.2, 160, 120, 20, 15, 0))), (0.15, mix(snare(0.2), 0.5 * kick(0.2, 120, 90, 20, 15, 0))), (0.35, hp(cymbal(1.2), 4000), 0.6)]))

RE = 'retro'
add(RE, 'coin_8bit', '8-bit coin', ['coin', '8bit', 'game'], lambda: chip([('C6', 0.04), ('G6', 0.04), ('C7', 0.22)], 'sq', 0.5, k=6))
add(RE, 'jump_8bit', '8-bit jump', ['jump', '8bit', 'game'], lambda: lp(sq(geo(220, 680, 0.16), 0.16, 0.25), 7000) * gate(0.16, 0.002, 0.02))
add(RE, 'powerup_8bit', '8-bit power-up scale', ['powerup', '8bit', 'game'],
    lambda: chip([(nf('C5') * 2 ** (s / 12), 0.03) for s in [0, 4, 7, 2, 5, 9, 4, 7, 11, 5, 9, 12, 7, 11, 14, 12, 16, 19, 24]], 'sq', 0.25))
add(RE, 'laser_8bit', '8-bit laser', ['laser', '8bit', 'shoot'], lambda: lp(sq(geo(1800, 180, 0.2), 0.2), 7000) * gate(0.2, 0.001, 0.02))
add(RE, 'hit_8bit', '8-bit hit', ['hit', '8bit', 'damage'], lambda: mix(crush(white(0.1), 4, 16) * dec(0.1, 30), lp(sq(geo(220, 70, 0.12), 0.12), 4000) * gate(0.12)))
add(RE, 'explosion_8bit', '8-bit explosion', ['explosion', '8bit', 'boom'],
    lambda: crush(sweep(white(0.9), 'lp', geo(5000, 250, 0.9), 0.8) * dec(0.9, 3.5, 0.002), 4, 30))
add(RE, 'select_8bit', '8-bit menu select', ['select', '8bit', 'menu'], lambda: chip([('C6', 0.035), ('G6', 0.06)], 'sq', 0.5))
add(RE, 'gameover_8bit', '8-bit game-over tune', ['gameover', '8bit', 'lose'],
    lambda: chip([('G5', 0.16), ('D5', 0.16), ('Bb4', 0.16), ('A4', 0.16), ('G4', 0.6)], 'sq', 0.5, 0.02))
add(RE, 'extra_life_8bit', '8-bit extra life', ['life', '8bit', 'bonus'],
    lambda: chip([('C6', 0.06), ('E6', 0.06), ('G6', 0.06), ('C7', 0.06), ('G6', 0.06), ('C7', 0.18)], 'sq', 0.25))
add(RE, 'blip_8bit', '8-bit blip', ['blip', '8bit'], lambda: tri(880, 0.06) * gate(0.06, 0.001, 0.01))
add(RE, 'warp_8bit', '8-bit warp pipe', ['warp', '8bit', 'travel'],
    lambda: lp(sq(geo(1500, 200, 0.7) * (1 + 0.1 * np.sin(ph(20, 0.7))), 0.7), 7000) * gate(0.7, 0.002, 0.05))
add(RE, 'win_jingle_8bit', '8-bit victory jingle', ['win', '8bit', 'victory'],
    lambda: mix(chip([('G4', 0.1), ('C5', 0.1), ('E5', 0.1), ('G5', 0.25), ('E5', 0.1), ('G5', 0.5)], 'sq', 0.5, 0.02),
                0.5 * chip([('C3', 0.62), ('G3', 0.62)], 'tri', gap=0.0)))
add(RE, 'step_8bit', '8-bit footstep blips', ['step', '8bit', 'walk'], lambda: mixat([(j * 0.15, crush(white(0.03), 4, 10) * dec(0.03, 80), 0.6) for j in range(4)]))
add(RE, 'error_8bit', '8-bit error', ['error', '8bit', 'wrong'], lambda: chip([('E3', 0.08), ('C3', 0.2)], 'sq', 0.5, 0.02))

STG = 'stinger'
add(STG, 'success_jingle_1', 'Marimba success jingle', ['success', 'win', 'jingle'],
    lambda: verb(mixat([(0, mel([(j * 0.09, n, 0.5) for j, n in enumerate(['C5', 'E5', 'G5', 'C6'])], marimba)),
                        (0.38, mel([(0, 'C6', 1.4), (0, 'E6', 1.4), (0, 'G6', 1.4)], partial(bell, k=2.5)), 0.5)]), 1.0, 0.2))
add(STG, 'success_jingle_2', 'Plucked success jingle', ['success', 'jingle', 'happy'],
    lambda: verb(mixat([(j * 0.1, pluck(nf(n), 1.2, 0.997)) for j, n in enumerate(['G4', 'B4', 'D5', 'G5', 'B5'])] + [(0.5, sparkle(1.0, 14), 0.3)]), 1.0, 0.25))
add(STG, 'fail_jingle', 'Sad fail jingle', ['fail', 'lose', 'sad'],
    lambda: verb(mel([(0, 'G4', .5), (0.25, 'Eb4', .5), (0.5, 'C4', 1.2)], partial(marimba, k=4)), 1.0, 0.2))
add(STG, 'tada', 'Ta-da fanfare', ['tada', 'fanfare', 'reveal'],
    lambda: verb(mixat([(0, brass(nf('G4'), 0.12, 2500))] + [(0.13, brass(nf(n), 1.3, 3500, 0.004, 0.02), 0.8) for n in ('C5', 'E5', 'G5', 'C6')]), 1.2, 0.25))
add(STG, 'reveal_stinger', 'Build, hit and chord', ['reveal', 'stinger', 'drama'],
    lambda: mixat([(0, riser(0.8), 0.6), (0.8, impact(1.5, 120, 40, 18, 4, 0.5, 3000, 1.5, 1.2, 0.25)), (0.8, verb(pad([nf(n) for n in ('C3', 'G3', 'C4', 'E4')], 2.0, 2500), 1.5, 0.3), 0.8)]))
add(STG, 'transition_stinger', 'Whoosh into a chord stab', ['transition', 'stinger', 'stab'],
    lambda: mixat([(0, whoosh(0.4, 400, 2800, 2000, 1.1, 0.9, 2, 0.5), 0.8), (0.38, verb(mix(*[brass(nf(n), 0.5, 3000) for n in ('D4', 'F#4', 'A4', 'D5')]), 1.2, 0.3))]))
add(STG, 'suspense_hit', 'Low hit + dissonant stab', ['suspense', 'hit', 'drama'],
    lambda: mixat([(0, impact(1.5, 90, 35, 14, 3, 0.4, 2500, 1.8, 0, 0, 0.6)), (0, verb(lp(sum(saw(nf(n), 1.8) for n in ('C3', 'C#3', 'F#3', 'G4')), 2500) * dec(1.8, 2.2, 0.01) * 0.3, 1.8, 0.35))]))
add(STG, 'positive_chord', 'Warm uplifting chord swell', ['positive', 'chord', 'warm'],
    lambda: verb(pad([nf(n) for n in ('C3', 'G3', 'E4', 'B4', 'D5')], 2.2, 2000), 1.5, 0.3))
add(STG, 'mystery', 'Mysterious bell motif', ['mystery', 'curious', 'bell'],
    lambda: verb(mel([(0, 'C5', 1.5), (0.35, 'F#5', 1.5), (0.7, 'B4', 2.0)], partial(bell, k=1.8)), 2.0, 0.35))
add(STG, 'news_sting', 'Breaking-news style sting', ['news', 'breaking', 'urgent'],
    lambda: verb(mixat([(0, lp(kick(1.0, 110, 85, 6, 3.5, 0.2), 600), 0.8)] + [(t, brass(nf(n), d, 3500), 0.8) for t, n, d in ((0, 'D4', 0.12), (0.15, 'D4', 0.12), (0.3, 'F4', 0.12), (0.45, 'A4', 0.9))] + [(0.45, lp(kick(1.2, 100, 80, 6, 3, 0.2), 600), 0.8)]), 1.2, 0.2))
add(STG, 'question_hmm', 'Curious "hmm?" two-note', ['question', 'curious', 'hmm'],
    lambda: verb(mel([(0, 'E5', 0.3), (0.2, 'A5', 0.6)], partial(marimba, k=5)), 0.8, 0.15))

DR = 'drums'
add(DR, 'kick_1', 'Punchy kick', ['kick', 'drum', 'beat'], partial(kick, 0.45, 160, 48, 28, 8, 0.4))
add(DR, 'kick_2', 'Long 808-style kick', ['kick', '808', 'bass'], lambda: drive(kick(1.1, 140, 42, 20, 2.8, 0.3), 1.6))
add(DR, 'snare_1', 'Tight snare', ['snare', 'drum'], partial(snare, 0.3))
add(DR, 'snare_2', 'Big roomy snare', ['snare', 'big', 'reverb'], lambda: verb(snare(0.45, 170, 0.6, 10, 4000), 1.2, 0.35))
add(DR, 'clap_1', 'Hand clap', ['clap', 'hand'], partial(clap))
add(DR, 'clap_2', 'Clap with reverb', ['clap', 'reverb'], lambda: verb(clap(0.5, 1100, 14), 1.0, 0.35))
add(DR, 'hihat_closed', 'Closed hi-hat', ['hihat', 'hat'], partial(hat, 0.08, 60))
add(DR, 'hihat_open', 'Open hi-hat', ['hihat', 'open'], partial(hat, 0.5, 8))
add(DR, 'rim', 'Rim shot', ['rim', 'click', 'drum'], lambda: mix(sine(1650, 0.08) * dec(0.08, 70), click(3500, 0.03, 300) * 0.6))
add(DR, 'tom', 'Floor tom', ['tom', 'drum'], lambda: sine(geo(150, 95, 0.6), 0.6) * dec(0.6, 7, 0.001) + 0.2 * lp(white(0.6), 1500) * dec(0.6, 30))
add(DR, 'crash', 'Crash cymbal', ['crash', 'cymbal'], lambda: verb(cymbal(2.5), 1.0, 0.15))


@sfx(DR, 'drum_roll', 'Snare roll building up', ['roll', 'snare', 'build', 'drumroll'])
def _():
    ts, t, i = [], 0.0, 0
    while t < 1.8:
        ts.append(t)
        t += 0.09 - 0.05 * min(t / 1.4, 1)
    ev = [(t, snare(0.12, 200, 0.3, 30), 0.3 + 0.7 * t / 1.8) for t in ts]
    ev += [(1.85, verb(mix(snare(0.4), cymbal(1.5) * 0.6, kick(0.5, 150, 45, 25, 7, 0.3)), 1.0, 0.2))]
    return mixat(ev)
