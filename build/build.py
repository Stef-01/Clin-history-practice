#!/usr/bin/env python3
"""Build index.html from build/source.html by injecting the practice layer.

For every case card the builder adds a toggle button that opens a practice
drawer containing timed OSCE-style rehearsal cards: a 2-minute focused history
and a 3-minute focused examination, for the generalised presentation and for
each differential listed on that card.

Run:  python3 build/build.py
"""

import html
import json
import os
import re

from knowledge import (
    AFFECT,
    BACKGROUND,
    CLOSING,
    CLOSING_PATIENT,
    DIFFERENTIAL_KB,
    DISCLOSURE,
    EXAM_CLOSING,
    EXAM_OPENING,
    FINDING_PRESENTATIONS,
    LAY,
    OPENING,
    PRESENTATION_LAY,
    SYSTEM_KB,
)
from layer import PRACTICE_CSS, PRACTICE_HTML, PRACTICE_JS

LAY_KEYS = sorted(LAY, key=len, reverse=True)

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "source.html")
OUTPUT = os.path.join(os.path.dirname(HERE), "index.html")

# Keys sorted longest-first so "pulmonary oedema" beats "oedema".
KB_KEYS = sorted(DIFFERENTIAL_KB, key=len, reverse=True)
SHORT_KEYS = {k for k in KB_KEYS if len(k) <= 4}


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s).strip()


def match_kb(term):
    """Return the KB entry whose key best matches this differential, or None."""
    t = term.lower()
    for key in KB_KEYS:
        if key in SHORT_KEYS:
            if re.search(r"\b" + re.escape(key) + r"\b", t):
                return DIFFERENTIAL_KB[key]
        elif key in t:
            return DIFFERENTIAL_KB[key]
    return None


def parse_differentials(card_html):
    """Return [(label, group)] where group is 'must-not-miss' or 'other'."""
    m = re.search(r"Differentials</span><ul>(.*?)</ul>", card_html, re.S)
    if not m:
        return []
    out, seen = [], set()
    for li in re.findall(r"<li>(.*?)</li>", m.group(1), re.S):
        text = html.unescape(strip_tags(li))
        group = "other"
        pm = re.match(r"^([^:]{0,40}?):\s*(.*)$", text, re.S)
        if pm:
            head = pm.group(1).lower()
            if "not miss" in head or "critical" in head or "emergen" in head:
                group = "must-not-miss"
            text = pm.group(2)
        # Split on commas and semicolons; keep parenthetical detail attached.
        for part in re.split(r",(?![^(]*\))|;", text):
            label = part.strip().rstrip(".").strip()
            label = re.sub(r"^(and|or)\s+", "", label, flags=re.I)
            if not label or len(label) > 70:
                continue
            k = label.lower()
            if k in seen:
                continue
            seen.add(k)
            out.append((label[0].upper() + label[1:], group))
    return out


def section_bullets(card_html, label_fragment):
    m = re.search(
        r"case-section-label\">[^<]*" + label_fragment + r"[^<]*</span><ul>(.*?)</ul>",
        card_html,
        re.S | re.I,
    )
    if not m:
        return []
    return [html.unescape(strip_tags(li)) for li in re.findall(r"<li>(.*?)</li>", m.group(1), re.S)]


def clock(seconds):
    return "%d:%02d" % (seconds // 60, seconds % 60)


def lay(text):
    """Render a doctor-side prompt into lay language for the actor brief."""
    out = text
    for key in LAY_KEYS:
        out = re.sub(re.escape(key), LAY[key], out, flags=re.I)
    # Doctor prompts are written as instructions to the clinician; the actor
    # brief needs the topic, not the instruction verb.
    out = re.sub(r"^(ask (directly )?about|ask directly|ask|establish|determine|"
                 r"characterise|quantify|screen for|explore|elicit|clarify)\s*:?\s*",
                 "", out, flags=re.I)
    out = re.sub(r"^(a |an |the )", "", out, flags=re.I)
    return out[0].lower() + out[1:] if out else out


IMPERATIVE = re.compile(
    r"^(ask|establish|determine|characterise|quantify|screen|explore|elicit|clarify|"
    r"give|read|open|introduce|summarise|confirm|check|cover|take|note|look|"
    r"in |a complete|the )", re.I)


def question(prompt):
    """Phrase a doctor-side prompt as an instruction to ask, for the hover reveal.

    KB prompts are mostly bare topics ("Exposure to a known or new trigger"), so
    without this the reveal would just restate the patient's line back.
    """
    if IMPERATIVE.match(prompt):
        return prompt
    text = prompt[0].lower() + prompt[1:]
    return "Ask about %s" % text


def item(doctor, patient=None, rule=None, ask=None):
    """One rehearsal item: the doctor's prompt and the patient's instruction.

    patient=None means the line is doctor-only (clinician etiquette and
    technique), so the roleplay view simply omits it. 'q' is the question form
    shown when the patient line is hovered.
    """
    return {"d": doctor, "p": patient, "r": rule, "q": ask}


def timed(blocks):
    """Attach numeric start/end seconds and a display label to each block.

    Blocks arrive as (duration, heading, items); the numeric bounds let the
    drawer highlight whichever block you should be in as the timer runs.
    """
    out, at = [], 0
    for i, (dur, heading, items) in enumerate(blocks):
        out.append({
            "n": "%02d" % (i + 1),
            "s": at,
            "e": at + dur,
            "t": "%s - %s" % (clock(at), clock(at + dur)),
            "h": heading,
            "items": items,
        })
        at += dur
    return out


def build_history(presentation, system, focus_hx, red_flags):
    """A 2-minute history split into four timed blocks (120 seconds total).

    Every item carries both sides so the roleplay view can reveal the doctor's
    eliciting question on hover. `presentation` is always the case title, never
    the differential - the simulated patient describes the symptom they came in
    with and must never name their own diagnosis.
    """
    # Block 01 is technique: the doctor-side items have no patient counterpart,
    # so the actor gets an opening line and an affect cue instead.
    opening = [item(d) for d in OPENING]
    key = presentation.lower()
    if key in FINDING_PRESENTATIONS:
        line = ('You have been told you have %s and this appointment is about it. '
                'Open with "I was told there was something on my test, and I want to '
                'know what it means." Then wait to be asked.' % presentation.lower())
    else:
        line = ('Open in your own words with something like "I have been getting %s, '
                'and that is what brought me in." Then stop talking and wait to be asked.'
                % PRESENTATION_LAY.get(key, presentation.lower()))
    opening.insert(0, item(
        "Give the patient 30 seconds of uninterrupted opening before you narrow down.",
        line,
        "Your opening line",
    ))
    opening.append(item(
        "Read the patient's affect as well as their words - it is part of the history.",
        AFFECT.get(system, "Play it as someone genuinely worried by this symptom."),
        "How to play it",
    ))

    def disclose(prompt):
        text = lay(prompt).rstrip(".")
        return item(prompt, text[0].upper() + text[1:], "Only if asked",
                    ask=question(prompt))

    focused = [disclose(d) for d in focus_hx]
    background = [disclose(d) for d in BACKGROUND]

    # Red flags come from the card's clinical-priority line - a management
    # instruction to the clinician, so it stays doctor-only.
    closing = [item(d) for d in (red_flags or [])]
    closing += [item(d) for d in CLOSING]
    closing += [item("Summarise back, check for anything missed, and signpost the plan.", p,
                     "How to play it") for p in CLOSING_PATIENT]

    return timed([
        (20, "Open and orient", opening),
        (50, "Focused discriminators", focused),
        (25, "Background in one sweep", background),
        (25, "Red flags, then close", closing),
    ])


def build_exam(system, focus_ex):
    """A 3-minute examination split into four timed blocks (180 seconds total)."""
    sys_entry = SYSTEM_KB.get(system, {})
    return timed([
        (25, "Setup and end of bed", list(EXAM_OPENING)),
        (60, "Systematic %s examination" % sys_entry.get("focus", "system"),
         sys_entry.get("ex", [])),
        (70, "Targeted signs", focus_ex),
        (25, "Complete and present", list(EXAM_CLOSING)),
    ])


def generic_focus(term, system):
    """Fallback discriminators when the differential is not in the knowledge base."""
    sys_entry = SYSTEM_KB.get(system, {})
    return (
        [
            "Establish the features that would make %s more likely than the alternatives: "
            "onset, time course, and the single most specific symptom." % term.lower(),
            "Ask directly about the risk factors and exposures that predispose to %s." % term.lower(),
            "Ask what would argue against it, so you can rule it in or out rather than only collecting positives.",
        ]
        + sys_entry.get("hx", [])[:2],
        [
            "Seek the signs that would confirm %s, and state explicitly whether each is present or absent."
            % term.lower(),
            "Compare with the contralateral side or an unaffected area wherever anatomy allows.",
            "Look for the complication of %s that would change management today." % term.lower(),
        ]
        + sys_entry.get("ex", [])[:2],
    )


def build_case_practice(card_html, system):
    title = html.unescape(strip_tags(re.search(r'case-title">(.*?)</h3>', card_html, re.S).group(1)))
    number = strip_tags(re.search(r'case-number">(.*?)</div>', card_html, re.S).group(1))
    priority = html.unescape(
        strip_tags(re.sub(r"<span class=\"priority-label\">.*?</span>", "",
                          re.search(r'class="priority">(.*?)</div>', card_html, re.S).group(1), flags=re.S))
    )
    bedside = section_bullets(card_html, "Bedside examination")
    mgmt = section_bullets(card_html, "Management")
    sys_entry = SYSTEM_KB.get(system, {})

    # --- generalised presentation tab ---
    gen_hx = [
        "Characterise %s itself: onset, duration, severity, pattern, and what changes it."
        % title.lower(),
        "Establish the time course precisely - abrupt, over hours, or over weeks - it narrows the list fastest.",
    ] + sys_entry.get("hx", [])
    gen_ex = bedside or sys_entry.get("ex", [])
    red_flags = [priority] if priority else []

    tabs = [
        {
            "id": "general",
            "label": "Generalised presentation",
            "group": "general",
            "hx": build_history(title, system, gen_hx, red_flags),
            "ex": build_exam(system, gen_ex),
            "note": mgmt[0] if mgmt else "",
        }
    ]

    for i, (term, group) in enumerate(parse_differentials(card_html)):
        entry = match_kb(term)
        if entry:
            focus_hx, focus_ex = list(entry["hx"]), list(entry["ex"])
            matched = True
        else:
            focus_hx, focus_ex = generic_focus(term, system)
            matched = False
        tabs.append(
            {
                "id": "d%d" % i,
                "label": term,
                "group": group,
                "matched": matched,
                # `title`, not `term`: the patient presents with the symptom and
                # must not name the diagnosis being tested.
                "hx": build_history(title, system, focus_hx, red_flags),
                "ex": build_exam(system, focus_ex),
                "note": "",
            }
        )

    return number, {"number": number, "title": title, "system": system, "tabs": tabs}


def main():
    src = open(SOURCE, encoding="utf-8").read()

    data = {}
    stats = {"cases": 0, "tabs": 0, "matched": 0, "fallback": 0}

    # Walk each source system so the card keeps its system context.
    for sysm in re.finditer(r'<section class="source-system"(.*?)</section>\s*(?=<section class="source-system"|</div>)', src, re.S):
        block = sysm.group(0)
        system = re.search(r'data-name="([^"]+)"', block).group(1)
        for cm in re.finditer(r'<article class="case-card.*?</article>', block, re.S):
            number, entry = build_case_practice(cm.group(0), system)
            data[number] = entry
            stats["cases"] += 1
            for t in entry["tabs"][1:]:
                stats["tabs"] += 1
                stats["matched" if t.get("matched") else "fallback"] += 1

    # Inject the toggle button into every case head in the source markup.
    def add_button(m):
        head = m.group(0)
        number = strip_tags(re.search(r'case-number">(.*?)</div>', head, re.S).group(1))
        btn = ('<button type="button" class="practice-toggle" data-case="%s" '
               'aria-haspopup="dialog">Practice</button>' % html.escape(number))
        return head.replace("</h3>", "</h3>" + btn, 1)

    out = re.sub(r'<div class="case-head">.*?</div></div>', add_button, src, flags=re.S)

    payload = "<script id=\"practice-data\" type=\"application/json\">%s</script>" % json.dumps(
        data, ensure_ascii=False
    ).replace("</", "<\\/")

    out = out.replace("</style>", PRACTICE_CSS + "\n</style>", 1)
    out = out.replace("</body>", payload + PRACTICE_HTML + PRACTICE_JS + "</body>", 1)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(out)

    print("cases: %(cases)d   differential tabs: %(tabs)d" % stats)
    print("knowledge-base matched: %d (%.0f%%)   template fallback: %d"
          % (stats["matched"], 100.0 * stats["matched"] / max(stats["tabs"], 1), stats["fallback"]))
    print("wrote %s (%.0f KB)" % (OUTPUT, os.path.getsize(OUTPUT) / 1024))


if __name__ == "__main__":
    main()
