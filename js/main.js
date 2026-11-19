/* Core UI behaviours: tabs, accordion, back-to-top, anchor offset, hash-linked tabs. */
(function () {
  "use strict";

  /* ---------- Tabs (WAI-ARIA tabs pattern) ---------- */
  function initTabs(root) {
    var tabs = [].slice.call(root.querySelectorAll('[role="tab"]'));
    if (!tabs.length) return;
    function select(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute("aria-selected", on ? "true" : "false");
        t.tabIndex = on ? 0 : -1;
        var p = document.getElementById(t.getAttribute("aria-controls"));
        if (p) p.hidden = !on;
      });
      if (focus) tab.focus();
      if (tab.scrollIntoView && root.querySelector('[role="tablist"]').scrollWidth > root.clientWidth) {
        try { tab.scrollIntoView({ block: "nearest", inline: "center" }); } catch (e) {}
      }
    }
    tabs.forEach(function (tab, i) {
      tab.addEventListener("click", function () { select(tab, false); });
      tab.addEventListener("keydown", function (e) {
        var vertical = root.querySelector('[role="tablist"]').getAttribute("aria-orientation") === "vertical";
        var next = vertical ? "ArrowDown" : "ArrowRight", prev = vertical ? "ArrowUp" : "ArrowLeft", n = null;
        if (e.key === next || (!vertical && e.key === "ArrowDown")) n = tabs[(i + 1) % tabs.length];
        else if (e.key === prev || (!vertical && e.key === "ArrowUp")) n = tabs[(i - 1 + tabs.length) % tabs.length];
        else if (e.key === "Home") n = tabs[0];
        else if (e.key === "End") n = tabs[tabs.length - 1];
        if (n) { e.preventDefault(); select(n, true); }
      });
    });
    // Deep link: pages/industries.html#healthcare selects that tab
    if (root.hasAttribute("data-hash-tabs") && location.hash.length > 1) {
      var id = location.hash.slice(1);
      var match = tabs.filter(function (t) { return t.id.slice(-id.length - 3) === "-t-" + id; })[0];
      if (match) select(match, false);
    }
  }
  document.querySelectorAll("[data-tabs]").forEach(initTabs);

  /* ---------- Accordion (one panel open at a time) ---------- */
  document.querySelectorAll("[data-accordion]").forEach(function (acc) {
    var btns = [].slice.call(acc.querySelectorAll(".acc-btn"));
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        var open = b.getAttribute("aria-expanded") === "true";
        btns.forEach(function (o) {
          o.setAttribute("aria-expanded", "false");
          document.getElementById(o.getAttribute("aria-controls")).hidden = true;
        });
        if (!open) {
          b.setAttribute("aria-expanded", "true");
          document.getElementById(b.getAttribute("aria-controls")).hidden = false;
        }
      });
    });
  });

  /* ---------- Back to top ---------- */
  var top = document.getElementById("to-top");
  if (top) {
    var ticking = false;
    var update = function () { top.hidden = window.scrollY < 700; ticking = false; };
    window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    top.addEventListener("click", function () {
      var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" });
      var skip = document.querySelector(".skip-link"); if (skip) skip.focus({ preventScroll: true });
    });
    update();
  }

  /* ---------- In-page anchors: move focus to the target for keyboard/screen-reader users ---------- */
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a || a.getAttribute("href") === "#") return;
    var t = document.getElementById(a.getAttribute("href").slice(1));
    if (t) { if (!t.hasAttribute("tabindex")) t.setAttribute("tabindex", "-1"); setTimeout(function () { t.focus({ preventScroll: true }); }, 400); }
  });
})();
