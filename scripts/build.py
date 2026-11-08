#!/usr/bin/env python3
"""Build calendar.ics and the README table from data/changes.json.

Run from the repository root: python3 scripts/build.py
Uses only the standard library.
"""
import datetime
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "changes.json"
README = ROOT / "README.md"
CALENDAR = ROOT / "calendar.ics"
START, END = "<!-- table:start -->", "<!-- table:end -->"
TYPES = {"shutdown", "reroute", "price", "feature"}
VERB = {"shutdown": "shuts down", "reroute": "reroutes", "price": "price change", "feature": "feature change"}


def load():
    doc = json.loads(DATA.read_text())
    changes = doc["changes"]
    for i, c in enumerate(changes):
        missing = [k for k in ("date", "provider", "type", "models", "source") if not c.get(k)]
        if missing or c["type"] not in TYPES:
            sys.exit(f"entry {i}: missing {missing} or bad type {c.get('type')!r}")
        datetime.date.fromisoformat(c["date"])
    changes.sort(key=lambda c: (c["date"], c["provider"], c["models"][0]))
    return doc["checked"], changes


def table(changes):
    lines = ["| Date | Provider | Change | Model | Replacement | Source |", "| :-- | :-- | :-- | :-- | :-- | :-- |"]
    for c in changes:
        model = "<br>".join(m if " " in m else f"`{m}`" for m in c["models"])
        rep = c["replacement"]
        detail = f"`{rep}`" if rep and " " not in rep else rep
        if c["note"]:
            detail = f"{detail}. {c['note']}" if detail else c["note"]
        lines.append(f"| {c['date']} | {c['provider']} | {c['type']} | {model} | {detail} | [link]({c['source']}) |")
    return "\n".join(lines)


def fold(line):
    """RFC 5545: lines longer than 75 octets continue on the next line after a space."""
    raw, out = line.encode(), []
    while len(raw) > 75:
        cut = 75 if not out else 74
        while (raw[cut] & 0xC0) == 0x80:  # do not split a UTF-8 sequence
            cut -= 1
        out.append(raw[:cut])
        raw = raw[cut:]
    out.append(raw)
    return b"\r\n ".join(out).decode()


def text(value):
    return value.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def calendar(checked, changes):
    stamp = checked.replace("-", "") + "T000000Z"
    groups = {}
    for c in changes:
        groups.setdefault((c["date"], c["provider"]), []).append(c)
    out = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//ai-model-deprecations//EN", "CALSCALE:GREGORIAN",
           "X-WR-CALNAME:AI model deprecations", "X-WR-CALDESC:Shutdown\\, reroute and price-change dates for AI model APIs"]
    for (date, provider), items in sorted(groups.items()):
        day = datetime.date.fromisoformat(date)
        names = ", ".join(c["models"][0] for c in items)
        summary = f"{provider}: {names} {VERB[items[0]['type']]}" if len(items) == 1 else f"{provider}: {len(items)} model changes"
        body = []
        for c in items:
            line = f"{c['models'][0]} ({c['type']})"
            if c["replacement"]:
                line += f" -> {c['replacement']}"
            if c["note"]:
                line += f". {c['note']}"
            body.append(line)
        body.append("Sources: " + " ".join(sorted({c["source"] for c in items})))
        uid = hashlib.sha1(f"{date}|{provider}".encode()).hexdigest()[:16]
        out += ["BEGIN:VEVENT", f"UID:{uid}@ai-model-deprecations", f"DTSTAMP:{stamp}",
                f"DTSTART;VALUE=DATE:{day:%Y%m%d}", f"DTEND;VALUE=DATE:{day + datetime.timedelta(days=1):%Y%m%d}",
                f"SUMMARY:{text(summary)}", f"DESCRIPTION:{text(chr(10).join(body))}", "TRANSP:TRANSPARENT", "END:VEVENT"]
    out.append("END:VCALENDAR")
    return "\r\n".join(fold(line) for line in out) + "\r\n"


def main():
    checked, changes = load()
    CALENDAR.write_text(calendar(checked, changes), newline="")
    readme = README.read_text()
    head, rest = readme.split(START, 1)
    _, tail = rest.split(END, 1)
    note = f"Checked against the official pages on {checked}. {len(changes)} entries."
    README.write_text(f"{head}{START}\n{note}\n\n{table(changes)}\n{END}{tail}")
    print(f"{len(changes)} entries, {CALENDAR.name} and {README.name} updated")


if __name__ == "__main__":
    main()
