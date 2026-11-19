"""Shared layout + helpers for the StrategicOps Global Consulting static site.

Every page renders through layout(), so header, footer, metadata and scripts stay identical.
Edit SITE below, then run `python3 build/build.py` from the project root.
"""
import json
from datetime import datetime
from html import escape as esc

SITE = {
    "name": "StrategicOps Global Consulting",
    "short": "StrategicOps",
    "base_url": "https://www.strategicops.example",   # replace with the real origin before launch
    "email": "[BUSINESS EMAIL]",
    "phone": "[BUSINESS PHONE]",
    "address": "[BUSINESS ADDRESS]",
    "year": str(datetime.now().year),
    "social": {"LinkedIn": "", "GitHub": "", "YouTube": ""},   # empty = "URL pending", never a dead link
    "tagline": "Agentic AI engineering, consulting and intelligent automation solutions.",
}

PAGES = {
    "home": ("index.html", "Home"),
    "about": ("pages/about.html", "About Us"),
    "services": ("pages/services.html", "Services"),
    "consulting": ("pages/consulting.html", "Agentic AI Consulting"),
    "agents": ("pages/agent-development.html", "AI Agent Development"),
    "multi": ("pages/multi-agent-systems.html", "Multi-Agent Systems"),
    "automation": ("pages/automation.html", "AI Automation"),
    "enterprise": ("pages/enterprise-ai.html", "Enterprise AI Solutions"),
    "integration": ("pages/integration.html", "AI Integration"),
    "solutions": ("pages/solutions.html", "Solutions"),
    "industries": ("pages/industries.html", "Industry Solutions"),
    "technology": ("pages/technology.html", "Technology"),
    "process": ("pages/process.html", "Our Process"),
    "cases": ("pages/case-studies.html", "Case Studies"),
    "insights": ("pages/insights.html", "Insights"),
    "contact": ("pages/contact.html", "Contact"),
    "consultation": ("pages/consultation.html", "Book an AI Consultation"),
    "privacy": ("pages/privacy.html", "Privacy Policy"),
    "terms": ("pages/terms.html", "Terms & Conditions"),
    "cookies": ("pages/cookies.html", "Cookie Policy"),
}


def href(key, frag=""):
    return "@R@" + PAGES[key][0] + (("#" + frag) if frag else "")


_I = {
    "autonomy": '<circle cx="12" cy="12" r="3"/><circle cx="5" cy="6" r="1.6"/><circle cx="19" cy="6" r="1.6"/><circle cx="5" cy="18" r="1.6"/><circle cx="19" cy="18" r="1.6"/><path d="M6.3 7.1l3.6 3.3M17.7 7.1l-3.6 3.3M6.3 16.9l3.6-3.3M17.7 16.9l-3.6-3.3"/>',
    "automation": '<path d="M4 7h9M4 12h16M4 17h7"/><path d="M16 4l3 3-3 3M14 14l3 3-3 3"/>',
    "integration": '<rect x="3" y="8" width="7" height="8" rx="1"/><rect x="14" y="8" width="7" height="8" rx="1"/><path d="M10 12h4M6.5 5v3M17.5 5v3"/>',
    "architecture": '<path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 12.5l9 5 9-5M3 17l9 5 9-5"/>',
    "shield": '<path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6l8-3z"/><path d="M9 12l2 2 4-4"/>',
    "support": '<path d="M4 5h16v11H9l-5 4V5z"/><path d="M8 9h8M8 12h5"/>',
    "sales": '<path d="M3 17l6-6 4 4 8-9"/><path d="M15 6h6v6"/>',
    "marketing": '<path d="M3 11v3l12 5V6L3 11z"/><path d="M18 9.5a4 4 0 010 5M6 15l1.5 5"/>',
    "finance": '<rect x="3" y="6" width="18" height="12" rx="1"/><circle cx="12" cy="12" r="2.5"/><path d="M6 9v.01M18 15v.01"/>',
    "hr": '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><path d="M16 5.2a3 3 0 010 5.6M21 20c0-2.5-1.5-4.6-4-5.5"/>',
    "research": '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>',
    "ops": '<circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "arrow-ur": '<path d="M7 17L17 7M8 7h9v9"/>',
    "chevron": '<path d="M6 9l6 6 6-6"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7"/>',
    "up": '<path d="M12 19V5M6 11l6-6 6 6"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
}


def icon(name, cls="icon"):
    return ('<svg class="%s" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">%s</svg>'
            % (cls, _I[name]))


MARK = ('<svg class="brand-svg" viewBox="0 0 32 32" aria-hidden="true" focusable="false">'
        '<rect width="32" height="32" rx="9" fill="#2438F5"/><path d="M8 21l5-5 4 4 7-8" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
        '<circle cx="24" cy="12" r="2.6" fill="#FFD43B"/></svg>')

SERVICES_MENU = [
    ("services", "Services overview", "Everything we do, in one place"),
    ("consulting", "Agentic AI Consulting", "Strategy, readiness and roadmaps"),
    ("agents", "AI Agent Development", "Custom agents that reason and act"),
    ("multi", "Multi-Agent Systems", "Orchestrated, specialised agents"),
    ("automation", "AI Automation", "Agent-powered business workflows"),
    ("enterprise", "Enterprise AI Solutions", "Secure, governed deployments"),
    ("integration", "AI Integration", "Connect AI to your systems"),
]
SOLUTIONS_MENU = [
    ("solutions", "By business function", "Support, sales, finance, HR and more"),
    ("industries", "Industry solutions", "Agentic AI across sectors"),
    ("process", "Our process", "From discovery to optimisation"),
    ("cases", "Case studies", "Applied architectures and projects"),
]


def _dropdown(label, key, items, active_keys, current):
    lis = "".join(
        '<li><a class="mega-link" data-cursor="Open" href="%s"%s><span class="mega-title">%s</span><span class="mega-sub">%s</span></a></li>'
        % (href(k), ' aria-current="page"' if k == current else "", esc(t), esc(s)) for k, t, s in items)
    did = "dd-" + key
    return (
        '<li class="nav-item has-dropdown"><a class="nav-link%s" href="%s"%s><span class="roll"><span>%s</span><span aria-hidden="true">%s</span></span></a>'
        '<button class="dd-toggle" type="button" aria-expanded="false" aria-controls="%s" aria-label="Toggle %s submenu">%s</button>'
        '<div class="mega" id="%s"><ul class="mega-list">%s</ul></div></li>'
        % (" is-active" if current in active_keys else "", href(key), ' aria-current="page"' if current == key else "",
           esc(label), esc(label), did, esc(label), icon("chevron", "icon icon-sm"), did, lis))


def header(current):
    def link(k, label):
        return ('<li class="nav-item"><a class="nav-link%s" href="%s"%s><span class="roll"><span>%s</span><span aria-hidden="true">%s</span></span></a></li>'
                % (" is-active" if current == k else "", href(k), ' aria-current="page"' if current == k else "", label, label))

    items = (link("home", "Home")
             + _dropdown("Services", "services", SERVICES_MENU, {k for k, _, _ in SERVICES_MENU}, current)
             + _dropdown("Solutions", "solutions", SOLUTIONS_MENU, {"solutions", "process", "cases"}, current)
             + link("industries", "Industries") + link("technology", "Technology")
             + link("insights", "Insights") + link("about", "About"))
    return (
        '<header class="site-header" id="site-header"><div class="nav-pill">'
        '<a class="brand" href="' + href("home") + '" aria-label="StrategicOps Global Consulting home">' + MARK +
        '<span class="brand-text"><b>StrategicOps</b><i>Global Consulting</i></span></a>'
        '<nav class="primary-nav" id="primary-nav" aria-label="Primary"><ul class="nav-list">' + items +
        '<li class="nav-blob" aria-hidden="true"></li></ul>'
        '<a class="btn-sy btn-sy-sun btn-sy-sm nav-cta" data-magnetic href="' + href("consultation") + '"><span class="roll"><span>Book an AI Consultation</span><span aria-hidden="true">Book an AI Consultation</span></span></a></nav>'
        '<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav"><span class="nt-label">Menu</span>'
        '<span class="bars" aria-hidden="true"><i></i><i></i></span></button></div></header>')


def marquee(words, cls=""):
    row = "".join('<li>%s<span class="mq-dot" aria-hidden="true"></span></li>' % esc(w) for w in words)
    return ('<div class="marquee %s" data-marquee aria-hidden="true"><ul class="mq-track">%s</ul><ul class="mq-track" aria-hidden="true">%s</ul></div>'
            % (cls, row, row))


def footer():
    def col(title, items):
        return '<div class="col-6 col-lg-2"><h2 class="foot-h">%s</h2><ul class="foot-list">%s</ul></div>' % (
            title, "".join('<li><a href="%s">%s</a></li>' % (href(k), esc(t)) for k, t in items))

    quick = [("home", "Home"), ("about", "About"), ("services", "Services"), ("solutions", "Solutions"),
             ("industries", "Industries"), ("technology", "Technology"), ("insights", "Insights"), ("contact", "Contact")]
    svc = [("consulting", "AI Consulting"), ("agents", "AI Agent Development"), ("multi", "Multi-Agent Systems"),
           ("automation", "AI Automation"), ("enterprise", "Enterprise AI Integration")]

    def real(v):
        return v and not v.startswith("[")

    email = ('<a href="mailto:%s">%s</a>' % (esc(SITE["email"]), esc(SITE["email"]))) if real(SITE["email"]) else esc(SITE["email"])
    phone = ('<a href="tel:%s">%s</a>' % (esc(SITE["phone"]), esc(SITE["phone"]))) if real(SITE["phone"]) else esc(SITE["phone"])
    soc = ""
    for n, u in SITE["social"].items():
        soc += ('<li><a href="%s" rel="noopener noreferrer" target="_blank">%s</a></li>' % (esc(u), n)) if u else \
            '<li><span class="social-pending" title="Add the company URL in build/common.py">%s <em>(URL pending)</em></span></li>' % n
    legal = "".join('<a href="%s">%s</a>' % (href(k), t) for k, t in
                    [("privacy", "Privacy Policy"), ("terms", "Terms &amp; Conditions"), ("cookies", "Cookie Policy")])
    return (
        '<footer class="site-footer"><div class="container"><div class="foot-top"><p class="foot-big">Let&rsquo;s put intelligence to work in your operations.</p>'
        '<a class="btn-sy btn-sy-sun" data-magnetic href="' + href("consultation") + '"><span class="roll"><span>Book an AI Consultation</span><span aria-hidden="true">Book an AI Consultation</span></span></a></div>'
        '<div class="row gx-lg-5 gy-5"><div class="col-lg-4"><a class="brand brand-foot" href="' + href("home") + '">' + MARK +
        '<span class="brand-text"><b>StrategicOps</b><i>Global Consulting</i></span></a><p class="foot-desc">' + SITE["tagline"] + '</p></div>'
        + col("Quick links", quick) + col("Services", svc) +
        '<div class="col-12 col-lg-4"><div class="row gx-lg-5 gy-5"><div class="col-12 col-sm-6"><h2 class="foot-h">Contact</h2>'
        '<ul class="foot-list"><li>' + email + '</li><li>' + phone + '</li><li>' + esc(SITE["address"]) + '</li></ul></div>'
        '<div class="col-12 col-sm-6"><h2 class="foot-h">Social</h2><ul class="foot-list">' + soc + '</ul></div></div></div></div>'
        '<p class="foot-word" data-spotlight aria-hidden="true">StrategicOps</p>'
        '<div class="foot-bottom"><p>&copy; <span data-year>' + SITE["year"] + '</span> StrategicOps Global Consulting. All rights reserved.</p>'
        '<nav class="foot-legal" aria-label="Legal">' + legal + '</nav></div></div></footer>')


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


def org_schema():
    d = {"@context": "https://schema.org", "@type": "Organization", "name": SITE["name"], "url": SITE["base_url"] + "/",
         "description": "Agentic AI engineering, consulting and technology services: AI consulting, custom AI agent development and enterprise AI integration.",
         "logo": SITE["base_url"] + "/assets/logos/strategicops-mark.svg"}
    sa = [u for u in SITE["social"].values() if u]
    if sa:
        d["sameAs"] = sa
    return d


def breadcrumbs(crumbs):
    items = [("Home", "home")] + crumbs
    lis = ""
    for i, (lbl, k) in enumerate(items):
        lis += ('<li><a href="%s">%s</a></li>' % (href(k), esc(lbl))) if (k and i < len(items) - 1) else '<li aria-current="page">%s</li>' % esc(lbl)
    return '<nav class="crumbs" aria-label="Breadcrumb"><ol>%s</ol></nav>' % lis


def breadcrumb_schema(path, crumbs):
    items = [("Home", "index.html")] + [(l, PAGES[k][0] if k else path) for l, k in crumbs]
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE["base_url"] + "/" + (p if p != "index.html" else "")}
        for i, (n, p) in enumerate(items)]}


def layout(key, title, desc, body, nav=None, crumbs=None, schema=None, og_type="website", full_title=False):
    path = PAGES[key][0]
    R = "../" * path.count("/")
    canon = SITE["base_url"] + "/" + ("" if path == "index.html" else path)
    t = title if full_title else "%s | StrategicOps Global Consulting" % title
    sch = [org_schema()] if key == "home" else []
    if crumbs:
        sch.append(breadcrumb_schema(path, crumbs))
    sch += (schema or [])
    og = SITE["base_url"] + "/assets/images/og-image.png"
    head = f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(t)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#2438F5">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="StrategicOps Global Consulting">
<meta property="og:title" content="{esc(t)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(t)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{og}">
<link rel="icon" href="@R@assets/icons/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,600;12..96,700;12..96,800&family=DM+Mono:wght@400;500&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<link rel="stylesheet" href="@R@css/style.css">
<link rel="stylesheet" href="@R@css/responsive.css">
<link rel="stylesheet" href="@R@css/animations.css">
<script>document.documentElement.className=document.documentElement.className.replace("no-js","js");</script>
{"".join(jsonld(s) for s in sch)}
</head>
<body data-page="{key}">
<a class="skip-link" href="#main">Skip to main content</a>
<div class="progress" id="progress" aria-hidden="true"></div>
{header(nav or key)}
<main id="main">
{breadcrumbs(crumbs) if crumbs else ""}
{body}
</main>
{footer()}
<button class="to-top" id="to-top" type="button" aria-label="Back to top" data-magnetic hidden>{icon("up")}</button>
<script src="@R@js/config.js"></script>
<script src="@R@js/main.js" defer></script>
<script src="@R@js/navigation.js" defer></script>
<script src="@R@js/cursor.js" defer></script>
<script src="@R@js/animations.js" defer></script>
<script src="@R@js/agent-visualization.js" defer></script>
<script src="@R@js/forms.js" defer></script>
<script src="@R@js/components.js" defer></script>
</body>
</html>
'''
    return head.replace("@R@", R)


# ------------------------------------------------------------ component helpers
def sec_head(eyebrow, title, lead=None, center=False, h=2):
    return ('<div class="sec-head%s"><p class="eyebrow">%s</p><h%d class="h2x" data-split>%s</h%d>%s</div>'
            % (" is-center" if center else "", esc(eyebrow), h, title, h, ('<p class="lead-sy reveal">%s</p>' % lead) if lead else ""))


def btn(label, link, kind="primary", extra=""):
    cls = {"primary": "btn-sy", "ghost": "btn-sy btn-sy-ghost", "sun": "btn-sy btn-sy-sun", "light": "btn-sy btn-sy-light",
           "ghost-light": "btn-sy btn-sy-ghost-light", "link": "link-arrow"}[kind]
    ic = icon("arrow-ur", "icon icon-sm") if kind == "link" else ""
    mag = "" if kind == "link" else " data-magnetic"
    return '<a class="%s %s"%s href="%s"><span class="roll"><span>%s</span><span aria-hidden="true">%s</span></span>%s</a>' % (cls, extra, mag, link, esc(label), label, ic)


def badge_svg():
    return ('<div class="hero-badge" aria-hidden="true"><svg viewBox="0 0 200 200" focusable="false"><defs><path id="bp" d="M100,100 m-76,0 a76,76 0 1,1 152,0 a76,76 0 1,1 -152,0"/></defs>'
            '<circle cx="100" cy="100" r="98" fill="#FFD43B"/><text><textPath href="#bp" font-size="15" letter-spacing="3.4">AGENTIC AI  /  STRATEGY  /  OPERATIONS  /  </textPath></text>'
            '<path d="M70 118l20-22 14 14 26-32" fill="none" stroke="#0C1020" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>')


def page_hero(eyebrow, h1, sub, ctas=""):
    return ('<section class="page-hero"><div class="ph-grid" aria-hidden="true"></div><span class="ph-orb" data-float aria-hidden="true"></span>' + badge_svg() +
            '<div class="container"><div class="page-hero-inner"><p class="eyebrow">%s</p><h1 class="display display-md">%s</h1>'
            '<p class="lead-sy">%s</p><div class="btn-row">%s</div></div></div></section>' % (esc(eyebrow), h1, sub, ctas))


def cta_band(title, text, primary=("Book an AI Consultation", "consultation"), secondary=("Discuss Your Project", "contact")):
    return ('<section class="cta-band"><div class="ph-grid" aria-hidden="true"></div><div class="container"><h2 class="display display-sm" data-split>%s</h2>'
            '<p class="lead-sy reveal">%s</p><div class="btn-row">%s%s</div></div></section>'
            % (title, text, btn(primary[0], href(primary[1]), "sun"),
               btn(secondary[0], href(secondary[1]), "ghost-light") if secondary else ""))


def faq(items, fid="faq"):
    out = ""
    for i, (q, a) in enumerate(items):
        out += ('<div class="acc-item"><h3 class="acc-h"><button class="acc-btn" type="button" aria-expanded="false" data-cursor="Toggle" '
                'aria-controls="%s-%d" id="%s-b%d"><span>%s</span><span class="acc-ic">%s</span></button></h3>'
                '<div class="acc-panel" id="%s-%d" role="region" aria-labelledby="%s-b%d" hidden><p>%s</p></div></div>'
                % (fid, i, fid, i, esc(q), icon("plus", "icon icon-sm"), fid, i, fid, i, esc(a)))
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
    return '<div class="accordion-sy" data-accordion>%s</div>' % out, schema


def service_schema(name, desc, key):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc, "serviceType": name,
            "url": SITE["base_url"] + "/" + PAGES[key][0],
            "provider": {"@type": "Organization", "name": SITE["name"], "url": SITE["base_url"] + "/"}}


# ------------------------------------------------------------ forms
INDUSTRIES = ["Healthcare", "Manufacturing", "Banking & Financial Services", "Retail & E-commerce", "Education", "Logistics",
              "Real Estate", "Professional Services", "Technology & SaaS", "Other"]
SIZES = ["1–10 employees", "11–50 employees", "51–200 employees", "201–1,000 employees", "1,000+ employees"]
SERVICES = ["Agentic AI Consulting", "Custom AI Agent Development", "Multi-Agent Systems", "AI Automation",
            "Enterprise AI Solutions", "AI Integration", "AI Application Development", "Other"]
BUDGETS = ["Not sure yet", "Under $10,000", "$10,000 – $25,000", "$25,000 – $75,000", "$75,000 – $150,000", "$150,000+"]
TIMELINES = ["Exploring options", "Within 1 month", "1–3 months", "3–6 months", "6+ months"]


def _field(pid, name, label, typ="text", req=True, auto="", opts=None, ph="", half=True):
    fid = "%s-%s" % (pid, name)
    err = '<p class="field-error" id="%s-err" role="alert" hidden></p>' % fid
    rq = ' <span class="req" aria-hidden="true">*</span>' if req else ' <span class="opt">(optional)</span>'
    attrs = ' name="%s" id="%s" aria-describedby="%s-err"%s%s' % (name, fid, fid, ' required' if req else '', (' autocomplete="%s"' % auto) if auto else "")
    if opts is not None:
        ctl = '<select class="ctl"%s><option value="">Select…</option>%s</select>' % (attrs, "".join('<option>%s</option>' % esc(x) for x in opts))
    elif typ == "textarea":
        ctl = '<textarea class="ctl" rows="5" placeholder="%s"%s></textarea>' % (esc(ph), attrs)
    else:
        ctl = '<input class="ctl" type="%s" placeholder="%s"%s>' % (typ, esc(ph), attrs)
    return '<div class="%s"><label class="lbl" for="%s">%s%s</label>%s%s</div>' % ("col-md-6" if half else "col-12", fid, label, rq, ctl, err)


def enquiry_form(pid="enq", default_service=None, intent="enquiry"):
    f = [
        _field(pid, "full_name", "Full name", auto="name"),
        _field(pid, "email", "Business email", "email", auto="email", ph="name@company.com"),
        _field(pid, "company", "Company name", auto="organization"),
        _field(pid, "website", "Website", "url", req=False, auto="url", ph="https://"),
        _field(pid, "industry", "Industry", opts=INDUSTRIES),
        _field(pid, "company_size", "Company size", opts=SIZES),
        _field(pid, "service", "Service required", opts=SERVICES),
        _field(pid, "budget", "Project budget", opts=BUDGETS),
        _field(pid, "timeline", "Project timeline", opts=TIMELINES),
        _field(pid, "description", "Project description", "textarea", half=False,
               ph="What are you trying to achieve? Which processes, systems or data are involved?"),
    ]
    sel = ('data-default-service="%s"' % esc(default_service)) if default_service else ""
    return (
        '<form class="enq-form" data-sy-form data-intent="%s" %s method="post" novalidate aria-label="Project enquiry form">'
        '<div class="row g-4">%s'
        '<div class="col-12"><div class="check"><input type="checkbox" id="%s-consent" name="consent" required aria-describedby="%s-consent-err">'
        '<label for="%s-consent">I agree to StrategicOps processing my details to respond to this enquiry, as described in the <a href="%s">Privacy Policy</a>. <span class="req" aria-hidden="true">*</span></label></div>'
        '<p class="field-error" id="%s-consent-err" role="alert" hidden></p></div>'
        '<div class="hp" aria-hidden="true"><label>Leave this field empty<input type="text" name="company_website_confirm" tabindex="-1" autocomplete="off"></label></div>'
        '<div class="col-12 turnstile-slot" data-turnstile></div>'
        '<div class="col-12"><button class="btn-sy btn-sy-sun" data-magnetic type="submit"><span class="btn-label">Send enquiry</span>'
        '<span class="btn-spin" aria-hidden="true"></span></button></div>'
        '<div class="col-12"><div class="form-status" role="status" aria-live="polite" tabindex="-1" hidden></div></div>'
        '</div></form>'
    ) % (intent, sel, "".join(f), pid, pid, pid, href("privacy"), pid)
