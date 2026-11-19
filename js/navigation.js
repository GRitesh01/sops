/* Floating pill header: hide on scroll down / show on scroll up, sliding hover blob,
   full-screen mobile menu, keyboard-accessible dropdowns. */
(function () {
  "use strict";
  var header = document.getElementById("site-header");
  if (!header) return;
  var toggle = header.querySelector(".nav-toggle"), label = header.querySelector(".nt-label");
  var mq = window.matchMedia("(max-width: 991.98px)");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* hide on scroll down, reveal on scroll up */
  var lastY = window.scrollY, ticking = false;
  function onScroll() {
    var y = window.scrollY, d = y - lastY;
    if (!header.classList.contains("menu-open") && !header.contains(document.activeElement) && !header.querySelector(".is-open")) {
      if (y > 360 && d > 6) header.classList.add("is-hidden"); else if (d < -4 || y < 200) header.classList.remove("is-hidden");
    }
    lastY = y; ticking = false;
  }
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  header.addEventListener("focusin", function () { header.classList.remove("is-hidden"); });

  /* sliding hover blob (desktop, pointer devices) */
  var list = header.querySelector(".nav-list"), blob = header.querySelector(".nav-blob");
  function moveBlob(li) {
    if (!blob || mq.matches || reduce.matches) return;
    blob.style.width = li.offsetWidth + "px"; blob.style.transform = "translateX(" + li.offsetLeft + "px)"; blob.classList.add("on");
  }
  if (list && blob) {
    [].forEach.call(list.querySelectorAll(".nav-item"), function (li) {
      li.addEventListener("pointerenter", function () { moveBlob(li); });
      li.addEventListener("focusin", function () { moveBlob(li); });
    });
    list.addEventListener("pointerleave", function () { blob.classList.remove("on"); });
    list.addEventListener("focusout", function (e) { if (!list.contains(e.relatedTarget)) blob.classList.remove("on"); });
  }

  /* mobile menu */
  function setMenu(open) {
    header.classList.toggle("menu-open", open); header.classList.remove("is-hidden");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    if (label) label.textContent = open ? "Close" : "Menu";
    document.documentElement.style.overflow = open ? "hidden" : "";
    if (!open) closeAll();
  }
  toggle.addEventListener("click", function () { setMenu(toggle.getAttribute("aria-expanded") !== "true"); });

  /* dropdowns */
  var dds = [].slice.call(header.querySelectorAll(".has-dropdown"));
  function closeAll(except) {
    dds.forEach(function (d) {
      if (d === except) return;
      d.classList.remove("is-open"); var b = d.querySelector(".dd-toggle"); if (b) b.setAttribute("aria-expanded", "false");
    });
  }
  dds.forEach(function (d) {
    var b = d.querySelector(".dd-toggle");
    b.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = !d.classList.contains("is-open");
      closeAll(d); d.classList.remove("is-dismissed"); d.classList.toggle("is-open", open); b.setAttribute("aria-expanded", open ? "true" : "false");
    });
    d.addEventListener("mouseenter", function () { if (!mq.matches) b.setAttribute("aria-expanded", "true"); });
    d.addEventListener("mouseleave", function () { d.classList.remove("is-dismissed"); if (!mq.matches && !d.classList.contains("is-open")) b.setAttribute("aria-expanded", "false"); });
    d.addEventListener("focusin", function () { if (!mq.matches && !d.classList.contains("is-dismissed")) b.setAttribute("aria-expanded", "true"); });
    d.addEventListener("focusout", function (e) {
      if (!d.contains(e.relatedTarget)) d.classList.remove("is-dismissed");
      if (!d.contains(e.relatedTarget) && !mq.matches && !d.classList.contains("is-open")) b.setAttribute("aria-expanded", "false");
    });
  });
  document.addEventListener("click", function (e) { if (!header.contains(e.target)) closeAll(); });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    var openDd = dds.filter(function (d) { return d.classList.contains("is-open") || d.contains(document.activeElement); })[0];
    closeAll();
    if (openDd) {
      var b = openDd.querySelector(".dd-toggle");
      openDd.classList.add("is-dismissed"); b.setAttribute("aria-expanded", "false");
      if (document.activeElement && openDd.contains(document.activeElement) && document.activeElement !== b) b.focus();
    }
    if (header.classList.contains("menu-open")) { setMenu(false); toggle.focus(); }
  });
  header.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", function () { if (mq.matches) setMenu(false); }); });
  var onMq = function () { if (!mq.matches) setMenu(false); };
  if (mq.addEventListener) mq.addEventListener("change", onMq); else mq.addListener(onMq);
})();
