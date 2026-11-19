/* =========================================================
   StrategicOps visualisations
   1. Hero "operations field": a dot grid that bends around the cursor, with an
      orchestrator and agent chips that lean toward it. Click to send signals.
   2. Agent loop: 7 stages with a token that travels the loop.
   3. Mission-control board: draggable agent nodes with live connections and a
      dispatch simulation.
   No mouse effects on touch devices; static under prefers-reduced-motion.
   ========================================================= */
(function () {
  "use strict";
  var TAU = Math.PI * 2;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  var fine = window.matchMedia("(hover: hover) and (pointer: fine)");
  var NS = "http://www.w3.org/2000/svg";
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }

  /* =====================================================
     1. HERO FIELD
     ===================================================== */
  function initHero(canvas) {
    var ctx = canvas.getContext("2d"); if (!ctx) return;
    var W = 0, H = 0, dpr = 1, dots = [], S = 30, raf = null, visible = true, last = 0, time = 0;
    var cur = { x: -999, y: -999, tx: -999, ty: -999, on: false };
    var ripples = [], packets = [], autoT = 0;
    var C = { ink: "12,16,32", cobalt: "36,56,245" };
    var agents = [
      { l: "Research agent", a: -2.45, d: 1.0 }, { l: "Planning agent", a: -1.1, d: 1.0 }, { l: "Data agent", a: 0.2, d: 1.0 },
      { l: "Execution agent", a: 1.3, d: 1.0 }, { l: "Review agent", a: 2.45, d: 1.0 }
    ];
    var hub = { x: 0, y: 0, R: 0 };

    function resize() {
      var r = canvas.getBoundingClientRect(); dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = Math.max(1, r.width); H = Math.max(1, r.height); canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      S = W < 700 ? 34 : 30; dots = [];
      for (var y = S / 2; y < H + S; y += S) for (var x = S / 2; x < W + S; x += S) dots.push({ x: x, y: y });
      var wide = W >= 992;
      hub.x = wide ? W * 0.74 : W * 0.5; hub.y = wide ? H * 0.5 : H * 0.8; hub.R = wide ? Math.min(W * 0.2, H * 0.34) : Math.min(W * 0.34, H * 0.16);
      if (reduce.matches) draw(0);
    }
    function agentPos(a, i, t) {
      var an = a.a + Math.sin(t * 0.0005 + i * 1.7) * 0.07, rr = hub.R * (1 + Math.sin(t * 0.0007 + i) * 0.05);
      var x = hub.x + Math.cos(an) * rr * 1.25, y = hub.y + Math.sin(an) * rr * 0.9;
      if (cur.on) { var dx = cur.x - x, dy = cur.y - y, d = Math.hypot(dx, dy); if (d < 320) { var k = (1 - d / 320) * 26; x += dx / (d || 1) * k; y += dy / (d || 1) * k; } }
      return { x: Math.max(70, Math.min(W - 70, x)), y: Math.max(40, Math.min(H - 40, y)) };
    }
    function roundRect(x, y, w, h, r) { ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r); ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath(); }
    function chip(x, y, text, fill, color) {
      ctx.font = "600 13px 'Bricolage Grotesque','DM Sans',system-ui,sans-serif"; var w = ctx.measureText(text).width + 30, h = 34;
      ctx.fillStyle = "rgb(" + C.ink + ")"; roundRect(x - w / 2 + 3, y - h / 2 + 3, w, h, 17); ctx.fill();
      ctx.fillStyle = fill; roundRect(x - w / 2, y - h / 2, w, h, 17); ctx.fill(); ctx.lineWidth = 1.5; ctx.strokeStyle = "rgb(" + C.ink + ")"; ctx.stroke();
      ctx.fillStyle = color; ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText(text, x, y + 0.5);
    }
    function signal() {
      agents.forEach(function (a, i) { packets.push({ i: i, t: -i * 0.08, v: 0.0011 + Math.random() * 0.0004 }); });
    }
    function draw(t) {
      ctx.clearRect(0, 0, W, H);
      // ripples
      for (var q = ripples.length - 1; q >= 0; q--) if (t - ripples[q].t0 > 1800) ripples.splice(q, 1);
      // dots
      var R = 150;
      for (var i = 0; i < dots.length; i++) {
        var d = dots[i], x = d.x, y = d.y, size = 1.5, hot = 0;
        if (cur.on) {
          var dx = x - cur.x, dy = y - cur.y, dd = Math.hypot(dx, dy);
          if (dd < R) { var f = 1 - dd / R, e = f * f; x += dx / (dd || 1) * e * 22; y += dy / (dd || 1) * e * 22; size += e * 3.4; hot = Math.max(hot, e); }
        }
        for (var k = 0; k < ripples.length; k++) {
          var rp = ripples[k], rr = (t - rp.t0) * 0.55, rdx = d.x - rp.x, rdy = d.y - rp.y, rd = Math.hypot(rdx, rdy), df = rd - rr;
          if (Math.abs(df) < 55) { var w = Math.cos((df / 55) * Math.PI / 2), fade = 1 - (t - rp.t0) / 1800; x += rdx / (rd || 1) * w * 14 * fade; y += rdy / (rd || 1) * w * 14 * fade; size += w * 2.2 * fade; hot = Math.max(hot, w * fade); }
        }
        ctx.fillStyle = hot > 0.02 ? "rgba(" + C.cobalt + "," + (0.35 + hot * 0.65).toFixed(2) + ")" : "rgba(" + C.ink + ",.2)";
        ctx.beginPath(); ctx.arc(x, y, size, 0, TAU); ctx.fill();
      }
      // links + agents
      var ap = agents.map(function (a, i) { return agentPos(a, i, t); });
      ctx.lineWidth = 2;
      ap.forEach(function (p, i) {
        var near = cur.on && Math.hypot(cur.x - p.x, cur.y - p.y) < 90;
        ctx.strokeStyle = near ? "rgb(" + C.cobalt + ")" : "rgba(" + C.ink + ",.35)"; ctx.setLineDash(near ? [] : [6, 6]);
        ctx.beginPath(); ctx.moveTo(hub.x, hub.y); ctx.quadraticCurveTo((hub.x + p.x) / 2, (hub.y + p.y) / 2 - 24, p.x, p.y); ctx.stroke();
      });
      ctx.setLineDash([]);
      // packets
      for (var n = packets.length - 1; n >= 0; n--) {
        var pk = packets[n]; if (pk.t >= 1) { packets.splice(n, 1); continue; }
        if (pk.t > 0) {
          var p2 = ap[pk.i], tt = pk.t, x1 = hub.x, y1 = hub.y, cx = (hub.x + p2.x) / 2, cy = (hub.y + p2.y) / 2 - 24;
          var bx = (1 - tt) * (1 - tt) * x1 + 2 * (1 - tt) * tt * cx + tt * tt * p2.x, by = (1 - tt) * (1 - tt) * y1 + 2 * (1 - tt) * tt * cy + tt * tt * p2.y;
          ctx.fillStyle = "#ffd43b"; ctx.strokeStyle = "rgb(" + C.ink + ")"; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.arc(bx, by, 6, 0, TAU); ctx.fill(); ctx.stroke();
        }
      }
      ap.forEach(function (p, i) { chip(p.x, p.y, agents[i].l, "#ffffff", "rgb(" + C.ink + ")"); });
      // hub
      var pulse = reduce.matches ? 0 : (Math.sin(t * 0.003) + 1) / 2;
      ctx.strokeStyle = "rgba(" + C.cobalt + ",.35)"; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(hub.x, hub.y, 54 + pulse * 8, 0, TAU); ctx.stroke();
      chip(hub.x, hub.y, "Orchestrator", "rgb(" + C.cobalt + ")", "#ffffff");
    }
    function frame(ts) {
      if (!last) last = ts; var dt = Math.min(ts - last, 50); last = ts; time += dt;
      cur.x += (cur.tx - cur.x) * 0.2; cur.y += (cur.ty - cur.y) * 0.2;
      packets.forEach(function (p) { p.t += p.v * dt; });
      autoT += dt; if (autoT > 5200) { autoT = 0; ripples.push({ x: hub.x, y: hub.y, t0: time }); signal(); }
      draw(time); raf = requestAnimationFrame(frame);
    }
    function start() { if (raf || reduce.matches || !visible || document.hidden) return; last = 0; raf = requestAnimationFrame(frame); }
    function stop() { if (raf) { cancelAnimationFrame(raf); raf = null; } }
    resize(); if (reduce.matches) draw(0);
    var rt; window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(resize, 120); });
    if (fine.matches && !reduce.matches) {
      var hero = canvas.parentElement;
      hero.addEventListener("pointermove", function (e) {
        var r = canvas.getBoundingClientRect(); cur.tx = e.clientX - r.left; cur.ty = e.clientY - r.top; if (!cur.on) { cur.on = true; cur.x = cur.tx; cur.y = cur.ty; }
      }, { passive: true });
      hero.addEventListener("pointerleave", function () { cur.on = false; });
      hero.addEventListener("pointerdown", function (e) {
        if (e.target.closest("a,button")) return;
        var r = canvas.getBoundingClientRect(); ripples.push({ x: e.clientX - r.left, y: e.clientY - r.top, t0: time }); signal();
      });
    }
    if ("IntersectionObserver" in window) new IntersectionObserver(function (e) { visible = e[0].isIntersecting; visible ? start() : stop(); }).observe(canvas);
    document.addEventListener("visibilitychange", function () { document.hidden ? stop() : start(); });
    var onRM = function () { if (reduce.matches) { stop(); draw(0); } else start(); };
    if (reduce.addEventListener) reduce.addEventListener("change", onRM);
    start();
  }

  /* =====================================================
     2. AGENT LOOP
     ===================================================== */
  var ARCH = [
    { s: "Perception", t: "Perception and input", d: "The agent receives a task from a person, a system event, a schedule or an API call, and turns it into something it can work with.", ex: "Task: \"Summarise delayed supplier shipments and propose next steps.\"" },
    { s: "Context", t: "Context understanding", d: "It interprets the request against business context: who is asking, which policies apply and what permissions are in force.", ex: "Identifies the requester's role, the suppliers involved and the escalation policy." },
    { s: "Reasoning", t: "Reasoning and planning", d: "It breaks the goal into steps, picks an approach and decides what to do next based on what it finds.", ex: "Plan: pull shipment data, compare with purchase orders, draft summary, flag items for approval." },
    { s: "Memory", t: "Memory and knowledge", d: "It retrieves relevant documents, history and facts from governed knowledge sources and keeps working memory for the task.", ex: "Retrieves supplier agreements and earlier delay notes the requester may see." },
    { s: "Tools", t: "Tool calling", d: "It invokes approved tools such as APIs, databases, search and internal systems, within defined permission boundaries.", ex: "Calls a read-only logistics API and an ERP query tool; every call is logged." },
    { s: "Execution", t: "Task execution", d: "It does the work: drafting, updating records, sending messages. Higher-risk actions pause for human approval where configured.", ex: "Drafts supplier emails and waits for a person to approve before anything is sent." },
    { s: "Evaluation", t: "Evaluation and feedback", d: "It checks outputs against criteria, records a full trace and feeds outcomes back so the system can be reviewed and improved.", ex: "Validates figures against source data, logs the trace and records the reviewer's decision." }
  ];

  function initLoop(root) {
    var stages = ARCH.map(function (a, i) {
      return '<li><button type="button" class="stage" data-i="' + i + '" aria-pressed="false" data-cursor="Select"><span class="stage-n">0' + (i + 1) + '</span><span>' + esc(a.s) + "</span></button></li>";
    }).join("");
    root.innerHTML = '<div class="loop-top"><button type="button" class="viz-btn" data-play>Play sample task</button><span class="loop-hint">The outcome of stage 07 feeds back into stage 01.</span></div>' +
      '<ol class="loop-track">' + stages + '<span class="loop-token" aria-hidden="true"></span></ol><div class="loop-detail tile" aria-live="polite"></div>';
    var btns = [].slice.call(root.querySelectorAll(".stage")), token = root.querySelector(".loop-token"), track = root.querySelector(".loop-track"),
      detail = root.querySelector(".loop-detail"), play = root.querySelector("[data-play]"), timer = null;
    function show(i, scroll) {
      var a = ARCH[i], b = btns[i];
      btns.forEach(function (x, k) { x.setAttribute("aria-pressed", k === i ? "true" : "false"); });
      token.style.left = (b.parentNode.offsetLeft + b.parentNode.offsetWidth / 2) + "px";
      if (scroll && track.scrollWidth > track.clientWidth) track.scrollTo({ left: Math.max(0, b.parentNode.offsetLeft - 40), behavior: reduce.matches ? "auto" : "smooth" });
      detail.innerHTML = '<div class="ld-n">0' + (i + 1) + '</div><div><h3>' + esc(a.t) + "</h3><p>" + esc(a.d) + '</p><p class="ex">' + esc(a.ex) + "</p>" + (i === 6 ? "<p>The loop closes here: feedback shapes the next task and future improvements.</p>" : "") + "</div>";
    }
    function stop() { if (timer) { clearInterval(timer); timer = null; } play.textContent = "Play sample task"; }
    play.addEventListener("click", function () {
      if (timer) { stop(); return; }
      var i = 0; show(0, true); play.textContent = "Pause";
      timer = setInterval(function () { i++; if (i > 6) { stop(); return; } show(i, true); }, 2400);
    });
    btns.forEach(function (b) { b.addEventListener("click", function () { stop(); show(+b.getAttribute("data-i"), false); }); });
    show(0, false); window.addEventListener("resize", function () { var k = btns.findIndex(function (x) { return x.getAttribute("aria-pressed") === "true"; }); show(Math.max(0, k), false); });
  }

  /* =====================================================
     3. MISSION-CONTROL BOARD
     ===================================================== */
  var NODES = {
    request: { x: 50, y: 7, t: "User request", s: "goal arrives", d: "A goal arrives from a person, a system event or an API call, for example \"Prepare a competitor briefing and update the CRM.\"" },
    orch: { x: 50, y: 24, t: "AI orchestrator", s: "plans, delegates, tracks", k: "k-orch", d: "Interprets the goal, breaks it into tasks, delegates to the right agents, tracks progress and decides when the work is complete." },
    research: { x: 14, y: 45, t: "Research agent", s: "gathers information", d: "Searches approved sources and internal knowledge, extracts relevant evidence and records where it came from." },
    planning: { x: 38, y: 45, t: "Planning agent", s: "sequences the work", d: "Turns findings and constraints into a step-by-step plan, resolves dependencies and proposes alternatives." },
    data: { x: 62, y: 45, t: "Data agent", s: "queries and analyses", d: "Reads from databases and business systems through governed tools and prepares structured data for the other agents." },
    exec: { x: 86, y: 45, t: "Execution agent", s: "acts through tools", d: "Carries out approved actions such as updating records or drafting communications, using scoped permissions." },
    context: { x: 50, y: 63, t: "Shared context, memory and tool access", s: "role-based and logged", k: "k-ctx", d: "A governed workspace where agents share state and findings. Access is role-based and every read and write is logged." },
    approval: { x: 86, y: 78, t: "Human approval", s: "review, edit, reject", k: "k-human", d: "A person reviews, edits or rejects defined high-impact actions before they run. Which actions need approval is configurable." },
    validation: { x: 50, y: 82, t: "Validation and evaluation", s: "review agent + checks", d: "A review agent and automated checks verify outputs against criteria, sources and policies. Failures loop back for revision or escalate to a person." },
    result: { x: 50, y: 95, t: "Final result", s: "with audit trace", k: "k-orch", d: "The completed output is returned with a trace of the steps, sources and approvals involved." }
  };
  var EDGES = [["request", "orch"], ["orch", "research"], ["orch", "planning"], ["orch", "data"], ["orch", "exec"],
    ["research", "context"], ["planning", "context"], ["data", "context"], ["exec", "context"], ["context", "validation"], ["validation", "result"],
    ["context", "approval"], ["approval", "validation", true]];
  var SIM = [
    { n: ["request"], e: [], log: "User request received." },
    { n: ["orch"], e: ["request>orch"], log: "Orchestrator interprets the goal and plans sub-tasks." },
    { n: ["research", "planning", "data"], e: ["orch>research", "orch>planning", "orch>data"], log: "Research, planning and data agents work in parallel." },
    { n: ["context"], e: ["research>context", "planning>context", "data>context"], log: "Findings are written to shared context and memory." },
    { n: ["exec", "approval"], e: ["orch>exec", "exec>context", "context>approval"], log: "Execution agent proposes actions; the approval gate checks them." },
    { n: ["validation"], e: ["context>validation", "approval>validation"], log: "Validation and evaluation check outputs against criteria." },
    { n: ["result"], e: ["validation>result"], log: "Final result returned with an audit trace." }
  ];

  function initBoard(root) {
    var ids = Object.keys(NODES);
    root.innerHTML = '<div class="board-bar"><button type="button" class="viz-btn" data-run>Dispatch a request</button><button type="button" class="viz-btn alt" data-reset>Reset board</button><ol class="board-log" aria-live="polite"></ol></div>' +
      '<div class="board-surface"></div><div class="board-detail" aria-live="polite"><h3>Select a node</h3><p>Drag nodes to rearrange the system. Select one to read its role, or dispatch a request to watch work move from orchestrator to result.</p></div>';
    var surface = root.querySelector(".board-surface"); surface.className = "board-surface board";
    // board-surface becomes the board element
    var svg = document.createElementNS(NS, "svg"); svg.setAttribute("class", "board-svg"); svg.setAttribute("aria-hidden", "true"); surface.appendChild(svg);
    var gE = document.createElementNS(NS, "g"), gP = document.createElementNS(NS, "g"); svg.appendChild(gE); svg.appendChild(gP);
    var nodes = {}, edges = {}, pos = {};
    ids.forEach(function (id) {
      var n = NODES[id], b = document.createElement("button"); b.type = "button"; b.className = "bnode " + (n.k || ""); b.setAttribute("data-id", id); b.setAttribute("data-cursor", "Drag");
      b.setAttribute("aria-label", n.t + ": select for details. Arrow keys move the node.");
      b.innerHTML = "<b>" + esc(n.t) + "</b><small>" + esc(n.s) + "</small>"; surface.appendChild(b); nodes[id] = b; pos[id] = { x: n.x, y: n.y };
    });
    EDGES.forEach(function (e) {
      var p = document.createElementNS(NS, "path"); p.setAttribute("class", "b-edge" + (e[2] ? " dash" : "")); gE.appendChild(p); edges[e[0] + ">" + e[1]] = { el: p, a: e[0], b: e[1] };
    });
    var log = root.querySelector(".board-log"), detail = root.querySelector(".board-detail"), runBtn = root.querySelector("[data-run]"), timers = [], raf = [];

    function stacked() { return surface.clientWidth < 720; }
    function layout() {
      var st = stacked(); surface.classList.toggle("is-stacked", st);
      ids.forEach(function (id) { nodes[id].setAttribute("data-cursor", st ? "Open" : "Drag"); if (!st) { nodes[id].style.left = pos[id].x + "%"; nodes[id].style.top = pos[id].y + "%"; } else { nodes[id].style.left = nodes[id].style.top = ""; } });
      draw();
    }
    function center(id) { var r = nodes[id], s = surface.getBoundingClientRect(), b = r.getBoundingClientRect(); return { x: b.left - s.left + b.width / 2, y: b.top - s.top + b.height / 2 }; }
    function draw() {
      if (stacked()) return;
      svg.setAttribute("viewBox", "0 0 " + surface.clientWidth + " " + surface.clientHeight);
      Object.keys(edges).forEach(function (k) {
        var e = edges[k], a = center(e.a), b = center(e.b), my = (a.y + b.y) / 2;
        e.d = "M" + a.x.toFixed(1) + " " + a.y.toFixed(1) + " C" + a.x.toFixed(1) + " " + my.toFixed(1) + " " + b.x.toFixed(1) + " " + my.toFixed(1) + " " + b.x.toFixed(1) + " " + b.y.toFixed(1);
        e.el.setAttribute("d", e.d);
      });
    }
    function clear() {
      timers.forEach(clearTimeout); timers = []; raf.forEach(cancelAnimationFrame); raf = []; gP.innerHTML = "";
      ids.forEach(function (id) { nodes[id].classList.remove("is-active"); }); Object.keys(edges).forEach(function (k) { edges[k].el.classList.remove("on"); });
    }
    function packet(key) {
      if (reduce.matches || stacked()) return; var e = edges[key]; if (!e) return;
      var c = document.createElementNS(NS, "circle"); c.setAttribute("r", "7"); c.setAttribute("class", "b-packet"); gP.appendChild(c);
      var len = e.el.getTotalLength(), t0 = performance.now(), dur = 950;
      (function go(now) { var t = Math.min(1, (now - t0) / dur), p = e.el.getPointAtLength(len * t); c.setAttribute("cx", p.x); c.setAttribute("cy", p.y); if (t < 1) raf.push(requestAnimationFrame(go)); else c.remove(); })(t0);
    }
    function select(id) {
      stopRun(); clear(); nodes[id].classList.add("is-active");
      Object.keys(edges).forEach(function (k) { var e = edges[k]; if (e.a === id || e.b === id) e.el.classList.add("on"); });
      detail.innerHTML = "<h3>" + esc(NODES[id].t) + "</h3><p>" + esc(NODES[id].d) + "</p>";
    }
    function stopRun() { timers.forEach(clearTimeout); timers = []; runBtn.textContent = "Dispatch a request"; }
    function run() {
      if (timers.length) { stopRun(); return; }
      clear(); log.innerHTML = ""; runBtn.textContent = "Pause";
      SIM.forEach(function (s, i) {
        timers.push(setTimeout(function () {
          s.n.forEach(function (n) { nodes[n].classList.add("is-active"); }); s.e.forEach(function (k) { if (edges[k]) { edges[k].el.classList.add("on"); packet(k); } });
          [].forEach.call(log.querySelectorAll(".on"), function (l) { l.classList.remove("on"); });
          var li = document.createElement("li"); li.className = "on"; li.textContent = (i + 1) + ". " + s.log; log.appendChild(li);
          detail.innerHTML = "<h3>Step " + (i + 1) + " of " + SIM.length + "</h3><p>" + esc(s.log) + "</p>";
          if (i === SIM.length - 1) { timers = []; runBtn.textContent = "Dispatch again"; }
        }, i * 1500));
      });
    }

    /* drag */
    ids.forEach(function (id) {
      var el = nodes[id], sx, sy, ox, oy, moved, dragging = false;
      el.addEventListener("pointerdown", function (e) {
        if (stacked() || (e.pointerType === "mouse" && e.button !== 0)) return;
        dragging = true; moved = false; el.setPointerCapture(e.pointerId); var s = surface.getBoundingClientRect(), c = center(id); sx = e.clientX; sy = e.clientY; ox = c.x; oy = c.y; el.classList.add("is-drag");
      });
      el.addEventListener("pointermove", function (e) {
        if (!dragging) return; var dx = e.clientX - sx, dy = e.clientY - sy; if (Math.abs(dx) + Math.abs(dy) > 4) moved = true; if (!moved) return;
        var W = surface.clientWidth, H = surface.clientHeight, hw = el.offsetWidth / 2, hh = el.offsetHeight / 2;
        var x = Math.max(hw, Math.min(W - hw, ox + dx)), y = Math.max(hh, Math.min(H - hh, oy + dy));
        pos[id] = { x: x / W * 100, y: y / H * 100 }; el.style.left = pos[id].x + "%"; el.style.top = pos[id].y + "%"; draw();
      });
      function end(e) { if (!dragging) return; dragging = false; el.classList.remove("is-drag"); try { el.releasePointerCapture(e.pointerId); } catch (x) {} if (!moved) select(id); }
      el.addEventListener("pointerup", end); el.addEventListener("pointercancel", end);
      el.addEventListener("click", function (e) { if (e.detail === 0 || stacked()) select(id); });   // keyboard + stacked mode
      el.addEventListener("keydown", function (e) {
        var step = 1.5, k = e.key, dx = 0, dy = 0;
        if (stacked()) return;
        if (k === "ArrowLeft") dx = -step; else if (k === "ArrowRight") dx = step; else if (k === "ArrowUp") dy = -step; else if (k === "ArrowDown") dy = step; else return;
        e.preventDefault(); pos[id] = { x: Math.max(4, Math.min(96, pos[id].x + dx)), y: Math.max(4, Math.min(96, pos[id].y + dy)) };
        el.style.left = pos[id].x + "%"; el.style.top = pos[id].y + "%"; draw();
      });
    });
    runBtn.addEventListener("click", run);
    root.querySelector("[data-reset]").addEventListener("click", function () {
      stopRun(); clear(); log.innerHTML = ""; ids.forEach(function (id) { pos[id] = { x: NODES[id].x, y: NODES[id].y }; });
      layout(); detail.innerHTML = "<h3>Select a node</h3><p>Drag nodes to rearrange the system. Select one to read its role, or dispatch a request to watch work move from orchestrator to result.</p>";
    });
    var rt; window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(layout, 100); });
    layout(); if ("ResizeObserver" in window) new ResizeObserver(draw).observe(surface);
  }

  function boot() {
    var hc = document.querySelector("[data-hero-canvas]"); if (hc) initHero(hc);
    document.querySelectorAll("[data-agent-loop]").forEach(initLoop);
    document.querySelectorAll("[data-agent-board]").forEach(initBoard);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
