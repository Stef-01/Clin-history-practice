"""The injected practice layer: styles, drawer markup and behaviour.

Kept separate from build.py so the presentation can be iterated on without
touching the parsing and content-generation logic.
"""

PRACTICE_CSS = """
/* ---------- PRACTICE LAYER ---------- */
.case-head>div:last-child{position:relative}
.practice-toggle{
  position:absolute;top:.2mm;right:0;
  font-family:var(--mono);font-size:4.9pt;letter-spacing:.13em;text-transform:uppercase;
  font-weight:700;color:var(--accent);background:none;border:0;cursor:pointer;
  padding:.4mm 0 .7mm;line-height:1;
  border-bottom:.5pt solid var(--accent);
  transition:color .14s,border-color .14s,letter-spacing .14s;
}
.practice-toggle::after{content:" \\2192"}
.practice-toggle:hover,.practice-toggle:focus-visible{
  color:var(--ink);border-color:var(--ink);letter-spacing:.17em;outline:none;
}
.critical .practice-toggle{color:var(--red);border-color:var(--red)}
.critical .practice-toggle:hover,.critical .practice-toggle:focus-visible{color:var(--ink);border-color:var(--ink)}
@media print{.practice-toggle{display:none}#practice-drawer{display:none!important}}

/* ---- scrim + panel ---- */
#practice-drawer{position:fixed;inset:0;z-index:9000;visibility:hidden;opacity:0;
  transition:opacity .22s ease,visibility .22s;
  background:rgba(20,28,33,.52);backdrop-filter:blur(3px) saturate(.9);}
#practice-drawer[data-open="1"]{visibility:visible;opacity:1}
.pr-panel{
  position:absolute;top:0;right:0;bottom:0;width:min(760px,100vw);
  background:var(--paper);display:flex;flex-direction:column;
  box-shadow:-1px 0 0 rgba(33,46,54,.16),-30px 0 80px -20px rgba(20,28,33,.42);
  transform:translateX(28px);transition:transform .26s cubic-bezier(.22,.8,.3,1);
  font-family:var(--sans);color:var(--body);
}
#practice-drawer[data-open="1"] .pr-panel{transform:none}

/* ---- header: ink block ---- */
.pr-head{flex:0 0 auto;background:var(--ink);color:var(--paper);padding:26px 34px 22px;position:relative}
.pr-kicker{font-family:var(--mono);font-size:9.5px;letter-spacing:.19em;text-transform:uppercase;
  color:var(--accent);font-weight:700}
.pr-head h2{font-family:var(--display);font-size:30px;line-height:1.06;font-weight:500;
  letter-spacing:-.02em;margin:9px 0 9px;color:#fff}
.pr-sub{font-family:var(--mono);font-size:9.5px;letter-spacing:.13em;text-transform:uppercase;
  color:rgba(248,246,241,.5)}
.pr-close{position:absolute;top:20px;right:24px;width:30px;height:30px;border-radius:50%;
  background:rgba(248,246,241,.09);border:0;color:rgba(248,246,241,.75);
  font-size:17px;line-height:1;cursor:pointer;transition:background .14s,color .14s}
.pr-close:hover{background:var(--accent);color:#fff}

/* ---- differential tabs, grouped ---- */
.pr-tabs{flex:0 0 auto;padding:16px 34px 14px;border-bottom:.75pt solid var(--hair);
  max-height:172px;overflow-y:auto;background:var(--paper);
  /* fade the cut edge when the differential list overflows */
  mask-image:linear-gradient(to bottom,#000 calc(100% - 22px),transparent);
  -webkit-mask-image:linear-gradient(to bottom,#000 calc(100% - 22px),transparent)}
.pr-group+.pr-group{margin-top:12px}
.pr-group-label{font-family:var(--mono);font-size:8.5px;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mute);margin-bottom:7px}
.pr-group-label.danger{color:var(--red)}
.pr-group-row{display:flex;flex-wrap:wrap;gap:5px}
.pr-tab{font-family:var(--sans);font-size:11.5px;letter-spacing:.005em;
  border:.75pt solid var(--hair);background:transparent;color:var(--body);
  border-radius:2px;padding:5px 10px 6px;cursor:pointer;line-height:1.25;
  transition:border-color .13s,color .13s,background .13s}
.pr-tab:hover{border-color:var(--ink);color:var(--ink)}
.pr-tab[aria-selected="true"]{background:var(--ink);border-color:var(--ink);color:var(--paper)}
.pr-tab.general{border-color:var(--accent);color:var(--accent);font-weight:600}
.pr-tab.general[aria-selected="true"]{background:var(--accent);border-color:var(--accent);color:#fff}
.pr-tab.must-not-miss{border-color:rgba(169,64,53,.45);color:var(--red)}
.pr-tab.must-not-miss[aria-selected="true"]{background:var(--red);border-color:var(--red);color:#fff}

/* ---- mode switch + timer ---- */
.pr-controls{flex:0 0 auto;padding:15px 34px 0;display:flex;align-items:center;gap:16px}
.pr-seg{display:inline-flex;border:.75pt solid var(--ink);border-radius:2px;overflow:hidden}
.pr-mode{font-family:var(--mono);font-size:9.5px;letter-spacing:.13em;text-transform:uppercase;
  font-weight:700;border:0;background:transparent;color:var(--ink);
  padding:8px 14px;cursor:pointer;transition:background .14s,color .14s}
.pr-mode+.pr-mode{border-left:.75pt solid var(--ink)}
.pr-mode[aria-pressed="true"]{background:var(--ink);color:var(--paper)}
.pr-clock{margin-left:auto;display:flex;align-items:center;gap:12px}
.pr-timer{font-family:var(--mono);font-size:21px;font-weight:700;color:var(--ink);
  font-variant-numeric:tabular-nums;letter-spacing:-.01em;transition:color .2s}
.pr-timer.over{color:var(--red)}
.pr-timer-btn{font-family:var(--mono);font-size:9.5px;letter-spacing:.13em;text-transform:uppercase;
  font-weight:700;border:.75pt solid var(--accent);color:var(--accent);background:transparent;
  border-radius:2px;padding:8px 13px;cursor:pointer;min-width:76px;
  transition:background .14s,color .14s}
.pr-timer-btn:hover{background:var(--accent);color:#fff}

/* ---- progress bar with block boundaries ---- */
.pr-progress{flex:0 0 auto;margin:14px 34px 0;height:3px;background:var(--hair);position:relative}
.pr-progress-fill{position:absolute;inset:0 auto 0 0;width:0;background:var(--accent);
  transition:width .95s linear}
.pr-progress.over .pr-progress-fill{background:var(--red)}
.pr-tickmark{position:absolute;top:-2px;bottom:-2px;width:.75pt;background:var(--paper)}

/* ---- timed blocks as a numbered rail ---- */
.pr-body{flex:1 1 auto;overflow-y:auto;padding:6px 34px 48px}
.pr-block{position:relative;padding:20px 0 4px 46px}
.pr-block::before{content:"";position:absolute;left:11px;top:0;bottom:0;
  width:.75pt;background:var(--hair)}
.pr-block:first-of-type::before{top:26px}
.pr-block:last-of-type::before{bottom:auto;height:26px}
.pr-dot{position:absolute;left:5.5px;top:22px;width:12px;height:12px;border-radius:50%;
  background:var(--paper);border:1.5pt solid var(--hair);transition:border-color .2s,background .2s}
.pr-num{position:absolute;left:0;top:38px;font-family:var(--mono);font-size:8.5px;
  font-weight:700;letter-spacing:.06em;color:var(--mute);width:23px;text-align:center;transition:color .2s}
.pr-block-head{display:flex;align-items:baseline;gap:11px;margin-bottom:9px;flex-wrap:wrap}
.pr-block h3{font-family:var(--display);font-size:18px;font-weight:600;letter-spacing:-.012em;
  margin:0;color:var(--ink)}
.pr-time{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.09em;
  color:var(--mute);font-variant-numeric:tabular-nums;white-space:nowrap;transition:color .2s}
.pr-block ul{padding-left:17px;margin:0}
.pr-block li{font-size:13.5px;line-height:1.56;margin-bottom:7px;color:var(--body)}
.pr-block li::marker{color:var(--hair);font-size:.8em}

/* active block, driven by the timer */
.pr-block.live .pr-dot{background:var(--accent);border-color:var(--accent);
  box-shadow:0 0 0 4px rgba(243,121,64,.16)}
.pr-block.live .pr-num,.pr-block.live .pr-time{color:var(--accent)}
.pr-block.live li::marker{color:var(--accent)}
.pr-block.done .pr-dot{background:var(--hair);border-color:var(--hair)}
.pr-block.done .pr-block-head,.pr-block.done ul{opacity:.5;transition:opacity .3s}

/* ---- doctor / patient side switch (history only) ---- */
.pr-sides{display:none;align-items:center;gap:9px}
.pr-sides.on{display:inline-flex}
.pr-side{font-family:var(--mono);font-size:9px;letter-spacing:.13em;text-transform:uppercase;
  font-weight:700;border:.75pt solid var(--hair);background:transparent;color:var(--mute);
  border-radius:2px;padding:7px 11px;cursor:pointer;transition:all .14s}
.pr-side:hover{border-color:var(--ink);color:var(--ink)}
.pr-side[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:var(--paper)}

/* ---- roleplay: patient line, doctor prompt revealed on hover ---- */
.pr-pair{list-style:none;margin:0 0 8px;padding:0}
.pr-pt{position:relative;display:block;cursor:help;
  padding:9px 12px 9px 13px;border-left:2pt solid var(--hair);
  background:rgba(33,46,54,.028);transition:border-color .16s,background .16s}
.pr-pt:hover,.pr-pt:focus-visible{border-color:var(--accent);background:var(--accent-soft);outline:none}
.pr-rule{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.14em;
  text-transform:uppercase;font-weight:700;color:var(--mute);margin-bottom:4px;transition:color .16s}
.pr-pt:hover .pr-rule,.pr-pt:focus-visible .pr-rule{color:var(--accent)}
.pr-rule.free{color:var(--accent)}
.pr-say{display:block;font-family:var(--display);font-size:14.5px;line-height:1.5;
  font-style:italic;color:var(--ink)}
/* display toggle rather than an animated height: no clipping of wrapped text */
.pr-dr{display:none}
.pr-pt:hover .pr-dr,.pr-pt:focus-visible .pr-dr{
  display:block;margin-top:8px;padding-top:8px;
  border-top:.75pt dotted rgba(243,121,64,.5);animation:pr-reveal .16s ease-out}
@keyframes pr-reveal{from{opacity:0;transform:translateY(-2px)}to{opacity:1;transform:none}}
.pr-dr-label{font-family:var(--mono);font-size:8.5px;letter-spacing:.14em;text-transform:uppercase;
  font-weight:700;color:var(--accent);display:block;margin-bottom:3px}
.pr-dr-text{font-size:12.8px;line-height:1.52;color:var(--body)}
.pr-hint{font-family:var(--mono);font-size:8.5px;letter-spacing:.12em;text-transform:uppercase;
  color:var(--mute);margin:2px 0 14px 46px}

/* ---- callouts ---- */
.pr-flag{background:var(--red-soft);border-left:2pt solid var(--red);
  padding:12px 15px;margin:18px 0 4px;font-size:13px;line-height:1.55;color:var(--ink)}
.pr-note{background:var(--accent-soft);border-left:2pt solid var(--accent);
  padding:12px 15px;margin:22px 0 0 46px;font-size:13px;line-height:1.55;color:var(--ink)}
.pr-flag strong,.pr-note strong{font-weight:650}
.pr-disclaimer{margin:26px 0 0 46px;padding-top:13px;border-top:.75pt solid var(--hair);
  font-family:var(--mono);font-size:8.5px;line-height:1.7;letter-spacing:.07em;
  text-transform:uppercase;color:var(--mute)}

@media (prefers-reduced-motion:reduce){
  .pr-panel,#practice-drawer,.pr-progress-fill{transition:none}
}
@media (max-width:680px){
  .pr-panel{width:100vw}
  .pr-head,.pr-tabs,.pr-controls,.pr-body{padding-left:18px;padding-right:18px}
  .pr-progress{margin-left:18px;margin-right:18px}
  .pr-head h2{font-size:25px}
  .pr-note,.pr-disclaimer{margin-left:46px}
  .pr-controls{flex-wrap:wrap;gap:11px}
  .pr-clock{margin-left:0;width:100%;justify-content:space-between}
}
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
    <div class="pr-tabs" id="pr-tabs" role="tablist" aria-label="Differentials"></div>
    <div class="pr-controls">
      <div class="pr-seg" role="group" aria-label="Practice mode">
        <button class="pr-mode" type="button" data-mode="hx" aria-pressed="true">2 min history</button>
        <button class="pr-mode" type="button" data-mode="ex" aria-pressed="false">3 min exam</button>
      </div>
      <div class="pr-sides on" id="pr-sides" role="group" aria-label="Whose side to show">
        <button class="pr-side" type="button" data-side="dr" aria-pressed="true">Doctor</button>
        <button class="pr-side" type="button" data-side="pt" aria-pressed="false">Patient roleplay</button>
      </div>
      <div class="pr-clock">
        <div class="pr-timer" id="pr-timer" role="timer" aria-live="off">2:00</div>
        <button class="pr-timer-btn" type="button" id="pr-timer-btn">Start</button>
      </div>
    </div>
    <div class="pr-progress" id="pr-progress"><div class="pr-progress-fill" id="pr-fill"></div></div>
    <div class="pr-body" id="pr-body"></div>
  </div>
</div>
"""

PRACTICE_JS = """
<script>
(function(){
  var DATA = JSON.parse(document.getElementById('practice-data').textContent);
  var drawer  = document.getElementById('practice-drawer');
  var tabsEl  = document.getElementById('pr-tabs');
  var bodyEl  = document.getElementById('pr-body');
  var timerEl = document.getElementById('pr-timer');
  var timerBtn= document.getElementById('pr-timer-btn');
  var progEl  = document.getElementById('pr-progress');
  var fillEl  = document.getElementById('pr-fill');

  var sidesEl = document.getElementById('pr-sides');

  var state = {caseNo:null, tab:0, mode:'hx', side:'dr'};
  var tick=null, elapsed=0, lastFocus=null;

  var GROUP_ORDER = [
    {key:'general',       label:'This presentation'},
    {key:'must-not-miss', label:'Must not miss', danger:true},
    {key:'other',         label:'Other differentials'}
  ];

  function esc(s){return String(s).replace(/[&<>"]/g,function(ch){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[ch];});}

  function fmt(s){var m=Math.floor(Math.abs(s)/60), r=Math.abs(s)%60;
    return (s<0?'-':'')+m+':'+(r<10?'0':'')+r;}

  function limit(){return state.mode==='hx'?120:180;}
  function blocks(){return DATA[state.caseNo].tabs[state.tab][state.mode];}

  /* ---- timer ---- */
  function stopTimer(){ if(tick){clearInterval(tick); tick=null;} }
  function resetTimer(){
    stopTimer(); elapsed=0;
    timerEl.textContent=fmt(limit());
    timerEl.classList.remove('over'); progEl.classList.remove('over');
    fillEl.style.transition='none'; fillEl.style.width='0%';
    void fillEl.offsetWidth; fillEl.style.transition='';
    timerBtn.textContent='Start';
    paintProgress();
  }
  function toggleTimer(){
    if(tick){stopTimer(); timerBtn.textContent='Resume'; return;}
    timerBtn.textContent='Pause';
    tick=setInterval(function(){ elapsed++; paintProgress(); },1000);
  }
  function paintProgress(){
    var lim=limit(), left=lim-elapsed;
    timerEl.textContent=fmt(left);
    var over = left<0;
    timerEl.classList.toggle('over', over);
    progEl.classList.toggle('over', over);
    fillEl.style.width = Math.min(100, (elapsed/lim)*100)+'%';
    markLive();
  }
  /* Highlight the block you should be in right now. */
  function markLive(){
    var bs=blocks();
    [].forEach.call(bodyEl.querySelectorAll('.pr-block'), function(el,i){
      var b=bs[i]; if(!b) return;
      var live = tick!==null || elapsed>0;
      el.classList.toggle('live', live && elapsed>=b.s && elapsed<b.e);
      el.classList.toggle('done', live && elapsed>=b.e);
    });
  }

  /* ---- render ---- */
  function renderTabs(c){
    var html='';
    GROUP_ORDER.forEach(function(g){
      var members=[];
      c.tabs.forEach(function(t,i){ if(t.group===g.key) members.push({t:t,i:i}); });
      if(!members.length) return;
      html+='<div class="pr-group"><div class="pr-group-label'+(g.danger?' danger':'')+'">'
          + esc(g.label)+' <span aria-hidden="true">&middot; '+members.length+'</span></div>'
          + '<div class="pr-group-row">';
      members.forEach(function(m){
        html+='<button type="button" role="tab" class="pr-tab '+m.t.group
            + '" data-i="'+m.i+'" aria-selected="'+(m.i===state.tab)+'">'
            + esc(m.t.label)+'</button>';
      });
      html+='</div></div>';
    });
    tabsEl.innerHTML=html;
  }

  function renderTicks(){
    [].forEach.call(progEl.querySelectorAll('.pr-tickmark'), function(n){n.remove();});
    var lim=limit();
    blocks().slice(1).forEach(function(b){
      var d=document.createElement('div');
      d.className='pr-tickmark'; d.style.left=(b.s/lim*100)+'%';
      progEl.appendChild(d);
    });
  }

  function render(){
    var c = DATA[state.caseNo]; if(!c) return;
    document.getElementById('pr-kicker').textContent = 'Case '+c.number+' \\u2014 practice';
    document.getElementById('pr-title').textContent  = c.title;
    document.getElementById('pr-sub').textContent    = c.system;

    renderTabs(c);
    [].forEach.call(document.querySelectorAll('.pr-mode'), function(m){
      m.setAttribute('aria-pressed', m.dataset.mode===state.mode ? 'true':'false');
    });

    /* The doctor/patient switch only applies to the history. */
    sidesEl.classList.toggle('on', state.mode==='hx');
    var roleplay = state.mode==='hx' && state.side==='pt';
    [].forEach.call(document.querySelectorAll('.pr-side'), function(s){
      s.setAttribute('aria-pressed', s.dataset.side===state.side ? 'true':'false');
    });

    var tab=c.tabs[state.tab], out='';
    if(state.mode==='hx' && tab.group!=='general'){
      out+='<div class="pr-flag"><strong>'+(roleplay?'The case you are playing:':'Your task:')+'</strong> '
        + (roleplay
            ? 'you have '+esc(tab.label.toLowerCase())+', presenting as '
              +esc(c.title.toLowerCase())+'. Do not name it, and do not volunteer the '
              +'discriminating details unless you are asked for them.'
            : 'take this history to confirm or exclude '+esc(tab.label.toLowerCase())
              +' as the cause of '+esc(c.title.toLowerCase())+'.')
        + '</div>';
    }
    if(roleplay){
      out+='<div class="pr-hint">Hover or tap any line to reveal the question that should elicit it</div>';
    }

    tab[state.mode].forEach(function(b){
      out+='<div class="pr-block"><span class="pr-dot"></span><span class="pr-num">'+esc(b.n)+'</span>'
        + '<div class="pr-block-head"><h3>'+esc(b.h)+'</h3>'
        + '<span class="pr-time">'+esc(b.t)+'</span></div>';
      if(roleplay){
        /* Doctor-only technique lines have no patient counterpart - skip them. */
        var acted = b.items.filter(function(it){ return it.p; });
        if(!acted.length){
          out+='<div class="pr-hint" style="margin-left:0">Nothing for the patient to do in '
            + 'this block - it is the doctor\\'s technique.</div>';
        }
        out+='<ul class="pr-pair">';
        acted.forEach(function(it){
          out+='<li><span class="pr-pt" tabindex="0">'
            + (it.r ? '<span class="pr-rule'+(/opening|play it/i.test(it.r)?' free':'')+'">'
                      +esc(it.r)+'</span>' : '')
            + '<span class="pr-say">'+esc(it.p)+'</span>'
            + '<span class="pr-dr">'
            + '<span class="pr-dr-label">Doctor, to elicit this</span>'
            + '<span class="pr-dr-text">'+esc(it.q || it.d)+'</span>'
            + '</span></span></li>';
        });
        out+='</ul>';
      } else {
        out+='<ul>';
        b.items.forEach(function(it){
          out+='<li>'+esc(typeof it==='string' ? it : it.d)+'</li>';
        });
        out+='</ul>';
      }
      out+='</div>';
    });
    if(state.mode==='hx' && tab.note){
      out+='<div class="pr-note"><strong>First management priority for this presentation:</strong> '
        + esc(tab.note)+'</div>';
    }
    out+='<div class="pr-disclaimer">Rehearsal aid built from this handbook. Confirm dosing and '
       + 'thresholds against current local guidelines before clinical use.</div>';
    bodyEl.innerHTML=out; bodyEl.scrollTop=0;
    renderTicks(); markLive();
  }

  /* ---- open / close ---- */
  function open(caseNo){
    if(!DATA[caseNo]) return;
    lastFocus=document.activeElement;
    state.caseNo=caseNo; state.tab=0; state.mode='hx';
    drawer.dataset.open='1';
    document.documentElement.style.overflow='hidden';
    render(); resetTimer();
    document.querySelector('.pr-close').focus();
  }
  function close(){
    drawer.removeAttribute('data-open'); stopTimer();
    document.documentElement.style.overflow='';
    if(lastFocus && lastFocus.focus) lastFocus.focus();
  }

  document.addEventListener('click', function(e){
    var t=e.target.closest('.practice-toggle');
    if(t){ e.preventDefault(); open(t.dataset.case); return; }
    if(e.target.closest('.pr-close')){ close(); return; }
    if(e.target===drawer){ close(); return; }
    var tab=e.target.closest('.pr-tab');
    if(tab){ state.tab=+tab.dataset.i; render(); resetTimer(); return; }
    var side=e.target.closest('.pr-side');
    if(side && side.dataset.side!==state.side){ state.side=side.dataset.side; render(); return; }
    var m=e.target.closest('.pr-mode');
    if(m && m.dataset.mode!==state.mode){ state.mode=m.dataset.mode; render(); resetTimer(); }
  });
  timerBtn.addEventListener('click', toggleTimer);
  document.addEventListener('keydown', function(e){
    if(!drawer.dataset.open) return;
    if(e.key==='Escape'){ close(); return; }
    if(e.key===' ' && !e.target.closest('button')){ e.preventDefault(); toggleTimer(); }
  });
})();
</script>
"""
