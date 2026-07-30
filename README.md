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

Differentials are grouped into **This presentation / Must not miss / Other**,
with must-not-miss outlined in red, so the tab strip doubles as a safety
checklist.

The timed blocks are laid out on a numbered rail, and **the block you should be
in lights up as the timer runs** — the current block takes an accent dot and
rail, completed blocks fade back. A countdown runs to the correct limit for the
mode (2:00 or 3:00) and turns red when you go over, and the progress bar is
notched at each block boundary so you can see at a glance whether you are ahead
or behind. Space bar starts and pauses.

### Patient roleplay

In history mode there is a **Doctor / Patient roleplay** switch, so two people
can run the station from one screen.

The roleplay view is a simulated-patient brief — which is how real OSCE actor
briefs work: instructions on what to disclose and when, not a verbatim script.
Each line is tagged with its disclosure rule (**Your opening line**, **How to
play it**, **Only if asked**), and **hovering or tapping any line reveals the
question the doctor needs to ask to elicit it**. Keyboard users can tab to each
line for the same reveal.

The brief gives the actor an opening line in lay language ("I have been getting
noisy, harsh breathing"), an affect cue for the system ("play it breathless:
short sentences, pause for air"), and the discriminating details to hold back
until asked. On a differential tab the actor is told which diagnosis they are
playing and instructed not to name it. Doctor-side technique lines — introducing
yourself, gaining consent, summarising back — have no patient counterpart and
are simply omitted from the roleplay view.

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
- `build/build.py` — parses each case and derives the practice cards.
- `build/layer.py` — the injected presentation: styles, drawer markup and
  behaviour. Separated from `build.py` so the design can be iterated on without
  touching the parsing and content generation.

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
- The patient brief is generated from the doctor-side prompts by lay-language
  substitution (`LAY` and `PRESENTATION_LAY` in `knowledge.py`). Concrete
  symptom nouns translate well — *haemoptysis* becomes *coughing up blood* — but
  where a prompt has no lay equivalent the patient line stays in clinical
  register and reads as a disclosure topic rather than natural speech. The
  doctor-side reveal is the prompt rephrased as an instruction to ask, so on
  those lines the two sides are close in wording. Adding a `LAY` entry improves
  both sides at once.
- The affect cues are per system, not per diagnosis, so they set the register
  rather than portraying a specific case.
