"""Render every sound, normalize, QC, and write catalog.json + audition files + README tables.

    python generator/build.py              # everything
    python generator/build.py pop ui       # only these categories (or sound names)
    python generator/build.py --no-audition
"""
import json
import subprocess
import sys
import zlib
from pathlib import Path

import numpy as np
from scipy import signal
from scipy.io import wavfile

sys.path.insert(0, str(Path(__file__).parent))
import dsp  # noqa: E402
import r_motion, r_ui, r_fx, r_fun, r_world, r_more  # noqa: E402,F401

ROOT = Path(__file__).resolve().parent.parent
SOUNDS = ROOT / 'sounds'
SR = dsp.SR

# Loudness target per category: loudest 50 ms window, RMS in dBFS. Peaks are capped at -1 dBTP.
TARGET = dict(whoosh=-14, swish=-14, transition=-14, riser=-14, pop=-14, ui=-16, ding=-15, social=-15,
              money=-14, typing=-16, timer=-16, alert=-15, glitch=-14, tech=-15, impact=-11, cinematic=-12,
              camera=-15, magic=-16, cartoon=-14, retro=-15, stinger=-14, drums=-12, paper=-15, nature=-18, foley=-15, crowd=-16)
ORDER = ['whoosh', 'swish', 'transition', 'riser', 'impact', 'cinematic', 'pop', 'ui', 'ding', 'social', 'crowd', 'money',
         'typing', 'camera', 'glitch', 'tech', 'magic', 'cartoon', 'retro', 'stinger', 'alert', 'timer', 'drums',
         'paper', 'foley', 'nature']
GOOD = dict(whoosh='cuts, text fly-ins, fast transitions', swish='whips, slices, quick motion',
            transition='swipes, zooms, slides between shots', riser='builds before a drop, reveal or CTA',
            impact='hits, booms, drops, punches', cinematic='trailer hits, braams, tension, suspense',
            pop='stickers, text pop-ups, emojis', ui='clicks, taps, toggles, app demos',
            ding='notifications, success, highlights', social='likes, follows, messages, phone buzz', crowd='applause, cheers, ooh/aww/wow reactions, whistles',
            money='sales, prices, cash, counters', typing='keyboards, typewriters, text typing on',
            camera='shutters, flashes, photo moments', glitch='glitch transitions, errors, digital looks',
            tech='sci-fi, HUD, lasers, AI/tech videos', magic='sparkles, reveals, glow moments',
            cartoon='funny moments, memes, bounces', retro='8-bit game sounds, gamified content',
            stinger='short jingles: win, fail, ta-da, news', alert='error, correct/wrong, alarms, censor bleep',
            timer='ticks, countdowns, clocks', drums='beat-synced cuts and accents',
            paper='paper, notes, stamps, writing', foley='real-world props: zipper, knock, glass, steps',
            nature='ambience beds: wind, rain, fire, waves')
TP_CEIL = -1.0


def true_peak_db(x):
    up = signal.resample_poly(x, 4, 1, axis=-1)
    return 20 * np.log10(np.max(np.abs(up)) + 1e-12)


def max_rms_db(x, win=0.05):
    p = np.mean(np.atleast_2d(x) ** 2, axis=0)
    w = int(win * SR)
    if len(p) <= w:
        m = p.mean()
    else:
        c = np.cumsum(np.concatenate([[0], p]))
        m = np.max((c[w:] - c[:-w]) / w)
    return 10 * np.log10(m + 1e-20)


PURE_SUB = {'boom_sub_1', 'boom_sub_2'}


def phone_share(x):
    m = x.mean(0)
    P = np.abs(np.fft.rfft(m)) ** 2
    f = np.fft.rfftfreq(len(m), 1 / SR)
    return P[(f >= 150) & (f <= 8000)].sum() / (P.sum() + 1e-20)


def phonify(x, name, want=0.15):
    """Bass-heavy sounds get a saturated harmonic layer so they still read on phone speakers."""
    if name in PURE_SUB or phone_share(x) >= want:
        return x
    lo = signal.sosfilt(signal.butter(2, 160, 'low', fs=SR, output='sos'), x, axis=-1)
    h = np.tanh(8 * lo / (np.max(np.abs(lo)) + 1e-12))
    h = signal.sosfilt(signal.butter(2, [150, 2500], 'band', fs=SR, output='sos'), h, axis=-1)
    h *= np.sqrt(np.mean(x ** 2) / (np.mean(h ** 2) + 1e-20))
    for amt in (0.15, 0.25, 0.4, 0.6, 0.9):
        y = x + amt * h
        if phone_share(y) >= want:
            break
    return y


def finalize(x, cat, name=''):
    x = np.atleast_2d(np.asarray(x, float))
    x = signal.sosfilt(signal.butter(2, 25, 'high', fs=SR, output='sos'), x, axis=-1)
    if not np.all(np.isfinite(x)):
        raise ValueError('NaN/inf in signal')
    env = np.max(np.abs(x), axis=0)
    pk = env.max()
    if pk <= 0:
        raise ValueError('silent')
    above_s = np.nonzero(env > pk * 10 ** (-50 / 20))[0]
    above_e = np.nonzero(env > pk * 10 ** (-60 / 20))[0]
    s = max(0, above_s[0] - int(0.002 * SR))
    e = min(x.shape[1], above_e[-1] + int(0.01 * SR))
    x = x[:, s:e]
    n = x.shape[1]
    fi, fo = min(int(0.0008 * SR), n // 4), min(int(0.015 * SR), n // 4)
    x[:, :fi] *= np.linspace(0, 1, fi)
    x[:, n - fo:] *= np.linspace(1, 0, fo)
    x = phonify(x, name)
    g_rms = 10 ** ((TARGET[cat] - max_rms_db(x)) / 20)
    g_tp = 10 ** ((TP_CEIL - 0.15 - true_peak_db(x)) / 20)
    x = x * min(g_rms, g_tp)
    if x.shape[0] == 2 and np.allclose(x[0], x[1], atol=1e-6):
        x = x[:1]
    return x


def render(item):
    dsp.reseed(zlib.crc32(item['name'].encode()))
    return finalize(item['fn'](), item['cat'], item['name'])


def ffqc(path):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', str(path), '-af', 'ebur128=peak=true,volumedetect',
                        '-f', 'null', '-'], capture_output=True, text=True, encoding='utf-8', errors='replace')
    out, q = r.stderr, {}
    for line in out.splitlines():
        line = line.strip()
        if 'mean_volume:' in line:
            q['mean'] = float(line.split('mean_volume:')[1].split()[0])
        elif 'max_volume:' in line:
            q['max'] = float(line.split('max_volume:')[1].split()[0])
        elif line.startswith('Peak:'):
            q['tp'] = float(line.split()[1])
    return q


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    items = [it for it in dsp.REG if not args or it['cat'] in args or it['name'] in args]
    names = [it['name'] for it in dsp.REG]
    dup = {n for n in names if names.count(n) > 1}
    assert not dup, f'duplicate names: {dup}'
    assert all(it['cat'] in TARGET for it in dsp.REG)
    rendered, fails = {}, []
    for it in items:
        try:
            x = render(it)
        except Exception as ex:  # report and keep going
            fails.append(f"{it['name']}: {ex!r}")
            continue
        out = SOUNDS / it['cat'] / f"{it['name']}.wav"
        out.parent.mkdir(parents=True, exist_ok=True)
        wavfile.write(out, SR, (np.clip(x, -1, 1).T * 32767).round().astype(np.int16))
        rendered[it['name']] = x
    print(f'rendered {len(rendered)}/{len(items)}')
    for f in fails:
        print('FAIL', f)

    # QC with ffmpeg (independent check of what was written)
    from concurrent.futures import ThreadPoolExecutor
    paths = {it['name']: SOUNDS / it['cat'] / f"{it['name']}.wav" for it in items if it['name'] in rendered}
    with ThreadPoolExecutor(8) as ex:
        qc = dict(zip(paths, ex.map(ffqc, paths.values())))
    bad = []
    for n, q in qc.items():
        dur = rendered[n].shape[1] / SR
        if q.get('tp', 0) > TP_CEIL or q.get('mean', -99) < -45 or dur < 0.02 or 'tp' not in q:
            bad.append(f'{n}: {q} dur={dur:.2f}')
    print(f'QC: {len(qc) - len(bad)} ok, {len(bad)} flagged')
    for b in bad:
        print('QC', b)

    # catalog (always rebuilt from the files on disk)
    cat = []
    for it in sorted(dsp.REG, key=lambda i: (ORDER.index(i['cat']), dsp.REG.index(i))):
        p = SOUNDS / it['cat'] / f"{it['name']}.wav"
        if not p.exists():
            continue
        sr, data = wavfile.read(p)
        ch = 1 if data.ndim == 1 else data.shape[1]
        cat.append(dict(name=it['name'], category=it['cat'], file=f"sounds/{it['cat']}/{it['name']}.wav",
                        duration=round(len(data) / sr, 3), channels=ch, tags=it['tags'], description=it['desc']))
    (ROOT / 'catalog.json').write_text(json.dumps(cat, indent=1, ensure_ascii=False), encoding='utf-8')
    print(f'catalog: {len(cat)} sounds')
    if '--no-audition' not in sys.argv:
        audition(cat)
    tables(cat)


def load(p):
    sr, d = wavfile.read(p)
    d = d.astype(float) / 32767
    return np.stack([d, d]) if d.ndim == 1 else d.T


def audition(cat, gap=0.7):
    adir = ROOT / 'audition'
    adir.mkdir(exist_ok=True)
    lines, parts, t = [], [], 0.0
    bycat = {}
    for c in cat:
        x = load(ROOT / c['file'])
        bycat.setdefault(c['category'], []).append((c['name'], x))
    for k in ORDER:
        if k not in bycat:
            continue
        lines.append(f'\n[{k}]')
        cparts = []
        for name, x in bycat[k]:
            lines.append(f'{int(t // 60):02d}:{t % 60:05.2f}  {name}')
            seg = np.concatenate([x, np.zeros((2, int(gap * SR)))], axis=1)
            parts.append(seg)
            cparts.append(seg)
            t += seg.shape[1] / SR
        enc(np.concatenate(cparts, axis=1), adir / f'{k}.mp3')
    enc(np.concatenate(parts, axis=1), adir / 'ALL.mp3')  # local only (gitignored)
    (adir / 'ALL_index.txt').write_text('Timestamps for ALL.mp3\n' + '\n'.join(lines) + '\n', encoding='utf-8')
    print(f'audition: {t / 60:.1f} min')


def enc(x, out):
    tmp = out.with_suffix('.tmp.wav')
    wavfile.write(tmp, SR, (np.clip(x, -1, 1).T * 32767).round().astype(np.int16))
    subprocess.run(['ffmpeg', '-y', '-hide_banner', '-loglevel', 'error', '-i', str(tmp), '-c:a', 'libmp3lame', '-b:a', '128k', str(out)], check=True)
    tmp.unlink()


def tables(cat):
    md = []
    bycat = {}
    for c in cat:
        bycat.setdefault(c['category'], []).append(c)
    for k in ORDER:
        if k not in bycat:
            continue
        md.append(f"\n### {k} ({len(bycat[k])})\n\nPreview: [audition/{k}.mp3](audition/{k}.mp3)\n\n| Sound | Length | What it is |\n|---|---|---|")
        for c in bycat[k]:
            md.append(f"| [`{c['name']}`]({c['file']}) | {c['duration']:.2f} s | {c['description']} |")
    head = (ROOT / 'generator' / 'readme_head.md').read_text(encoding='utf-8')
    rows = '\n'.join(f"| [{k}](#{k}-{len(bycat[k])}) | {len(bycat[k])} | {GOOD[k]} |" for k in ORDER if k in bycat)
    for k, v in dict(count=len(cat), cats=len(bycat), styles=177, cat_rows=rows).items():
        head = head.replace('{' + k + '}', str(v))
    foot = (ROOT / 'generator' / 'readme_foot.md').read_text(encoding='utf-8')
    (ROOT / 'README.md').write_text(head + '\n'.join(md) + '\n\n' + foot, encoding='utf-8')


if __name__ == '__main__':
    main()
