# Clinical history & examination practice

An interactive rehearsal layer built on top of the *Clinical Presentation
Approaches* bedside handbook.

Open **`index.html`** in any browser. It is a single self-contained file — no
build step, no server, no network access required.

## What it does

The handbook itself is unchanged: 102 presentations across 11 systems, each
laid out as a vertical sequence (bedside examination → investigations → imaging
→ management → differentials), still paginated for A4 printing.

On top of that, every case now carries a **Practice** button. Pressing it opens
a drawer with timed OSCE-style rehearsal cards:

- **2 min history** — four timed blocks: open and orient (0:00–0:20), focused
  discriminators (0:20–1:10), background in one sweep (1:10–1:35), red flags
  then close (1:35–2:00).
- **3 min examination** — setup and end of bed (0:00–0:25), systematic
  system examination (0:25–1:25), targeted signs (1:25–2:35), complete and
  present (2:35–3:00).

Each case has one tab per differential plus a **Generalised presentation** tab:

- The generalised tab rehearses the presenting complaint itself, using the
  card's own bedside-examination content and its clinical-priority statement as
  the red-flag block.
- Each differential tab reframes the task — *"you are taking this history to
  confirm or exclude X as the cause of Y"* — and swaps in discriminators and
  targeted signs specific to that diagnosis.

Must-not-miss differentials are outlined in red, so the tab strip doubles as a
safety checklist. A countdown timer runs to the correct limit for the mode
(2:00 or 3:00) and turns red when you go over.

Printing is unaffected — the Practice buttons and drawer are hidden in print,
and the original 58-page pagination is preserved.

## How the content is generated

`index.html` is generated, not hand-edited. Do not edit it directly; edit the
build inputs and regenerate:

```bash
python3 build/build.py
```

- `build/source.html` — the original handbook, untouched.
- `build/knowledge.py` — the content knowledge base.
- `build/build.py` — parses each case, derives the practice cards, and injects
  the CSS, JSON payload, drawer markup and behaviour.

Differential-specific content comes from two layers:

1. **`DIFFERENTIAL_KB`** — hand-written discriminating questions and targeted
   signs, matched by keyword stem so `pneumonia` also covers *aspiration
   pneumonia* and *hospital-acquired pneumonia*. Longer keys win over shorter
   ones.
2. **`SYSTEM_KB`** — per-system fallbacks, so a differential with no curated
   entry still produces a usable focused history and examination framed around
   that specific diagnosis, plus the correct system examination sequence.

Current coverage: **1,094 differential tabs across 102 cases; 51% resolve to a
hand-written knowledge-base entry, 49% use the system-level template.** To
improve a differential that currently falls back, add an entry to
`DIFFERENTIAL_KB` and rerun the build — the printed statistics tell you the new
match rate. `build/coverage.py` lists the unmatched differentials by frequency
so you can target the highest-yield gaps first.

## Scope and limitations

- This is a **rehearsal aid for structuring histories and examinations**, not a
  clinical decision tool and not a source of doses or thresholds. Confirm
  everything against current local guidelines before clinical use.
- The template-generated tabs (the 49%) give a sound *structure* and correctly
  frame the diagnostic question, but they do not contain
  diagnosis-specific clinical detail. Treat them as a scaffold to fill in, not
  as taught content.
