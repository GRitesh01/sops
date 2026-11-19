/* =========================================================
   Cursor system (fine pointers only, disabled for reduced motion)
   - Dot + lagging ring (blend-mode inverts over any background)
   - Contextual states: link (ring fills), text (ring shrinks), label bubble from data-cursor
   - Comet trail on a canvas, click ripples
   Touch devices and prefers-reduced-motion users keep the native cursor.
   ========================================================= */
(function () {
  "use strict";
  var fine = window.matchMedia("(hover: hover) and (pointer: fine)");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (!fine.matches || reduce.matches) return;

  var root = document.documentElement;
  function mk(cls, html) { var d = document.createElement("div"); d.className = cls; d.innerHTML = html || "<i></i>"; d.setAttribute("aria-hidden", "true"); document.body.appendChild(d); return d; }
  var dot = mk("cur-dot"), ring = mk("cur-ring"), lab = mk("cur-label", "<i></i>");
  var labText = lab.firstChild;
  var cv = document.createElement("canvas"); cv.className = "cur-trail"; cv.setAttribute("aria-hidden", "true"); document.body.appendChild(cv);
  var ctx = cv.getContext("2d"), dpr = Math.min(window.devicePixelRatio || 1, 2);
  function size() { cv.width = innerWidth * dpr; cv.height = innerHeight * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); }
  size(); window.addEventListener("resize", size);

  var mx = innerWidth / 2, my = innerHeight / 2, rx = mx, ry = my, lx = mx, ly = my, seen = false, raf = null;
  var pts = [], LIFE = 420;
  dot.classList.add("is-hidden"); ring.classList.add("is-hidden");

  var INTERACTIVE = "a,button,[role=button],select,label,summary,.bnode,.stage,.tab";
  function setState(t) {
    var nat = t.closest && t.closest("input,textarea");
    var cur = t.closest && t.closest("[data-cursor]");
    var link = t.closest && t.closest(INTERACTIVE);
    var text = t.closest && t.closest("h1,h2,.statement-text,.foot-word");
    ring.classList.toggle("is-hidden", !!nat); dot.classList.toggle("is-hidden", !!nat);
    var l = !nat && cur ? cur.getAttribute("data-cursor") : "";
    if (l) labText.textContent = l;
    lab.classList.toggle("on", !!l); ring.classList.toggle("is-label", !!l);
    ring.classList.toggle("is-link", !l && !!link && !nat);
    ring.classList.toggle("is-text", !l && !link && !!text && !nat);
  }
  window.addEventListener("pointermove", function (e) {
    if (e.pointerType && e.pointerType !== "mouse" && e.pointerType !== "pen") return;
    mx = e.clientX; my = e.clientY;
    if (!seen) { seen = true; rx = lx = mx; ry = ly = my; root.classList.add("has-cursor"); dot.classList.remove("is-hidden"); ring.classList.remove("is-hidden"); }
    setState(e.target);
    pts.push({ x: mx, y: my, t: performance.now() });
  }, { passive: true });
  document.addEventListener("pointerdown", function (e) {
    if (e.pointerType && e.pointerType !== "mouse") return;
    ring.classList.add("is-down");
    var r = document.createElement("div"); r.className = "cur-ripple"; r.style.left = e.clientX + "px"; r.style.top = e.clientY + "px";
    document.body.appendChild(r); setTimeout(function () { r.remove(); }, 850);
  });
  document.addEventListener("pointerup", function () { ring.classList.remove("is-down"); });
  document.documentElement.addEventListener("mouseleave", function () { dot.classList.add("is-hidden"); ring.classList.add("is-hidden"); lab.classList.remove("on"); });
  document.documentElement.addEventListener("mouseenter", function () { if (seen) { dot.classList.remove("is-hidden"); ring.classList.remove("is-hidden"); } });

  function frame(now) {
    rx += (mx - rx) * 0.17; ry += (my - ry) * 0.17; lx += (mx - lx) * 0.24; ly += (my - ly) * 0.24;
    dot.style.transform = "translate3d(" + mx + "px," + my + "px,0)";
    ring.style.transform = "translate3d(" + rx.toFixed(1) + "px," + ry.toFixed(1) + "px,0)";
    lab.style.transform = "translate3d(" + lx.toFixed(1) + "px," + ly.toFixed(1) + "px,0)";
    // comet trail
    ctx.clearRect(0, 0, innerWidth, innerHeight);
    while (pts.length && now - pts[0].t > LIFE) pts.shift();
    if (pts.length > 1) {
      ctx.lineCap = "round"; ctx.lineJoin = "round";
      for (var i = 1; i < pts.length; i++) {
        var a = pts[i - 1], b = pts[i], age = 1 - (now - b.t) / LIFE;
        ctx.strokeStyle = "rgba(255,255,255," + (age * 0.9).toFixed(3) + ")"; ctx.lineWidth = 1 + age * 5;
        ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
      }
    }
    raf = requestAnimationFrame(frame);
  }
  raf = requestAnimationFrame(frame);
  document.addEventListener("visibilitychange", function () {
    if (document.hidden) { cancelAnimationFrame(raf); raf = null; } else if (!raf) raf = requestAnimationFrame(frame);
  });
})();
