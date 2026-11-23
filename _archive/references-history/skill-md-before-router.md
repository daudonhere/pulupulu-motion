---
name: pulupulu-motion
description: >-
  Use when making a motion-graphics film, launch video, explainer, data story, or
  talking-head package. Directs commercial-grade motion as editable HTML +
  GSAP/Three.js, composes local ABC-notation music and sound effects, and renders
  frame-accurately in Chrome; also punches up or edits an existing film. Carries a
  merged art-direction library: 57 style recipes, 9 explainer grammars, camera
  language, palette sets and a shot-list linter.
metadata:
  author: "Alucard0x1"
  homepage: "https://github.com/Alucard0x1/pulupulu-motion"
  repository: "https://github.com/Alucard0x1/pulupulu-motion"
  version: "1.0"
  license: "MIT"
---



# pulupulu-motion

You are the **director, designer, composer, and animator**. Every film is a single self-contained composition (`index.html`: HTML + GSAP / Canvas / SVG / Three.js, rendered frame-by-frame in the user's own Chrome) with local synthesized/sampled music and sound effects. The user watches live in the studio, points at any frame, and you change that exact moment.

Aim for something people want to share — a film that could only be about **this** product, not a slide deck with easing and not the generic AI house style. Working code is the starting line; the finished frames and 1× playback with sound are the bar.

---

## 0. Sibling skills — when to hand off

This skill draws and scores the film. Other skills own the parts it must not fake. Read the matching
row before you start, and say which handoff you took when you report back.

| Skill | Hand off when | What it owns |
|---|---|---|
| **`tts-intonation`** | any film with spoken narration | phrase segmentation, planned gaps, micro tempo/pitch, the measured `timeline.json` the picture is cut against |
| **`agent-skill-sourcing`** | merging another motion library in, translating this one, or publishing a skill repo | namespacing a source, routing index, rebrand + history rewrite, bulk-translation waves |
| **`media-content-safety`** | before anything is published or posted | rights, likeness, disclosure, platform rules |
| **`streaming-mirror-extraction`** | the brief is "recreate this video" | pulling the reference file off a streaming/ad page, cleanly and lawfully |
| **`cinetic`** / **`headless-three-video-render`** | the story needs real footage, 3D, or a rendered rig | Remotion footage pipeline, scripted Three.js MP4 render |
| **`kinetic-typography`** | the film is type-first (words are the visuals) | type as the subject, per-word choreography |
| **`pdf-document-redesign`** | the deliverable is a static page, not motion | one branded page from a source document |
| **`youtube-content`** | research, reference selection, or publishing metadata | transcript/metadata work around the film |

Handoffs are one-way invitations, not merges: this skill never copies another skill's scripts into its own
tree, it points at them. Every reference document in this repo carries the same pointer footer
(`<!-- related-skills -->`) so a reader who lands on page 40 of the art library still finds the way back.

---

## 1. The Bar & Job Router

**Three tests, in the order films fail them:**
1. **Is it this product?** Real UI, real output, real words, real logo, and the product's own colours. Cover the logo: could the film be about a competitor?
2. **Does the energy have a shape?** A hook inside 3 s, a climb in steps, a burst, one earned stop, a peak, a resolve. A flat motion-per-second curve is a flat film, however good each frame looks.
3. **Is any stretch a slide?** A thing on a ground with a caption under it is a slide, however well it eases in. Every stretch gets its own shot scale and its own move.

| User intent | Workflow |
|---|---|
| **New film** | Follow the 9-step production workflow (§3) |
| **Existing film needs to be much better** | Follow *Punch-up* (§9.1): diagnose with numbers, keep idea & approved copy, rebuild shots & score |
| **Pointed at a frame in studio** | Follow *Comment loop* (§11): edit that exact place and time, nothing else |
| **Talking-head video packaging** | Follow *Talking-head* (§9.3) with `talking-head` template |
| **Overlay, loop, or single shot** | Steps 3–6 and 8; skip the 3-direction gate if a style was already given |

**Deliverable rules (this user).**
- **No tool signature.** Set `data-om-signature="off"` on the root element — this user rejects AI/tool credit text on anything delivered.
- **One language on screen.** An Indonesian film is Indonesian everywhere except proper nouns and names that stay untranslated ("Grand Prix"); an English label dropped into foreign-language copy gets called out as a messed-up mix, however good the frame looks. **One term per concept for the whole film too:** if the narration says *release*, every card and caption says *release* — a synonym swap (*ship* on one card, *release* on the next) reads as the same sloppiness, and the fix is a find-and-replace across the copy table plus one re-synthesis of the affected line.
- **Proofread the spoken script, not only the captions.** TTS reads a doubled or garbled word verbatim — an Indonesian line that doubled its preposition came out as "from land land, he moved…" — read the narration table once before spending a synthesis run, and re-read it after any edit.

**Fixed gates (non-negotiable):**
- **The topic fits the engine** — check the brief against `references/topic-fit.md` before designing anything. A subject with no real material, no numbers and no drawable process (a biography, a historical figure, a character acting out a scene) cannot be carried by drawn geometry and comes back as "jelek" however good the craft; say so and offer the material-led route instead of building it.
- Real material collected in `materials/` and `materials.md` before any design.
- Three genuinely different directions (one in depth) with full-res key frames + `om swatch`, then wait for choice (unless user named a style or said "just make it").
- `treatment.md` written before full build.
- `om check` passes with 0 errors.
- Your own inspection of `om still` frames + `om qa --sheet` contact sheets + 1× playback before the user sees a render.
- **Craft gate before the taste gate:** every still passes `references/visual-craft.md` — four-layer shading with one light direction, a ground plane with cast shadows, a far band that is visibly desaturated, one subject per shot that bleeds past an edge, palette per act, and caption contrast that works on light acts. A scene that is technically clean but has no shading and no depth is the "visuals are weird and bad" failure, and no checker catches it.
- Every sourced glyph looked at on an `icon_audit.py contact` sheet at final size (greyscale + phone scale) before it enters a scene.
- `pulupulu qa` on the **final mapped file**; `no single-frame pops` must pass. Every other line it prints is a reading note (§ gates). Never publish or post anything yourself.

---

## 2. CLI Reference (`pulupulu`)

Invoke the self-hosted CLI (`pulupulu <cmd>`, or `om <cmd>`); if it is genuinely absent, install it once and never fall back to `npx` per command (§ below). `om check`, `om still`, `om look`, `om sound`, and `om render` drive the user's installed Chrome locally (no cloud API). If your sandbox blocks starting Chrome or a local server (`127.0.0.1`), request permission to run outside the sandbox rather than skipping visual checks.

```sh
# Material & Setup
om grab <url|folder> [dir]          # Collect screenshots, logo, images, CSS colours & fonts into <dir>/materials/
om templates                        # List starter templates (blank, ui-space, object-3d, talking-head, + 8 grammars)
om new <dir> [--template t]         # Create contract-ready project
om demo [dir]                       # Copy showcase film and open in studio
om fonts [add <family> [dir]]       # List bundled typefaces (CJK 500-900, serif, display) or install into project

# Studio & Point-to-Edit Loop
om studio [dir] [--no-open] [--lang zh|en|es]  # Live preview + direct variable edits + frame comments
om inbox [dir] [--wait] [--timeout 540]        # Block until user comments, claim & print context + source line
om look <id|--at sec> [dir]         # Save frame PNG + close-up of clicked spot
om done <id> [dir] --note "…"       # Resolve comment with one-line summary in user's language
om vars [dir] · om set k=v… [dir]   # List or update composition variable defaults in index.html
om scan [dir] · om undo [dir]       # JSON map of vars/objects/scenes · restore previous version in .om/history

# Audio & Narration
om samples [build [ids…]]           # Status / one-time install (~55 MB) of real-instrument samples (piano, strings, drums)
om voice <dir> --text <file|"text"> | --audio <file> [--voice say:Tingting|zf_xiaobei] [--fit]
om sound [dir] [--list] [--off]     # Render assets/sound.wav from om-score / OM.music / OM.sfx; prints energy curve

# Visual Checks, Render & Share
om still <page.html|dir> [--at 0,2.5] [--out file]  # Render PNG(s) of any page or composition
om swatch [directions.md] [--out file]              # Render direction card palettes + contrast/house-look warnings
om check [dir] [--samples n] [--source] [--json]    # Validate scripts, motion rules, layout/contrast, seek determinism
om render [dir] [--format mp4|mov|webm|gif] [--fps 30] [--blur [n]] [--transparent] [--silent]
om qa [dir|video] [--loop] [--sheet [fps]]          # Check pops, dead time, hard cuts, motion curve, loop seam, contact sheet
om fork <dir> <newdir> --size 1080x1920             # Copy to new aspect ratio; queues re-layout task in inbox
om share [dir] [--from s] [--to s]                  # Generate <=10 MB GIF + out/share/share.md
om export html [dir] [--out folder]                 # Standalone share page (player, Remix prompt, source.zip)
om learn [topics…] · om learn harvest [dir]         # Read/extract user preferences & film lessons
om doctor                                           # Check Node (>=22), FFmpeg, and Chrome renderer
```

---

## 3. Nine-Step Production Workflow

1. **Direct it.** Run `om learn <topics>` first. Read the product (site, repo, app, README, screenshots) and gather real material into `materials/` + `materials.md` via `om grab <folder|url> <dir>` and live app captures.
   - **Real material rules:** Logo on screen = real SVG/image file, never redrawn. UI = real capture for context, or **rebuilt in HTML/CSS** traced over a capture at exact size when it must move (typing, clicking, scrolling) — never grey placeholder boxes or invented UI. Photos/avatars/thumbnails = real product assets or openly licensed (Unsplash/Pexels/Wikimedia) with source + license in `materials.md`. Mask private data in local screenshots.
   - **Icons and objects come from a real vector library, not from your hands.** `svgrepo.com` serves direct SVG files (`https://www.svgrepo.com/show/547900/<slug>.svg`) and organises them into single-style collections. Take every icon from **one family** (line, solid, duotone, rounded — matching stroke weight, grid and corner language), keep them **monochrome and recoloured into the film palette** by default, and reserve **multicolour** for the one hero object whose real colour means something. License is per icon page: follow SVG Repo License / PD / MIT for client work, never CC BY-NC.
     - **Order of operations (do not shuffle it):** write the film's own drawing language down (`flat fills → silhouettes only`) *before* searching; then `classify` every download, `families`-group them, pick from the dominant compatible group, `normalise`, inline at build time, and **look at a contact sheet at final size** before the glyph enters the film. A line-art glyph in a flat-fill film reads as a sticker; a one-colour etched illustration and a silhouette are indistinguishable from the file text — only the rendered sheet separates them.
     - **Tooling:** `python scripts/art-motion/icon_audit.py --film-style solid classify DIR | families DIR | normalise FILE.svg | contact DIR` (grid, line-vs-solid, colour count, path count, family grouping, recolour, contact sheet). It says `undecided` when the text cannot tell — resolve those by looking, never by assuming.
     - **Licence:** record `name.svg_<id> — source URL — licence` in `materials.md` at normalise time. If the label cannot be read (SVG Repo renders it with JS), write `not verified` and treat the file as a placeholder, never as a named licence.
     - Full loop, search vocabulary, decision tables, failure log: `references/asset-sourcing.md`.
   - **When no library carries the object, generate the print instead of drawing it.** Pictorial material (a 1980s terminal, a magazine page, a console, a portrait mount, a map) is where hand-drawn paths read as stickers and an icon library has nothing. Brief a register into `DESIGN.md`, generate 1024 px prints four at a time with an image model, crop each to its content, mount it as a panel, and add all type in HTML. Full route with the crop script, mount geometry, register table and the one-round critique: `references/generated-assets.md`.
   - **Documented is not applied — this user checks.** A film built shot by shot on hand-drawn geometry while this section sits in the skill comes back as "why didn't you use the icon library" — the question this user actually asked. Close the loop mechanically: every build ends with a `materials.md` that either lists the sourced files (source URL + licence) or states in one line why no library asset fits that shot. Keep the budget small and honest — on a 21-shot story film **two** shots needed a real object (a locomotive, a flag) and the rest were bespoke geometry no library carries; an icon in every scene is decoration, which §3e forbids. In a flat-shape film only **single-colour silhouette** glyphs survive the recolour test; a line-art glyph among flat fills reads as a sticker.
   - **One-line user requests:** Do the research first, then send **one** plain message with what you understood (product + the one takeaway) and 3–4 high-impact decisions with your defaults marked and 2 real-world alternatives each (where it plays & length, energy, narration). Never send a multi-question form. Always settle **narration**: none (music+sfx), system TTS (`om voice --text`), user recording (`om voice --audio`), or footage audio. Default: none.
   - **Energetic default (when no style/energy named):** Frame 0 is the poster (subject already present, never blank/black or a lone glowing dot). Move at once, land the first burst < 5 s, cut on the beat, keep type large enough for a phone feed, and stay in the product's palette.

2. **Three directions** (skip only if user named a style or project already has one). Offer A (Fit), B (Amplify), and C (Unexpected) differing in **motion language or material**, not just colour:
   - **Exactly one** of the three must be a **depth direction** (`ui-space` or `object-3d`); the other two must have no 3D as their core idea. Never three quiet directions for a launch film.
   - If directions share a drawn character/emblem, build that artwork alone at full size first. Never draw organic animals/people as crude geometric SVG — cut from real art/photos.
   - For each direction, output the card below, render **one real full-res key frame** (`om still directions/a.html`), and run `om swatch directions.md`:
     ```text
     A · <name>       language: <id> (+ technique highlights)   look: <type, material, light>
     Palette:         <role #hex share · …> — from: <source of each colour>
     Logline:         <one sentence with hook and ending>
     Why it fits:     <message shape + personality sentence → this>
     Feel:            <route (continuous/montage/hybrid), BPM, events/bar, first 3 s muted>
     Risk:            <what could make it fail>
     ```
   - Keep `Palette:`, `look:`, and `Feel:` separable so the user can mix layers ("A's palette with C's composition"). Pick the music world yourself after direction approval; don't put music on direction cards unless asked.

3. **Treatment (`treatment.md`).** Write before building the full film:
   - **Rhythm sheet** (stretch, bars, energy 0–10, events/bar, moves, music) + **Beat map** (`bar.beat | time | what happens | language move | sound`).
   - **Four stills** (`om still <dir> --at t1,t2,t3,t4`): hook frame, hero moment, densest frame, end card.
   - **Continuity chain**: one line per transition naming what object or colour carries the eye from shot N to N+1. Any unlinked jump is a hard cut — keep only if intentional.

4. **Build the hardest shot first.** Use a grammar template (`om new <dir> --template <id>`) if narration fits a structured explainer; otherwise `om new <dir>` (`blank`, `ui-space`, or `object-3d`). Build the hardest/most important moment at full resolution with final fonts and colours before laying out the rest. Place `OM.sfx(name, t)` on landing frames and `scene:<id>` labels on `OM.beat(n)`.

5. **Look at it & self-critique.** Run `om check <dir>` (0 errors). Inspect `om still` frames (especially frame 0, end frame, and 0.25 beats after every cut). Render without `--blur`, run `om qa <dir> --sheet`, and inspect every contact sheet for identical-tile runs (dead time), slide-like repeats, and ugly mid-transition frames. Watch at 1× speed (or have a cold reviewer agent watch it) and write & fix the 3 notes a demanding director would give.

6. **Give it sound.** Run `om voice` first if narrated, then `om sound <dir>` (ducks music automatically). For launch films, write a custom ABC `<script type="text/vnd.abc" id="om-score">` (Composer mode, §10); use `OM.music({ product })` only for quick drafts/stings. Fix every `warning score:` line. Aim for 8–15 `OM.sfx` hits per 30 s. Check spectrogram (`ffmpeg -i assets/sound.wav -lavfi showspectrumpic=s=1600x400 spec.png`) to verify hits align and no stretch is empty. Skip only for `--transparent` overlays or requested silence.

7. **Hand over studio.** Run `om studio <dir> --no-open &`, share the URL, and loop on `om inbox <dir> --wait` → `om look` → minimal edit / `om set` → `om done` until signed off. Re-run `om sound` after any timing change.

8. **Export & Share.** Render final export with `om render <dir> --blur` (and `data-fps="60"` for fast UI). Run `om qa <dir>` (`--loop` for loops). Run `om share <dir>` and write `out/share/share.md` in the user's language (what the film is + 1 concrete making detail). Report the MP4, GIF, and `share.md`, noting the end carries a small toggleable signature. Never post anything yourself.

9. **Harvest.** Run `om learn harvest <dir>` on sign-off to distil studio edits/comments into `~/.pulupulu-motion/experience.md`.

---

## 3a. Storyboard & narration contract (before any HTML)

A narrated film that comes back as "captions don't match the story" was authored on two clocks: the words in one table, the pictures and captions in another. Fix it by construction, not by proofreading.

**Write `storyboard.md` first — one row per beat, nothing else in the file:**

```text
beat | spoken phrase (verbatim)            | picture (the ONE thing that changes) | pause after
b01  | Two in the morning and your phone rings. | 02:00 clock, phone buzzing      | 0.55
b02  | Your site is down.                   | red flood + 500, hard cut in         | 0.90
b03  | You check hosting: the machine is alive. | dashboard card, all green         | 0.50
```

Rules that make the film cohere:
1. **One beat = one spoken phrase = one visual change = one caption.** If a beat needs two pictures, it is two beats.
2. **The caption is the spoken phrase, verbatim.** Never a summary, never a rephrase, never "better written" — a caption written separately from the voice drifts away from the story within three beats, and the viewer sees it immediately. The **only** licensed difference is *display form vs spoken form*: the voice says `five oh two` while the screen shows `502`, the voice says `D N S` while the screen shows `DNS`. Same sentence, different notation — see the `tts-intonation` skill §2b for how to decide per token, and let `tts-prosody.py --expand en|id` write and audit it. Style it with `<em>`, never rewrite it.
   - **Chunk to 2–4 words on the spoken punctuation, and never leave a one-word last chunk.** Splitting a phrase into fixed-size groups strands a single final word (`In nineteen eighty` / `four,`), which occupies a whole cue slot alone and reads as a typo rather than a caption. After chunking, merge any trailing chunk of one word into the one before it, and size the cue windows from the measured beat length divided by the final chunk count — not by the count before the merge.
   - **Show notation, speak words — and weight cue windows by their word count.** A year reads as `1984` on screen while the voice says *nineteen eighty four* (a spelled year splits across cues and the first chunk reads as the wrong year); small prose numbers keep their words, and a large statistic compresses to a readable unit (`2 million`, not `2 000 000`). Give each cue a window weighted by its own length instead of an equal share of the beat — an equal share makes a one-word chunk linger as long as a four-word one, which is what makes captions feel late. Never split a year or a number+unit across two cues. Detail: `references/visual-craft.md` § *Number and year captions*.
3. **Narration is written to the clock, not to the screen.** Budget ≈ **2.4–2.7 spoken words per second**: a 60 s film holds **120–150 words including pauses**. Over budget means cutting words, not reading faster.
4. **Phrases of 4–12 words, one idea each**, with a planned pause after (0.2 s inside an idea, 0.5 s for a new claim, 0.9–1.2 s before the payoff). Full method: the `tts-intonation` skill.
5. **The timeline is measured audio, never a number picked in advance.** Synthesise the phrases, measure each one, emit `timeline.json`, then place every beat's picture and caption inside its own `[start, end]` window. Film length = the timeline total.
6. **Split the voice from the score before it is too late:** `om sound` is generated against the film length produced by the timeline, and the mix is padded with `apad=whole_dur=<film length>`.

**Self-check before building:** read the storyboard aloud, ticking a finger per word. Any beat whose phrase cannot be said inside its slot is already broken — cut words now, not after the render. Then check the reverse direction: every picture must be *caused* by its phrase (the phrase "disk full" cannot sit on a shot of a server rack) — and when the phrase names a set, a count or a shape, draw exactly that: a beat about *twelve pentominoes* cannot show four-cell tetrominoes, and a beat about *seven shapes* cannot show twelve, however good the grid looks. Two beats showing the same layout with different captions is a slide deck, not a storyboard.

## 3c. One language, checked mechanically (not by proofreading)

**The film's language covers every visible string and the voice: captions, headlines, card labels, tags, units, end card — plus art-template literals, which are the ones that leak.** Copy tables get translated on a re-language; the headline baked into a `visual()` template does not. One Indonesian film was rebuilt in English with every caption and card converted and still shipped the flood beat with the old-language headline, because that string lived in the generator's HTML, not in `beats.json`.

So the gate is mechanical, and it runs on the **rendered HTML**:

```sh
python scripts/lang-audit.py film/index.html --lang en    # exit 1 = leftovers
```

`scripts/lang-audit.py` strips tags/styles for the markup pass, then scans **two** haystacks against the *other* language's stopword list and fails the build: the visible text, and the **string literals inside `<script>`**. The second one is not optional — a runtime label or a canvas caption lives only in JS, so an audit that drops scripts wholesale (the original behaviour) cannot see the leak it exists to catch. Repro of both directions: a page whose only foreign text sits in a script returns hits with `where: script` and exit 1, and the same page under `--no-scripts` passes. Prove the gate is alive that way after touching it, before trusting a green run.

Read those literals with a small hand-written scanner, not a regex: a character class that must exclude both the quote and the backslash ends in a trailing backslash and either refuses to compile or matches across the closing quote, returning fragments like `').textContent = '`. Filter out identifiers, selectors and URLs by shape, dedupe, then scan. Wire it into the generator so it cannot be skipped:

```python
subprocess.run([sys.executable, "../lang-audit.py", os.path.join(OUT, "index.html"),
                "--lang", "en"], check=True)   # build.py aborts on a leak
```

Then look at one frame per scene. The audit catches tokens, not tone: a frame can pass the scan and still read like a translation.

## 3d. Duration policy: the format is fixed, the length is negotiated

**Fixed, never traded away:** width × height, aspect ratio, fps, codec, safe zones, and any platform constraint the brief names (9:16 for Shorts, 1:1 for a feed ad, alpha for overlays). Screen format is a hard requirement.

**Negotiated:** the running time. A "1 minute film" means *about* a minute: 55–69 s is inside tolerance (60 s +15 % = 69 s, so the window and the cap are the same rule), and inside that window the film takes the length that keeps the narration good. An explicit cap from the brief wins over this tolerance. The order of preference, when a script will not fit:

1. **Cut a beat, or cut a clause.** Copy is cheap and gets sharper.
2. **Lengthen the film** by the seconds the narration actually needs (up to ~+15%).
3. **Only then** trim pauses, and never below 0.2 s between phrases.

**Never compress speech to hit a round number.** `atempo` past 1.08, dropped pauses and crammed phrases all make the voice sound like a machine reading a legal notice — a worse defect than being four seconds long. Report the final length and the reason in one line (`64 s — the English script needs 55 s of speech; cutting a beat would have removed the turn`).

## 3e. Design taste: theme, elements, motion

Taste is not decoration, it is a series of defensible defaults. Decide these before the first frame and write them into `treatment.md`.

### Ground: dark or light

| The film is about | Ground | Why |
|---|---|---|
| infrastructure, servers, terminals, security, night, uptime, gaming, music, a launch at night | **dark** | the subject *is* the dark; status colours glow, codes read as light |
| data reports, editorial, teaching, health, daylight service, documents, a light product UI | **light** | matches the artifact, reads faster at a glance, prints well |
| an emotional or cinematic story | **dark, desaturated** | falls back, lets one accent carry feeling |
| a product whose own UI is light | **light** | the screen must match the product, never invert it |

Rules: dark ground = one luminous accent + a 3-step value ramp, never `#000`; light ground = a warm or cool off-white, never `#fff`, with an ink accent. **Flip the ground at most once per film**, and only on a story beat (a flood, a verdict, the drop).

### Element budget (what may exist in a frame)

- **Three zones, one each:** headline, artifact (diagram / chart / object / UI), caption. Nothing else competes.
- **Colour:** 3 hues + a neutral ramp; accent ≤ 5% of pixels; state colours are reserved (red = failure, amber = warning, green = healthy) and never reused decoratively.
- **Type:** at most 2 families (display + text), scale contrast ≥ 3× between the largest and the body, captions ≥ 56 px at 1080 wide, contrast ≥ 4.5:1.
- **A hero label sitting on a prop takes that prop's contrast, not the act's ground colour.** `color: ink` is right for a label on the background and invisible for the same label on a light sheet inside a dark act — a price stamp on paper, a caption over a cream card. Pass an explicit colour when the label's backdrop is an object; `om check` reports `low-contrast … 1.2:1` and the words simply are not there.
- **Nothing without a job.** A border, glow, rule or icon that carries no meaning gets deleted. Density is a genre decision: explainer = dense cards, launch = one hero object, data story = chart + one number, kinetic = type only.

### Motion register (match the subject, not your mood)

| Subject | Motion |
|---|---|
| systems, infra, code | snap into a grid, `expo.out`, hard cuts, terminals typing |
| data, numbers | count-up, bars from zero, draw-on, one turning point |
| hardware, objects | camera in space, rack focus, one slow orbit |
| human, emotion | long eases, small moves, no bounce |
| lists, chapters | one-word-at-a-time type, wipe, chapter counter |

One move per beat; exits faster than entrances; never drift every element at once. A reading hold still gets a 1–3% push so the frame is never a freeze.

### Composition of a flat scene (no depth to hide behind)

Drawn-vector scenes fail in three ways no checker sees:

- **Seat every object on its surface, arithmetically.** A subject placed by eye (a train at `y: 600` over rails at `y: 886`) floats or sinks. Compute `top = surfaceY - objectHeight` from the same constant the surface uses, and keep one `HORIZON`/`BED` constant per film so all scenes share one geometry.
- **A generated scene is drawn in the frame's coordinates, not the frame's size.** Scene helpers authored around a comfortable `y 600–1300` band leave a 1080×1920 frame two-thirds empty, and `om qa` reads the result as a still film. Rather than re-lay out every scene, put a static CSS scale on the scene wrapper — `.art { transform: scale(1.5–1.8); transform-origin: 50% 40% }` — then re-open the widest and tallest scenes to check nothing crops. Keep that transform static: animating it is the full-frame-tween render trap in the field notes below.
- **The bottom quarter is where flat films look cheap.** A backdrop helper that stops at `y ≈ 800` leaves 40% of a 1920 frame as a single value. Carry the ground texture (scatter, ballast, stones) to the frame edge and add two or three foreground shapes; empty ground under a caption reads as unfinished.
- **A caption over mid-value ground needs a scrim — and the scrim belongs inside the shot, not above it.** White text plus a black outline still vanishes over a brown or grey field at partial opacity, so put a `linear-gradient` behind the caption band and keep the caption topmost *within the beat*. A single global scrim `<div>` placed after the beats paints over every caption, because `z-index` on the caption only ranks it inside its own parent's stacking context: `om check` then reports `text-covered` once per caption and the render shows the words at ~15% opacity. One scrim per beat, between the art and the `.capbox`.

### Taste checks before a render

Squint test at 25% scale (hierarchy must survive) · greyscale test (value, not hue, must carry the hierarchy) · phone test at 1080 width · count the colours, fonts and accents out loud · "could this frame be about a different subject?" — if yes, it is a template; change the ground or the type rather than the easing.

## 4. Director System: Shape, Personality & Taste Rules

### Message Shape → Motion Language
| Shape | Sounds like | Natural languages | Avoid |
|---|---|---|---|
| **Claim / feeling** | "Introducing X." | `kinetic-type`, `generative-field`, `3d-object`, brand ident | UI tour |
| **Workflow** | "Type this, get that." | `cursor-demo`, `continuous-morph` | abstract shapes, no product |
| **Mechanism** | "Here is why it works." | `mechanism`, `system-diagram`, `flat-world` | fast cut reel |
| **Evidence** | "Signups doubled." | `data-story`, `editorial-collage` | unreadable flashing numbers |
| **List** | "Five new things." | `kinetic-type` chapters, `modular-grid`, `card-montage`, `continuous-morph` | five equal slides |
| **Transformation** | "Before / after." | `continuous-morph`, `data-story`, split compare | hard cut between two stills |
| **Story** | "An agent wakes up…" | `talking-head`, `photo-led`, `character`, `flat-world`, `hand-drawn` | bullet points |
| **Showcase** | "Look what it can do." | one deep artifact (`mechanism`, `3d-object`), `showreel`, `art-styles` | feature list |

### Five Personality Sliders (-2 to +2)
Score from product evidence (site type, copy, UI) and summarize in one sentence (e.g., *"Precise, calm, premium, technical, new — Linear-like"*):
- **precise ↔ playful**: easing (hard `expo.out`/linear → `OM.spring` with overshoot) & shape (grids → blobs).
- **calm ↔ energetic**: tempo (80–100 → 125–150 BPM), shot length, cut density. *(Note: Launch films default to energetic 100–125 BPM with 15–33 cuts/min and a 5–8 cut burst even for calm brands; brand calm sets palette/type/eases, not energy, unless user asks for calm or it's an ambient loop.)*
- **premium ↔ accessible**: negative space, type scale contrast, colour count, screen density.
- **technical ↔ human**: monospace/code/diagrams vs photos/faces/hand-drawn warmth.
- **established ↔ new**: restraint & continuity vs bold, surprising, meme-literate.

### Film-Wide Taste Rules (Defaults)
1. **Start moving.** Frame 0 has the subject in it and is already moving or unresolved. Never open on a blank card or lone glowing dot on black.
2. **Choose the route intentionally.** Continuous (0–2 cuts, UI recordings), Montage (beat-locked cuts), or Hybrid (continuous spine + montage bursts — best for tech launches).
3. **Energy has a shape.** Hook ≤ 3 s, climb in steps, burst at 30–60%, hero on the drop, resolve on the mark.
4. **Real product.** Rebuilt UI or real captures/recordings. Never grey boxes, invented UI, or panned static screenshots.
5. **Craft shows at rest.** Every hold is a poster: real font (`om fonts`), weight contrast, tabular numerals (`font-variant-numeric: tabular-nums`), clean alignment.
6. **Sound matches format.** Short UI films/loops (< 20 s) must read muted; > 30 s or with people are sound-led.
7. **End right.** Launches end on the mark (URL optional); showcases/lists/loops return to frame 0.
8. **Give something to take.** Saves come from reusable artifacts (prompts on screen, named lists, labelled specs).
9. **Not a template.** The product's own colours, shapes, and vocabulary must generate the motion.

---

## 5. Colour System

**Find colours before inventing any** (document source in `Palette: ... — from: <source>`):
1. **Brand's own values:** site CSS custom properties, `theme-color`, logo SVG, app icon.
2. **Product itself:** sample real UI screenshots, hardware finish, or product outputs.
3. **Material world of the idea:** sample real photography of the physical domain (paper, clay, phosphor, anodized metal).
4. **Invention (last resort):** label `"invented: no brand colours found"`.

**System roles:** `ground` (most of frame) · `surface` (~20%, 1–2 steps off ground) · `ink` & `muted ink` (neutral white/black, ≥ 4.5:1 contrast for small text) · `accent` (~1–5%, marks only the active/new thing) · `flood` (optional full-screen accent on a beat).
- **Value first:** Desaturate a still — hierarchy must still read in greyscale.
- **Light is part of colour:** Subtle vignette, falloff, or seeded grain (3–6% opacity); flat hex fills read as slides.
- **Avoid the AI house-look** (unless the brand itself actually uses these exact hexes):
  - Dark ground + warm accent (terracotta/amber/vermilion) + bone/cream type.
  - Warm off-white/cream ground + serif/giant grotesk + terracotta accent.
  - Near-black + acid lime/green; purple-to-blue gradients; neon on GitHub-dark.

---

## 6. Rhythm & Contrast

Boring = 1 event every 4–5 s, same move every scene, 0.6–0.8 s soft eases everywhere, flat pad music.

| Stretch | Bars | Energy (0–10) | Events / bar (4 beats) | Shot / move length |
|---|---|---|---|---|
| **Hook** | 1–2 | 6–7 | 2–4 | 0.25–0.5 s moves; onset ≤ 3 s |
| **Build** | 3–6 | 5 → 7 | 2–4, rising | 1–2 beats per move |
| **Stop** (optional) | 1 | 1 | 0–1 | hold 1–2 beats (0.5–1.6 s) |
| **Peak / Montage** | 4–8 | 9–10 | 4–8 (5–8 cuts in ~5 s at 30–60%) | ½–1 beat per shot |
| **Resolve / Mark** | 2 | 4 | 1–2 | hold ≥ 1.5 s on mark (with 3–6% linear drift) |

**Fixed rule:** No stretch > ~2 bars without a new event (outside a planned stop).
**Contrast schedule:** Change **≥ 2** of these at every section boundary (and all at the drop):
- **Shot scale** (ECU detail ↔ wide system) · **Speed** (0.25 s snap ↔ 2 s glide, speed ramps) · **Ease family** (`expo.out` tech ↔ `OM.spring` physical) · **Camera** (still ↔ drift ↔ whip) · **Density** (1 object ↔ 3×3 grid) · **Colour/ground** (flip or flood) · **Music texture** (half-time ↔ full beat ↔ stop ↔ drop).

**Beat-locked montage pattern:**
```js
OM.music({ bpm: 128 });
const B = (n) => OM.beat(n);
const shots = gsap.utils.toArray('.shot');
const beats = [2, 2, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5]; // accelerate into stop
let t = B(32);
tl.addLabel('scene:montage', t);
shots.forEach((el, i) => {
  const cutT = (Math.floor(t * 30) + 0.5) / 30; // half-frame in for --blur
  tl.set(el, { autoAlpha: 1 }, cutT);
  if (i) tl.set(shots[i - 1], { autoAlpha: 0 }, cutT);
  tl.fromTo(el, { scale: 1.12 }, { scale: 1, duration: B(beats[i]), ease: 'none', immediateRender: false }, cutT);
  OM.sfx('hit', cutT, { gain: 0.45, pitch: 1 + i * 0.04 });
  t += B(beats[i]);
});
```

---

## 7. Motion Library: Formats, Languages & Techniques

### Formats Quick-Reference
- **Launch sting (6–15 s):** Hook (0–4B) → product action (4–16B) → drop hero (16B) → payoff (20–26B) → mark (26–32B). Muted-safe, name ≥ 1.5 s.
- **Launch film (30–90 s):** Cold open on result/problem (0–5 s) → 2–4 distinct capability moments → optional non-UI spectacle → proof → mark (2–4 s). Climax at 70–85%.
- **Feature demo (10–45 s):** Context (1–2 s) → action → response → readable result. Follow §9.2 continuity.
- **Explainer (30–180 s):** Question → intuition → step-by-step mechanism (1 visual change/sentence) → payoff → whole-system recap.
- **Data story (15–60 s):** Question → baseline (bars start at 0!) → change → turning point → takeaway + source.
- **Kinetic manifesto (8–30 s):** 1 word/phrase per 1–2 beats → build → silence/break → payoff → mark.
- **Showreel (10–20 s):** ~8 sections of 1–1.3 s on one spine (colour, HUD chrome, shape, track).
- **Social hook / ad (6–20 s, 9:16):** Hook in 0.5 s → problem → product → CTA ≥ 2 s. Safe zones at 1080×1920: top 220 px, bottom 520 px, right 14%.
- **Resource list loop (8–25 s):** Title + count → numbered items (~2–2.5 s each) with chapter counter → full wall → seamless return to frame 0.
- **Loop (4–12 s):** Last frame = first frame including velocities (`om qa --loop`).
- **Step promo (15–30 s):** Problem (2–3 s) → 3–6 numbered working UI cards + progress bar → completion receipt → mark.

### 20 Motion Languages
Mix at most 3 languages in 30 s, carrying a shared spine (palette, shape, or cursor) across switches:

| Language | Says | Best for | Template / Route |
|---|---|---|---|
| `cursor-demo` | It works; here's how | Workflows, SaaS, AI apps | `blank` + §9.2 |
| `continuous-morph` | One crafted system | Consumer apps, UI states, loops | `blank` |
| `card-montage` | Step by step, real | Indie promos, step promos | `blank` |
| `kinetic-type` | Claim with conviction | Slogans, lists, hooks, endings | `kinetic-type` / `blank` |
| `modular-grid` | Precise, engineered | Dev tools, infra, fintech, specs | `blank` |
| `data-story` | Here's the evidence | Metrics, earnings, milestones | `finance-chart` / `blank` |
| `mechanism` | Why it works | AI/ML, algorithms, math/science | `math-3b1b` |
| `system-diagram` | How parts connect | Infra, APIs, agent pipelines | `blank` |
| `flat-world` | Wonder, scale | Science, health, education | `kurzgesagt` |
| `editorial-collage` | Real; look at this line | News, commentary, case studies | `vox-collage` |
| `hand-drawn` | Human, thinking aloud | Teaching, friendly brands | `whiteboard` |
| `character` | Emotion, heart | Stories, mascots, agents as actors | `storytime` |
| `3d-object` | Tangible, premium | Hardware, logos, devices, UI in space | `object-3d` / `ui-space` |
| `generative-field` | Intelligence, mood | Model launches, music, ambient loops | `blank` |
| `liquid-glass` | Premium consumer | iOS apps, photo/media | `blank` |
| `photo-led` | The real world | Travel, food, fashion, UGC ads | `blank` |
| `showreel` | Range & mastery | Capability reels, "made with X" | `blank` |
| `retro-digital` | Culture, edge | CLI tools, dev culture, games | `blank` |
| `art-styles` | Culture, delight | Showcases, unexpected direction C | `blank` (canvas/SVG) |
| `talking-head` | Real person behind it | Founders, creators | `talking-head` |

### Techniques Vocabulary & Rules
- **Timing & Easing:** `expo.out` (0.5–0.9 s) for arrivals (sfx at ~35% where it visually lands); `OM.spring(0.08)` UI / `OM.spring(0.25)` playful / `OM.spring(0)` damped; `power2.inOut` for camera moves only; `linear` for tickers/drifts/rotations only; anticipation (2–6% reverse move 0.1–0.15 s prior); stagger (30–60 ms UI, 15–25 ms letters); exits faster than entrances (0.25–0.4 s `power2.in`).
- **Entrances:** Mask reveal (`overflow:hidden`, `yPercent: 110 -> 0` `expo.out`), scale from 0 on spring, SVG `stroke-dashoffset` draw-on, deterministic `type-on` (`Math.floor((t - t0) * cps)`), `clip-path` wipe. **Avoid `blur-in`** as a generic entrance. **Never** animate `left`/`top`/`width`/`height` (animate `x`, `y`, `scale`, `rotation`). An SVG `<g>` target also needs `transformOrigin: "50% 50%"` (`transform-box: fill-box`), or a `pop`/`stamp` scale paints from `(0,0)` and the element flies in diagonally. Physics: overshoot for things arriving in air; something that lands on a surface accelerates (`power2.in`) and locks with a 4 px recoil — `back.out` bounces it back through solid ground.
- **Continuity devices (prefer over cuts):** Shared element box morph, UI pill/card morph, flood-and-contract (0.3–0.35 s overscale), nested reveal (pull back from result into editor/app), path-follow, match cut, whip (0.15–0.25 s + `--blur`), colour-field flip, collapse into the mark. **Avoid crossfades** between scenes.
- **Camera (`OM.camera('#world')`):** `cam.to(tl, t, { fit: '#el', pad: 120, duration: .8, ease: 'expo.inOut' })`, push in, pull back, screen-studio zoom (1.6–3×), linear drift (3–6% during holds — no dead frames!), parallax, camera shake (2–6 px decaying 0.2 s via `OM.random(seed)`). Never reverse direction mid-scene.
- **Typography:** Variable font weight/width animation, scale slam (140–200% → 100%), word-by-word on beat, kerning squeeze, pill highlight (0.3 s L→R), text reel, strike-through & replace, punctuation as character, type as mask container.
- **UI & Data:** Cursor choreography (hover ×1.55, press −15% + ripple), prompt receipt on screen, chat-bubble stack, completion receipt (`6/6`, 100% ring), split compare, count-up with `tabular-nums`, bars from zero, price anchor flip.
- **Finishing:** Motion blur (`om render --blur`), 60 fps (`data-fps="60"`) for fast UI, seeded grain (3–6% opacity), HUD chrome / chapter counter (`01/08`), editor-on-screen keyframes. **Use particle bursts / glow sparingly** (only on 1–2 major hits or light-emitting terminals).

---

## 8. Depth & 3D (`OM.space` & `OM3`)

When a depth direction is chosen, **the whole film lives in space** (every stretch has a camera move in space; transitions fly through layers, pull back to a wall, or rack-focus; flat is only a rare 1-beat contrast or `flat: true` landing).

- **CSS 3D (`--template ui-space`):** Sharp live DOM text, pickable pieces, `OM.space('#world', { fov })`. Pitfall: a page world flattens if any ancestor between `#world` and a layer has `overflow != visible`, `filter`, `opacity < 1`, or `mix-blend-mode` — put those on the layer itself.
- **Three.js (`--template object-3d`):** Extruded real SVG logos, device screens, GLBs, lighting & DOF (`vendor/three.min.js` + `vendor/om-three.js`).
  - `OM3.stage(canvas, { background, env: 'studio'|'room'|'x.hdr', exposure, fov, dof: { aperture: 0.002, maxblur }, bloom, fog, units: 'px' })`
  - `OM3.lights(stage, { span })` · `OM3.cyc(stage, { color, y, depth, radius })` (photo-studio sweep so there's no black void)
  - `OM3.logo(svg, { size, depth, bevel, color, metalness, roughness })` (extrudes real SVG in its own colours)
  - `OM3.screen(img, { width, aspect, bezel, depth, radius, body, glass, crop: [l,t,r,b] })` (unlit screen keeps exact UI colours)
  - `OM3.gltf('x.glb')` · `OM3.texture(url)` · `OM3.read(url, type)` (XHR/blob-safe for `file://`; export `.glb`, not multi-file `.gltf`)
  - `OM3.film(stage, tl, duration, cam, update)` · `OM3.region(id, object, stage, label)` · `OM3.ready(promise)`
- **Strong camera moves:** Swing reveal (close oblique yaw 40–55° → `expo.out` 1.5–1.8 s), Orbit drift (yaw 10–25° `sine.inOut` during holds), Push to detail (`fit` 0.9–1.3 s `expo.inOut`), Crane pull-back (distance ×1.5–2, pitch +15–25°), Snap (0.3–0.5 s on a beat), Land (`flat: true`). Never spin without a target or let a dark slab back fill frame 0.

---

## 9. Specialized Workflows

### 9.1 Punch-up (Making an Existing Film Much Better)
Do not "polish" a flat film with longer eases or shadows. Copy old `index.html` and `treatment.md` to `tools/` (never overwrite old renders in `out/`), then:
1. **Diagnose with numbers:** Run `om qa <dir>` (flat = most seconds < 1 motion/sec; healthy launch = 4–15 with 1 dip), `om qa <dir> --sheet` (look for repeated slide layouts), `om sound <dir>` (fix `warning score:` and flat energy), and spectrogram. Report before-numbers to user.
2. **Keep** the spine, approved copy/claims, palette, type, material, and delivery settings. **Rebuild** layouts, eases, camera, cut points, and score.
3. **Pass the Slide Test:** Replace any slide-like stretch with one of: **Full bleed** (material fills frame) · **Macro** (cut to changed detail at ≥⅓ frame, using measured 10%-grid coordinates) · **In space** (perspective row/stack, step camera) · **All at once** (versions fly out into wall, pull one forward) · **Collision** (two elements meet on beat, one emerges). Keep caption/tag positions fixed in screen space, never over material.
4. **Frame on the change:** When UI edits/transforms, camera is already zoomed in (≥⅓ frame). Follow dynamic targets in `OM.clock` via `getBoundingClientRect() / scale`.
5. **Rewrite score on the picture's grid**, adding one instrument role per section.

### 9.2 Product Demo Continuity
For cross-device / UI workflows, follow the causal viewing arc: **Full device → Action close-up (typing/click) → Full device (reply) → Cross-device juxtaposition (primary readable, secondary anchor) → Detail extraction (remove chrome) → Result notification** (reusing opening avatar/request).
- Separate 4 layers: **content/scroll**, **device/window frame**, **framing wrapper**, **fixed captions**.
- Planar framing formula (top-left `transform-origin`, unscaled layout offset `(bx, by)`, local focus `(fx, fy)`, target screen point `(vx, vy)`, scale `s`):
  `x = vx - bx - s * fx`, `y = vy - by - s * fy`.
- Write a shot log per seam: `Event | Active reading zone | Kept identity anchor | Start/End framing | Action | Settle time | Read window | Next-shot new info`.

### 9.3 Talking-Head Packaging (`--template talking-head`)
1. **HDR check first:** If `ffprobe` shows `arib-std-b67` (HLG) or `smpte2084` (PQ), tone-map to SDR `yuv420p` before importing.
2. **Extract & align words:** `om voice talk --audio talk/assets/talk.mp4 --text script.txt` (supply spoken-form `--text`, e.g. `"twenty-something models"`, so Whisper aligns accurately; aim ≥ 90% match).
3. **Pick 3–6 moments** (~1 every 4 s): name plate, counting stat card, 4–8 character keyword overlay, chapter card at turns, corner badge. Never package what's already shown or duplicate card + keyword overlay.
4. **Anchor to words:** Use `cue` in `om set` (`OM.cue`, `lead: 0.25s`, `"nth": 2` for repeats). Verify every cue exists in `assets/voice.words.json` (generated in the project by `references/narration/scripts/tts-prosody.py`, not shipped in this repo).
5. **Keep off the speaker:** Measure `subjectX`, `subjectW`, `subjectTop`, `subjectBottom` from real frames (`om look --at`); raise `cardBottom` if speaker holds objects.
6. **9:16 & Transparent Overlay:** `om fork talk talk-9x16 --size 1080x1920`. For NLE overlay: `om render talk --transparent` (ProRes 4444 `yuva444p12le` with `#talk` removed and transparent `html/body`); verify alpha with `ffprobe` + `ffmpeg` overlay check.

### 9.4 Grammar Templates (8 JSON-Driven Explainers)
Start with `om new <dir> --template <id>` when narration fits a structured explainer:
- `math-3b1b` (formulas, curves, ML; 1 sentence = 1 transform) · `keynote-ui` (launch cards, screenshot highlights) · `finance-chart` (trends, turning points; bars from 0) · `kurzgesagt` (systems, parts, scale) · `vox-collage` (real docs/clippings) · `whiteboard` (step-by-step "why") · `storytime` (first-person stories/fails) · `kinetic-type` (lists/chapters ≤ 5 items).
- Edit `data-composition-variables` + `<script type="application/json" id="clip-spec">`, not `vendor/clip/`. Anchor cues with `"word"`, `"nth"`, `"edge": "end"`, `"offset"`. Never guess `highlightRect` by eye — measure with `om look --at`.

---

## 10. Sound & Music

### 16 Musical Worlds (Pick by Product, Never Reuse Last Film's Band)
1. **Pulse minimalism** (130–150 BPM, 3/4 or 4/4, no drums, interlocking `marimba` + `piano` + `strings` + `pizz`) — AI, dev tools, infra, data.
2. **UK garage / 2-step** (128–134 BPM, `808`+`pop` skip beat, `rhodes` m9, `sinebass`, `pluck`) — urban, social, consumer mobile apps.
3. **Minimal techno** (122–128 BPM, 4-on-floor `808`, `synbass` 16ths, `sqlead` stabs, filter builds) — speed, infra, precision.
4. **Drum and bass** (170–176 BPM, `acoustic` breakbeat, `saw` reese, `warmpad`, `bell`) — extreme speed, sport, gaming.
5. **Funk / disco** (108–120 BPM, `acoustic` kit, octave `bass`, `clav`, `brass`) — joyful creators, design tools, playful consumer.
6. **Lo-fi hip-hop** (76–90 BPM, `lofi` kit, `rhodes` 7ths, `bass`, `vibes`) — notes, reading, calm productivity.
7. **Trap half-time** (136–150 BPM, `808`+`sub808`, rolling hats, `bell`) — hype, game launches (not default tech).
8. **Synthwave** (96–112 BPM, `gated` kit, `sinebass` octaves, `saw` arp, `sqlead`) — retro, nostalgia, games.
9. **Cinematic orchestral** (80–100 BPM, `cinematic` taiko, `lowstr` ostinato, `horn`, `brass`) — big model releases, hardware, historic scale.
10. **Lyrical piano & strings** (72–96 BPM, 3/4 waltz, Lydian #4, `piano` + `strings` + `harp` + `flute`) — warm, human, family, wonder.
11. **Jazz trio** (120–180 BPM swung `A3/ B/`, `acoustic` brushes, walking `bass`, `piano`, `vibes`) — writing tools, craft, warm premium.
12. **Acoustic folk** (92–112 BPM, `folk` stomps/claps, `guitar`, `uke`, `glock`) — friendly small teams, cute/everyday consumer.
13. **Chiptune** (140–170 BPM, `chip` kit, `tri` bass, `chip` arp lead) — pixel brands, games, playful dev tools.
14. **Ambient glass** (60–80 BPM, no beat, `warmpad`, `glass`, `kalimba`, `sinebass`) — privacy, wellness, meditative loops, quiet idents.
15. **Chinese-style electronic** (88–104 BPM, tight `pop` kick + `808` hats, `guzheng`, `dizi`, `erhu`, `sub808`) — Chinese culture, tea, heritage.
16. **Amapiano** (110–116 BPM, soft 4-on-floor, shakers + rim, `sub808` log drum, jazzy `piano`) — fashion, music, social launches.

### Composer Mode (`<script type="text/vnd.abc" id="om-score">`)
- Spot 3–5 sync points (`!mark:hook!`, `!mark:turn!`, `!mark:stop!`, `!mark:drop!`, `!mark:logo!`) matching `scene:<id>` timeline labels. Build picture on `OM.music({ bpm })` + `OM.beat(n)` for 0% tempo bend (or keep tempo bend < 8% by adjusting bar counts / `3/4` bars when scoring pre-cut film).
- **ABC syntax & rules:** Standard `X:1`, `T:`, `M:4/4`, `L:1/8`, `Q:1/4=120`, `K:Em`, `V:ID inst=... gain=... role=melody`. Every bar in every voice must sum to the exact meter (`om sound` prints `warning score:` if off — fix every warning!). Inline `[K:]` affects all voices; `[M:]` must be written in every voice.
- **Instruments:** `piano`, `strings`, `violins`, `violas`, `celli`, `basses`, `violin`, `trem`, `lowstr`, `pizz`, `stacc`, `harp`, `horn`, `brass`, `flute`, `dizi`, `erhu`, `guzheng`, `guitar`, `uke`, `rhodes`, `epiano`, `vibes`, `marimba`, `kalimba`, `glock`, `bell`, `glass`, `pad`, `warmpad`, `supersaw`, `saw`, `sqlead`, `synpluck`, `pluck`, `chip`, `tri`, `clav`, `bass`, `synbass`, `sub808`, `sinebass`.
- **Drums:** `inst=drums kit=pop|acoustic|808|cinematic|lofi|gated|chip|folk`. GM map: `C,,` kick, `^C,,` rim, `D,,` snare, `^D,,` clap, `^F,,` closed hat, `^A,,` open hat, `A,,` tom, `^C,` crash, `^F,` tamb, `^A` shaker.
- **Decorations:** `!pp!..!ff!`, `!crescendo(!..!crescendo)!`, `!diminuendo(!..!diminuendo)!`, `!accent!`, `!fermata!`, `!rit(!..!rit)!`, `!ped!..!ped-up!`, `!mark:name!`, `!hit!` (impact+subdrop), `!rise(!..!rise)!`, `!filter(!..!filter)!` (build), `!stop(!..!stop)!` (tape stop), `!stutter(!..!stutter)!` (beat repeat).
- **Arrangement craft:** Write a 3–4 note **motif** stated early, developed mid-film, and resolved as the sonic logo. Separate roles by register (no two parts clashing in same octave). Leave an empty half-bar/bar before the drop. Lift up a whole step (or relative major) at the reveal.
- **Fallback:** `OM.music({ product: 'devtool'|'ai'|'hardware'|'consumer'|'cute'|'creative'|'game'|'data'|'explainer'|'calm'|'guofeng'|'hype', style, drop: 'sceneId', ending: 'ring'|'button'|'stop', floor: 0.55 })`.

### Sound Effects (`OM.sfx`) & Levels
- `OM.sfx(name, at, { gain, pan, note, pitch, dur })` returns `at`. Place `at` on the **visual landing frame** (~30–45% into an `expo.out` or `back.out` tween, not the start!). For `riser`/`reverse`, `at` is the swell end.
- Effects: `pop`, `tick`, `click`, `type`, `shutter`, `thud`, `paper`, `stamp`, `draw`, `count`, `boing`, `slide`, `whoosh`, `whip`, `impact`, `ding`, `chime`, `sparkle`, `hit`, `glitch`, `subdrop`, `reverse`, `riser`.
- Vary repeats: pan 4 cards L→R; climb `note: i + 1` on `pop`/`ding`. 8–15 hits per 30 s; max 1 `impact` and 1 `chime`.
- **Levels:** Social master at −14 LUFS (−1.5 dBFS peak, sub-30 Hz cut); music ducks −12 LU under voice.

---

## 10b. Narration with DeepSeek TTS

When the film needs a spoken voice-over and the user has a DeepSeek key, DeepSeek's own speech endpoint is the cheapest path that speaks Indonesian. Same key as the chat models, separate endpoint — the tools live under `/v1/tools/`, not on the chat API.

**Endpoint** `POST https://api.deepseek.com/v1/tools/tts` · auth `Authorization: Bearer $DEEPSEEK_API_KEY` · body `{"text", "voice_id", "format", "filter_markdown"}` · returns `audio/wav` (default) or raw 16-bit mono PCM at 24 kHz. WebSocket `wss://api.deepseek.com/v1/tools/tts` streams `pcm`/`opus` for live read-aloud; a film only needs the HTTP form.

- **Voices:** `stella` (female, default) and `tide` (male). No voice cloning, no SSML.
- **Languages:** detected from the text, never passed — Mandarin, Cantonese, English, Japanese, Korean, Malay, **Indonesian**, Arabic, Thai, Vietnamese. Indonesian copy just works; no language parameter to set.
- **Limits:** 10,000 billed characters and 64 KiB per request, at most 30 minutes of audio, 50 requests in progress per account. A Chinese character bills as 2, any other character as 1. Price US$0.45 / 10k characters (limited-time US$0.225).
- **No speed control and no resume.** A response that ends early is a failure, not a short take — every line has to fit its slot by *writing* to length, not by stretching audio.

### Wiring it into a film

`om voice <dir> --text <file>` uses the system TTS, which is not DeepSeek. To use DeepSeek:

1. Write the script as lines with the time each line must start, e.g. `lines.json` = `[{"text": "Tebak nama buah.", "start": 0.0}, {"text": "Soal pertama.", "start": 2.9}]`.
2. Synthesise, measure and lay the lines on the timeline in one step — `scripts/deepseek_voice.py` (`beats --timeline timeline.json` writes the measured timeline*; `lay` is the simple path; `gate` transcribes every phrase back to prove it was spoken). Each line is cached, so a re-run only pays for changed copy. Full API contract, limits, error table, language-detection traps and the digit-vs-word decision table: `references/narration/deepseek-tts.md`. The old `scripts/deepseek-tts.py` still works and is kept for existing builds:
   ```sh
   DEEPSEEK_API_KEY=… python scripts/deepseek_voice.py lay lines.json assets/voice.wav --voice stella
   ```
   It prints the finished length, warns when a line overruns the `end` of its slot, and writes 24 kHz mono 16-bit WAV ready for FFmpeg.
3. Import it as the recording: `om voice <dir> --audio assets/voice.wav [--fit]`, or mux it directly when the film has no word-level cues (`ffmpeg -i out/film.mp4 -i assets/voice.wav -c:v copy -c:a aac -b:a 192k -shortest out/final.mp4`).
4. Re-run `om sound` afterwards: `om sound` ducks the music under the voice and re-mixes `assets/sound.wav` with narration in place.

**Cues need real timings, so keep the line list as the source of truth.** DeepSeek ASR (`POST /v1/tools/asr`, Ogg Opus or 16-bit PCM WAV, ≤120 s, ≤8 MiB) returns only the transcript plus `duration_ms` — no word-level timings — so it cannot drive `OM.cue` by itself. If a film needs word-accurate cues on DeepSeek speech, either measure them from the line list (TTS speaks a line almost immediately after its start) or align with the CLI's own aligner.

**Failure handling:** `400` = empty text or `Content Exists Risk` (content review — rewrite the line, do not retry); `429` = >50 requests in flight (serialise, one line at a time); `503`/`504` = busy or timed out (retry with backoff, the helper does 4 tries).

---

**Mixing the voice under `om sound`'s music.** `om sound` renders the score at roughly −14 LUFS, which is *louder than a TTS voice*: measure before shipping, because a cinematic score will bury narration and an ASR check will come back empty. The recipe that works — normalise the voice, duck the score with the voice as the sidechain, then sum:

```sh
ffmpeg -y -i assets/sound.wav -i assets/voice.wav -filter_complex "\
 [1:a]aformat=sample_fmts=fltp:channel_layouts=mono,loudnorm=I=-16:TP=-1.5:LRA=11,asplit=2[voice][sc0];\
 [sc0]apad=whole_dur=<film seconds>[sc];\
 [0:a]aformat=sample_fmts=fltp:channel_layouts=mono,volume=0.30[music];\
 [music][sc]sidechaincompress=threshold=0.02:ratio=12:attack=5:release=400[duck];\
 [duck][voice]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.95,aresample=48000[out]" \
 -map "[out]" assets/mix.wav
```

**Pad the sidechain, or the picture gets cut.** `sidechaincompress` returns only as much audio as its sidechain has, so a 57 s voice under a 60 s score yields a 57 s mix — and `-shortest` on the mux then silently drops the last 3 s of picture. `apad=whole_dur=<film length>` on the sidechain copy is what keeps the mix (and the video) full length; check `ffprobe` on the muxed file against the render before reporting it.

Then mux onto the silent-ish render with `-c:v copy -c:a aac -b:a 192k -shortest`. Verify with `volumedetect` per segment: voice should sit ~5–10 dB above the score in every stretch that has speech.

**Cache keys in helper scripts must be stable.** Python's `hash()` is salted per process, so a cache named from it never hits and every run re-bills the whole script — use `hashlib.sha1` over the text and voice.

**Verify narration by transcription, not by hope.** DeepSeek ASR (`POST /v1/tools/asr`) on 10 s slices of the final mix proves the words actually made it into the file; a whole 60 s file sometimes returns an empty transcript even when the slices transcribe perfectly. Send slices.

**DeepSeek TTS language quirks in Indonesian copy:** a line that starts with a bare name ("Dia Mansa Musa…") gets blended into one word — write "Dia, Mansa Musa, …" and the comma fixes it. Loan words read with English phonetics ("Juli" comes out as *July*) — prefer "bulan ketujuh". Isolated Latin text (a two-word line) can be detected as Mandarin, so always give the voice a full sentence.

---

## 11. Project Contract, Determinism & Comment Loop

```text
my-film/
  index.html      # Single root composition per project (drafts go in tools/)
  vendor/         # gsap.min.js, om.js (+ three.min.js, om-three.js for 3D, clip/ for grammars)
  assets/         # fonts, images, audio (sound.wav generated by om sound)
  out/            # Renders from om render
  .om/            # history, inbox.jsonl, render log
```

- **Root & Variables:** `<html data-composition-variables='[{"id":"title","type":"string","default":"…","group":"Copy"}]'>` (types: `string`, `number`, `color`, `boolean`, `enum`). Root element needs `data-composition-id`, `data-width`, `data-height` (optional `data-fps="60"`, `data-duration`, `data-om-signature="off"|"top-left"`). Omit `data-duration` so hold variables control length via `tl.to({}, { duration: V.endHold })`. Bind with `data-var-text="id"`, `var(--id)`, `data-om-var="id"` (for JS-split text), and `OM.vars()`.
- **Pickable Targets & Scenes:** `data-om-id="name"` on every interactive/visible element (or `OM.region(id, t => [x,y,w,h] | null, label)` for canvas). Scenes: `tl.addLabel('scene:intro', 0)`.
- **Signature:** Films ≥ 4 s automatically show a subtle "Made with pulupulu-motion" for the last 1.2 s in a free corner. Leave one corner clear (`om check` warns `signature-covers`), or set `data-om-signature="off"` only when requested or for paid client deliverables.
- **Seek Determinism (Renderers jump to `t`, never play sequentially):**
  - Always use `tl.fromTo(..., { ... }, { ..., immediateRender: false })` so start states don't leak to frame 0.
  - **Never** use `overwrite: true` on a timeline.
  - Keep every timeline position `>= 0`.
  - Hide groups with `opacity`/`autoAlpha`, not `visibility`.
  - Quantise hard cuts half a frame in (`(Math.floor(t * fps) + 0.5) / fps`) and counters to whole frames when using `--blur`.
  - Put decorative overlays (vignette, grain) **before** content in DOM, or mark intentional overlaps with `data-layout-allow-occlusion` / `-overflow` / `-overlap`.
  - No `Date.now()`, no `Math.random()` (`OM.random(seed)`), no external network URLs at render time.
  - Canvas/WebGL loops use `OM.clock(tl, t => draw(t), duration)` (runs *after* GSAP tweens on every seek).
- **Comment Loop:** `om inbox <dir> --wait` → `om look <id> <dir>` → minimal edit (`om set` or targeted `index.html` edit without renaming `data-om-id`s) → `om done <id> <dir> --note "<1-line summary>"`. Every version is saved in `.om/history` (`om undo` always works).

---

## 12. Verification & Independent Review

- **Machine checks (`om check` + `om qa --sheet`):** Verify 0 errors, no single-frame pops, no dead stretches (> 2 bars), no blank frame 0, clean loop seam (`--loop`), readable contrast, and valid audio spectrogram.
- **Cold Review Protocol:** Never grade your own film "done" from `om check` alone. Have an independent reviewer (or fresh context) watch the **final MP4** with only the original brief, confirmed direction, `treatment.md`, and a source table for on-screen text/numbers. Mandatory review question: *"At which timestamp does attention drop or feel flat?"*
- **Second opinion from another model, when the gates are green and it still reads cheap.** Six to eight stills pulled from the *delivered* MP4 plus the generator script in one folder, a brief that demands ranked fixes with px/colour/easing numbers, and a read-only instruction: `agy --print "<brief>" --model <id> --add-dir <folder>`, ids from `agy models` (they encode effort — never combine `--model` with `--effort`). Put `qa.txt` and `timeline.json` in that folder as well, and run a frontier model as a background job writing to a file — ten images plus the generator outlive a foreground call, and a call killed at the timeout saves nothing. **One round, then converge — this user pays for both sides.** A critique exchange is expensive and its
marginal value collapses after the first answer: send the stills, the generator and one brief that states what you assembled and what you believe is wrong, demand numbers back (px, seconds, easing, colour), apply everything you accept in a single pass, re-render once, and report what you took and what you rejected. Agree the convergence point with the user before starting rather than announcing rounds. Run that call as a background job writing to a file — ten images plus the generator outlive a foreground call, and a call killed at the timeout saves nothing. Two frontier models in parallel on the same brief is the exception worth paying for, because their disagreements mark where the craft decision actually is: a craft-focused model will rebuild your shading and miss that your material is fake, an editorial-focused one will hand you licensed sources and corrected facts and leave the frames plain. **Attach the frames with `-i` on `codex exec` and feed the brief on stdin** (`codex exec -m <model> -c model_reasoning_effort="medium" -i f1.png -i f2.png < prompt.txt > review.md`) — `-i` is variadic, so a prompt passed as an argument after the images is swallowed as another filename and the run exits with `No prompt provided via stdin`. Codex also runs long enough to need a background job with `notify`, like the `agy` calls. This finds what no checker sees: a blanket `scale()` cropping artwork, a caption scrim ending in a razor cut, labels off centre from a `translateX` fighting a GSAP `y`, `back.out` bouncing through floors, an SVG `pop` painting from `(0,0)`, and — on one film — twelve *tetrominoes* drawn on the beat that says *pentominoes*. Recipe and the full list: `references/visual-craft.md` §11.
- **Fix defects by layer:** Looks cheap → fix craft/type/lighting/materials (not camera). Looks boring → fix pacing/shot-scale/contrast/score (not decorative particles). Unclear → fix focal hierarchy/identity anchors/read time (not extra voice-over). When the complaint is "the visuals look weird and bad" and every machine gate passed, the defect is craft — re-derive the rules from `references/visual-craft.md` (its §10 lists the sources) and rebuild the shading, depth and composition of each scene; do not patch the eases, and do not defend the frame with the fact that `om check` is clean.

---

## Field notes (learned on a real 30 s quiz film)

- **Looping ambient motion stretches the timeline.** A `repeat: 8` coin/particle tween is the film's last child, so GSAP reports the timeline as long as that tween ends — a 54 s film rendered as 91 s with a dead tail. Bound every repeat to the film: `const loops = Math.max(1, Math.floor((END - start) / d))` then `repeat: loops - 1`, and check `duration` with ffprobe after each render. The same arithmetic bites per-limb oscillation in a rig: `duration × (repeat + 1)` must equal the scene length, or a `len/5` step with `repeat: 6` runs 1.4× the scene and quietly pushes a 60 s film's soundtrack to 62.8 s. `om sound`'s printed length is the cheapest check that the timeline is still the length you asked for.
- **Anything with a `fromTo` must start hidden in CSS.** An element whose entrance tween begins at 36 s is otherwise visible from the moment its scene appears — `opacity: 0` in the stylesheet, tween it in. Same for source lines, counters and captions.
- **Captions that also carry narration want one chunk per spoken sentence.** Split the script into the sentences the voice will actually say, synthesise each chunk separately, and give every chunk a known start: the caption and the audio then cannot drift. Keep a `fromTo` hand-over between chunks (next fades in at its start, previous fades out 0.02 s before) so the text never blinks out between lines.
- **Hand a beat over to the next one; never let the frame blink black between them.** Hiding beat *i* at `end - 0.01` while beat *i+1* turns on at `start - 0.30` leaves pure `#000` frames for the whole narration gap — at 0.5–0.6 s gaps that is a 0.2–0.3 s black strobe before every single shot, the single biggest reason a beat-driven film feels broken while `om check` stays clean and `om qa` only reports holds. Keep the outgoing beat visible until the *next* beat's `start` (`tl.set(node, {display:'none'}, next ? next.start - .02 : END + .2)`) and bring the incoming plate in 0.15–0.2 s early on top of it. **The last beat is the one everyone forgets:** hiding it at its own `end` while the render continues to the padded audio length ends the delivered film on a black frame — `om check` reports `blank-frame` at the tail, and a Shorts loop replays that black. Bind the final hide to the film length, not to the beat.
- **Keep a caption band free of art.** Falling coins and camel friezes read fine above `~1030px`; below that put a soft scrim (`linear-gradient(#0b102000, #0b1020e6)`) and keep the captions and progress bar on top of it (`z-index`), or particles cross the words.

---

## Field notes (the CLI and the render path)

- **Page boilerplate the CLI demands.** A hand-written `index.html` must load `vendor/gsap.min.js` *and* `vendor/om.js` before the inline script, create the timeline with `{ paused: true }`, and register it: `window.__timelines = window.__timelines || {}; window.__timelines['film'] = tl;`. Missing any of the three fails `om check` with "the composition did not start" or "OM.sfx is not a function". **The registration key must equal the root's `data-composition-id`** — a timeline registered as `film` under a root named anything else raises `timeline-id` and the studio seeks the wrong object, so name both the same string in the generator.
- **Every generated scene needs its own SVG `id` namespace.** A backdrop helper that emits `<defs>` (a ground gradient, a sky gradient, a grain `feTurbulence` filter) reuses one id per scene, and eighteen scenes then ship eighteen copies of `skyGrad`: `om check` fails `duplicate-id` and every `url(#…)` reference resolves to whichever came first, so all eighteen floors render with one scene's colours. Suffix every generated id with the beat id (`skyGrad{beat}`, `floorGrad{beat}`, `grain{beat}`) and pass the beat id down into each scene helper.
- **`om render` dies with `Page.captureScreenshot timed out after 15000 ms` when the page is expensive to paint.** Large multi-stop `radial-gradient` overlays and wide `box-shadow` blurs on many elements are enough to stall the compositor on every frame. Replace the vignette with a single `linear-gradient`, cut shadows to ~`0 6px 14px`, then re-render — the same page then renders 900 frames without a miss. Stills may pass while rendering still stalls, so test with `om render`, not only `om still`. **A repeating background pattern is a third trap:** a CSS "graph paper" grid (a `background-image` gradient pair plus a `background-size` tile) repaints the whole surface every frame and stalls exactly the same way — replace it with one static `linear-gradient` or a handful of SVG lines. **An SVG filter inside a `background-image` is the worst variant of it:** a `feTurbulence` grain shipped as a data-URI tile re-runs the filter over the full surface on every repaint and stalls a page whose stills look perfect — bake the noise to a PNG tile once (`PIL`, 220 px, `optimize=True`) and reference the file instead. If that tile is blended with `background-blend-mode: multiply` it must be near-white (mean ≈ 247, sd ≈ 7); a mid-grey noise tile multiplies a cream ground down to grey, which is a silent art bug no checker reports. A render that ends in a Node stack (`at listOnTimeout (node:internal/timers…`) and leaves nothing in `out/` is this timeout, not a JavaScript bug: check paint cost before reading the tween code.
- **A full-frame transform is only a trap when it SCALES.** Verified on a 1080×1920 inline `<svg>`: a `fromTo` on `scale` stalls the renderer (`Page.captureScreenshot timed out after 15000 ms`, twice in a row, on a page whose stills were fine), while the *same* element tweened on `y` renders in five minutes — Chrome re-rasterises a vector layer on scale, and merely composites it on translate. So the camera move on the plate is a **translate**: `tl.fromTo(art, {y:0}, {y:-150, duration: beat, ease:'none'}, beat.start)`, with `.art { will-change: transform }` and `gsap.config({force3D:true})`. Keep any *scale* on the plate static in CSS (`transform: scale(1.5)`) and scale only small inner groups. **A bitmap layer is exempt from the whole trap:** an `<img>` panel scaled 1.00 → 1.09 across a shot, or displaced in `y`, composites without re-rasterising its pixels — so an image-based film (generated prints, photographs, captured UI) gets a real camera move back, and that is the reason to bake art to PNG instead of inlining it as SVG. Test the difference in one still before building a film on it. **Do not blame the grain filter:** removing every per-beat `feTurbulence` did not stop the stall; consolidating the eighteen per-beat grain filters into one film-wide noise tile is still worth doing for paint cost, but it is not the fix. Use `ease:'none'` for camera moves inside a shot — an eased push leaves a still tail the QA reads as dead time. Also: a `repeat: -1` tween makes the timeline length infinite; compute a finite repeat (`Math.floor(END/dur) - 1`) or the render silently grows past the audio (a 87 s film became 117 s).
- **The QA motion and still metrics compare frames downscaled to roughly 96×54 greyscale, so only large-area, high-contrast movement registers.** A 46 px plate translate over five seconds, drifted background blobs at 1.1:1 contrast, grain jitter and small inner-group bobs all score as nothing however alive they feel at 1× — that is why `still for ≥1 s` and `flat opening` survive a film that visibly moves. Move area, not detail: a full-plate translate of 150 px per shot plus one wide high-contrast event at the open (a 1200 px line-clear flash bar) took one film from 28 held stretches and a failing opening to 10 stretches with `flat opening` cleared. Score the fix with `pulupulu qa` on the delivered file, not by eye.
- **Webfont text inside inline SVG is a fourth trap, and the worst one.** `<text font-family="Inter">` inside an `<svg>` forces Chrome to re-raster that layer every frame while the font resolves; a 21-scene film with one `39 ft` chip per scene rendered zero frames in 8 minutes and timed out, then rendered in 4 minutes once every SVG `<text>` was replaced by an HTML `<div>` overlay positioned at the same coordinates. Rule: **cheap to keep — SVG for shapes, HTML for words.** Strip SVG text mechanically (`re.sub(r"<text[^>]*>.*?</text>", "", svg, flags=re.S)`) and emit a `.lab { position:absolute; transform:translateX(-50%) }` div per label; CSS `font-weight:900` gives the same look with none of the cost.
- **HTML labels do not inherit an SVG element's rotation.** Moving words out of `<text>` into absolutely positioned `<div>`s gives up the transform stack: a card tilted `rotate(-3)` leaves its headline level and off-register. Either keep the label's container unrotated (correctness beats a 3° tilt) or apply the same `rotate()` to the label about the same origin — and re-open the frame after any resize, because label coordinates are absolute while the card scales from its own box.
- **`om still --out <path>` writes a single PNG at that exact path when `--at` holds one time, and a directory of `index-<t>s.png` when it holds a list.** A later `ls .om/frames/` then fails with "Not a directory" and the still looks missing. Name the out path explicitly when sampling one time; use the directory form when sampling several.
- **One still per scene is not enough when scenes share a backdrop helper.** A `railbed()`/`canyon()` helper added to fix “too sparse” scenes left `closed` drawing its rail at y = 1500 with an empty middle — visible only after sampling **every** beat's midpoint, not the four treatment frames. Build a contact sheet of all beats (`om still --at <midpoint of each beat>`, then tile them) and read it before the render pass.
- **An HTML element inside an `<svg>` renders nothing, and nothing warns you.** Raw `<g>`/`<rect>`/`<path>` children dropped straight into a `<div>` (a cloud layer, then a whole scene) produce a black frame, a clean console and a passing `om check`. Any scene fragment must be wrapped in `<svg viewBox="…">…</svg>` at the point it enters the DOM; grep the generated page for `<svg class=` per scene to prove it. **Two more traps, both found on a scrolling-world film:** a **webfont inside SVG `<text>`** (`<text font-family="Anton">`) forces that layer to re-raster every frame, so draw the glyph as shapes or put the text in HTML; and **`will-change: transform` on every prop** costs as much as one giant layer, because thirty promoted layers have to be composited separately. One huge scrolling strip (4400×1400) stalls no matter how you scale or promote it — the shape that renders is many small elements placed by transform (recipe: `references/2d-vector-motion.md`, *Side-scrolling world*). **Retry the render once or twice after a stall before redesigning** — the same page often renders on a second pass — but kill the **headless** Chrome instances a failed run left behind first, and only those — never `taskkill //IM chrome.exe`, which closes the user's own browser: on Windows run `powershell -NoProfile -Command "Get-CimInstance Win32_Process -Filter \"Name='chrome.exe'\" | Where-Object { $_.CommandLine -match '--headless' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }"` then a short sleep: a dozen orphans from earlier stalls compete for the same CPU and reproduce the identical timeout on a page that otherwise renders. If two attempts still fail after that, cut paint cost; do not spend a third attempt.
- **Render one still per scene, not only the four treatment frames.** Absolutely positioned blocks (`top: 520px` and friends) drift into each other as copy changes — a progress bar ended up lying across the card above it, invisible to `om check` and to the console, obvious in one screenshot. Pull a mid-animation frame from every scene and look at all of them before spending the render pass.
- **Audio goes stale silently.** After any edit to `index.html`, re-run `om sound` before `om render`; otherwise the render logs `no soundtrack` and writes a silent MP4. If a render still lands without audio, mux it: `ffmpeg -i out/film.mp4 -i assets/sound.wav -c:v copy -c:a aac -b:a 192k -shortest out/final.mp4`.
- **Build the composition from a generator script** (`build_film.py` writing `index.html`) when the film repeats a layout N times: rounds stay identical in structure, copy lives in one table, and a failed experiment is a one-line revert instead of hand-edited HTML. Write the CSS/JS in the generator as plain strings and substitute only small data tables (`json.dumps`), never as f-string bodies — a stray `{{ }}` left over from f-string style is a `SyntaxError: Unexpected token '{'` that costs a whole render pass. **Re-run `om fonts add <family> <dir>` after every regeneration:** the generator rewrites `<head>`, so the `@font-face` block the CLI injected is gone, `om check` returns `font-not-shipped` again, and the render falls back to a system face — read the check after the last build, not after the first.
- **Render filenames increment** (`film-v1`, `-v2`, `-v3`…), they are not overwritten: mux `$(ls -t out/*.mp4 | head -1)` rather than naming the expected file, or the mux dies on a path the renderer never wrote.
- **`OM.music` takes a product *or* a style, and the vocabularies differ.** `product` accepts only `devtool, ai, hardware, consumer, cute, creative, game, data, explainer, calm, guofeng, hype`; a sound name such as `cinematic`, `synthwave` or `piano` belongs in `style:`. `om sound --list` prints both lists. Passing a style as the product fails with `unknown product "cinematic"` and writes no soundtrack — check the `om sound` header line, not just that it exited 0.
- **Never name the film file from an id already used in another scene** — duplicated SVG art duplicates its `id`s; see `references/2d-vector-motion.md` for characters, aerial tracks and the declutter rules, and `references/topic-fit.md` for which subjects this pipeline can carry at all.
- **Silence the layout linter where the design is intentional:** `data-layout-allow-overflow` on mask-reveal containers (`overflow:hidden` is the reveal) and `data-layout-allow-occlusion` on full-frame transition veils.
- **`om qa` calls every thinking hold dead time.** On a quiz/trivia format the hold while the viewer reads the options *is* the format; answer it with a countdown pop per second plus a soft light sweep, and accept the remaining `still for ≥1 s` note instead of adding motion that fights the idea.
- **`om qa` and `om sound` are advisory, not gates.** They flag flat energy and missing contour; a drop on the final scene (`OM.music({ drop: 'scene:round5' })`) lifts the peak ~2.5 dB and is usually the cheapest fix.

---

## Field notes (narration, captions and the clock)

- **Mux with an explicit map, or the narrator disappears.** `pulupulu render` already embeds the score, so `ffmpeg -i render.mp4 -i mix.wav -c:v copy -c:a aac …` picks the render's own music-only audio stream and silently drops the mix — the delivered film plays music and no voice, while `om qa`, `ffprobe` and every level check still look healthy (one AAC stream, −16 LUFS). Always `-map 0:v:0 -map 1:a:0`, then confirm the voice is really in the file by transcribing a slice of the **final MP4**, not of `voice.wav`.
- **The per-phrase ASR gate is not optional.** Slice `assets/voice.wav` at each beat's measured window, transcribe each slice, and compare with the script before building the picture. On one 60 s explainer it caught two phrases the ear would only notice at 1× playback: a three-word fragment that the engine transcribed as a nonsense phrase in another language, and a loanword-heavy line that came back as gibberish English. Both were fixed by rewriting the words, not the audio — fragments get a full sentence, loanwords get outnumbered or moved on screen.
- **Caption drift is a build-order bug, not a proofreading bug.** When the copy table, the caption table and the scene timings are authored separately they disagree within three beats. Generate all three from one `beats.json` plus the measured `timeline.json`, one beat per spoken phrase, and the mismatch cannot exist.
- **A calm opening still needs motion.** A hook beat whose only movement is a caption fade scores `flat opening` (0.5–1.2 motion/sec) and loses the scroll. Push the hero element (scale 1.0 → 1.06 over the beat) and pulse one peripheral element; that alone lifts the first five seconds above 2 without turning the film loud.

## 13. Art, style & cinematic extension (merged library)

Everything artistic lives in `references/art-motion/` — a curated library of style recipes, grammar cards and craft documents — with executable gates in `scripts/art-motion/`. Read `references/art-motion/INDEX.md` first — it routes every need to one file. The four entry points you will actually use:

| Need | Go to |
|---|---|
| Shot list before code, with the linter that enforces it | `references/art-motion/storyboard-template.md` → `scripts/art-motion/storyboard_lint.py` |
| Camera behaviour (push / pull / whip / slam / cut as punctuation) | `references/art-motion/camera-language.md` |
| A named visual style (57 recipes: cave → bauhaus → Ghibli → pixel → ukiyo-e) | `references/art-motion/style-recipes/INDEX.md` |
| An explainer grammar beyond GSAP cards (3b1b, keynote, finance chart, kurzgesagt, Vox, whiteboard, storytime, kinetic type, presenter) | `references/art-motion/09-animation-grammar.md` §selection → `animation-grammar/<card>.md` |

**When to reach for it:** the brief asks for an art style, an illustrative look, characters, a painted/scene-based film, a long-scroll traversal, or cinematic camera moves. **When not to:** a UI/demo/data explainer stays on the GSAP path in §3–§7 — the recipes cost far more and add nothing there.

Three guardrails, learned the hard way:

1. **The linter matches English and Chinese — write the shot list in either.** Required columns `Time | Subject | Action | Camera | Tags | On-screen text | Method`; camera cell one of `Stop ／ Slow push-in ／ Pull back ／ Lateral truck ／ Fast push-in ／ Slam in ／ Whip ／ Cut`; the three lines above the table are `Style ／ Palette ／ Character`, plus `Allow blue-purple` when you need it. English shot lists are fully validated — every rule bites on English subject and action cells, not just the camera column — so keep them in English unless you are updating a legacy list, where the Chinese camera tokens used by earlier versions still parse. Verdict legend for every code: `references/art-motion/INDEX.md` §8.
2. **Two render paths, never in one film.** `pulupulu render` (this skill's CLI) is for GSAP/CSS compositions. `scripts/art-motion/engine/render.py` (`uv run --with playwright`) renders style-recipe `scenes` and parameterised clip specs. Pick one per project; `film_gate.py`/`subzone_gate.py` only understand the shot-based project layout, while a `pulupulu` project is gated by `pulupulu check` + `pulupulu qa`.
3. **A style card is a starting point, not a registered scene.** Anything not yet implemented must be authored and verified against the reference (`15-style-transfer.md`, `16-style-demo-95.md`); never ship a card name as if it were a working scene.

**The library is English throughout.** Every document was translated and the Chinese filenames were renamed, so there is no `en/` subdirectory any more — `INDEX.md` is the one router, and every path inside the library resolves to a file in this repo. Chinese now survives only where it is *matched data* rather than prose: the shot-list linter's legacy control tokens, the CJK line-break classes and two sample glyphs. Translating those would blind the tools, which is why they stay. Upstream `assets/` (49 MB of showcase stills) was deliberately not copied — the recipes are code — and the clip spec JSON ships in `scripts/art-motion/engine/clips/` while the clip scripts sit in `.../engine/clips/`; the two directories are one letter apart and the wrong one to rewrite from memory. **After any merge or rename in this tree, re-prove the paths** with `path_audit.py . --fallback scripts/art-motion` from the **`agent-skill-sourcing`** skill (that skill's `scripts/`, not this one) — a namespaced merge silently kills references that the source project resolved from its own layout, and nothing in the render path tells you a doc now points at nothing.

### 13b. Timing, easing and feel at the sub-second level — `references/ui-motion/`

A library of timing-and-feel documents (English, kept verbatim). It answers the questions the film rules do **not**: how long a single move takes, which curve carries which emotion, how elements enter together, and how to scale motion per device. Read `references/ui-motion/INDEX.md` for the full routing; the four files that pay for themselves immediately:

| Question | File |
|---|---|
| How long, and with which easing, for a given feeling | `reference/timing-easing-tables.md`, `director/emotion-mapping.md` |
| Several elements entering or leaving together | `director/choreography.md`, `patterns/multi-element.md` |
| One house style for this brand (Playful / Premium / Corporate / Editorial) | `director/motion-personality.md` |
| Pre-delivery sign-off beyond machine checks | `reference/quality-checklist.md` |

Numbers to keep in mind: delight 200–400 ms `ease-out-back` · calm 500–1000 ms sine in-out · urgency 100–200 ms `ease-out` · trust 300–400 ms gentle curves · mobile runs at 0.8× desktop with fewer properties · staggers 60 ms (playful) / 80 ms (premium).

Three rules for using it here: **milliseconds are not beats** (anything that must land on a spoken word takes its timing from the measured audio timeline, not from a 240 ms table); **one archetype per film**, with every duration and overshoot taken from that column; and **the third-party Creator MCP handoff is not part of this skill** — export is `pulupulu render` plus `ffmpeg`, never a vendor MCP.

## 14. Verification gate order (what has to pass, in order)

1. `scripts/lang-audit.py film/index.html --lang <en|id>` — no leftovers from another language (§3c).
2. Shot list linted (`scripts/art-motion/storyboard_lint.py`) when the film uses the art path.
3. `pulupulu check .` — 0 errors.
4. Per-phrase ASR gate on the narration (`tts-intonation` §6), then the same check on a slice of the **final MP4**. Use the shipped command, not hand-rolled curl: `python scripts/deepseek_voice.py gate beats.json --voice <stella|tide>` synthesises, transcribes each phrase back and compares — **exit 1 means do not render**, and the fix is always the copy (a fragment becomes a full sentence, a loanword gets outnumbered), never the audio. Then `asr` on three or four 4 s slices of the delivered file proves the mix did not bury the voice.
5. `pulupulu qa <file>` — **Check digits and proper nouns as tokens, not as similarity**: a 0.6 transcript match passes a line that says the wrong year or the wrong surname. `no single-frame pops` is a gate; `still for ≥1 s` and `flat opening` are reading notes, answered with argument not with random motion.
6. One frame per scene opened and looked at, plus 1× playback with sound.
7. `references/ui-motion/reference/quality-checklist.md` — the five axes (visual, technical, emotional, performance, accessibility) walked once, out loud, on the finished film.

## Local install (this machine)

The CLI is **self-hosted and rebranded — never call `npx` in this workflow.** An npm fetch per command costs seconds and re-hits the network on every `check`, `still`, `sound` and `render`; a 60 s film makes dozens of those calls.

- **Command:** `om <cmd>` (or the rebranded `pulupulu <cmd>`), e.g. `om check .`, `om render . --fps 30`.
- **If a shell has not picked the binary up:** `npm prefix -g` locates it; `node <prefix>/cli/om.js <cmd>` runs it directly.
- **Rebranding scope (deliberately minimal):** package name, help header text, the docs path in help, the default demo folder name, plus a second bin alias `pulupulu`. No behaviour, template or render-path change — so every flag and every existing project keeps working.
- **State:** the CLI writes per-user state under `~/.<cli-name>/` (for example `soundtracks.jsonl`). Stills and renders use the Chrome already installed on the machine.

## 15. Publishing this skill

This directory is also the public repo. Repo shape, the `.gitignore` that keeps heavy sample media out, the publish/tag/release commands, the footprint-scrub procedure (including the orphan-branch history rewrite) and the one licence line that must stay: `references/publishing.md`.

**Only when the user asks to publish.** History is always ONE commit, rewritten on every update (`references/publishing.md` §2b) — the version stays `1.0` and the tag stays `v1.0`, then `scripts/publish-squash.sh <skill dir> <message file>`, then prove it: remote SHA equals local HEAD and `gh api repos/<owner>/<repo>/commits --jq 'length'` prints 1.

**The message argument is a FILE, and passing it inline strands the repo.** The script checks out a commitless orphan branch (`__single`) first, so when the second argument is a string instead of a path, `git commit -F "<that string>"` fails on a too-long filename and leaves the working tree on `__single` with **zero commits** — `git checkout main` then aborts on the dirty tree and nothing is pushed. The script now validates the file before it touches the branch; if you inherit the broken state, recover with `git add -A && git commit -F <msgfile> && git branch -M main && git push -f origin main`, then re-tag: `git tag -fa v1.0 -m "…" && git push -f origin v1.0`. Do the work in the same turn as the edit once publishing is wanted; say that the force push invalidates existing clones, and that old commits stay reachable by SHA until GitHub's GC runs.

**Every file carries the credit mark, and the repo prose is English-only** (`references/publishing.md` §1b) — `scripts/stamp_credit.py <root> --owner <name>` stamps all 364-odd files idempotently, after frontmatter, after shebang, after doctype, never into JSON; re-run `compileall` / `node --check` / `json.load` afterwards. Foreign-language words survive only as a tool's own data (a detector's stopword list, an expander's spoken-digit table), and every such block needs a comment saying so. When the user says the repo must contain no foreign language, they mean the prose — rewrite quoted examples in English and describe the incident instead of repeating the quote.

**Merging another library in, or translating this one, is a procedure — follow it from the sourcing skill.** `agent-skill-sourcing` §6 plus its `agent-skill-sourcing:references/rebrand-and-translate.md` — in that skill's tree, not this repo — carry the order (namespace each source, write the routing index yourself, neutralise vendor upsells, rebrand minimally, scrub prose but keep the copyright notice, rewrite history, verify from a fresh clone) and the bulk-translation wave recipe (measure the volume, ~10 subagents one directory each with a numeric-token diff, then one parent-owned rename-and-relink pass, then `node --check` / `ast.parse` / `json.load` over the whole tree). Two failures from doing it casually: a blind token replacement turned an identifier into a syntax error, and a renamed asset left a dangling `src`.
