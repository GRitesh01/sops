/* =========================================================
   Enquiry forms
   - Client-side validation with accessible, field-level errors
   - Spam protection: honeypot + minimum-time check + optional Cloudflare Turnstile
   - Backend-ready: posts multipart/form-data to SOPS_CONFIG.formEndpoint
   - Never shows a success message unless the server confirms receipt
   ========================================================= */
(function () {
  "use strict";
  var cfg = window.SOPS_CONFIG || {};
  var MIN_FILL_MS = 2000;

  var MESSAGES = {
    full_name: "Enter your full name.",
    email: "Enter your business email address.",
    company: "Enter your company name.",
    industry: "Select your industry.",
    company_size: "Select your company size.",
    service: "Select the service you need.",
    budget: "Select a project budget range.",
    timeline: "Select a project timeline.",
    description: "Describe your project in at least 20 characters.",
    consent: "Confirm consent so we can respond to your enquiry."
  };
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

  function errEl(field) { return document.getElementById(field.id + "-err"); }

  function validateField(f) {
    var v = (f.type === "checkbox" ? f.checked : f.value.trim()), msg = "";
    if (f.name === "company_website_confirm") return "";
    if (f.type === "checkbox") { if (f.required && !v) msg = MESSAGES.consent; }
    else if (f.required && !v) msg = MESSAGES[f.name] || "This field is required.";
    else if (f.name === "email" && v && !EMAIL_RE.test(v)) msg = "Enter a valid email address, for example name@company.com.";
    else if (f.name === "website" && v) {
      try { var u = new URL(v); if (u.protocol !== "http:" && u.protocol !== "https:") throw 0; }
      catch (e) { msg = "Enter a full web address starting with https://"; }
    } else if (f.name === "description" && v.length > 0 && v.length < 20) msg = MESSAGES.description;
    return msg;
  }
  function setError(f, msg) {
    var e = errEl(f);
    if (msg) { f.setAttribute("aria-invalid", "true"); if (e) { e.textContent = msg; e.hidden = false; } }
    else { f.removeAttribute("aria-invalid"); if (e) { e.textContent = ""; e.hidden = true; } }
  }
  function status(form, kind, html) {
    var s = form.querySelector(".form-status");
    s.className = "form-status is-" + kind; s.innerHTML = html; s.hidden = false; s.focus();
  }
  function fallbackLink() {
    return /^[^\s@\[]+@[^\s@]+$/.test(cfg.fallbackEmail || "") ? ' You can also email us at <a href="mailto:' + cfg.fallbackEmail + '">' + cfg.fallbackEmail + "</a>." : "";
  }

  /* ---------- Turnstile (optional) ---------- */
  var tsLoading = false;
  function initTurnstile(forms) {
    if (!cfg.turnstileSiteKey) return;
    function render() {
      forms.forEach(function (f) {
        var slot = f.querySelector("[data-turnstile]");
        if (slot && window.turnstile && !slot.hasChildNodes()) window.turnstile.render(slot, { sitekey: cfg.turnstileSiteKey, theme: "dark" });
      });
    }
    if (window.turnstile) return render();
    if (tsLoading) return; tsLoading = true;
    var s = document.createElement("script");
    s.src = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit"; s.async = true; s.defer = true; s.onload = render;
    document.head.appendChild(s);
  }

  function setup(form) {
    var loadedAt = Date.now(), attempted = false;
    var fields = [].slice.call(form.querySelectorAll("input, select, textarea")).filter(function (f) { return f.name && f.name !== "company_website_confirm"; });

    var def = form.getAttribute("data-default-service");
    if (def) { var sel = form.querySelector('select[name="service"]'); if (sel && !sel.value) for (var i = 0; i < sel.options.length; i++) if (sel.options[i].text === def) sel.selectedIndex = i; }

    fields.forEach(function (f) {
      f.addEventListener("blur", function () { if (attempted || f.value) setError(f, validateField(f)); });
      f.addEventListener("input", function () { if (f.getAttribute("aria-invalid") === "true") setError(f, validateField(f)); });
      f.addEventListener("change", function () { if (f.getAttribute("aria-invalid") === "true") setError(f, validateField(f)); });
    });

    form.addEventListener("submit", function (ev) {
      ev.preventDefault(); attempted = true;
      var first = null;
      fields.forEach(function (f) { var m = validateField(f); setError(f, m); if (m && !first) first = f; });
      if (first) { first.focus(); status(form, "error", "Check the highlighted fields and try again."); return; }

      // Honeypot: bots fill hidden fields. Drop silently.
      var hp = form.querySelector('[name="company_website_confirm"]');
      if (hp && hp.value) return;
      if (Date.now() - loadedAt < MIN_FILL_MS) { status(form, "error", "That was very quick. Please review your details and send again."); return; }

      if (cfg.turnstileSiteKey) {
        var tok = form.querySelector('[name="cf-turnstile-response"]');
        if (!tok || !tok.value) { status(form, "error", "Complete the verification challenge, then send again."); return; }
      }

      var endpoint = form.getAttribute("data-endpoint") || cfg.formEndpoint;
      if (!endpoint) {
        status(form, "info", "<strong>Your message has not been sent.</strong> This form is not connected to a submission service yet." + fallbackLink() + " Your entries are still on the page.");
        return;
      }

      var fd = new FormData(form);
      fd.delete("company_website_confirm");
      fd.append("form_intent", form.getAttribute("data-intent") || "enquiry");
      fd.append("page_url", location.href);
      fd.append("submitted_at", new Date().toISOString());

      form.classList.add("is-loading"); form.setAttribute("aria-busy", "true");
      var label = form.querySelector(".btn-label"), prev = label.textContent; label.textContent = "Sending…";
      var ctl = ("AbortController" in window) ? new AbortController() : null, to = ctl ? setTimeout(function () { ctl.abort(); }, 20000) : null;

      fetch(endpoint, { method: "POST", body: fd, headers: { Accept: "application/json" }, signal: ctl ? ctl.signal : undefined })
        .then(function (res) {
          if (!res.ok) throw new Error("status " + res.status);
          var email = form.querySelector('[name="email"]').value;
          form.reset(); fields.forEach(function (f) { setError(f, ""); });
          status(form, "success", "<strong>Thank you. Your enquiry has been sent.</strong> We will reply to " + email.replace(/</g, "&lt;") + ".");
          if (window.turnstile) try { window.turnstile.reset(); } catch (e) {}
          loadedAt = Date.now(); attempted = false;
        })
        .catch(function (err) {
          status(form, "error", "<strong>We could not send your enquiry.</strong> " + (err && err.name === "AbortError" ? "The request timed out." : "Please check your connection and try again.") + fallbackLink());
        })
        .then(function () { if (to) clearTimeout(to); form.classList.remove("is-loading"); form.removeAttribute("aria-busy"); label.textContent = prev; });
    });
  }

  var forms = [].slice.call(document.querySelectorAll("form[data-sy-form]"));
  forms.forEach(setup);
  initTurnstile(forms);
})();
