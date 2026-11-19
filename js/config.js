/* =========================================================
   StrategicOps site configuration. Edit these values at launch.
   ========================================================= */
window.SOPS_CONFIG = {
  // Form backend. POST endpoint that accepts multipart/form-data.
  // Examples: your own API route, Formspree, Getform, a serverless function.
  // Leave empty and forms will clearly report that submission is not configured
  // (they will NOT show a fake success message).
  formEndpoint: "",

  // Optional: Cloudflare Turnstile site key (https://developers.cloudflare.com/turnstile/).
  // When set, a challenge widget is rendered in each form. Your backend must verify
  // the "cf-turnstile-response" token server-side.
  turnstileSiteKey: "",

  // Scheduling page for the consultation booking section (Calendly, Cal.com, etc.).
  // Must be an https:// URL that allows embedding in an iframe.
  calendarUrl: "",

  // Optional real address used for an "email us instead" link in form error messages.
  fallbackEmail: ""
};
