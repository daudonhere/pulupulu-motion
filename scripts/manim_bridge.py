#!/usr/bin/env python3
"""Turn a measured beat list into a t1_3b1b clip spec skeleton.

Usage:
    python scripts/manim_bridge.py beats.json --out spec.json
    python scripts/manim_bridge.py beats.json --timeline timeline.json --out spec.json

Beats carry `text` or `caption`, plus either a measured `start`/`seconds` pair or a
`gap` from the previous beat. A `timeline.json` written by deepseek_voice.py wins:
its starts and ends were measured from the voice, so the cue timings follow speech.

The output is a skeleton, not a finished film. Captions decide the cue kind, but
token colours, shared symbols and the object each colour names still need a person
to assign them. Review every `equation` cue before rendering, then run
scripts/math_gate.py and scripts/art-motion/clip_lint.py on the spec.
"""

import argparse
import json
import re
import sys
from pathlib import Path

HOLD = 0.6
DEFAULT_GAP = 0.6
MATH = re.compile(r"[=→←∇∑∫≤≥×÷±θλμσπ√]")
SHORT_TITLE = 42


def load_beats(source, timeline):
    """Return (captions with timings, duration hint)."""
    if timeline:
        payload = json.loads(Path(timeline).read_text(encoding="utf-8"))
        rows = payload.get("beats") or []
        items = [
            {
                "caption": r.get("caption") or r.get("text") or r.get("spoken") or "",
                "start": float(r.get("start", 0)),
                "seconds": float(r.get("seconds") or max(0, r["end"] - r["start"]))
                if "end" in r
                else 1.0,
            }
            for r in rows
            if isinstance(r, dict)
        ]
        return items, payload.get("duration")

    payload = json.loads(Path(source).read_text(encoding="utf-8"))
    if isinstance(payload, list):
        rows = payload
    elif isinstance(payload, dict):
        rows = payload.get("beats") or payload.get("lines") or []
    else:
        rows = []
    items, cursor = [], 0.0
    for r in rows:
        if not isinstance(r, dict):
            continue
        caption = (r.get("caption") or r.get("text") or "").strip()
        if not caption:
            continue
        if "start" in r:
            cursor = float(r["start"])
        items.append(
            {
                "caption": caption,
                "start": round(cursor, 3),
                "seconds": float(r.get("seconds") or r.get("dur") or 1.0),
            }
        )
        cursor += items[-1]["seconds"] + float(r.get("gap", DEFAULT_GAP))
    return items, None


def cue_kind(caption, index):
    if MATH.search(caption):
        return "equation"
    return "title" if index == 0 and len(caption) <= SHORT_TITLE else "point"


def build(rows, duration_hint, width, height):
    cues = []
    for i, row in enumerate(rows):
        caption = row["caption"].strip()
        if not caption:
            continue
        kind = cue_kind(caption, i)
        dur = round(min(2.0, max(0.4, row["seconds"])), 2)
        cue = {"at": round(row["start"], 3), "kind": kind, "dur": dur}
        if kind == "equation":
            cue["text"] = caption
        else:
            cue["text"] = caption
        cues.append(cue)
    if not cues:
        raise SystemExit("no captions found; every beat needs a text or caption field")
    last_end = max(q["at"] + q["dur"] for q in cues)
    duration = round(max(duration_hint or 0, last_end + HOLD), 3)
    return {
        "grammar": "t1_3b1b",
        "duration": duration,
        "fps": 30,
        "width": width,
        "height": height,
        "theme": "ink",
        "_note": "Generated skeleton from a beat list. Equation tokens and their colours are not "
        "assigned: set data.tokens so each symbol matches the object of the same colour "
        "on screen. Review by hand, then run math_gate.py and clip_lint.py.",
        "cues": cues,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source", type=Path, help="beats.json (list, or {beats:[...]})")
    ap.add_argument(
        "--timeline", type=Path, help="measured timeline.json from deepseek_voice.py"
    )
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--height", type=int, default=1080)
    a = ap.parse_args()
    try:
        rows, duration_hint = load_beats(a.source, a.timeline)
        spec = build(rows, duration_hint, a.width, a.height)
    except (OSError, ValueError, json.JSONDecodeError) as e:
        sys.exit(f"cannot build spec: {e}")
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(
        json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    pending = [q["at"] for q in spec["cues"] if q["kind"] == "equation"]
    print(f"{a.out}: {len(spec['cues'])} cues, {spec['duration']}s")
    if pending:
        print(
            f"equation cues need token colours before rendering: {', '.join(str(t) for t in pending)}s"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
