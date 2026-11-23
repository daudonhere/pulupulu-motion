#!/usr/bin/env python3
"""Read-only maths check for a t1_3b1b clip spec.

Usage:
    python scripts/math_gate.py spec.json [--strict]

It answers the questions a render gate cannot: does a symbol keep its colour across
equations, does the film stay inside its semantic palette, is the conclusion given
time to land, and did on-screen text slip back into spelled-out numbers.

Advisory by default: warnings print and the command exits 0. With --strict they fail.
Keep it advisory until it has been run against finished films; a deliberate fifth
colour or a short last shot is a reason to answer the warning, not proof of a bug.
The hold value lives in references/verification.md, which owns gate numbers.
"""

import argparse
import json
import re
import sys
from pathlib import Path

HOLD = 0.6
SEMANTIC_LIMIT = 4
NEUTRAL = {"white", "black", "grey", "gray", "ink", "sub", "bg", "surface"}
COLUMN = {"line", "vector", "matrix", "brace", "grid", "axes", "title"}
MONTHS = re.compile(
    r"\b(january|february|march|april|may|june|july|august|september|october|november|december)\b",
    re.I,
)
SPELLED = re.compile(
    r"\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|hundred|thousand)\b",
    re.I,
)


def colour_key(value):
    """Fold a manim name to its concept, keep a hex as written, drop palette neutrals."""
    if not isinstance(value, str):
        return None
    v = value.strip().lower()
    if v.startswith("#"):
        return v
    v = re.sub(r"_[a-z]$", "", v)
    return None if v in NEUTRAL else v


def tokens_of(cue):
    data = cue.get("data") or {}
    return [t for t in (data.get("tokens") or []) if isinstance(t, dict)]


def text_of(cue):
    return " ".join(
        str(x)
        for x in (cue.get("text"), cue.get("sub"), (cue.get("data") or {}).get("label"))
        if x
    )


def check(spec):
    warnings = []
    cues = [q for q in (spec.get("cues") or []) if isinstance(q, dict)]
    duration = spec.get("duration")
    if not isinstance(duration, (int, float)) or duration <= 0:
        return ["duration must be a number greater than 0"]

    # One symbol, one colour. Names are case sensitive: w and W are different concepts.
    colours = {}
    semantic = set()
    for cue in cues:
        for field in ("col", "color"):
            c = colour_key((cue.get("data") or {}).get(field))
            if c:
                semantic.add(c)
        for tok in tokens_of(cue):
            c = colour_key(tok.get("col"))
            if not c:
                continue
            semantic.add(c)
            symbol = tok.get("s")
            if symbol:
                colours.setdefault(symbol, set()).add(c)
    for symbol, seen in sorted(colours.items()):
        if len(seen) > 1:
            warnings.append(
                f"symbol {symbol!r} appears in {len(seen)} colours ({', '.join(sorted(seen))}); "
                "one concept keeps one colour for the whole film"
            )
    if len(semantic) > SEMANTIC_LIMIT:
        warnings.append(
            f"{len(semantic)} semantic colours ({', '.join(sorted(semantic))}); "
            f"the grammar budget is {SEMANTIC_LIMIT}"
        )

    # A conclusion needs room to be looked at after its cue arrives.
    timed = [q for q in cues if isinstance(q.get("at"), (int, float))]
    if timed:
        last = max(timed, key=lambda q: q["at"])
        if last["at"] > duration - HOLD:
            warnings.append(
                f"last cue {last.get('kind')} starts at {last['at']}s in a {duration}s clip, "
                f"leaving {duration - last['at']:.2f}s; leave at least {HOLD}s after the conclusion"
            )
        extended = last["at"] + (last.get("dur") or 0)
        if last.get("dur") and extended > duration - HOLD:
            warnings.append(
                f"last cue declares dur={last['dur']}s and ends {duration - extended:.2f}s "
                f"before the clip ends; leave at least {HOLD}s"
            )

    # A target that names an absent cue can never be drawn.
    kinds = {q.get("kind") for q in cues}
    for i, cue in enumerate(cues):
        target = (cue.get("data") or {}).get("target")
        if target in COLUMN and target not in kinds:
            warnings.append(
                f"cue[{i}] {cue.get('kind')} targets {target!r} but no {target} cue exists"
            )

    # Caption notation follows the spoken/written split already enforced on beats.
    for i, cue in enumerate(cues):
        text = (
            text_of(cue) + " " + " ".join(str(t.get("s") or "") for t in tokens_of(cue))
        )
        hit = MONTHS.search(text) or SPELLED.search(text)
        if hit:
            warnings.append(
                f"cue[{i}] writes {hit.group(0)!r} in words; on-screen numbers use digits, "
                "the voice keeps the spoken form (scripts/audit_numbers.py)"
            )
    return warnings


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("spec", type=Path)
    ap.add_argument("--strict", action="store_true", help="warnings become exit code 1")
    a = ap.parse_args()
    try:
        spec = json.loads(a.spec.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"cannot read {a.spec}: {e}")
    if not isinstance(spec, dict):
        sys.exit(f"{a.spec}: expected a JSON object")
    warnings = check(spec)
    if not warnings:
        print(f"OK {a.spec}: no maths warnings")
        return 0
    for w in warnings:
        print(f"WARN {a.spec}: {w}")
    print(f"advisory: {len(warnings)} warning(s); --strict makes them fail")
    return 1 if a.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
