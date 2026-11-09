## Make your own variations

Every sound is a short Python recipe, so you can change a pitch, length or envelope and re-render the pack in about a minute.

```bash
pip install numpy scipy        # plus ffmpeg on your PATH (used for QC and the MP3 previews)
python generator/build.py                 # render everything + QC + catalog + previews + README
python generator/build.py whoosh pop      # only some categories (or sound names)
python generator/build.py --no-audition   # skip the MP3 previews
```

- `generator/dsp.py` is a small synth kit: oscillators, noise, envelopes, sweeping filters, reverb, bell, pluck, kick and more.
- The recipes live in `generator/r_*.py`, one `add(category, name, description, tags, fn)` per sound.
- `generator/build.py` handles the finishing for every sound: it trims silence, makes bass-heavy hits audible on phone speakers, normalizes loudness per category, caps true peak at -1 dBTP, checks every file with ffmpeg, and writes `catalog.json`, the previews and this README.
- Rendering is deterministic: each sound is seeded from its name, so a rebuild gives the same files.

## License

[CC0 1.0](LICENSE): public domain. Use, edit, remix and sell projects that contain these sounds, with no attribution required. Credit and a ⭐ are always appreciated.
