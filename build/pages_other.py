from html import escape as esc
from common import *
from data import *
from pages_home import industry_tabs, tech_grid, timeline, article_card, read_time


def ul(items):
    return "<ul class='list-dash'>%s</ul>" % "".join("<li>%s</li>" % esc(i) for i in items)


# ------------------------------------------------------------ ABOUT
def build_about():
    principles = [("Business first", "Technology choices follow from the process and outcome, not the other way round."),
                  ("Engineering rigour", "Agents are tested, traced and monitored like any production software."),
                  ("Supervised autonomy", "People stay in control. Autonomy is configured and widened as evidence supports it."),
                  ("Honest expectations", "We do not promise guaranteed outcomes. We measure and report what we find."),
                  ("Security by design", "Permissions, audit logs and data handling are part of the architecture."),
                  ("Long-term partnership", "We aim to be a transformation partner, not a one-off software vendor.")]
    body = (
        page_hero("About StrategicOps Global Consulting", "A global partner for intelligent, autonomous operations.",
                  "StrategicOps Global Consulting is an Agentic AI engineering, consulting and technology company. We help businesses design, develop and deploy intelligent autonomous AI systems.",
                  btn("Book an AI Consultation", href("consultation")) + btn("Our process", href("process"), "ghost")) +
        '<section class="sec"><div class="container"><div class="row gx-lg-5 gy-5"><div class="col-lg-5">' +
        sec_head("Who we are", "Consult intelligently. Engineer autonomously. Transform operations.") +
        '</div><div class="col-lg-7 reveal prose"><p>We help businesses turn complex processes into scalable, efficient and intelligent operations. Our work spans three areas: Agentic AI consulting, custom AI agent development, and enterprise AI integration and transformation.</p>'
        '<p>We work with startups, growing businesses and large enterprises across sectors including technology, manufacturing, financial services, healthcare, retail, logistics and professional services.</p>'
        '<p class="placeholder">[COMPANY STORY: founding background, mission and milestones to be supplied by StrategicOps]</p></div></div></div></section>'
        '<section class="sec sec-alt"><div class="container">' + sec_head("How we work", "Principles that guide our engineering.") +
        '<div class="row g-0 why-grid">' + "".join(
            '<div class="col-md-6 col-xl-4"><div class="why-item reveal"><span class="why-ic">%s</span><h3>%s</h3><p>%s</p></div></div>'
            % (icon("check", "icon icon-sm"), t, d) for t, d in principles) + '</div></div></section>'
        '<section class="sec"><div class="container">' + sec_head("Leadership and team", "The people behind the systems.") +
        '<div class="row g-4"><div class="col-md-4"><div class="tile"><p class="placeholder">[LEADERSHIP PROFILE 1: name, role, short bio]</p></div></div>'
        '<div class="col-md-4"><div class="tile"><p class="placeholder">[LEADERSHIP PROFILE 2: name, role, short bio]</p></div></div>'
        '<div class="col-md-4"><div class="tile"><p class="placeholder">[LEADERSHIP PROFILE 3: name, role, short bio]</p></div></div></div></div></section>' +
        cta_band("Let&rsquo;s build something intelligent together.", "Tell us what you are trying to achieve and we will help you find the right approach.")
    )
    return layout("about", "About Us", "About StrategicOps: an Agentic AI engineering and consulting company helping businesses design, build and deploy intelligent autonomous AI systems.",
                  body, nav="about", crumbs=[("About Us", None)])


# ------------------------------------------------------------ SOLUTIONS
def build_solutions():
    secs = ""
    for sid, ic, title, blurb, items, long in SOLUTIONS:
        secs += (
            '<section class="sec sol-sec" id="%s"><div class="container"><div class="row gx-lg-5 gy-5"><div class="col-lg-5 reveal">'
            '<div class="card-ic">%s</div><h2 class="h3x">%s</h2><p class="lead-sy">%s</p></div>'
            '<div class="col-lg-7 reveal"><h3 class="mini-h">What agents can do</h3>%s<h3 class="mini-h mt-lg">How it works</h3><p>%s</p>'
            '<p class="fineprint">Scope, accuracy and outcomes depend on your data, systems and process. A discovery phase confirms what is feasible.</p>%s</div></div></div></section>'
            % (sid, icon(ic), esc(title), esc(blurb), ul(items), esc(long), btn("Discuss " + title, href("contact"), "link")))
    nav_chips = "".join('<li><a href="#%s">%s</a></li>' % (s[0], esc(s[2])) for s in SOLUTIONS)
    body = (
        page_hero("Solutions by business function", "Intelligence for every function in the business.",
                  "Agentic AI applied to support, sales, marketing, finance, HR, research and operations.",
                  btn("Book an AI Consultation", href("consultation")) + btn("Industry solutions", href("industries"), "ghost")) +
        '<nav class="jump" aria-label="Solutions on this page"><div class="container"><ul>%s</ul></div></nav>' % nav_chips + secs +
        cta_band("Have a function in mind?", "Tell us about the process and we will assess where agents can help.")
    )
    return layout("solutions", "AI Solutions by Business Function",
                  "AI agent solutions for customer support, sales, marketing, finance, HR, research and operations from StrategicOps.",
                  body, nav="solutions", crumbs=[("Solutions", None)])


# ------------------------------------------------------------ INDUSTRIES
def build_industries():
    body = (
        page_hero("Industry solutions", "Agentic AI across industries.",
                  "Typical challenges, potential applications, recommended agent types and integration opportunities for nine sectors.",
                  btn("Book an AI Consultation", href("consultation")) + btn("Solutions by function", href("solutions"), "ghost")) +
        '<section class="sec"><div class="container">' + industry_tabs("ind-page", 2) +
        '<p class="fineprint spacer-sm">Examples are illustrative starting points, not guarantees. Every engagement begins with discovery of your own processes, data and constraints.</p>'
        '</div></section>' + cta_band("Don&rsquo;t see your industry?", "The same patterns apply wherever work is document-heavy, multi-system and exception-driven. Tell us about yours.")
    )
    return layout("industries", "Industry Solutions", "Agentic AI solutions for healthcare, manufacturing, financial services, retail, education, logistics, real estate, professional services and technology.",
                  body, nav="industries", crumbs=[("Industry Solutions", None)])


# ------------------------------------------------------------ TECHNOLOGY
def build_technology():
    tabs, panels = "", ""
    for i, (tid, name, items, desc) in enumerate(TECH_LAYERS):
        sel = i == 0
        tabs += ('<button class="tab" role="tab" id="tech-t-%s" aria-controls="tech-p-%s" aria-selected="%s" tabindex="%s" type="button">%s</button>'
                 % (tid, tid, str(sel).lower(), "0" if sel else "-1", esc(name)))
        panels += ('<div class="tab-panel" role="tabpanel" id="tech-p-%s" aria-labelledby="tech-t-%s"%s tabindex="0"><h3 class="panel-title">%s</h3>'
                   '<ul class="chips chips-lg">%s</ul><p class="prose-p">%s</p></div>'
                   % (tid, tid, "" if sel else " hidden", esc(name), "".join("<li>%s</li>" % esc(x) for x in items), esc(desc)))
    body = (
        page_hero("Technology", "Engineered with modern AI technologies.",
                  "We choose technologies per project, based on requirements for capability, security, cost and maintainability.",
                  btn("Book an AI Consultation", href("consultation")) + btn("Our process", href("process"), "ghost")) +
        '<section class="sec"><div class="container">' + sec_head("Capability layers", "The stack, layer by layer.") +
        '<div class="tabs-sy tabs-side reveal" data-tabs><div class="tab-list" role="tablist" aria-label="Technology layers" aria-orientation="vertical">%s</div>%s</div></div></section>' % (tabs, panels) +
        '<section class="sec sec-alt"><div class="container">' + sec_head("At a glance", "All layers.") + tech_grid() +
        '<p class="fineprint spacer-sm">Technology names are shown as text. Product names and trademarks belong to their respective owners, and their inclusion does not imply endorsement or partnership.</p></div></section>'
        '<section class="sec"><div class="container"><div class="row gx-lg-5 gy-5"><div class="col-lg-5">' +
        sec_head("How we choose", "Fit over fashion.") + '</div><div class="col-lg-7 reveal prose">'
        '<p>The right model, framework and infrastructure depend on the task, the data, the risk profile and your team. We evaluate options against your requirements, keep architectures modular so components can be replaced, and prefer simple designs that can be tested and operated.</p>'
        '<p>Every production system includes tracing, evaluation and guardrails, so behaviour can be inspected, measured and improved over time.</p></div></div></div></section>' +
        cta_band("Discuss your technical requirements", "Share your environment and constraints and we will propose a suitable architecture.")
    )
    return layout("technology", "Technology Stack for Agentic AI", "The technology StrategicOps uses to build agentic AI systems: AI models, agent frameworks, MCP and A2A, RAG, backend, databases, automation, infrastructure and AI operations.",
                  body, nav="technology", crumbs=[("Technology", None)])


# ------------------------------------------------------------ PROCESS
def build_process():
    body = (
        page_hero("Our process", "From business challenge to intelligent execution.",
                  "A seven-stage approach that moves from understanding the problem to operating, measuring and improving the solution.",
                  btn("Book an AI Consultation", href("consultation")) + btn("Case studies", href("cases"), "ghost")) +
        '<section class="sec"><div class="container">' + timeline(False) + '</div></section>'
        '<section class="sec sec-alt"><div class="container"><div class="row gx-lg-5 gy-5"><div class="col-lg-5">' + sec_head("Principles", "How every engagement runs.") +
        '</div><div class="col-lg-7 reveal">' + ul(["Start with a focused use case and prove value before expanding", "Measure quality with evaluation sets from the beginning",
                                                "Keep humans in control of sensitive actions", "Make security, permissions and logging part of the design",
                                                "Review traces and outcomes regularly and improve deliberately"]) + '</div></div></div></section>' +
        cta_band("Ready to start with discovery?", "A short conversation is the first step in the process.")
    )
    return layout("process", "Our AI Development Process", "How StrategicOps delivers agentic AI: discover, assess, architect, engineer, integrate, deploy and optimize.",
                  body, nav="process", crumbs=[("Our Process", None)])


# ------------------------------------------------------------ CASES
def build_cases():
    blocks = ""
    for cid, name, ind, ch, sol, agents, stack, proc in CASES:
        blocks += (
            '<article class="case-full reveal" id="%s"><div class="case-head"><span class="badge-demo">Demonstration project</span><p class="tag">%s</p><h2 class="h3x">%s</h2></div>'
            '<div class="row g-4"><div class="col-lg-6"><h3 class="mini-h">Business challenge</h3><p>%s</p><h3 class="mini-h mt-lg">AI solution architecture</h3><p>%s</p></div>'
            '<div class="col-lg-6"><h3 class="mini-h">Agents involved</h3><ul class="chips">%s</ul><h3 class="mini-h mt-lg">Technology stack</h3><ul class="chips">%s</ul></div>'
            '<div class="col-lg-6"><h3 class="mini-h">Implementation process</h3><ol class="list-num">%s</ol></div>'
            '<div class="col-lg-6"><h3 class="mini-h">Measurable results</h3><p class="placeholder">[No verified results: this is an illustrative architecture. Publish measured results only for real, approved client projects.]</p></div></div></article>'
            % (cid, esc(ind), esc(name), esc(ch), esc(sol), "".join("<li>%s</li>" % esc(a) for a in agents),
               "".join("<li>%s</li>" % esc(s) for s in stack), "".join("<li>%s</li>" % esc(p) for p in proc)))
    body = (
        page_hero("Case studies", "Intelligence applied to real business challenges.",
                  "Real client case studies will be published here once approved. Until then, the projects below are clearly labelled demonstrations of how we would architect typical solutions.",
                  btn("Book an AI Consultation", href("consultation")) + btn("Discuss Your Project", href("contact"), "ghost")) +
        '<section class="sec"><div class="container"><div class="notice reveal" role="note"><strong>About these projects.</strong> They are illustrative demonstration architectures. They are not client engagements, and they include no client names, testimonials or performance metrics.</div>' +
        blocks + '</div></section>' + cta_band("Have a similar challenge?", "We will assess whether an agentic approach fits and what a sensible first project looks like.")
    )
    return layout("cases", "Case Studies & Demonstration Projects", "Demonstration projects showing how StrategicOps architects agentic AI solutions for support, finance and research use cases.",
                  body, nav="cases", crumbs=[("Case Studies", None)])


# ------------------------------------------------------------ INSIGHTS
def build_insights():
    cards = "".join('<div class="col-md-6 col-xl-4">%s</div>' % article_card(a, 2) for a in ARTICLES)
    full, schemas = "", []
    for slug, title, cat, summary, paras in ARTICLES:
        full += ('<article class="article reveal" id="%s"><p class="tag">%s</p><h2 class="h3x">%s</h2><p class="muted">%s &middot; [PUBLISH DATE]</p>%s'
                 '<p><a class="link-arrow" href="#top-articles">Back to all articles%s</a></p></article>'
                 % (slug, esc(cat), esc(title), read_time(paras), "".join("<p>%s</p>" % esc(p) for p in paras), icon("up", "icon icon-sm")))
        schemas.append({"@context": "https://schema.org", "@type": "Article", "headline": title, "description": summary,
                        "articleSection": cat, "author": {"@type": "Organization", "name": SITE["name"]},
                        "publisher": {"@type": "Organization", "name": SITE["name"]},
                        "mainEntityOfPage": SITE["base_url"] + "/" + PAGES["insights"][0] + "#" + slug})
    body = (
        page_hero("Insights & resources", "Thinking beyond the next generation of AI.",
                  "Plain-language explanations of agentic AI, architecture, governance and use cases.",
                  btn("Book an AI Consultation", href("consultation"))) +
        '<section class="sec" id="top-articles"><div class="container"><div class="row g-4">%s</div></div></section>' % cards +
        '<section class="sec sec-alt"><div class="container"><div class="article-col">%s</div></div></section>' % full +
        cta_band("Questions about your own AI plans?", "Talk to us about what these ideas could mean for your organization.")
    )
    return layout("insights", "Insights: Agentic AI Explained", "Articles on agentic AI: what it is, agents vs automation, multi-agent systems, enterprise architecture, RAG, MCP, governance and use cases.",
                  body, nav="insights", crumbs=[("Insights", None)], schema=schemas)


# ------------------------------------------------------------ CONTACT
def build_contact():
    def real(v):
        return not v.startswith("[")
    body = (
        page_hero("Contact", "Discuss your project.",
                  "Tell us about your goals, systems and timeline. We will respond with a sensible next step.",
                  btn("Book an AI Consultation", href("consultation"), "ghost")) +
        '<section class="sec"><div class="container"><div class="row gx-lg-5 gy-5"><div class="col-lg-8 reveal">' +
        '<h2 class="h3x">Project enquiry</h2><p class="lead-sy">Fields marked * are required.</p>' + enquiry_form("enq") + '</div>'
        '<aside class="col-lg-4 reveal"><div class="tile"><h2 class="mini-h">Contact details</h2><ul class="foot-list">'
        '<li><span class="muted">Email</span><br>%s</li><li><span class="muted">Phone</span><br>%s</li><li><span class="muted">Address</span><br>%s</li></ul></div>'
        '<div class="tile spacer-sm"><h2 class="mini-h">Prefer a call?</h2><p>Book a consultation to talk through your use case with an AI specialist.</p>%s</div></aside>'
        '</div></div></section>'
    ) % (
        ('<a href="mailto:%s">%s</a>' % (esc(SITE["email"]), esc(SITE["email"]))) if real(SITE["email"]) else '<span class="placeholder">%s</span>' % esc(SITE["email"]),
        ('<a href="tel:%s">%s</a>' % (esc(SITE["phone"]), esc(SITE["phone"]))) if real(SITE["phone"]) else '<span class="placeholder">%s</span>' % esc(SITE["phone"]),
        '<span class="placeholder">%s</span>' % esc(SITE["address"]),
        btn("Book an AI Consultation", href("consultation"), "link"))
    return layout("contact", "Contact & Project Enquiry", "Contact StrategicOps to discuss agentic AI consulting, custom AI agent development, automation or enterprise AI integration.",
                  body, nav="contact", crumbs=[("Contact", None)])


# ------------------------------------------------------------ CONSULTATION
def build_consultation():
    expect = [("Understand your goal", "We listen to what you want to achieve and which processes are involved."),
              ("Explore feasibility", "We discuss where agentic AI could help, and where simpler options are better."),
              ("Agree next steps", "You leave with a clear view of options, a suggested first step and what we would need to proceed.")]
    body = (
        page_hero("Book an AI consultation", "Start the conversation about intelligent automation.",
                  "A focused discussion with an AI specialist about your goals, systems and the most sensible first project. [CONSULTATION LENGTH AND FORMAT: to be confirmed]") +
        '<section class="sec"><div class="container"><div class="row g-4">' + "".join(
            '<div class="col-md-4"><div class="mini-card reveal"><h2 class="mini-h">%s</h2><p>%s</p></div></div>' % (esc(t), esc(d)) for t, d in expect) +
        '</div></div></section>'
        '<section class="sec sec-alt" id="book"><div class="container">' + sec_head("Choose a time", "Book directly in our calendar.") +
        '<div class="calendar-shell reveal" data-calendar>'
        '<div class="calendar-fallback" data-calendar-fallback><p><strong>Online booking is not connected yet.</strong></p>'
        '<p>Set <code>calendarUrl</code> in <code>js/config.js</code> to your scheduling link (for example a Calendly or Cal.com page) and it will appear here. Until then, send a request below and we will arrange a time.</p></div></div>'
        '<noscript><p class="fineprint">The booking calendar needs JavaScript. Use the request form below instead.</p></noscript></div></section>'
        '<section class="sec"><div class="container"><div class="row gx-lg-5 gy-5"><div class="col-lg-4">' + sec_head("Request a consultation", "Prefer to write first?",
                                                                                                  "Share a few details and we will propose times.") +
        '</div><div class="col-lg-8 reveal">' + enquiry_form("con", default_service="Agentic AI Consulting", intent="consultation") + '</div></div></div></section>'
    )
    return layout("consultation", "Book an AI Consultation", "Book an AI consultation with StrategicOps to discuss agentic AI strategy, custom agent development, automation and enterprise integration.",
                  body, nav="consultation", crumbs=[("Book an AI Consultation", None)])


# ------------------------------------------------------------ LEGAL (templates)
def _legal(key, title, desc, sections):
    body = (
        page_hero("Legal", title, "Last updated: [DATE]") +
        '<section class="sec"><div class="container"><div class="notice" role="note"><strong>Draft template.</strong> This text is a starting point only. Replace placeholders and have it reviewed by qualified legal counsel before publishing.</div>'
        '<div class="legal prose">' + "".join("<h2>%s</h2>%s" % (esc(h), "".join("<p>%s</p>" % t for t in ps)) for h, ps in sections) +
        '</div></div></section>')
    return layout(key, title, desc, body, nav=key, crumbs=[(title, None)])


def build_privacy():
    return _legal("privacy", "Privacy Policy", "How StrategicOps collects, uses and protects personal information submitted through this website.", [
        ("Who we are", ["[LEGAL ENTITY NAME], [REGISTERED ADDRESS] (&ldquo;StrategicOps&rdquo;) is responsible for personal data collected through this website. Contact: [PRIVACY CONTACT EMAIL]."]),
        ("Information we collect", ["Details you submit in our enquiry and consultation forms: name, business email, company, website, industry, company size, service interest, budget, timeline and project description.",
                                    "Technical data such as IP address and browser type, if analytics or server logs are enabled. [CONFIRM ANALYTICS TOOLS IN USE]"]),
        ("How we use it", ["To respond to enquiries, arrange consultations, and improve our services. [ADD LAWFUL BASES FOR YOUR JURISDICTION]"]),
        ("Sharing and retention", ["[LIST PROCESSORS, E.G. FORM HANDLER, CRM, EMAIL PROVIDER, AND RETENTION PERIODS]"]),
        ("Your rights", ["Depending on your location you may have rights to access, correct, delete or restrict use of your data. Contact [PRIVACY CONTACT EMAIL]."]),
    ])


def build_terms():
    return _legal("terms", "Terms & Conditions", "Terms and conditions for using the StrategicOps website.", [
        ("Use of this website", ["By using this website you agree to these terms. Content is provided for general information and does not constitute professional advice."]),
        ("Intellectual property", ["Website content and design belong to [LEGAL ENTITY NAME] unless stated otherwise. Third-party names and trademarks belong to their respective owners."]),
        ("No guarantee of results", ["Descriptions of AI capabilities and potential benefits are illustrative. Outcomes depend on data, systems and implementation."]),
        ("Limitation of liability and governing law", ["[ADD LIABILITY LIMITS AND GOVERNING LAW / JURISDICTION]"]),
    ])


def build_cookies():
    return _legal("cookies", "Cookie Policy", "How StrategicOps uses cookies and similar technologies on this website.", [
        ("What this site stores", ["The static site as supplied sets no tracking cookies. If you add analytics, advertising or a form-protection service such as Cloudflare Turnstile, update this policy and add a consent mechanism where required. [CONFIRM]"]),
        ("Managing cookies", ["You can control cookies through your browser settings."]),
        ("Third-party content", ["Fonts are loaded from Google Fonts and styles from the jsDelivr CDN. A booking calendar embed, if configured, is provided by a third party with its own policies. [CONFIRM AND DOCUMENT]"]),
    ])
