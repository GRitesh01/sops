import math
from html import escape as esc
from common import *
from data import *


# ------------------------------------------------------------ reusable components
def read_time(paras):
    words = sum(len(p.split()) for p in paras)
    return "%d min read" % max(1, math.ceil(words / 200))


def article_card(a, lvl=3):
    slug, title, cat, summary, paras = a
    return ('<article class="tile post" data-tilt data-cursor="Read"><div class="post-meta"><span class="tag">%s</span><span class="muted">[PUBLISH DATE]</span><span class="muted">%s</span></div>'
            '<h%d class="card-title"><a class="stretch" href="%s">%s</a></h%d><p>%s</p><span class="link-arrow" aria-hidden="true">Read article%s</span></article>'
            % (esc(cat), read_time(paras), lvl, href("insights", slug), esc(title), lvl, esc(summary), icon("arrow-ur", "icon icon-sm")))


def solution_card(s):
    sid, ic, title, blurb, items, _ = s
    return ('<article class="tile sol" data-tilt data-cursor="Explore"><div class="card-ic">%s</div><h3 class="card-title">%s</h3><p class="sol-blurb">%s</p>'
            '<ul class="list-dash">%s</ul><a class="link-arrow stretch" href="%s">Explore %s%s</a></article>'
            % (icon(ic), esc(title), esc(blurb), "".join("<li>%s</li>" % esc(i) for i in items), href("solutions", sid), esc(title), icon("arrow-ur", "icon icon-sm")))


def industry_tabs(prefix="ind", lvl=3):
    def ul(items):
        return "<ul class='list-dash'>%s</ul>" % "".join("<li>%s</li>" % esc(x) for x in items)

    tabs, panels = "", ""
    for i, (iid, name, ch, ap, ag, integ, ben) in enumerate(INDUSTRIES):
        sel = i == 0
        tabs += ('<button class="tab" role="tab" id="%s-t-%s" aria-controls="%s-p-%s" aria-selected="%s" tabindex="%s" type="button" data-cursor="Select">%s</button>'
                 % (prefix, iid, prefix, iid, str(sel).lower(), "0" if sel else "-1", esc(name)))

        def col(cls, title, items):
            return '<div class="%s"><div class="facet"><h%d class="mini-h">%s</h%d>%s</div></div>' % (cls, lvl + 1, title, lvl + 1, ul(items))

        panels += ('<div class="tab-panel" role="tabpanel" id="%s-p-%s" aria-labelledby="%s-t-%s"%s tabindex="0">'
                   '<h%d class="panel-title">%s</h%d><div class="row g-3">%s%s%s%s%s</div>'
                   '<p class="fineprint">Outcomes depend on data quality, process design and implementation. No results are guaranteed.</p></div>'
                   % (prefix, iid, prefix, iid, "" if sel else " hidden", lvl, esc(name), lvl,
                      col("col-md-6 col-xl-4", "Business challenges", ch), col("col-md-6 col-xl-4", "Potential AI applications", ap),
                      col("col-md-6 col-xl-4", "Recommended agent types", ag), col("col-md-6 col-xl-6", "Integration opportunities", integ),
                      col("col-md-6 col-xl-6", "Potential operational benefits", ben)))
    return ('<div class="tabs-sy" data-tabs data-hash-tabs="%s"><div class="tab-list" role="tablist" aria-label="Industries">%s</div>%s</div>' % (prefix, tabs, panels))


def tech_grid():
    out = ""
    for tid, name, items, _ in TECH_LAYERS:
        out += ('<div class="col-md-6 col-xl-4"><div class="tech-layer" data-tilt><h3 class="tech-h">%s</h3><ul class="chips">%s</ul></div></div>'
                % (esc(name), "".join("<li>%s</li>" % esc(i) for i in items)))
    return '<div class="row g-3">%s</div>' % out


def timeline(compact=True):
    lv = 3 if compact else 2
    tone = ["cobalt", "sun", "ink", "white", "cobalt", "sun", "ink"]
    out = ""
    for i, (t, d, long, deliv) in enumerate(PROCESS):
        extra = "" if compact else "<p class='tl-long'>%s</p><ul class='list-dash'>%s</ul>" % (esc(long), "".join("<li>%s</li>" % esc(x) for x in deliv))
        out += ('<li class="stack-card tone-%s" style="--i:%d"><span class="tl-num">%02d</span><div><h%d class="tl-title">%s</h%d><p>%s</p>%s</div></li>'
                % (tone[i], i, i + 1, lv, t, lv, esc(d), extra))
    return '<ol class="stack" data-stack>%s</ol>' % out


def multi_agent_explainers():
    items = [("Agent coordination", "An orchestrator sequences work, tracks state and decides when a task is complete."),
             ("Task delegation", "Sub-tasks are routed to the agent with the right instructions and tools."),
             ("Shared context", "Agents read from and write to a common, access-controlled context."),
             ("Memory management", "Short-term working memory and long-term knowledge are kept separate and governed."),
             ("Tool integration", "Agents reach systems through approved tools with scoped permissions."),
             ("Human-in-the-loop approvals", "Defined actions pause for a person to approve, edit or reject."),
             ("Execution monitoring", "Every step is traced so behaviour can be inspected, evaluated and audited.")]
    return '<div class="row g-3">%s</div>' % "".join(
        '<div class="col-sm-6 col-xl-3"><div class="mini-card" data-tilt><h3>%s</h3><p>%s</p></div></div>' % (esc(a), esc(b)) for a, b in items)


def board_block():
    return ('<div class="board-wrap"><div data-agent-board><noscript><p class="fineprint">The interactive board requires JavaScript. Flow: user request, AI orchestrator, '
            'research, planning, data and execution agents, shared context, human approval, validation and evaluation, final result.</p></noscript></div></div>')


# ------------------------------------------------------------ HOME
def build_home():
    hero = (
        '<section class="hero" id="top"><canvas class="hero-canvas" id="hero-canvas" data-hero-canvas aria-hidden="true"></canvas>'
        '<div class="container hero-inner"><div class="hero-copy"><p class="eyebrow">Agentic AI engineering &amp; consulting</p>'
        '<h1 class="display">Strategy that thinks. <span class="hl">Operations that act.</span></h1>'
        '<p class="lead-sy">StrategicOps Global Consulting designs, builds and deploys intelligent AI agents that reason, collaborate and execute complex workflows, turning everyday operations into scalable, intelligent execution.</p>'
        '<div class="btn-row">' + btn("Explore AI Solutions", href("services")) + btn("Book an AI Consultation", href("consultation"), "ghost") + '</div></div></div>'
        '<p class="hero-hint" aria-hidden="true"><span class="pulse-dot"></span> Move your cursor. Click to send a signal.</p></section>'
        + marquee(["Agentic AI Consulting", "Custom AI Agents", "Multi-Agent Systems", "AI Automation", "Enterprise AI Integration", "RAG & Knowledge Systems", "AI Governance"], "mq-cobalt"))

    vals = [("autonomy", "Autonomous intelligence", "Agents that interpret goals, plan the steps and use tools to get work done, inside the boundaries you set."),
            ("automation", "Intelligent automation", "Workflows that handle unstructured inputs and exceptions, not only fixed rules."),
            ("integration", "Enterprise integration", "AI connected to your applications, databases and APIs, so it works inside real processes."),
            ("architecture", "Scalable AI architecture", "Modular designs for orchestration, knowledge and monitoring that grow with your needs.")]
    statement = (
        '<section class="sec sec-ink statement" id="value"><div class="container"><p class="eyebrow">Intelligence that moves business forward</p>'
        '<h2 class="statement-text" data-spotlight data-text="Beyond chatbots. Into autonomous operations.">Beyond chatbots. Into autonomous operations.</h2>'
        '<ul class="vrows">' + "".join(
            '<li class="vrow" data-cursor="Read"><span class="vr-ic">%s</span><h3>%s</h3><p>%s</p><span class="vr-go" aria-hidden="true">%s</span></li>' % (icon(i), t, d, icon("arrow-ur")) for i, t, d in vals) +
        '</ul></div></section>')

    def pillar(tone, n, title, desc, items, cta, link):
        return ('<article class="pillar tone-%s" data-tilt data-cursor="Open"><p class="pillar-n">Pillar %s</p><h3 class="pillar-t">%s</h3><p>%s</p><ul class="list-dash">%s</ul>%s</article>'
                % (tone, n, title, desc, "".join("<li>%s</li>" % i for i in items), btn(cta, link, "link")))

    what = (
        '<section class="sec" id="what-we-do"><div class="container">' + sec_head("What we do", "From AI strategy to autonomous execution.") +
        '<div class="row g-3"><div class="col-lg-4">' +
        pillar("cobalt", "01", "AI Consulting", "Identify AI opportunities, evaluate feasibility, develop strategies and establish an implementation roadmap.",
               ["AI Readiness Assessment", "Business Process Analysis", "AI Opportunity Discovery", "Agentic AI Strategy", "AI Architecture Consulting", "AI Governance Advisory"], "Explore AI Consulting", href("consulting")) +
        '</div><div class="col-lg-4">' +
        pillar("sun", "02", "AI Agent Development", "Build intelligent autonomous agents that can reason, plan, use tools, interact with systems and execute business tasks.",
               ["Custom AI Agents", "Multi-Agent Systems", "Research Agents", "Conversational Agents", "Knowledge Agents", "Enterprise AI Assistants"], "Explore Agent Development", href("agents")) +
        '</div><div class="col-lg-4">' +
        pillar("white", "03", "AI Integration &amp; Transformation", "Connect intelligent AI systems with existing applications, databases, APIs and enterprise workflows.",
               ["Enterprise AI Integration", "Workflow Automation", "CRM &amp; ERP Integration", "RAG &amp; Knowledge Systems", "AI Application Development", "AI Deployment &amp; Monitoring"], "Explore AI Integration", href("integration")) +
        '</div></div></div></section>')

    loop = (
        '<section class="sec sec-cobalt" id="capabilities"><div class="ph-grid" aria-hidden="true"></div><div class="container">' +
        sec_head("How an agent works", "The agent loop, from task to outcome.",
                 "Perceive, understand, plan, remember, call tools, act and evaluate. Pick a stage or press play to follow a sample task around the loop.") +
        '<div data-agent-loop class="loop"><noscript><p class="fineprint">Interactive diagram requires JavaScript. Stages: perception and input, context understanding, reasoning and planning, memory and knowledge, tool calling, task execution, and evaluation and feedback.</p></noscript></div>'
        '<div class="callout reveal"><h3 class="mini-h">Autonomy is configured, not assumed</h3>'
        '<p>Each agent operates with defined permissions, human approval points and safety controls. The level of autonomy is set per workflow and widened only as evidence supports it.</p></div>'
        '</div></section>')

    multi = (
        '<section class="sec" id="multi-agent"><div class="container">' +
        sec_head("Multi-agent systems", "One intelligent ecosystem. Multiple specialised agents.",
                 "This is a live mission-control board. Drag any node, select one to read its role, then dispatch a request to watch it travel from orchestrator to result.") +
        board_block() + '<div class="spacer-lg"></div>' + multi_agent_explainers() +
        '<div class="sec-foot">' + btn("Explore multi-agent systems", href("multi"), "link") + '</div></div></section>')

    solutions = (
        '<section class="sec sec-white" id="solutions"><div class="container">' + sec_head("Solutions by business function", "Intelligent solutions for every business function.") +
        '<div class="row g-3">' + "".join('<div class="col-md-6 col-xl-4">%s</div>' % solution_card(s) for s in SOLUTIONS) +
        '<div class="col-md-6 col-xl-4"><article class="tile sol sol-more" data-cursor="Talk"><h3 class="card-title">Not seeing your function?</h3>'
        '<p>Agentic AI applies wherever work involves information, decisions and systems. Tell us about your process.</p>' + btn("Discuss Your Project", href("contact"), "link") + '</article></div></div></div></section>')

    industries = (
        '<section class="sec" id="industries"><div class="container">' + sec_head("Industry solutions", "Agentic AI across industries.",
                                                                              "Typical challenges, applications and agent types for each sector.") +
        industry_tabs("ind") + '<div class="sec-foot">' + btn("See all industry solutions", href("industries"), "link") + '</div></div></section>')

    tech = (
        '<section class="sec sec-ink" id="technology"><div class="container">' + sec_head("Technology stack", "Engineered with modern AI technologies.",
                                                                                      "We select technologies per project. This is the toolbox we work from, organised by layer.") +
        tech_grid() + '<div class="sec-foot">' + btn("Technology in depth", href("technology"), "link") + '</div></div></section>')

    process = (
        '<section class="sec" id="process"><div class="container"><div class="row gx-lg-5 gy-4"><div class="col-lg-4"><div class="sticky-head">' +
        sec_head("Our development process", "From business challenge to intelligent execution.") + btn("See the full process", href("process"), "link") +
        '</div></div><div class="col-lg-8">' + timeline(True) + '</div></div></div></section>')

    cases = (
        '<section class="sec sec-white" id="case-studies"><div class="container">' + sec_head("Case studies", "Intelligence applied to real business challenges.",
            "Our first published case studies will appear here. Until then, these demonstration projects show how we would architect typical solutions. They are not client engagements.") +
        '<div class="row g-3">' + "".join(
            '<div class="col-lg-4"><article class="tile case" data-tilt data-cursor="View"><span class="badge-demo">Demonstration project</span><p class="tag">%s</p><h3 class="card-title">%s</h3><p>%s</p>%s</article></div>'
            % (esc(c[2]), esc(c[1]), esc(c[3]), btn("View architecture", href("cases", c[0]), "link")) for c in CASES) + '</div></div></section>')

    why = [("Business-first AI consulting", "We start from the process and the outcome, then choose the technology."),
           ("Purpose-built AI architecture", "Designs are shaped to your systems, data and risk profile."),
           ("Multi-agent engineering expertise", "We design and orchestrate specialised agents, not only single chatbots."),
           ("Enterprise integration capabilities", "Agents connect to your applications, databases and APIs."),
           ("Security-conscious development", "Permissions, audit logs and data handling are designed in from the start."),
           ("Human-supervised autonomy", "Approval points and oversight are part of the architecture."),
           ("Continuous optimization", "Tracing and evaluation guide ongoing improvements."),
           ("Scalable implementation strategies", "Start with a focused use case and expand as results justify.")]
    whyc = (
        '<section class="sec sec-cobalt" id="why"><div class="ph-grid" aria-hidden="true"></div><div class="container">' + sec_head("Why choose us", "Built on engineering. Guided by intelligence.") +
        '<div class="row g-3">' + "".join('<div class="col-md-6 col-xl-3"><div class="why-item" data-tilt><span class="why-ic">%s</span><h3>%s</h3><p>%s</p></div></div>'
                                          % (icon("check", "icon icon-sm"), t, d) for t, d in why) + '</div></div></section>')

    ins = (
        '<section class="sec" id="insights"><div class="container">' + sec_head("Insights & resources", "Thinking beyond the next generation of AI.") +
        '<div class="row g-3">' + "".join('<div class="col-md-6 col-xl-4">%s</div>' % article_card(a) for a in ARTICLES[:6]) +
        '</div><div class="sec-foot">' + btn("All insights", href("insights"), "link") + '</div></div></section>')

    final = cta_band("Your next business advantage starts with intelligence.",
                     "Whether you are exploring Agentic AI, modernizing business operations or building autonomous enterprise systems, let&rsquo;s identify the right approach for your organization.")

    body = hero + statement + what + loop + multi + solutions + industries + tech + process + cases + whyc + ins + final
    return layout("home", "StrategicOps Global Consulting | Agentic AI Engineering & Consulting",
                  "StrategicOps Global Consulting designs, builds and deploys intelligent autonomous AI systems: agentic AI consulting, custom AI agent development and enterprise AI integration.",
                  body, nav="home", full_title=True)
