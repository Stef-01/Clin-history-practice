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
    BACKGROUND,
    CLOSING,
    DIFFERENTIAL_KB,
    EXAM_CLOSING,
    EXAM_OPENING,
    OPENING,
    SYSTEM_KB,
)

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


def build_history(title, system, focus_hx, red_flags):
    """A 2-minute history split into four timed blocks (120 seconds total)."""
    return [
        {"t": "0:00 - 0:20", "h": "Open and orient", "items": list(OPENING)},
        {"t": "0:20 - 1:10", "h": "Focused discriminators", "items": focus_hx},
        {"t": "1:10 - 1:35", "h": "Background in one sweep", "items": list(BACKGROUND)},
        {
            "t": "1:35 - 2:00",
            "h": "Red flags, then close",
            "items": (red_flags or []) + list(CLOSING),
        },
    ]


def build_exam(system, focus_ex):
    """A 3-minute examination split into four timed blocks (180 seconds total)."""
    sys_entry = SYSTEM_KB.get(system, {})
    return [
        {"t": "0:00 - 0:25", "h": "Setup and end of bed", "items": list(EXAM_OPENING)},
        {
            "t": "0:25 - 1:25",
            "h": "Systematic %s examination" % sys_entry.get("focus", "system"),
            "items": sys_entry.get("ex", []),
        },
        {"t": "1:25 - 2:35", "h": "Targeted signs", "items": focus_ex},
        {"t": "2:35 - 3:00", "h": "Complete and present", "items": list(EXAM_CLOSING)},
    ]


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
                "hx": build_history(term, system, focus_hx, red_flags),
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


PRACTICE_CSS = """
/* ---------- PRACTICE LAYER ---------- */
.practice-toggle{
  display:inline-block;margin-left:0;margin-top:.6mm;font-family:var(--mono);
  font-size:5pt;letter-spacing:.1em;text-transform:uppercase;font-weight:700;
  color:var(--accent);background:none;border:.4pt solid var(--accent);
  border-radius:1mm;padding:.5mm 1.4mm;cursor:pointer;line-height:1.3;
  transition:background .12s,color .12s;
}
.practice-toggle:hover,.practice-toggle:focus-visible{background:var(--accent);color:#fff;outline:none}
.critical .practice-toggle{color:var(--red);border-color:var(--red)}
.critical .practice-toggle:hover,.critical .practice-toggle:focus-visible{background:var(--red);color:#fff}
@media print{.practice-toggle{display:none}#practice-drawer{display:none!important}}

#practice-drawer{
  position:fixed;inset:0;z-index:9000;display:none;
  background:rgba(28,26,23,.46);backdrop-filter:blur(2px);
}
#practice-drawer[data-open="1"]{display:block}
.pr-panel{
  position:absolute;top:0;right:0;bottom:0;width:min(720px,100vw);
  background:var(--paper,#FBF9F4);box-shadow:-2px 0 40px rgba(0,0,0,.25);
  display:flex;flex-direction:column;font-size:14px;line-height:1.5;
  animation:pr-in .18s ease-out;
}
@keyframes pr-in{from{transform:translateX(24px);opacity:0}to{transform:none;opacity:1}}
.pr-head{padding:20px 26px 14px;border-bottom:1px solid var(--ink,#1C1A17);flex:0 0 auto}
.pr-kicker{font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);font-weight:700}
.pr-head h2{font-family:var(--display);font-size:26px;line-height:1.1;font-weight:600;margin:6px 0 2px;color:var(--ink)}
.pr-sub{font-family:var(--mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--mute)}
.pr-close{position:absolute;top:16px;right:18px;background:none;border:none;font-size:26px;line-height:1;cursor:pointer;color:var(--mute);padding:4px 8px}
.pr-close:hover{color:var(--ink)}

.pr-tabs{flex:0 0 auto;padding:12px 26px;border-bottom:1px solid #E0DDD6;display:flex;flex-wrap:wrap;gap:6px;max-height:150px;overflow-y:auto}
.pr-tab{
  font-family:var(--mono);font-size:10px;letter-spacing:.04em;text-transform:uppercase;
  border:1px solid #D8D4CB;background:transparent;color:var(--ink);border-radius:3px;
  padding:5px 9px;cursor:pointer;transition:all .12s;
}
.pr-tab:hover{border-color:var(--accent);color:var(--accent)}
.pr-tab[aria-selected="true"]{background:var(--ink);border-color:var(--ink);color:var(--paper)}
.pr-tab.general{border-color:var(--accent);color:var(--accent);font-weight:700}
.pr-tab.general[aria-selected="true"]{background:var(--accent);color:#fff}
.pr-tab.must-not-miss{border-color:var(--red);color:var(--red)}
.pr-tab.must-not-miss[aria-selected="true"]{background:var(--red);border-color:var(--red);color:#fff}

.pr-modes{flex:0 0 auto;padding:12px 26px 0;display:flex;gap:8px;align-items:center}
.pr-mode{font-family:var(--mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;font-weight:700;
  border:1px solid var(--ink);background:transparent;color:var(--ink);border-radius:3px;padding:6px 12px;cursor:pointer}
.pr-mode[aria-pressed="true"]{background:var(--ink);color:var(--paper)}
.pr-timer{margin-left:auto;font-family:var(--mono);font-size:15px;font-weight:700;color:var(--ink);font-variant-numeric:tabular-nums}
.pr-timer.over{color:var(--red)}
.pr-timer-btn{font-family:var(--mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;
  border:1px solid var(--accent);color:var(--accent);background:transparent;border-radius:3px;padding:6px 10px;cursor:pointer}
.pr-timer-btn:hover{background:var(--accent);color:#fff}

.pr-body{flex:1 1 auto;overflow-y:auto;padding:18px 26px 40px}
.pr-block{border-top:1px solid #E0DDD6;padding:14px 0 4px}
.pr-block:first-child{border-top:none}
.pr-block-head{display:flex;align-items:baseline;gap:10px;margin-bottom:7px}
.pr-time{font-family:var(--mono);font-size:11px;font-weight:700;color:var(--accent);font-variant-numeric:tabular-nums;white-space:nowrap}
.pr-block h3{font-family:var(--display);font-size:16px;font-weight:600;margin:0;color:var(--ink)}
.pr-block ul{padding-left:20px;margin:0}
.pr-block li{font-size:13.5px;line-height:1.5;margin-bottom:6px}
.pr-note{background:rgba(243,121,64,.09);border-left:2px solid var(--accent);padding:10px 12px;margin:14px 0 0;font-size:13px;line-height:1.5}
.pr-flag{background:rgba(198,58,42,.08);border-left:2px solid var(--red);padding:10px 12px;margin:0 0 12px;font-size:13px;line-height:1.5}
.pr-gen-hint{font-family:var(--mono);font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--mute);margin-top:16px;border-top:1px dotted #D8D4CB;padding-top:10px}
@media (max-width:640px){.pr-panel{width:100vw}.pr-head,.pr-tabs,.pr-modes,.pr-body{padding-left:16px;padding-right:16px}}
"""

PRACTICE_HTML = """
<div id="practice-drawer" role="dialog" aria-modal="true" aria-labelledby="pr-title">
  <div class="pr-panel">
    <div class="pr-head">
      <div class="pr-kicker" id="pr-kicker"></div>
      <h2 id="pr-title"></h2>
      <div class="pr-sub" id="pr-sub"></div>
      <button class="pr-close" type="button" aria-label="Close practice panel">&times;</button>
    </div>
    <div class="pr-tabs" id="pr-tabs" role="tablist"></div>
    <div class="pr-modes">
      <button class="pr-mode" type="button" data-mode="hx" aria-pressed="true">2 min history</button>
      <button class="pr-mode" type="button" data-mode="ex" aria-pressed="false">3 min examination</button>
      <div class="pr-timer" id="pr-timer">2:00</div>
      <button class="pr-timer-btn" type="button" id="pr-timer-btn">Start</button>
    </div>
    <div class="pr-body" id="pr-body"></div>
  </div>
</div>
"""

PRACTICE_JS = """
<script>
(function(){
  var DATA = JSON.parse(document.getElementById('practice-data').textContent);
  var drawer = document.getElementById('practice-drawer');
  var tabsEl = document.getElementById('pr-tabs');
  var bodyEl = document.getElementById('pr-body');
  var timerEl = document.getElementById('pr-timer');
  var timerBtn = document.getElementById('pr-timer-btn');
  var state = {caseNo:null, tab:0, mode:'hx'};
  var tick=null, remain=0, lastFocus=null;

  function fmt(s){var m=Math.floor(Math.abs(s)/60), r=Math.abs(s)%60;
    return (s<0?'-':'')+m+':'+(r<10?'0':'')+r;}

  function limit(){return state.mode==='hx'?120:180;}

  function resetTimer(){
    stopTimer(); remain=limit();
    timerEl.textContent=fmt(remain); timerEl.classList.remove('over'); timerBtn.textContent='Start';
  }
  function stopTimer(){ if(tick){clearInterval(tick); tick=null;} }
  function toggleTimer(){
    if(tick){stopTimer(); timerBtn.textContent='Resume'; return;}
    timerBtn.textContent='Pause';
    tick=setInterval(function(){
      remain--; timerEl.textContent=fmt(remain);
      if(remain<=0) timerEl.classList.add('over');
    },1000);
  }

  function render(){
    var c = DATA[state.caseNo]; if(!c) return;
    document.getElementById('pr-kicker').textContent = 'Case '+c.number+' / practice';
    document.getElementById('pr-title').textContent = c.title;
    document.getElementById('pr-sub').textContent = c.system;

    tabsEl.innerHTML='';
    c.tabs.forEach(function(t,i){
      var b=document.createElement('button');
      b.type='button'; b.className='pr-tab '+t.group; b.setAttribute('role','tab');
      b.setAttribute('aria-selected', i===state.tab?'true':'false');
      b.textContent=t.label;
      b.addEventListener('click', function(){ state.tab=i; render(); resetTimer(); });
      tabsEl.appendChild(b);
    });

    document.querySelectorAll('.pr-mode').forEach(function(m){
      m.setAttribute('aria-pressed', m.dataset.mode===state.mode ? 'true':'false');
    });

    var tab=c.tabs[state.tab]; var blocks=tab[state.mode]; var out='';
    if(state.mode==='hx' && tab.group!=='general'){
      out+='<div class="pr-flag"><strong>Target:</strong> you are taking this history to confirm or exclude '
        +esc(tab.label.toLowerCase())+' as the cause of '+esc(c.title.toLowerCase())+'.</div>';
    }
    blocks.forEach(function(b){
      out+='<div class="pr-block"><div class="pr-block-head"><span class="pr-time">'+esc(b.t)
        +'</span><h3>'+esc(b.h)+'</h3></div><ul>';
      b.items.forEach(function(it){ out+='<li>'+esc(it)+'</li>'; });
      out+='</ul></div>';
    });
    if(state.mode==='hx' && tab.note){
      out+='<div class="pr-note"><strong>First management priority for this presentation:</strong> '
        +esc(tab.note)+'</div>';
    }
    out+='<div class="pr-gen-hint">Rehearsal aid built from this handbook. Confirm dosing and thresholds against '
       +'current local guidelines before clinical use.</div>';
    bodyEl.innerHTML=out; bodyEl.scrollTop=0;
  }

  function esc(s){return String(s).replace(/[&<>"]/g,function(ch){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[ch];});}

  function open(caseNo){
    if(!DATA[caseNo]) return;
    lastFocus=document.activeElement;
    state.caseNo=caseNo; state.tab=0; state.mode='hx';
    drawer.dataset.open='1'; render(); resetTimer();
    document.querySelector('.pr-close').focus();
  }
  function close(){
    drawer.removeAttribute('data-open'); stopTimer();
    if(lastFocus && lastFocus.focus) lastFocus.focus();
  }

  document.addEventListener('click', function(e){
    var t=e.target.closest('.practice-toggle');
    if(t){ e.preventDefault(); open(t.dataset.case); return; }
    if(e.target.closest('.pr-close')){ close(); return; }
    if(e.target===drawer){ close(); return; }
    var m=e.target.closest('.pr-mode');
    if(m){ state.mode=m.dataset.mode; render(); resetTimer(); }
  });
  timerBtn.addEventListener('click', toggleTimer);
  document.addEventListener('keydown', function(e){
    if(e.key==='Escape' && drawer.dataset.open) close();
  });
})();
</script>
"""


if __name__ == "__main__":
    main()
