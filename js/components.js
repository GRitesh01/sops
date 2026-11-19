/* Small shared helpers that keep reusable components consistent across pages. */
(function () {
  "use strict";
  // Footer year stays current even if the static HTML is not rebuilt.
  var y = new Date().getFullYear();
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = y; });

  // External links open safely.
  document.querySelectorAll('a[target="_blank"]').forEach(function (a) {
    var rel = (a.getAttribute("rel") || "").split(/\s+/);
    ["noopener", "noreferrer"].forEach(function (r) { if (rel.indexOf(r) < 0) rel.push(r); });
    a.setAttribute("rel", rel.join(" ").trim());
  });

  // Consultation page: pre-select the service from ?service=... when provided.
  var p = new URLSearchParams(location.search).get("service");
  if (p) document.querySelectorAll('select[name="service"]').forEach(function (s) {
    for (var i = 0; i < s.options.length; i++) if (s.options[i].text.toLowerCase() === p.toLowerCase()) s.selectedIndex = i;
  });

  // Calendar embed (https only). Fallback copy stays when no URL is configured.
  var cfg = window.SOPS_CONFIG || {};
  var cal = document.querySelector("[data-calendar]");
  if (cal && /^https:\/\//i.test(cfg.calendarUrl || "")) {
    var f = document.createElement("iframe");
    f.src = cfg.calendarUrl; f.title = "Book an AI consultation"; f.loading = "lazy";
    f.setAttribute("referrerpolicy", "strict-origin-when-cross-origin");
    cal.innerHTML = ""; cal.appendChild(f);
  }
})();
