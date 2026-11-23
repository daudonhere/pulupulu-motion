# Specialized workflows

Owner: punch-up, product demo and talking-head grammars


Punch-up of an existing film, product-demo continuity, talking-head packaging, and the eight JSON-driven grammar templates.

Part of the `pulupulu-motion` skill. The entry point and the gate table live in `SKILL.md`.

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
