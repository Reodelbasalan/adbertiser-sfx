# Adbertiser SFX: {count} free sound effects for video editors

Whooshes, pops, clicks, dings, cash register, typing, glitches, risers, impacts, cinematic hits, camera shutters, magic sparkles, cartoon boings, 8-bit game sounds, alerts, drums, paper, nature and foley. These are the everyday sounds you reach for when you edit Reels, TikToks, Shorts, ads and YouTube videos.

- **Free for anything, including commercial work.** CC0 (public domain). No credit needed, no sign-up, no watermark.
- **100% original.** Every sound is synthesized from code in [`generator/`](generator/). Nothing is sampled, ripped or copied from other libraries or apps.
- **Ready to drop in.** WAV, 48 kHz, 16-bit, trimmed tight, peaks at or below -1 dBTP, loudness matched within each category.

Companion to [Adbertiser Istayle](https://github.com/Reodelbasalan/adbertiser-istayle), the free Claude Code skill with {styles} video-ad style templates.

## Listen first

Each category has a preview MP3 in [`audition/`](audition/): every sound in that category played back to back. The tables below link to them.

## Get the sounds

- **Everything:** click **Code → Download ZIP** on this page, or run `git clone https://github.com/Reodelbasalan/adbertiser-sfx`.
- **One sound:** open it in the table below and click **Download raw file**.
- **Machine-readable list:** [`catalog.json`](catalog.json) lists every sound's name, category, file, duration, channels, tags and description.

## Use them

| Editor | How |
|---|---|
| **CapCut (desktop)** | Media → Import → pick the WAVs or the whole `sounds` folder, then drag a sound onto the timeline under your clip. |
| **CapCut (phone)** | Copy the WAVs to your phone (Drive, AirDrop or USB). In a project, tap **Audio → Extracted** or **Sounds → Your sounds/Device** and add the file. |
| **Premiere Pro / DaVinci Resolve / Final Cut** | Import the `sounds` folder as a bin and drag sounds to an audio track. |
| **Remotion** | Copy `sounds/` into `public/sfx/`, then add `<Sequence from={30}><Audio src={staticFile('sfx/whoosh/whoosh_fast_1.wav')} /></Sequence>`. |

Mixing tip: keep SFX roughly 15–20 dB under the voice. Whooshes and risers land best when they peak right on the cut, and impacts land best on the beat or the reveal.

## Sounds ({count} in {cats} categories)

| Category | Count | Good for |
|---|---|---|
{cat_rows}
