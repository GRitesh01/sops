from html import escape as esc
from common import *
from data import *
from pages_home import multi_agent_explainers, board_block

TRUST = [
    ("Secure API integrations", "Agents reach systems through authenticated, validated and rate-limited interfaces."),
    ("Authentication and authorization", "Each agent has its own identity and only the roles it needs."),
    ("Data access controls", "Retrieval and tools respect existing permissions, so agents see only what they are allowed to."),
    ("Human approval mechanisms", "Defined actions pause for a person to approve, edit or reject."),
    ("Agent permission boundaries", "Allowed tools, data and actions are explicit, minimal and reviewable."),
    ("Audit logs", "Inputs, decisions, tool calls and outputs are recorded for review."),
    ("Data privacy considerations", "Data handling, retention and residency are designed with your policies and regulations in mind."),
    ("AI evaluation", "Test sets and review processes measure quality before and after release."),
    ("Monitoring and observability", "Tracing, metrics and alerts show what agents are doing in production."),
    ("Failure handling", "Retries, fallbacks and escalation paths define what happens when something goes wrong."),
]

S = {}

S["consulting"] = dict(
    title="Agentic AI Consulting", nav="consulting",
    desc="Agentic AI consulting from StrategicOps: AI readiness assessments, process discovery, opportunity mapping, architecture strategy, governance and implementation roadmaps.",
    eyebrow="Agentic AI Consulting", h1="Turn AI possibilities into business strategy.",
    sub="Decide where autonomous AI creates value for your organization, how to build it safely and in what order.",
    sections=[
        ("What is Agentic AI Consulting?", "It is the work that happens before and alongside engineering: choosing the right problems, the right architecture and the right level of autonomy, so AI investment is tied to business outcomes.", None),
        ("AI readiness assessment", "A structured review of data availability, systems, skills, security posture and organizational readiness, giving a clear view of strengths, gaps and prerequisites.", ["Data and systems review", "Security and compliance review", "Skills and operating-model review"]),
        ("Business process discovery", "We map how work really flows, including inputs, decisions, handoffs and exceptions, to find the steps where agents can assist or act.", None),
        ("AI opportunity mapping", "Candidate use cases are assessed on business value, feasibility, risk and effort, producing a prioritised shortlist instead of a long wish list.", None),
        ("Feasibility analysis", "We test the riskiest assumptions early, such as data quality, accuracy requirements and integration access, so investment decisions rest on evidence.", None),
        ("Agentic architecture strategy", "Recommendations on single-agent versus multi-agent designs, model options, knowledge strategy, tool boundaries and human oversight.", None),
        ("AI governance and security", "Policies and controls for permissions, approvals, audit logging, data handling and evaluation, aligned to your regulatory context.", None),
        ("Implementation roadmap", "A phased plan with milestones, dependencies, ownership and success criteria, ready to execute with your team or with us.", None),
        ("Consulting engagement model", "Engagements can be scoped as a short assessment, a roadmap sprint or an ongoing advisory relationship. [ENGAGEMENT STRUCTURE, DURATION AND PRICING: to be defined by StrategicOps]", None),
    ],
    faq=[("Do we need to have data ready before we start?", "No. Part of the assessment is establishing what data exists, where it lives and how usable it is. The output is a plan for closing any gaps."),
         ("Is consulting separate from development?", "It can be. Many organizations start with a consulting engagement and then build with us, with their own team or with another partner. The roadmap is designed to be actionable either way."),
         ("How do you decide whether we need agents at all?", "We compare simpler options, such as rules-based automation or conventional software, with agentic approaches and recommend the simplest solution that meets the need."),
         ("How do you handle sensitive data during assessment?", "We agree data-handling rules at the outset and can work from samples, anonymised data or inside your environment, depending on your requirements.")],
    cta=("Start with a consultation", "Tell us about your goals and we will outline the most sensible first step.", "Book an AI Consultation", "consultation"))

S["agents"] = dict(
    title="Custom AI Agent Development", nav="agents",
    desc="Custom AI agent development from StrategicOps: purpose-built agents with reasoning, planning, tool integrations, memory, human-in-the-loop controls, evaluation and monitoring.",
    eyebrow="AI Agent Development", h1="Intelligent agents. Purpose-built for your business.",
    sub="Agents that reason, plan, use your tools and complete real tasks, with the controls enterprises need.",
    sections=[
        ("Custom AI agents", "We design agents around a specific job: its inputs, goals, tools, constraints and definition of done. Focused agents tend to be more reliable than general-purpose ones.", ["Research agents", "Conversational agents", "Knowledge agents", "Enterprise AI assistants"]),
        ("Reasoning and planning", "Agents break goals into steps, choose actions and revise their plans based on what they find. We select the planning approach that fits the task, from simple tool loops to explicit workflow graphs.", None),
        ("Tool integrations", "Agents act through tools: APIs, databases, search, internal systems. Each tool is defined with clear inputs, outputs and scoped permissions, using open protocols such as MCP where appropriate.", None),
        ("Memory and context", "We separate working memory for the current task from long-term knowledge and history, using retrieval to bring in the right information with the right access controls.", None),
        ("Agent workflows", "For processes with required steps, agents run inside defined workflows with branching, retries and checkpoints, combining flexible reasoning with predictable structure.", None),
        ("Human-in-the-loop controls", "Approval steps, review queues and escalation rules let people supervise sensitive actions. Autonomy can be widened over time as measured quality supports it.", None),
        ("Evaluation and testing", "We build evaluation sets from real examples and test accuracy, safety behaviour and regressions before release and after every change.", None),
        ("Deployment and monitoring", "Agents ship with tracing, logging, cost and latency monitoring, and alerting, deployed in your cloud or a private environment.", None),
        ("Use cases", "Typical starting points include support triage, document processing, research and reporting, lead research and internal knowledge assistants. See solutions by business function.", None),
    ],
    faq=[("What is the difference between an AI agent and a chatbot?", "A chatbot mainly responds to messages. An agent pursues a goal: it can plan steps, call tools, act on systems and check its own results, within permissions you define."),
         ("Can agents take actions without approval?", "Only if you configure them to. Actions are classified by risk, and higher-risk actions can require human approval."),
         ("Which models do you use?", "We choose per use case, considering capability, cost, latency and data requirements. Architectures are designed so the model can be changed."),
         ("How do you measure whether an agent is good enough?", "By testing against representative examples agreed with you and tracking agreed metrics in production. We do not promise a fixed accuracy before we have tested your data.")],
    cta=("Discuss an agent project", "Describe the task you want an agent to handle and we will propose an approach.", "Start a Project Enquiry", "contact"))

S["multi"] = dict(
    title="Multi-Agent Systems", nav="multi",
    desc="Multi-agent systems engineering from StrategicOps: orchestration, specialised agent roles, communication protocols, shared memory, failure recovery and observability.",
    eyebrow="Multi-Agent Systems", h1="Orchestrating intelligence at scale.",
    sub="Specialised agents, coordinated by an orchestrator, working from shared context to deliver complex outcomes.",
    sections=[
        ("Multi-agent architecture", "Complex work is decomposed across agents with distinct roles. We design the topology (hierarchical, pipeline or collaborative) to match how the work really flows.", None),
        ("Agent orchestration", "An orchestrator interprets the request, plans, delegates, tracks state and decides when to stop. Orchestration can be explicit workflow graphs or dynamic planning.", None),
        ("Specialized agent roles", "Typical roles include research, planning, data, execution and review agents. Narrow roles keep instructions and tools focused and easier to test.", ["Research Agent", "Planning Agent", "Data Agent", "Execution Agent", "Review Agent"]),
        ("Communication protocols", "Agents exchange structured messages. We use frameworks and open protocols such as A2A and MCP where they fit, and keep message formats explicit and logged.", None),
        ("Shared memory", "A governed shared context lets agents build on each other's work, with controls on who can read and write what.", None),
        ("Workflow coordination", "Parallel and sequential work, dependencies, timeouts and handoffs are coordinated so results arrive complete and in order.", None),
        ("Failure recovery", "We design for failure: retries, fallbacks, checkpoints, loop and budget limits, and escalation to a person when the system cannot proceed confidently.", None),
        ("Evaluation and observability", "End-to-end and per-agent evaluation, plus tracing across agents, show where quality is gained or lost.", None),
        ("Enterprise applications", "Common applications include research teams, document pipelines, operations monitoring and complex customer workflows. We recommend multiple agents only where they add clear value.", None),
    ],
    faq=[("When do I need multiple agents instead of one?", "When a task has distinct phases or skills, benefits from independent review, or exceeds what one agent can handle reliably. Otherwise a single agent is simpler to build, test and run."),
         ("Do more agents mean more cost?", "Often, yes, because more model calls are made. We design with cost budgets and measure whether added agents improve results enough to justify it."),
         ("How do agents avoid conflicting with each other?", "Through an orchestrator, defined ownership of tasks and data, and controlled shared state."),
         ("Which frameworks do you use?", "LangGraph, CrewAI, AutoGen and Semantic Kernel are in our toolbox, and we can build lightweight custom orchestration when that is the better fit.")],
    cta=("Plan your multi-agent system", "Share the workflow you want to orchestrate and we will map the agent roles with you.", "Book an AI Consultation", "consultation"),
    extra="multi")

S["automation"] = dict(
    title="AI Automation", nav="automation",
    desc="AI automation from StrategicOps: workflow discovery, agent-powered workflows, API integrations, approval flows and monitoring to turn complex processes into intelligent operations.",
    eyebrow="AI Automation", h1="Transform complex workflows into intelligent operations.",
    sub="Combine dependable workflow automation with agents that handle unstructured inputs, exceptions and decisions.",
    sections=[
        ("Workflow discovery", "We identify high-volume, repetitive and exception-prone processes and document how they work today, including the cases that break the rules.", None),
        ("Automation architecture", "We design the split between deterministic steps, which are fast and predictable, and agent steps, which interpret and decide. Triggers, queues and error paths are defined up front.", None),
        ("Agent-powered workflows", "Agents read emails and documents, classify requests, extract data, draft responses and decide the next step, inside a workflow that keeps the overall process controlled.", None),
        ("API integrations", "Workflows connect to your systems through APIs and event streams, using orchestration tools such as n8n or custom services as appropriate.", None),
        ("Business process automation", "From intake to completion, we automate end-to-end processes such as onboarding, claims-style handling, reporting and order exceptions.", None),
        ("Approval workflows", "Approval steps are first-class: the right person is asked to approve with the right context, and the decision is recorded.", None),
        ("Monitoring and optimization", "Dashboards and alerts show volumes, outcomes, exceptions and costs. Traces reveal where to improve, and what to automate next.", None),
        ("Industry use cases", "Examples include invoice handling in finance, shipment exceptions in logistics, enquiry handling in retail and document intake in professional services.", None),
    ],
    faq=[("How is AI automation different from RPA or standard workflow tools?", "Standard tools follow predefined rules. AI automation adds agents that can interpret unstructured information and handle variation. We often combine both."),
         ("What processes are the best candidates?", "High-volume, text- or document-heavy processes with clear outcomes and some variation. Discovery helps rank candidates."),
         ("Can we keep people involved?", "Yes. Approval steps, review queues and exception handling are designed in, and autonomy can grow gradually."),
         ("Do you replace our existing tools?", "Usually not. We integrate with the systems you already use.")],
    cta=("Find your first workflow to automate", "Describe a process that slows your team down and we will assess how AI could help.", "Book an AI Consultation", "consultation"))

S["enterprise"] = dict(
    title="Enterprise AI Solutions", nav="enterprise",
    desc="Enterprise AI solutions from StrategicOps: secure architecture, private and cloud deployment, knowledge systems, identity and access control, governance and monitoring.",
    eyebrow="Enterprise AI Solutions", h1="Bring intelligence into your enterprise ecosystem.",
    sub="Production-grade agentic AI designed around your security, governance, data and operating requirements.",
    sections=[
        ("Enterprise AI architecture", "Reference architectures covering orchestration, tools, knowledge, identity, evaluation and human review, adapted to your environment and standards.", None),
        ("Private and cloud deployments", "Agents can run in your cloud, in a private environment or in hybrid setups, using containers and orchestration platforms, with model options that match your data policies.", None),
        ("Enterprise knowledge systems", "Retrieval systems over your documents and data with ingestion pipelines, hybrid search and permission-aware access.", None),
        ("Data integration", "Secure connections to data warehouses, operational databases, document stores and business applications.", None),
        ("Identity and access control", "Agents and users authenticate through your identity systems. Role-based access limits what each can see and do.", None),
        ("Security and governance", "Permission boundaries, approval policies, audit logs, data-handling rules and review processes, defined with your security and compliance teams.", None),
        ("Monitoring and evaluation", "Tracing, metrics, evaluation pipelines and alerting provide visibility into quality, safety, cost and usage.", None),
        ("Deployment strategy", "Staged rollouts, from pilot to supervised production to wider autonomy, with rollback plans and operational runbooks.", None),
    ],
    faq=[("Can our data stay in our own environment?", "Often, yes. Private and hybrid deployments are possible, depending on the models and infrastructure you choose. We review options against your data policies."),
         ("How do you approach compliance?", "We design controls such as access management, logging and data handling to support your obligations and work with your compliance team. We do not claim to certify compliance."),
         ("How do agents get access to internal systems?", "Through service identities with least-privilege permissions, exposed via governed tool interfaces."),
         ("Can you work with our internal engineering team?", "Yes. We can build jointly, hand over documentation and train your team to operate the system.")],
    cta=("Plan an enterprise AI deployment", "Speak with us about security, integration and rollout for your organization.", "Book an AI Consultation", "consultation"),
    extra="trust")

S["integration"] = dict(
    title="AI Integration", nav="integration",
    desc="AI integration services from StrategicOps: connect AI agents to CRM, ERP, databases, APIs, document systems, knowledge bases and internal applications.",
    eyebrow="AI Integration", h1="Connect AI with the systems that power your business.",
    sub="Agents are only as useful as the systems they can reach. We connect them securely to the tools and data your teams already use.",
    sections=[
        ("CRM integration", "Agents read and update customer and pipeline records, log activity and prepare follow-ups, with approval where changes are sensitive.", None),
        ("ERP integration", "Connect agents to finance, inventory and order processes for tasks such as document matching, exception handling and reporting.", None),
        ("Database integration", "Governed access to operational and analytical databases, including read-only patterns and query guardrails.", None),
        ("API integration", "Well-defined tool interfaces over REST and event-based APIs, with authentication, validation, rate limits and error handling.", None),
        ("Document systems", "Ingest and act on content from document management systems, shared drives and email, including extraction from PDFs and scans.", None),
        ("Knowledge bases", "Make wikis, help centres and policy libraries searchable through retrieval, keeping content fresh and access-controlled.", None),
        ("Internal applications", "Embed agents inside the tools your teams use, or expose them through new interfaces for review and approval.", None),
        ("Third-party platforms", "Connect to external SaaS platforms and partners through their APIs, using open protocols such as MCP where available.", None),
        ("Integration architecture", "We design the integration layer for security, observability and change: clear contracts, versioning, logging and a way to test end-to-end.", None),
    ],
    faq=[("What if our systems have no API?", "We assess options such as database access, file exchange or UI-level automation, and tell you the trade-offs, including when it is better to modernise the interface first."),
         ("Will agents be able to change records?", "Only where you allow it. Write actions can be limited, logged and approval-gated."),
         ("How do you keep integrations secure?", "Least-privilege credentials, secrets management, network controls, input validation and audit logging."),
         ("Can you integrate with legacy systems?", "Often, yes. Feasibility depends on the available interfaces. We review this during assessment.")],
    cta=("Map your integrations", "List the systems your AI needs to reach and we will propose an integration approach.", "Book an AI Consultation", "consultation"))


# Operations-led hero copy for StrategicOps
S["consulting"].update(h1="Turn AI possibilities into an operating strategy.", sub="Work out where autonomous AI belongs in your operating model, how to introduce it safely, and in what order.")
S["agents"].update(h1="Agents built around the way your business runs.", sub="Purpose-built agents that reason, plan and complete real tasks in your tools, with the controls enterprises need.")
S["multi"].update(h1="Specialist agents. One coordinated operation.", sub="Orchestrated teams of agents working from shared context to deliver outcomes no single agent could reliably handle.")
S["automation"].update(h1="From manual handoffs to intelligent operations.", sub="Pair dependable workflow automation with agents that handle unstructured inputs, exceptions and decisions.")
S["enterprise"].update(h1="Enterprise intelligence, inside your guardrails.", sub="Production-grade agentic AI designed around your security, governance, data and operating requirements.")
S["integration"].update(h1="Plug AI into the systems that run the business.", sub="Agents are only as useful as the systems they can reach. We connect them securely to the tools and data your teams already use.")


def _section_block(i, title, text, bullets):
    b = "<ul class='list-dash'>%s</ul>" % "".join("<li>%s</li>" % esc(x) for x in bullets) if bullets else ""
    return ('<article class="block reveal"><div class="block-n">%02d</div><div class="block-body"><h2>%s</h2><p>%s</p>%s</div></article>'
            % (i, esc(title), esc(text), b))


def build_service(key):
    d = S[key]
    fhtml, fschema = faq(d["faq"], "faq")
    secs = "".join(_section_block(i + 1, t, x, b) for i, (t, x, b) in enumerate(d["sections"]))
    extra = ""
    if d.get("extra") == "multi":
        extra = ('<section class="sec sec-alt"><div class="container">' +
                 sec_head("Interactive architecture", "See how agents collaborate.", "Drag any node, select it to read its role, or dispatch a sample request.") +
                 board_block() + '<div class="spacer-lg"></div>' + multi_agent_explainers() + '</div></section>')
    if d.get("extra") == "trust":
        extra = ('<section class="sec sec-alt" id="trust"><div class="container">' +
                 sec_head("Security and enterprise trust", "Autonomy within clear boundaries.",
                          "Controls we design into enterprise agent systems. Security is a continuous practice, and no system is risk-free, so we aim to make risks visible, bounded and monitored.") +
                 '<div class="row g-0 why-grid">' + "".join(
                     '<div class="col-md-6 col-xl-4"><div class="why-item reveal"><span class="why-ic">%s</span><h3>%s</h3><p>%s</p></div></div>'
                     % (icon("shield", "icon icon-sm"), esc(t), esc(x)) for t, x in TRUST) + '</div></div></section>')
    body = (
        page_hero(d["eyebrow"], d["h1"], d["sub"], btn(d["cta"][2], href(d["cta"][3])) + btn("All services", href("services"), "ghost")) +
        '<section class="sec"><div class="container"><div class="blocks">' + secs + '</div></div></section>' + extra +
        '<section class="sec%s" id="faq"><div class="container"><div class="row gx-lg-5 gy-5"><div class="col-lg-4">' % ("" if extra else " sec-alt") +
        sec_head("FAQ", "Common questions.") + '</div><div class="col-lg-8 reveal">' + fhtml + '</div></div></div></section>' +
        cta_band(d["cta"][0], d["cta"][1], (d["cta"][2], d["cta"][3]), ("Discuss Your Project", "contact") if d["cta"][3] != "contact" else ("Book an AI Consultation", "consultation"))
    )
    return layout(key, d["title"], d["desc"], body, nav=key, crumbs=[("Services", "services"), (d["title"], None)],
                  schema=[service_schema(d["title"], d["desc"], key), fschema])


def build_services():
    def pillar(n, title, desc, items, links):
        return ('<article class="pillar tone-white" data-tilt><p class="pillar-n">Pillar %s</p><h2 class="pillar-t">%s</h2><p>%s</p><ul class="list-dash">%s</ul><div class="pillar-links">%s</div></article>'
                % (n, title, desc, "".join("<li>%s</li>" % esc(i) for i in items),
                   "".join(btn(l, href(k), "link") for l, k in links)))

    body = (
        page_hero("Services", "From AI strategy to autonomous execution.",
                  "Three connected capabilities: consult on where AI creates value, build the agents, and integrate them into the way your organization works.",
                  btn("Book an AI Consultation", href("consultation")) + btn("Discuss Your Project", href("contact"), "ghost")) +
        '<section class="sec"><div class="container"><div class="row g-4"><div class="col-lg-4">' +
        pillar("01", "AI Consulting", "Identify opportunities, evaluate feasibility, develop strategy and establish an implementation roadmap.",
               ["AI Readiness Assessment", "Business Process Analysis", "AI Opportunity Discovery", "Agentic AI Strategy", "AI Architecture Consulting", "AI Governance Advisory"],
               [("Agentic AI Consulting", "consulting")]) + '</div><div class="col-lg-4">' +
        pillar("02", "AI Agent Development", "Build autonomous agents that reason, plan, use tools, interact with systems and execute business tasks.",
               ["Custom AI Agents", "Multi-Agent Systems", "Research Agents", "Conversational Agents", "Knowledge Agents", "Enterprise AI Assistants"],
               [("AI Agent Development", "agents"), ("Multi-Agent Systems", "multi")]) + '</div><div class="col-lg-4">' +
        pillar("03", "AI Integration &amp; Transformation", "Connect AI systems with existing applications, databases, APIs and enterprise workflows.",
               ["Enterprise AI Integration", "Workflow Automation", "CRM &amp; ERP Integration", "RAG &amp; Knowledge Systems", "AI Application Development", "AI Deployment &amp; Monitoring"],
               [("AI Integration", "integration"), ("AI Automation", "automation"), ("Enterprise AI Solutions", "enterprise")]) +
        '</div></div></div></section>'
        '<section class="sec sec-alt"><div class="container">' + sec_head("Service pages", "Explore each service in depth.") +
        '<div class="row g-4">' + "".join(
            '<div class="col-md-6 col-xl-4"><article class="tile" data-tilt><h3 class="card-title">%s</h3><p>%s</p><a class="link-arrow stretch" href="%s">Learn more%s</a></article></div>'
            % (esc(S[k]["title"]), esc(S[k]["sub"]), href(k), icon("arrow", "icon icon-sm")) for k in ["consulting", "agents", "multi", "automation", "enterprise", "integration"]) +
        '</div></div></section>' +
        cta_band("Not sure which service you need?", "Start with a conversation. We will help you identify the right first step.")
    )
    return layout("services", "AI Consulting, Agent Development & Integration Services",
                  "Explore StrategicOps services: agentic AI consulting, custom AI agent development, multi-agent systems, AI automation, enterprise AI solutions and AI integration.",
                  body, nav="services", crumbs=[("Services", None)])
