/* Motion layer: scroll progress, word reveals, tilt cards, magnetic buttons,
   spotlight text, cursor-reactive floats, marquee scroll-velocity.
   Pointer effects are off for touch devices and reduced-motion users. */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  var fine = window.matchMedia("(hover: hover) and (pointer: fine)");
  var pointerFx = fine.matches && !reduce.matches;

  /* ---------- scroll progress bar ---------- */
  var bar = document.getElementById("progress"), tick = false;
  function prog() { var h = document.documentElement.scrollHeight - innerHeight; document.documentElement.style.setProperty("--p", h > 0 ? Math.min(1, scrollY / h).toFixed(4) : 0); tick = false; }
  window.addEventListener("scroll", function () { if (!tick) { tick = true; requestAnimationFrame(prog); } }, { passive: true }); prog();

  /* ---------- word-by-word headline reveal ---------- */
  if (!reduce.matches) {
    document.querySelectorAll("[data-split]").forEach(function (el) {
      var i = 0;
      (function walk(node) {
        [].slice.call(node.childNodes).forEach(function (n) {
          if (n.nodeType === 3) {
            var frag = document.createDocumentFragment();
            n.textContent.split(/(\s+)/).forEach(function (part) {
              if (!part) return;
              if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(" ")); return; }
              var w = document.createElement("span"); w.className = "word"; var s = document.createElement("span"); s.style.setProperty("--w", i++); s.textContent = part; w.appendChild(s); frag.appendChild(w);
            });
            node.replaceChild(frag, n);
          } else if (n.nodeType === 1) walk(n);
        });
      })(el);
    });
  }

  /* ---------- reveal on scroll ---------- */
  var items = [].slice.call(document.querySelectorAll(".reveal, [data-split]"));
  if (!("IntersectionObserver" in window) || reduce.matches) items.forEach(function (el) { el.classList.add("is-visible"); });
  else {
    var io = new IntersectionObserver(function (en) { en.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("is-visible"); io.unobserve(e.target); } }); }, { rootMargin: "0px 0px -8% 0px", threshold: 0.1 });
    items.forEach(function (el) { io.observe(el); });
  }

  /* ---------- marquee speeds up with scroll velocity ---------- */
  var mqs = [].slice.call(document.querySelectorAll("[data-marquee]"));
  if (mqs.length && !reduce.matches && "getAnimations" in document.documentElement) {
    var lastY = scrollY, rate = 1, target = 1;
    window.addEventListener("scroll", function () { var v = Math.abs(scrollY - lastY); lastY = scrollY; target = 1 + Math.min(v / 12, 5); }, { passive: true });
    (function loop() {
      rate += (target - rate) * 0.08; target += (1 - target) * 0.05;
      mqs.forEach(function (m) { m.querySelectorAll(".mq-track").forEach(function (t) { t.getAnimations().forEach(function (a) { a.playbackRate = rate; }); }); });
      requestAnimationFrame(loop);
    })();
  }

  if (!pointerFx) return;

  /* ---------- 3D tilt + spotlight on cards ---------- */
  document.querySelectorAll("[data-tilt]").forEach(function (el) {
    var max = 5;
    el.addEventListener("pointermove", function (e) {
      var r = el.getBoundingClientRect(), px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
      el.style.transition = "transform .12s ease-out, box-shadow .35s, background .3s";
      el.style.transform = "perspective(900px) rotateX(" + ((0.5 - py) * max * 2).toFixed(2) + "deg) rotateY(" + ((px - 0.5) * max * 2).toFixed(2) + "deg) translateZ(0)";
      el.style.setProperty("--mx", (e.clientX - r.left) + "px"); el.style.setProperty("--my", (e.clientY - r.top) + "px");
    });
    el.addEventListener("pointerleave", function () { el.style.transition = "transform .7s cubic-bezier(.2,.7,.2,1), box-shadow .35s, background .3s"; el.style.transform = ""; });
  });

  /* ---------- magnetic buttons ---------- */
  var mags = [].slice.call(document.querySelectorAll("[data-magnetic]")).map(function (el) { return { el: el, x: 0, y: 0, tx: 0, ty: 0 }; });
  var running = false;
  function step() {
    var moving = false;
    mags.forEach(function (m) {
      m.x += (m.tx - m.x) * 0.18; m.y += (m.ty - m.y) * 0.18;
      if (Math.abs(m.tx - m.x) > 0.05 || Math.abs(m.ty - m.y) > 0.05) moving = true; else { m.x = m.tx; m.y = m.ty; }
      m.el.style.transform = (m.x || m.y) ? "translate3d(" + m.x.toFixed(2) + "px," + m.y.toFixed(2) + "px,0)" : "";
    });
    if (moving) requestAnimationFrame(step); else running = false;
  }
  window.addEventListener("pointermove", function (e) {
    mags.forEach(function (m) {
      var r = m.el.getBoundingClientRect(); if (r.bottom < 0 || r.top > innerHeight) return;
      var cx = r.left + r.width / 2, cy = r.top + r.height / 2, dx = e.clientX - cx, dy = e.clientY - cy, d = Math.hypot(dx, dy), reach = Math.max(r.width, r.height) * 0.9 + 30;
      if (d < reach) { m.tx = dx * 0.28; m.ty = dy * 0.34; } else { m.tx = 0; m.ty = 0; }
    });
    if (!running) { running = true; requestAnimationFrame(step); }
  }, { passive: true });

  /* ---------- spotlight text (cursor-lit overlay) ---------- */
  var spots = [].slice.call(document.querySelectorAll("[data-spotlight]"));
  spots.forEach(function (s) { if (!s.getAttribute("data-text")) s.setAttribute("data-text", s.textContent.trim()); });
  window.addEventListener("pointermove", function (e) {
    spots.forEach(function (s) {
      var r = s.getBoundingClientRect();
      if (r.bottom < -200 || r.top > innerHeight + 200) return;
      s.style.setProperty("--sx", (e.clientX - r.left) + "px"); s.style.setProperty("--sy", (e.clientY - r.top) + "px");
    });
  }, { passive: true });

  /* ---------- cursor-reactive floats ---------- */
  var floats = [].slice.call(document.querySelectorAll("[data-float]"));
  if (floats.length) window.addEventListener("pointermove", function (e) {
    var nx = e.clientX / innerWidth - 0.5, ny = e.clientY / innerHeight - 0.5;
    floats.forEach(function (f) { f.style.transform = "translate3d(" + (-nx * 46).toFixed(1) + "px," + (-ny * 36).toFixed(1) + "px,0)"; });
  }, { passive: true });
})();
