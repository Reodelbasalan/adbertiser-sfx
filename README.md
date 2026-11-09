# Adbertiser SFX: 408 free sound effects for video editors

Whooshes, pops, clicks, dings, cash register, typing, glitches, risers, impacts, cinematic hits, camera shutters, magic sparkles, cartoon boings, 8-bit game sounds, alerts, drums, paper, nature and foley. These are the everyday sounds you reach for when you edit Reels, TikToks, Shorts, ads and YouTube videos.

- **Free for anything, including commercial work.** CC0 (public domain). No credit needed, no sign-up, no watermark.
- **100% original.** Every sound is synthesized from code in [`generator/`](generator/). Nothing is sampled, ripped or copied from other libraries or apps.
- **Ready to drop in.** WAV, 48 kHz, 16-bit, trimmed tight, peaks at or below -1 dBTP, loudness matched within each category.

Companion to [Adbertiser Istayle](https://github.com/Reodelbasalan/adbertiser-istayle), the free Claude Code skill with 177 video-ad style templates.

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

## Sounds (408 in 30 categories)

| Category | Count | Good for |
|---|---|---|
| [whoosh](#whoosh-20) | 20 | cuts, text fly-ins, fast transitions |
| [swish](#swish-8) | 8 | whips, slices, quick motion |
| [transition](#transition-22) | 22 | swipes, zooms, slides between shots |
| [riser](#riser-12) | 12 | builds before a drop, reveal or CTA |
| [impact](#impact-22) | 22 | hits, booms, drops, punches |
| [cinematic](#cinematic-11) | 11 | trailer hits, braams, tension, suspense |
| [horror](#horror-6) | 6 | jump scares, creepy music box, ghost, dramatic dun-dun |
| [pop](#pop-15) | 15 | stickers, text pop-ups, emojis |
| [ui](#ui-29) | 29 | clicks, taps, toggles, app demos |
| [ding](#ding-18) | 18 | notifications, success, highlights |
| [social](#social-11) | 11 | likes, follows, messages, phone buzz |
| [crowd](#crowd-9) | 9 | applause, cheers, ooh/aww/wow reactions, whistles |
| [festive](#festive-7) | 7 | Christmas, New Year, parties: bells, torotot, air horn, paputok |
| [sports](#sports-5) | 5 | ball bounce, boxing bell, stadium horn, kicks |
| [money](#money-12) | 12 | sales, prices, cash, counters |
| [typing](#typing-9) | 9 | keyboards, typewriters, text typing on |
| [camera](#camera-9) | 9 | shutters, flashes, photo moments |
| [glitch](#glitch-16) | 16 | glitch transitions, errors, digital looks |
| [tech](#tech-13) | 13 | sci-fi, HUD, lasers, AI/tech videos |
| [magic](#magic-13) | 13 | sparkles, reveals, glow moments |
| [cartoon](#cartoon-23) | 23 | funny moments, memes, bounces |
| [retro](#retro-14) | 14 | 8-bit game sounds, gamified content |
| [stinger](#stinger-11) | 11 | short jingles: win, fail, ta-da, news |
| [alert](#alert-12) | 12 | error, correct/wrong, alarms, censor bleep |
| [timer](#timer-9) | 9 | ticks, countdowns, clocks |
| [drums](#drums-12) | 12 | beat-synced cuts and accents |
| [food](#food-7) | 7 | sizzle, crunch, pour, fizz, chopping (food ads) |
| [paper](#paper-11) | 11 | paper, notes, stamps, writing |
| [foley](#foley-30) | 30 | real-world props: zipper, knock, glass, steps |
| [nature](#nature-12) | 12 | ambience beds: wind, rain, fire, waves |

### whoosh (20)

Preview: [audition/whoosh.mp3](audition/whoosh.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`whoosh_fast_1`](sounds/whoosh/whoosh_fast_1.wav) | 0.28 s | Quick air pass for fast cuts |
| [`whoosh_fast_2`](sounds/whoosh/whoosh_fast_2.wav) | 0.32 s | Quick air pass for fast cuts |
| [`whoosh_fast_3`](sounds/whoosh/whoosh_fast_3.wav) | 0.36 s | Quick air pass for fast cuts |
| [`whoosh_fast_4`](sounds/whoosh/whoosh_fast_4.wav) | 0.23 s | Quick air pass for fast cuts |
| [`whoosh_soft_1`](sounds/whoosh/whoosh_soft_1.wav) | 0.66 s | Gentle, smooth whoosh |
| [`whoosh_soft_2`](sounds/whoosh/whoosh_soft_2.wav) | 0.80 s | Gentle, smooth whoosh |
| [`whoosh_soft_3`](sounds/whoosh/whoosh_soft_3.wav) | 0.56 s | Gentle, smooth whoosh |
| [`whoosh_big_1`](sounds/whoosh/whoosh_big_1.wav) | 1.63 s | Heavy, wide whoosh with low end and tail |
| [`whoosh_big_2`](sounds/whoosh/whoosh_big_2.wav) | 2.02 s | Heavy, wide whoosh with low end and tail |
| [`whoosh_big_3`](sounds/whoosh/whoosh_big_3.wav) | 2.44 s | Heavy, wide whoosh with low end and tail |
| [`whoosh_low_1`](sounds/whoosh/whoosh_low_1.wav) | 1.20 s | Deep rumbling pass |
| [`whoosh_low_2`](sounds/whoosh/whoosh_low_2.wav) | 1.35 s | Deep rumbling pass |
| [`whoosh_air_1`](sounds/whoosh/whoosh_air_1.wav) | 0.48 s | Bright airy whoosh |
| [`whoosh_air_2`](sounds/whoosh/whoosh_air_2.wav) | 0.57 s | Bright airy whoosh |
| [`whoosh_flyby_1`](sounds/whoosh/whoosh_flyby_1.wav) | 1.16 s | Fly-by that pans across the stereo field |
| [`whoosh_flyby_2`](sounds/whoosh/whoosh_flyby_2.wav) | 1.14 s | Fly-by that pans across the stereo field |
| [`whoosh_double`](sounds/whoosh/whoosh_double.wav) | 0.45 s | Two quick passes back to back |
| [`whoosh_reverse_1`](sounds/whoosh/whoosh_reverse_1.wav) | 0.99 s | Reverse swell that sucks into the cut |
| [`whoosh_reverse_2`](sounds/whoosh/whoosh_reverse_2.wav) | 1.54 s | Reverse swell that sucks into the cut |
| [`whoosh_sweep_up`](sounds/whoosh/whoosh_sweep_up.wav) | 1.00 s | Whoosh that rises in pitch |

### swish (8)

Preview: [audition/swish.mp3](audition/swish.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`swish_whip_1`](sounds/swish/swish_whip_1.wav) | 0.12 s | Very fast whip swish |
| [`swish_whip_2`](sounds/swish/swish_whip_2.wav) | 0.15 s | Very fast whip swish |
| [`swish_whip_3`](sounds/swish/swish_whip_3.wav) | 0.12 s | Very fast whip swish |
| [`swish_cloth_1`](sounds/swish/swish_cloth_1.wav) | 0.34 s | Fabric / jacket swish |
| [`swish_cloth_2`](sounds/swish/swish_cloth_2.wav) | 0.49 s | Fabric / jacket swish |
| [`swish_sword_1`](sounds/swish/swish_sword_1.wav) | 0.29 s | Sharp blade slice |
| [`swish_sword_2`](sounds/swish/swish_sword_2.wav) | 1.34 s | Sharp blade slice with metal ring |
| [`swish_stick`](sounds/swish/swish_stick.wav) | 0.29 s | Thin stick swing with a whistle |

### transition (22)

Preview: [audition/transition.mp3](audition/transition.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`swipe_1`](sounds/transition/swipe_1.wav) | 0.19 s | Phone-style screen swipe |
| [`swipe_2`](sounds/transition/swipe_2.wav) | 0.19 s | Phone-style screen swipe |
| [`swipe_3`](sounds/transition/swipe_3.wav) | 0.20 s | Phone-style screen swipe |
| [`slide_in`](sounds/transition/slide_in.wav) | 0.38 s | Smooth slide in (rising) |
| [`slide_out`](sounds/transition/slide_out.wav) | 0.38 s | Smooth slide out (falling) |
| [`zoom_in_1`](sounds/transition/zoom_in_1.wav) | 0.95 s | Rising zoom-in sweep |
| [`zoom_in_2`](sounds/transition/zoom_in_2.wav) | 0.83 s | Zoom-in sweep that ends on a click |
| [`zoom_out_1`](sounds/transition/zoom_out_1.wav) | 0.92 s | Falling zoom-out sweep |
| [`zoom_out_2`](sounds/transition/zoom_out_2.wav) | 0.75 s | Short zoom-out sweep |
| [`whoosh_hit_1`](sounds/transition/whoosh_hit_1.wav) | 1.34 s | Whoosh that lands on a hit |
| [`whoosh_hit_2`](sounds/transition/whoosh_hit_2.wav) | 1.42 s | Whoosh that lands on a hit |
| [`whoosh_hit_3`](sounds/transition/whoosh_hit_3.wav) | 1.23 s | Whoosh that lands on a hit |
| [`glide_up`](sounds/transition/glide_up.wav) | 1.15 s | Soft tonal glide up |
| [`glide_down`](sounds/transition/glide_down.wav) | 1.15 s | Soft tonal glide down |
| [`warp`](sounds/transition/warp.wav) | 1.35 s | Jet / flanger warp transition |
| [`spin`](sounds/transition/spin.wav) | 0.74 s | Spinning whoosh with a rotating flutter |
| [`swoosh_tape`](sounds/transition/swoosh_tape.wav) | 0.60 s | Tape-stop style downward swoosh |
| [`swoosh_rise`](sounds/transition/swoosh_rise.wav) | 0.41 s | Short rising swoosh into the next shot |
| [`record_scratch_1`](sounds/transition/record_scratch_1.wav) | 0.50 s | DJ record scratch (wikka) |
| [`record_scratch_2`](sounds/transition/record_scratch_2.wav) | 0.40 s | Record-stop scratch |
| [`rewind`](sounds/transition/rewind.wav) | 1.40 s | Tape rewind (speeding up backwards) |
| [`fast_forward`](sounds/transition/fast_forward.wav) | 1.40 s | Fast-forward (speeding up) |

### riser (12)

Preview: [audition/riser.mp3](audition/riser.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`riser_short_1`](sounds/riser/riser_short_1.wav) | 0.92 s | One-second build into a cut |
| [`riser_short_2`](sounds/riser/riser_short_2.wav) | 1.37 s | 1.5 s build with pulse |
| [`riser_long_1`](sounds/riser/riser_long_1.wav) | 3.71 s | Three-second tension build |
| [`riser_long_2`](sounds/riser/riser_long_2.wav) | 4.88 s | Four-second big build |
| [`riser_noise_1`](sounds/riser/riser_noise_1.wav) | 2.60 s | Pure white-noise sweep up |
| [`riser_noise_2`](sounds/riser/riser_noise_2.wav) | 3.56 s | Pure white-noise sweep up |
| [`riser_tonal_1`](sounds/riser/riser_tonal_1.wav) | 2.79 s | Major chord rising an octave |
| [`riser_tonal_2`](sounds/riser/riser_tonal_2.wav) | 2.34 s | Bright tonal rise |
| [`swell_reverse_1`](sounds/riser/swell_reverse_1.wav) | 1.72 s | Reverse cymbal swell |
| [`swell_reverse_2`](sounds/riser/swell_reverse_2.wav) | 2.54 s | Reverse cymbal swell |
| [`downlifter_1`](sounds/riser/downlifter_1.wav) | 2.05 s | Falling sweep after a drop |
| [`downlifter_2`](sounds/riser/downlifter_2.wav) | 3.07 s | Long falling sweep |

### impact (22)

Preview: [audition/impact.mp3](audition/impact.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`impact_1`](sounds/impact/impact_1.wav) | 1.57 s | Solid impact hit |
| [`impact_2`](sounds/impact/impact_2.wav) | 1.43 s | Solid impact hit |
| [`impact_3`](sounds/impact/impact_3.wav) | 1.73 s | Solid impact hit |
| [`impact_hard_1`](sounds/impact/impact_hard_1.wav) | 1.85 s | Hard distorted impact |
| [`impact_hard_2`](sounds/impact/impact_hard_2.wav) | 1.78 s | Hard distorted impact |
| [`boom_1`](sounds/impact/boom_1.wav) | 2.90 s | Deep boom |
| [`boom_2`](sounds/impact/boom_2.wav) | 3.15 s | Deep boom |
| [`boom_sub_1`](sounds/impact/boom_sub_1.wav) | 1.80 s | Sub-bass boom (use good speakers) |
| [`boom_sub_2`](sounds/impact/boom_sub_2.wav) | 1.80 s | Sub-bass boom (use good speakers) |
| [`bass_drop_1`](sounds/impact/bass_drop_1.wav) | 1.50 s | Bass drop glide |
| [`bass_drop_2`](sounds/impact/bass_drop_2.wav) | 2.20 s | Bass drop glide |
| [`punch_1`](sounds/impact/punch_1.wav) | 0.25 s | Body punch |
| [`punch_2`](sounds/impact/punch_2.wav) | 0.25 s | Body punch |
| [`punch_3`](sounds/impact/punch_3.wav) | 0.38 s | Body punch with swing |
| [`thud_1`](sounds/impact/thud_1.wav) | 0.40 s | Dull low thud |
| [`thud_2`](sounds/impact/thud_2.wav) | 0.40 s | Dull low thud |
| [`hit_metal_1`](sounds/impact/hit_metal_1.wav) | 1.82 s | Metal clang |
| [`hit_metal_2`](sounds/impact/hit_metal_2.wav) | 1.77 s | Metal clang |
| [`hit_cinematic_1`](sounds/impact/hit_cinematic_1.wav) | 3.79 s | Big trailer-style hit |
| [`hit_cinematic_2`](sounds/impact/hit_cinematic_2.wav) | 4.10 s | Darker cinematic hit |
| [`explosion_1`](sounds/impact/explosion_1.wav) | 2.77 s | Explosion |
| [`explosion_2`](sounds/impact/explosion_2.wav) | 2.95 s | Distant explosion |

### cinematic (11)

Preview: [audition/cinematic.mp3](audition/cinematic.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`braam_1`](sounds/cinematic/braam_1.wav) | 4.02 s | Big brassy BRAAM |
| [`braam_2`](sounds/cinematic/braam_2.wav) | 4.50 s | Dark low BRAAM |
| [`trailer_hit_1`](sounds/cinematic/trailer_hit_1.wav) | 4.37 s | Reverse swell into a trailer hit |
| [`trailer_hit_2`](sounds/cinematic/trailer_hit_2.wav) | 4.35 s | Reverse swell into a trailer hit |
| [`tension_drone_1`](sounds/cinematic/tension_drone_1.wav) | 5.00 s | Dark tension drone (4 s) |
| [`tension_drone_2`](sounds/cinematic/tension_drone_2.wav) | 5.09 s | Uneasy higher drone (4 s) |
| [`heartbeat`](sounds/cinematic/heartbeat.wav) | 2.15 s | Heartbeat (lub-dub x3) |
| [`suspense_sting`](sounds/cinematic/suspense_sting.wav) | 2.48 s | Sudden high string-like sting |
| [`tail_reverb`](sounds/cinematic/tail_reverb.wav) | 3.28 s | Impact with long reverb tail |
| [`rumble`](sounds/cinematic/rumble.wav) | 2.99 s | Low rumble (3 s) |
| [`slow_motion`](sounds/cinematic/slow_motion.wav) | 2.20 s | Slow-motion whoosh down |

### horror (6)

Preview: [audition/horror.mp3](audition/horror.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`music_box_creepy`](sounds/horror/music_box_creepy.wav) | 4.17 s | Out-of-tune creepy music box |
| [`jump_scare_1`](sounds/horror/jump_scare_1.wav) | 2.12 s | Sudden jump-scare stab |
| [`jump_scare_2`](sounds/horror/jump_scare_2.wav) | 2.17 s | Reverse swell into a scare |
| [`ghost_whoosh`](sounds/horror/ghost_whoosh.wav) | 3.57 s | Ghostly moaning whoosh |
| [`dun_dun_dunnn`](sounds/horror/dun_dun_dunnn.wav) | 4.00 s | Dramatic "dun dun DUNNN" |
| [`creak_long`](sounds/horror/creak_long.wav) | 1.78 s | Long creepy creak |

### pop (15)

Preview: [audition/pop.mp3](audition/pop.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`pop_1`](sounds/pop/pop_1.wav) | 0.13 s | Clean pop for text and stickers |
| [`pop_2`](sounds/pop/pop_2.wav) | 0.13 s | Clean pop for text and stickers |
| [`pop_3`](sounds/pop/pop_3.wav) | 0.13 s | Clean pop for text and stickers |
| [`pop_4`](sounds/pop/pop_4.wav) | 0.13 s | Clean pop for text and stickers |
| [`pop_bubble_1`](sounds/pop/pop_bubble_1.wav) | 0.12 s | Bubble pop (rising chirp) |
| [`pop_bubble_2`](sounds/pop/pop_bubble_2.wav) | 0.12 s | Bubble pop (rising chirp) |
| [`pop_bubble_3`](sounds/pop/pop_bubble_3.wav) | 0.12 s | Bubble pop (rising chirp) |
| [`pop_cork`](sounds/pop/pop_cork.wav) | 0.25 s | Cork / bottle pop |
| [`pop_soft_1`](sounds/pop/pop_soft_1.wav) | 0.14 s | Soft muted pop |
| [`pop_soft_2`](sounds/pop/pop_soft_2.wav) | 0.14 s | Soft muted pop |
| [`pop_high`](sounds/pop/pop_high.wav) | 0.09 s | High, bright pop |
| [`bloop_1`](sounds/pop/bloop_1.wav) | 0.20 s | Watery bloop |
| [`bloop_2`](sounds/pop/bloop_2.wav) | 0.16 s | Watery bloop |
| [`pop_mouth`](sounds/pop/pop_mouth.wav) | 0.07 s | Mouth / lip pop |
| [`pop_double`](sounds/pop/pop_double.wav) | 0.21 s | Two quick pops |

### ui (29)

Preview: [audition/ui.mp3](audition/ui.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`click_1`](sounds/ui/click_1.wav) | 0.04 s | Crisp UI click |
| [`click_2`](sounds/ui/click_2.wav) | 0.04 s | Crisp UI click |
| [`click_3`](sounds/ui/click_3.wav) | 0.03 s | Crisp UI click |
| [`click_4`](sounds/ui/click_4.wav) | 0.04 s | Crisp UI click |
| [`click_soft_1`](sounds/ui/click_soft_1.wav) | 0.05 s | Soft muted click |
| [`click_soft_2`](sounds/ui/click_soft_2.wav) | 0.05 s | Soft muted click |
| [`click_mouse`](sounds/ui/click_mouse.wav) | 0.10 s | Mouse click (press + release) |
| [`tap_1`](sounds/ui/tap_1.wav) | 0.08 s | Finger tap on glass |
| [`tap_2`](sounds/ui/tap_2.wav) | 0.08 s | Finger tap on glass |
| [`tap_3`](sounds/ui/tap_3.wav) | 0.08 s | Finger tap on glass |
| [`toggle_on`](sounds/ui/toggle_on.wav) | 0.12 s | Switch on (up blip) |
| [`toggle_off`](sounds/ui/toggle_off.wav) | 0.12 s | Switch off (down blip) |
| [`blip_1`](sounds/ui/blip_1.wav) | 0.08 s | Short digital blip |
| [`blip_2`](sounds/ui/blip_2.wav) | 0.08 s | Short digital blip |
| [`blip_3`](sounds/ui/blip_3.wav) | 0.08 s | Short digital blip |
| [`blip_up`](sounds/ui/blip_up.wav) | 0.09 s | Blip sliding up |
| [`blip_down`](sounds/ui/blip_down.wav) | 0.09 s | Blip sliding down |
| [`blip_retro_1`](sounds/ui/blip_retro_1.wav) | 0.07 s | Square-wave retro blip |
| [`blip_retro_2`](sounds/ui/blip_retro_2.wav) | 0.11 s | Two-note retro blip |
| [`ui_select`](sounds/ui/ui_select.wav) | 0.24 s | Pleasant select tone |
| [`ui_back`](sounds/ui/ui_back.wav) | 0.24 s | Back / close tone |
| [`ui_hover`](sounds/ui/ui_hover.wav) | 0.04 s | Very soft hover tick |
| [`ui_confirm`](sounds/ui/ui_confirm.wav) | 0.42 s | Three-note confirm |
| [`ui_cancel`](sounds/ui/ui_cancel.wav) | 0.19 s | Low two-note cancel |
| [`lock`](sounds/ui/lock.wav) | 0.18 s | Lock (click + clunk) |
| [`unlock`](sounds/ui/unlock.wav) | 0.18 s | Unlock (clunk + up blip) |
| [`download_complete`](sounds/ui/download_complete.wav) | 1.33 s | Download complete |
| [`delete_trash`](sounds/ui/delete_trash.wav) | 0.51 s | Delete: crumple into the trash |
| [`upload_whoosh`](sounds/ui/upload_whoosh.wav) | 0.35 s | Upload / send whoosh with blip |

### ding (18)

Preview: [audition/ding.mp3](audition/ding.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`ding_1`](sounds/ding/ding_1.wav) | 1.46 s | Clean bell ding |
| [`ding_2`](sounds/ding/ding_2.wav) | 1.48 s | Clean bell ding |
| [`ding_3`](sounds/ding/ding_3.wav) | 1.45 s | Clean bell ding |
| [`ding_success`](sounds/ding/ding_success.wav) | 1.54 s | Two-note success ding |
| [`chime_up_1`](sounds/ding/chime_up_1.wav) | 1.95 s | Rising bell arpeggio |
| [`chime_up_2`](sounds/ding/chime_up_2.wav) | 2.03 s | Rising bell arpeggio |
| [`chime_down`](sounds/ding/chime_down.wav) | 2.08 s | Falling bell arpeggio |
| [`bell_small_1`](sounds/ding/bell_small_1.wav) | 2.20 s | Desk / service bell |
| [`bell_small_2`](sounds/ding/bell_small_2.wav) | 2.16 s | Desk / service bell |
| [`notif_1`](sounds/ding/notif_1.wav) | 0.79 s | Phone-style notification |
| [`notif_2`](sounds/ding/notif_2.wav) | 0.86 s | Phone-style notification |
| [`notif_3`](sounds/ding/notif_3.wav) | 0.80 s | Phone-style notification |
| [`notif_message_1`](sounds/ding/notif_message_1.wav) | 0.19 s | New message bubble |
| [`notif_message_2`](sounds/ding/notif_message_2.wav) | 0.19 s | New message bubble |
| [`level_up_1`](sounds/ding/level_up_1.wav) | 1.08 s | Fast level-up arpeggio |
| [`level_up_2`](sounds/ding/level_up_2.wav) | 1.10 s | Fast level-up arpeggio |
| [`notif_4`](sounds/ding/notif_4.wav) | 0.87 s | Soft three-note notification |
| [`notif_5`](sounds/ding/notif_5.wav) | 0.99 s | Plucky notification |

### social (11)

Preview: [audition/social.mp3](audition/social.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`like_pop`](sounds/social/like_pop.wav) | 0.65 s | Like / heart tap |
| [`heart_pop`](sounds/social/heart_pop.wav) | 0.88 s | Heart burst with sparkle |
| [`follow_ding`](sounds/social/follow_ding.wav) | 1.17 s | Follow / subscribe ding |
| [`comment_blip`](sounds/social/comment_blip.wav) | 0.13 s | New comment double blip |
| [`share_swoosh`](sounds/social/share_swoosh.wav) | 0.26 s | Share: swoosh + blip |
| [`message_sent`](sounds/social/message_sent.wav) | 0.16 s | Message sent "whoop" |
| [`message_received`](sounds/social/message_received.wav) | 0.71 s | Message received pluck |
| [`vibrate_1`](sounds/social/vibrate_1.wav) | 0.95 s | Phone vibration buzz-buzz |
| [`vibrate_2`](sounds/social/vibrate_2.wav) | 0.25 s | Short single vibration |
| [`ringtone`](sounds/social/ringtone.wav) | 3.15 s | Original marimba ringtone |
| [`notification_stack`](sounds/social/notification_stack.wav) | 1.03 s | Several notifications in a row |

### crowd (9)

Preview: [audition/crowd.mp3](audition/crowd.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`applause_1`](sounds/crowd/applause_1.wav) | 4.28 s | Small group applause (4 s) |
| [`applause_2`](sounds/crowd/applause_2.wav) | 5.63 s | Big audience applause (5 s) |
| [`applause_short`](sounds/crowd/applause_short.wav) | 2.27 s | Short burst of applause (2 s) |
| [`crowd_ooh`](sounds/crowd/crowd_ooh.wav) | 2.41 s | Impressed crowd "ooooh" |
| [`crowd_aww`](sounds/crowd/crowd_aww.wav) | 2.34 s | Sympathetic crowd "awww" |
| [`crowd_wow`](sounds/crowd/crowd_wow.wav) | 2.19 s | Crowd "woooow" |
| [`cheer`](sounds/crowd/cheer.wav) | 4.08 s | Crowd cheer with applause and whistles |
| [`finger_whistle`](sounds/crowd/finger_whistle.wav) | 0.80 s | Loud finger whistle |
| [`whistle_wolf`](sounds/crowd/whistle_wolf.wav) | 1.05 s | Two-part "wheet-whew" whistle |

### festive (7)

Preview: [audition/festive.mp3](audition/festive.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`jingle_bells`](sounds/festive/jingle_bells.wav) | 2.46 s | Sleigh / jingle bells shaking (2 s) |
| [`party_horn_1`](sounds/festive/party_horn_1.wav) | 0.90 s | Party horn / torotot blow |
| [`party_horn_2`](sounds/festive/party_horn_2.wav) | 0.35 s | Party blowout toot |
| [`confetti_popper`](sounds/festive/confetti_popper.wav) | 1.33 s | Confetti popper bang + falling confetti |
| [`air_horn_1`](sounds/festive/air_horn_1.wav) | 1.47 s | Air horn blast |
| [`air_horn_2`](sounds/festive/air_horn_2.wav) | 1.71 s | Air horn x3 (short-short-long) |
| [`firecracker_string`](sounds/festive/firecracker_string.wav) | 3.23 s | String of firecrackers (2.5 s) |

### sports (5)

Preview: [audition/sports.mp3](audition/sports.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`basketball_bounce`](sounds/sports/basketball_bounce.wav) | 2.02 s | Basketball dribble |
| [`boxing_bell`](sounds/sports/boxing_bell.wav) | 2.37 s | Boxing ring bell ding-ding-ding |
| [`stadium_horn`](sounds/sports/stadium_horn.wav) | 3.34 s | Big stadium horn |
| [`ball_kick`](sounds/sports/ball_kick.wav) | 0.20 s | Ball kick |
| [`racket_hit`](sounds/sports/racket_hit.wav) | 0.30 s | Tennis / badminton racket hit |

### money (12)

Preview: [audition/money.mp3](audition/money.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`cash_register_1`](sounds/money/cash_register_1.wav) | 1.62 s | Cash register "ka-ching" |
| [`cash_register_2`](sounds/money/cash_register_2.wav) | 1.66 s | Cash register with double bell |
| [`coin_1`](sounds/money/coin_1.wav) | 0.70 s | Single coin ping |
| [`coin_2`](sounds/money/coin_2.wav) | 0.68 s | Coin dropping on a table |
| [`coin_3`](sounds/money/coin_3.wav) | 0.92 s | Bright coin collect |
| [`coins_drop_1`](sounds/money/coins_drop_1.wav) | 1.09 s | Pile of coins pouring |
| [`coins_drop_2`](sounds/money/coins_drop_2.wav) | 1.50 s | Pile of coins pouring |
| [`counter_roll_1`](sounds/money/counter_roll_1.wav) | 1.49 s | Number counter rolling up |
| [`counter_roll_2`](sounds/money/counter_roll_2.wav) | 2.44 s | Counter rolling then ding |
| [`cha_ching`](sounds/money/cha_ching.wav) | 1.61 s | Bright two-bell cha-ching |
| [`money_counter`](sounds/money/money_counter.wav) | 1.22 s | Bills flicking through a counter |
| [`payment_success`](sounds/money/payment_success.wav) | 1.78 s | Payment received chime |

### typing (9)

Preview: [audition/typing.mp3](audition/typing.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`typing_1`](sounds/typing/typing_1.wav) | 1.62 s | Mechanical keyboard typing |
| [`typing_2`](sounds/typing/typing_2.wav) | 1.64 s | Soft laptop typing |
| [`typing_3`](sounds/typing/typing_3.wav) | 1.60 s | Clicky keyboard typing |
| [`typing_fast`](sounds/typing/typing_fast.wav) | 1.44 s | Very fast typing burst |
| [`key_single_1`](sounds/typing/key_single_1.wav) | 0.07 s | Single key press |
| [`key_single_2`](sounds/typing/key_single_2.wav) | 0.07 s | Soft single key press |
| [`key_enter`](sounds/typing/key_enter.wav) | 0.16 s | Big enter / spacebar press |
| [`typewriter_bell`](sounds/typing/typewriter_bell.wav) | 1.60 s | Typewriter clacks, bell and carriage return |
| [`typewriter_keys`](sounds/typing/typewriter_keys.wav) | 1.22 s | Typewriter typing |

### camera (9)

Preview: [audition/camera.mp3](audition/camera.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`shutter_1`](sounds/camera/shutter_1.wav) | 0.11 s | Camera shutter |
| [`shutter_2`](sounds/camera/shutter_2.wav) | 0.13 s | DSLR shutter with mirror slap |
| [`shutter_quick`](sounds/camera/shutter_quick.wav) | 0.06 s | Phone camera snap |
| [`shutter_burst`](sounds/camera/shutter_burst.wav) | 0.51 s | Burst mode (5 shots) |
| [`flash_charge`](sounds/camera/flash_charge.wav) | 1.33 s | Flash charging whine + ready beep |
| [`film_wind`](sounds/camera/film_wind.wav) | 0.85 s | Film advance ratchet |
| [`focus_beep`](sounds/camera/focus_beep.wav) | 0.13 s | Autofocus bip-bip |
| [`polaroid`](sounds/camera/polaroid.wav) | 1.20 s | Instant camera shot + motor |
| [`lens_zoom`](sounds/camera/lens_zoom.wav) | 0.80 s | Lens zoom motor |

### glitch (16)

Preview: [audition/glitch.mp3](audition/glitch.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`glitch_1`](sounds/glitch/glitch_1.wav) | 0.46 s | Digital glitch burst |
| [`glitch_2`](sounds/glitch/glitch_2.wav) | 0.38 s | Digital glitch burst |
| [`glitch_3`](sounds/glitch/glitch_3.wav) | 0.61 s | Digital glitch burst |
| [`glitch_4`](sounds/glitch/glitch_4.wav) | 0.52 s | Digital glitch burst |
| [`glitch_5`](sounds/glitch/glitch_5.wav) | 0.41 s | Digital glitch burst |
| [`glitch_short_1`](sounds/glitch/glitch_short_1.wav) | 0.15 s | Tiny glitch for quick cuts |
| [`glitch_short_2`](sounds/glitch/glitch_short_2.wav) | 0.19 s | Tiny glitch for quick cuts |
| [`glitch_short_3`](sounds/glitch/glitch_short_3.wav) | 0.13 s | Tiny glitch for quick cuts |
| [`glitch_stutter_1`](sounds/glitch/glitch_stutter_1.wav) | 0.28 s | Buffer stutter that shrinks |
| [`glitch_stutter_2`](sounds/glitch/glitch_stutter_2.wav) | 0.59 s | Long buffer stutter |
| [`static_burst_1`](sounds/glitch/static_burst_1.wav) | 0.70 s | TV static burst |
| [`static_burst_2`](sounds/glitch/static_burst_2.wav) | 0.70 s | TV static burst with hum |
| [`data_chirp_1`](sounds/glitch/data_chirp_1.wav) | 0.60 s | Modem-like data chirps |
| [`data_chirp_2`](sounds/glitch/data_chirp_2.wav) | 0.99 s | Modem-like data chirps |
| [`power_up`](sounds/glitch/power_up.wav) | 1.68 s | Electric power-up |
| [`power_down`](sounds/glitch/power_down.wav) | 1.20 s | Electric power-down |

### tech (13)

Preview: [audition/tech.mp3](audition/tech.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`laser_1`](sounds/tech/laser_1.wav) | 0.38 s | Sci-fi laser shot |
| [`laser_2`](sounds/tech/laser_2.wav) | 0.43 s | Sci-fi laser shot |
| [`laser_3`](sounds/tech/laser_3.wav) | 0.52 s | Sci-fi laser shot |
| [`scanner`](sounds/tech/scanner.wav) | 1.50 s | Scanner sweeping back and forth |
| [`hologram`](sounds/tech/hologram.wav) | 2.15 s | Shimmering hologram |
| [`beam_up`](sounds/tech/beam_up.wav) | 2.44 s | Teleport beam rising |
| [`computer_beeps_1`](sounds/tech/computer_beeps_1.wav) | 0.78 s | Sci-fi computer beeps |
| [`computer_beeps_2`](sounds/tech/computer_beeps_2.wav) | 1.26 s | Sci-fi computer beeps |
| [`robot_blips`](sounds/tech/robot_blips.wav) | 0.83 s | Robot talking blips |
| [`teleport`](sounds/tech/teleport.wav) | 1.66 s | Teleport phase-out |
| [`charge_up`](sounds/tech/charge_up.wav) | 1.21 s | Energy charge-up whine |
| [`shield`](sounds/tech/shield.wav) | 1.47 s | Energy shield hum |
| [`ui_hud`](sounds/tech/ui_hud.wav) | 0.51 s | Futuristic HUD pop-up |

### magic (13)

Preview: [audition/magic.mp3](audition/magic.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`sparkle_1`](sounds/magic/sparkle_1.wav) | 1.52 s | Magic sparkle twinkles |
| [`sparkle_2`](sounds/magic/sparkle_2.wav) | 1.28 s | Magic sparkle twinkles |
| [`sparkle_3`](sounds/magic/sparkle_3.wav) | 1.71 s | Magic sparkle twinkles |
| [`magic_wand_1`](sounds/magic/magic_wand_1.wav) | 1.76 s | Wand swish + sparkles |
| [`magic_wand_2`](sounds/magic/magic_wand_2.wav) | 2.15 s | Longer wand spell |
| [`shimmer_1`](sounds/magic/shimmer_1.wav) | 2.84 s | Soft shimmer |
| [`shimmer_2`](sounds/magic/shimmer_2.wav) | 2.73 s | Soft shimmer |
| [`twinkle`](sounds/magic/twinkle.wav) | 1.15 s | Quick twinkle run |
| [`fairy_rise`](sounds/magic/fairy_rise.wav) | 1.70 s | Harp-like rising glissando |
| [`reveal_glow_1`](sounds/magic/reveal_glow_1.wav) | 2.77 s | Glowing reveal swell |
| [`reveal_glow_2`](sounds/magic/reveal_glow_2.wav) | 2.88 s | Glowing reveal swell |
| [`chime_tree`](sounds/magic/chime_tree.wav) | 2.05 s | Wind-chime glissando |
| [`poof`](sounds/magic/poof.wav) | 1.24 s | Magic poof (disappear) |

### cartoon (23)

Preview: [audition/cartoon.mp3](audition/cartoon.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`boing_1`](sounds/cartoon/boing_1.wav) | 0.80 s | Cartoon boing |
| [`boing_2`](sounds/cartoon/boing_2.wav) | 0.80 s | Cartoon boing |
| [`boing_3`](sounds/cartoon/boing_3.wav) | 0.80 s | Cartoon boing |
| [`spring`](sounds/cartoon/spring.wav) | 0.70 s | Springy sproing |
| [`slide_whistle_up`](sounds/cartoon/slide_whistle_up.wav) | 0.80 s | Slide whistle up |
| [`slide_whistle_down`](sounds/cartoon/slide_whistle_down.wav) | 0.80 s | Slide whistle down (falling) |
| [`bonk_1`](sounds/cartoon/bonk_1.wav) | 0.23 s | Wood-block bonk |
| [`bonk_2`](sounds/cartoon/bonk_2.wav) | 0.35 s | Head bonk |
| [`wobble_1`](sounds/cartoon/wobble_1.wav) | 1.00 s | Wah-wah wobble |
| [`wobble_2`](sounds/cartoon/wobble_2.wav) | 1.20 s | Wah-wah wobble |
| [`zip_1`](sounds/cartoon/zip_1.wav) | 0.15 s | Zip away (up) |
| [`zip_2`](sounds/cartoon/zip_2.wav) | 0.15 s | Zip down |
| [`squeak_1`](sounds/cartoon/squeak_1.wav) | 0.25 s | Rubber toy squeak |
| [`squeak_2`](sounds/cartoon/squeak_2.wav) | 0.35 s | Rubber toy squeak |
| [`wah_wah_fail`](sounds/cartoon/wah_wah_fail.wav) | 3.20 s | Sad descending "wah wah wah wahhh" |
| [`tiptoe`](sounds/cartoon/tiptoe.wav) | 1.80 s | Sneaky pizzicato tiptoe |
| [`run_away`](sounds/cartoon/run_away.wav) | 0.75 s | Run-away blips + zoom |
| [`pop_eyes`](sounds/cartoon/pop_eyes.wav) | 0.48 s | Eyes-pop "boink" |
| [`drum_hit_fail`](sounds/cartoon/drum_hit_fail.wav) | 1.55 s | Comedy ba-dum-tss |
| [`slip`](sounds/cartoon/slip.wav) | 0.65 s | Banana slip and fall |
| [`dizzy`](sounds/cartoon/dizzy.wav) | 2.09 s | Dizzy circling stars |
| [`honk_toy`](sounds/cartoon/honk_toy.wav) | 0.62 s | Clown horn honk-honk |
| [`splat`](sounds/cartoon/splat.wav) | 0.44 s | Wet splat |

### retro (14)

Preview: [audition/retro.mp3](audition/retro.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`coin_8bit`](sounds/retro/coin_8bit.wav) | 0.30 s | 8-bit coin |
| [`jump_8bit`](sounds/retro/jump_8bit.wav) | 0.16 s | 8-bit jump |
| [`powerup_8bit`](sounds/retro/powerup_8bit.wav) | 0.57 s | 8-bit power-up scale |
| [`laser_8bit`](sounds/retro/laser_8bit.wav) | 0.20 s | 8-bit laser |
| [`hit_8bit`](sounds/retro/hit_8bit.wav) | 0.12 s | 8-bit hit |
| [`explosion_8bit`](sounds/retro/explosion_8bit.wav) | 0.50 s | 8-bit explosion |
| [`select_8bit`](sounds/retro/select_8bit.wav) | 0.10 s | 8-bit menu select |
| [`gameover_8bit`](sounds/retro/gameover_8bit.wav) | 1.32 s | 8-bit game-over tune |
| [`extra_life_8bit`](sounds/retro/extra_life_8bit.wav) | 0.48 s | 8-bit extra life |
| [`blip_8bit`](sounds/retro/blip_8bit.wav) | 0.06 s | 8-bit blip |
| [`warp_8bit`](sounds/retro/warp_8bit.wav) | 0.70 s | 8-bit warp pipe |
| [`win_jingle_8bit`](sounds/retro/win_jingle_8bit.wav) | 1.25 s | 8-bit victory jingle |
| [`step_8bit`](sounds/retro/step_8bit.wav) | 0.48 s | 8-bit footstep blips |
| [`error_8bit`](sounds/retro/error_8bit.wav) | 0.30 s | 8-bit error |

### stinger (11)

Preview: [audition/stinger.mp3](audition/stinger.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`success_jingle_1`](sounds/stinger/success_jingle_1.wav) | 2.10 s | Marimba success jingle |
| [`success_jingle_2`](sounds/stinger/success_jingle_2.wav) | 1.91 s | Plucked success jingle |
| [`fail_jingle`](sounds/stinger/fail_jingle.wav) | 1.90 s | Sad fail jingle |
| [`tada`](sounds/stinger/tada.wav) | 2.37 s | Ta-da fanfare |
| [`reveal_stinger`](sounds/stinger/reveal_stinger.wav) | 3.26 s | Build, hit and chord |
| [`transition_stinger`](sounds/stinger/transition_stinger.wav) | 1.81 s | Whoosh into a chord stab |
| [`suspense_hit`](sounds/stinger/suspense_hit.wav) | 2.43 s | Low hit + dissonant stab |
| [`positive_chord`](sounds/stinger/positive_chord.wav) | 2.98 s | Warm uplifting chord swell |
| [`mystery`](sounds/stinger/mystery.wav) | 3.48 s | Mysterious bell motif |
| [`news_sting`](sounds/stinger/news_sting.wav) | 2.19 s | Breaking-news style sting |
| [`question_hmm`](sounds/stinger/question_hmm.wav) | 1.11 s | Curious "hmm?" two-note |

### alert (12)

Preview: [audition/alert.mp3](audition/alert.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`error_1`](sounds/alert/error_1.wav) | 0.37 s | Two-tone error |
| [`error_2`](sounds/alert/error_2.wav) | 0.33 s | Triple low error beep |
| [`error_buzz`](sounds/alert/error_buzz.wav) | 0.50 s | Harsh error buzz |
| [`wrong_buzzer`](sounds/alert/wrong_buzzer.wav) | 0.80 s | Game-show wrong-answer buzzer |
| [`correct_1`](sounds/alert/correct_1.wav) | 1.24 s | Correct-answer chime |
| [`correct_2`](sounds/alert/correct_2.wav) | 1.18 s | Bright two-note correct |
| [`alarm_beep_1`](sounds/alert/alarm_beep_1.wav) | 0.64 s | Four urgent beeps |
| [`alarm_beep_2`](sounds/alert/alarm_beep_2.wav) | 1.49 s | Hi-lo alarm |
| [`censor_beep`](sounds/alert/censor_beep.wav) | 0.60 s | Censor bleep (1 kHz) |
| [`warning_siren`](sounds/alert/warning_siren.wav) | 2.00 s | Siren sweep up and down |
| [`attention_ping`](sounds/alert/attention_ping.wav) | 1.63 s | Sonar-like attention ping |
| [`beep_short`](sounds/alert/beep_short.wav) | 0.12 s | Short beep |

### timer (9)

Preview: [audition/timer.mp3](audition/timer.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`tick_1`](sounds/timer/tick_1.wav) | 0.04 s | Clock tick |
| [`tick_2`](sounds/timer/tick_2.wav) | 0.05 s | Woody tick |
| [`clock_tick`](sounds/timer/clock_tick.wav) | 2.04 s | Tick-tock clock (2.5 s) |
| [`countdown_beep_1`](sounds/timer/countdown_beep_1.wav) | 3.60 s | 3-2-1-GO race beeps |
| [`countdown_beep_2`](sounds/timer/countdown_beep_2.wav) | 2.10 s | Fast 3-2-1 beeps |
| [`timer_done`](sounds/timer/timer_done.wav) | 0.96 s | Digital timer alarm |
| [`stopwatch`](sounds/timer/stopwatch.wav) | 1.59 s | Stopwatch start click and ticking |
| [`metronome`](sounds/timer/metronome.wav) | 1.55 s | Four metronome clicks (120 bpm) |
| [`ticking_bomb`](sounds/timer/ticking_bomb.wav) | 3.30 s | Ticking bomb countdown |

### drums (12)

Preview: [audition/drums.mp3](audition/drums.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`kick_1`](sounds/drums/kick_1.wav) | 0.45 s | Punchy kick |
| [`kick_2`](sounds/drums/kick_2.wav) | 1.10 s | Long 808-style kick |
| [`snare_1`](sounds/drums/snare_1.wav) | 0.30 s | Tight snare |
| [`snare_2`](sounds/drums/snare_2.wav) | 1.12 s | Big roomy snare |
| [`clap_1`](sounds/drums/clap_1.wav) | 0.43 s | Hand clap |
| [`clap_2`](sounds/drums/clap_2.wav) | 1.01 s | Clap with reverb |
| [`hihat_closed`](sounds/drums/hihat_closed.wav) | 0.08 s | Closed hi-hat |
| [`hihat_open`](sounds/drums/hihat_open.wav) | 0.50 s | Open hi-hat |
| [`rim`](sounds/drums/rim.wav) | 0.08 s | Rim shot |
| [`tom`](sounds/drums/tom.wav) | 0.60 s | Floor tom |
| [`crash`](sounds/drums/crash.wav) | 2.53 s | Crash cymbal |
| [`drum_roll`](sounds/drums/drum_roll.wav) | 3.54 s | Snare roll building up |

### food (7)

Preview: [audition/food.mp3](audition/food.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`sizzle`](sounds/food/sizzle.wav) | 4.00 s | Frying / sizzling pan (4 s) |
| [`crunch_1`](sounds/food/crunch_1.wav) | 0.25 s | Crunchy chip bite |
| [`crunch_2`](sounds/food/crunch_2.wav) | 1.06 s | Crunchy chewing |
| [`can_open_fizz`](sounds/food/can_open_fizz.wav) | 1.59 s | Soda can open + fizz |
| [`pour`](sounds/food/pour.wav) | 2.00 s | Pouring a drink into a glass |
| [`splash`](sounds/food/splash.wav) | 1.03 s | Water splash |
| [`chopping`](sounds/food/chopping.wav) | 1.13 s | Knife chopping on a board |

### paper (11)

Preview: [audition/paper.mp3](audition/paper.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`paper_1`](sounds/paper/paper_1.wav) | 0.47 s | Paper crinkle |
| [`paper_2`](sounds/paper/paper_2.wav) | 0.79 s | Paper crinkle |
| [`rip_1`](sounds/paper/rip_1.wav) | 0.45 s | Paper rip / tear |
| [`rip_2`](sounds/paper/rip_2.wav) | 0.80 s | Paper rip / tear |
| [`scribble_1`](sounds/paper/scribble_1.wav) | 0.80 s | Pen / marker scribble |
| [`scribble_2`](sounds/paper/scribble_2.wav) | 1.20 s | Pen / marker scribble |
| [`page_flip_1`](sounds/paper/page_flip_1.wav) | 0.35 s | Page flip |
| [`page_flip_2`](sounds/paper/page_flip_2.wav) | 0.50 s | Page flip |
| [`stamp`](sounds/paper/stamp.wav) | 0.29 s | Rubber stamp |
| [`crumple`](sounds/paper/crumple.wav) | 1.20 s | Paper crumpled into a ball |
| [`sticky_note`](sounds/paper/sticky_note.wav) | 0.32 s | Sticky note peel and slap |

### foley (30)

Preview: [audition/foley.mp3](audition/foley.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`zipper`](sounds/foley/zipper.wav) | 0.59 s | Zipper pull |
| [`knock_1`](sounds/foley/knock_1.wav) | 0.70 s | Door knock x3 |
| [`knock_2`](sounds/foley/knock_2.wav) | 0.58 s | Door knock x2 |
| [`glass_clink`](sounds/foley/glass_clink.wav) | 1.07 s | Glass clink / cheers |
| [`pen_click`](sounds/foley/pen_click.wav) | 0.15 s | Ballpoint pen click |
| [`light_switch`](sounds/foley/light_switch.wav) | 0.06 s | Light switch |
| [`spray`](sounds/foley/spray.wav) | 0.90 s | Spray can |
| [`fireworks`](sounds/foley/fireworks.wav) | 3.64 s | Firework whistle, bang and crackle |
| [`footsteps`](sounds/foley/footsteps.wav) | 2.24 s | Footsteps on a hard floor |
| [`door_open`](sounds/foley/door_open.wav) | 0.92 s | Door handle and creak |
| [`cup_set_down`](sounds/foley/cup_set_down.wav) | 0.40 s | Cup set down on a table |
| [`doorbell`](sounds/foley/doorbell.wav) | 2.97 s | Ding-dong doorbell |
| [`school_bell`](sounds/foley/school_bell.wav) | 2.46 s | Electric school bell (2 s) |
| [`bike_bell`](sounds/foley/bike_bell.wav) | 0.94 s | Bicycle bell ring-ring |
| [`car_horn_1`](sounds/foley/car_horn_1.wav) | 0.93 s | Car horn honk |
| [`car_horn_2`](sounds/foley/car_horn_2.wav) | 0.90 s | Double car honk |
| [`elevator_ding`](sounds/foley/elevator_ding.wav) | 2.55 s | Elevator arrival ding |
| [`referee_whistle`](sounds/foley/referee_whistle.wav) | 0.98 s | Referee whistle |
| [`kiss`](sounds/foley/kiss.wav) | 0.17 s | Kiss / smooch |
| [`slap`](sounds/foley/slap.wav) | 0.36 s | Face slap |
| [`bubble_wrap`](sounds/foley/bubble_wrap.wav) | 0.91 s | Bubble wrap popping |
| [`alarm_clock`](sounds/foley/alarm_clock.wav) | 2.56 s | Mechanical alarm clock ringing |
| [`glass_break`](sounds/foley/glass_break.wav) | 1.35 s | Glass breaking |
| [`door_slam`](sounds/foley/door_slam.wav) | 0.99 s | Door slam |
| [`keys_jingle`](sounds/foley/keys_jingle.wav) | 0.79 s | Keys jingling |
| [`phone_dial`](sounds/foley/phone_dial.wav) | 1.06 s | Phone keypad dialing tones |
| [`phone_busy`](sounds/foley/phone_busy.wav) | 2.50 s | Busy / hang-up tone |
| [`vinyl_crackle`](sounds/foley/vinyl_crackle.wav) | 3.98 s | Vinyl record crackle (4 s) |
| [`receipt_print`](sounds/foley/receipt_print.wav) | 1.30 s | Receipt printer |
| [`body_fall`](sounds/foley/body_fall.wav) | 0.92 s | Body falling to the floor |

### nature (12)

Preview: [audition/nature.mp3](audition/nature.mp3)

| Sound | Length | What it is |
|---|---|---|
| [`wind_1`](sounds/nature/wind_1.wav) | 5.00 s | Wind (5 s) |
| [`wind_2`](sounds/nature/wind_2.wav) | 5.00 s | Howling high wind (5 s) |
| [`rain`](sounds/nature/rain.wav) | 5.00 s | Rain (5 s) |
| [`thunder`](sounds/nature/thunder.wav) | 5.30 s | Thunder crack and roll |
| [`water_drop_1`](sounds/nature/water_drop_1.wav) | 0.48 s | Water drop |
| [`water_drop_2`](sounds/nature/water_drop_2.wav) | 1.59 s | Water drop in a cave |
| [`bubbles`](sounds/nature/bubbles.wav) | 1.64 s | Bubbles rising |
| [`fire_crackle`](sounds/nature/fire_crackle.wav) | 3.99 s | Campfire crackle (4 s) |
| [`wave`](sounds/nature/wave.wav) | 4.86 s | Ocean wave (5 s) |
| [`stream`](sounds/nature/stream.wav) | 4.00 s | Babbling stream (4 s) |
| [`birds`](sounds/nature/birds.wav) | 2.47 s | Birds chirping (3 s) |
| [`crickets`](sounds/nature/crickets.wav) | 3.89 s | Night crickets (4 s) |

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
