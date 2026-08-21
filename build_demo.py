from __future__ import annotations

import json
import os
import re
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
WORKSPACE = Path("/Users/workopenclaw/.openclaw/workspace")
SECRETS = WORKSPACE / ".env.secrets"
BASE = "https://api.gitbook.com/v1"
ORG_ID = "2DnmWBpytIOUKeXExonU"
REPO_OWNER = "gitbook-demo-sites"
REPO = "blue-yonder-demo-site-20260821"
REPO_URL = f"https://github.com/{REPO_OWNER}/{REPO}.git"

LOGO = "https://edge.sitecorecloud.io/blueyonderie8e6-corporateefb0-prod6ccb-be06/media/project/blueyonder/shared/default-images/logo-blue.png?h=76&iar=0&w=520"
ICON = "https://cdn.blueyonder.com/global/images/apple-touch-icon-180x180.png"

SPACES = [
    {
        "key": "HOME",
        "sentinel": "XSPACE_HOME",
        "folder": "home",
        "title": "Home",
        "icon": "house",
        "emoji": "1f3e0",
        "path": "home",
        "description": "Blue Yonder-style entry point, persona routes, and demo review notes.",
    },
    {
        "key": "PLATFORM",
        "sentinel": "XSPACE_PLATFORM",
        "folder": "platform-ai",
        "title": "Platform & AI",
        "icon": "brain-circuit",
        "emoji": "1f9e0",
        "path": "platform-ai",
        "description": "Agentic supply chain, platform services, extensibility, and decision intelligence.",
    },
    {
        "key": "SOLUTIONS",
        "sentinel": "XSPACE_SOLUTIONS",
        "folder": "planning-execution",
        "title": "Planning & Execution",
        "icon": "route",
        "emoji": "1f5fa",
        "path": "planning-execution",
        "description": "Planning, warehouse, transportation, commerce, and operational workflows.",
    },
    {
        "key": "CONNECT",
        "sentinel": "XSPACE_CONNECT",
        "folder": "connect-partners",
        "title": "Connect & Partners",
        "icon": "plug",
        "emoji": "1f50c",
        "path": "connect-partners",
        "description": "Developer environment, APIs, partner onboarding, release governance, and support.",
    },
]


def load_secret(name: str) -> str:
    if os.environ.get(name):
        return os.environ[name]
    if SECRETS.exists():
        for line in SECRETS.read_text(encoding="utf-8").splitlines():
            if line.startswith(f"{name}="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.strip() + "\n", encoding="utf-8")


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, check=check, text=True)


def api(method: str, path: str, body: Any | None = None, expected: tuple[int, ...] = (200, 201, 202, 204)) -> tuple[int, Any]:
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        BASE + path,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {os.environ['GITBOOK_TOKEN']}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            text = resp.read().decode()
            payload = json.loads(text) if text else None
            if resp.status not in expected:
                raise RuntimeError(f"{method} {path} returned {resp.status}: {text}")
            return resp.status, payload
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="ignore")
        raise RuntimeError(f"{method} {path} returned {exc.code}: {detail}") from exc


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def gitbook_yaml() -> str:
    return """
root: ./
structure:
  readme: README.md
  summary: SUMMARY.md
"""


def vars_yaml() -> str:
    return """
company: Blue Yonder
platform: Blue Yonder Platform
public_site: https://blueyonder.com
developer_portal: https://info.blueyonder.com/blue-yonder-platform/what-is-blue-yonder-connect-api-expansion-pack
support_portal: https://success.blueyonder.com
release_train: 2026.2
"""


def cover_svg() -> str:
    return """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 720" role="img" aria-labelledby="title desc">
  <title id="title">Blue Yonder documentation hub cover</title>
  <desc id="desc">Supply chain planning, execution, network, AI, and partner routes flowing into a unified documentation hub.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#061D49"/>
      <stop offset="0.48" stop-color="#005EB8"/>
      <stop offset="1" stop-color="#F4F8FB"/>
    </linearGradient>
  </defs>
  <rect width="1600" height="720" fill="url(#bg)"/>
  <g opacity="0.22" fill="none" stroke="#FFFFFF" stroke-width="3">
    <path d="M96 534 C 316 310, 548 284, 782 372 S 1194 450, 1484 176"/>
    <path d="M112 424 C 338 238, 586 220, 820 304 S 1208 346, 1492 118"/>
    <path d="M170 610 C 386 390, 660 390, 874 456 S 1210 516, 1450 342"/>
  </g>
  <g transform="translate(136 98)">
    <rect width="570" height="420" rx="28" fill="#FFFFFF"/>
    <rect x="44" y="48" width="240" height="28" rx="14" fill="#005EB8"/>
    <rect x="44" y="105" width="424" height="16" rx="8" fill="#C8D7E3"/>
    <rect x="44" y="140" width="364" height="16" rx="8" fill="#C8D7E3"/>
    <g transform="translate(44 218)">
      <rect width="138" height="100" rx="22" fill="#005EB8"/>
      <rect x="164" width="138" height="100" rx="22" fill="#2B72FF"/>
      <rect x="328" width="138" height="100" rx="22" fill="#00A6A6"/>
      <text x="31" y="59" fill="#FFFFFF" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700">Plan</text>
      <text x="194" y="59" fill="#FFFFFF" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700">Move</text>
      <text x="360" y="59" fill="#FFFFFF" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700">Sense</text>
    </g>
  </g>
  <g transform="translate(825 150)">
    <rect width="560" height="352" rx="38" fill="#071B38" opacity="0.96"/>
    <text x="56" y="88" fill="#FFFFFF" font-family="Arial, Helvetica, sans-serif" font-size="43" font-weight="800">Agentic Supply</text>
    <text x="56" y="143" fill="#FFFFFF" font-family="Arial, Helvetica, sans-serif" font-size="43" font-weight="800">Chain Docs</text>
    <rect x="56" y="192" width="188" height="52" rx="26" fill="#00A6A6"/>
    <rect x="266" y="192" width="208" height="52" rx="26" fill="#FFFFFF" opacity="0.16"/>
    <text x="84" y="226" fill="#FFFFFF" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700">unified routes</text>
    <text x="294" y="226" fill="#FFFFFF" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700">AI-ready answers</text>
  </g>
</svg>
"""


def card_rows(cards: list[tuple[str, str, str, str]]) -> str:
    rows = []
    for icon, title, desc, href in cards:
        rows.append(
            f'<tr><td><h3><i class="fa-{icon}" style="color:$primary;"></i></h3></td>'
            f"<td><strong>{title}</strong></td><td>{desc}</td>"
            f'<td><a href="{href}">{slug(title)}</a></td></tr>'
        )
    return (
        '<table data-view="cards"><thead><tr><th></th><th></th><th></th>'
        '<th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>\n'
        + "\n".join(rows)
        + "\n</tbody></table>"
    )


def scaffold() -> None:
    write("README.md", f"# {REPO}\n\nSource for a first-draft Blue Yonder demo documentation hub. Each top-level folder is a separate GitBook space.\n")
    write(".gitignore", ".DS_Store\nThumbs.db\n*.swp\n*.swo\n.idea/\n.vscode/\n__pycache__/\n*.pyc\n")
    write("assets/blue-yonder-cover.svg", cover_svg())
    for item in SPACES:
        write(f"{item['folder']}/.gitbook.yaml", gitbook_yaml())
        write(f"{item['folder']}/.gitbook/vars.yaml", vars_yaml())

    write(
        "home/README.md",
        f"""
---
description: Transform planning, execution, commerce, and partner knowledge into one AI-ready documentation experience.
icon: house
cover: ../assets/blue-yonder-cover.svg
coverY: 0
layout:
  width: wide
  cover:
    visible: true
    size: hero
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: false
  outline:
    visible: false
  pagination:
    visible: false
---

# Welcome to Blue Yonder

{{% columns %}}
{{% column width="50%" %}}
Plan, execute, and adapt across the end-to-end supply chain with one documentation hub for business users, implementation teams, developers, and partners.

<button type="button" class="button primary" data-action="ask" data-icon="gitbook-assistant">Ask the Blue Yonder docs</button>

<button type="button" class="button secondary" data-action="ask" data-query="How do I prepare for a planning rollout?" data-icon="route">Planning rollout</button> <button type="button" class="button secondary" data-action="ask" data-query="Where do partners find API guidance?" data-icon="plug">Partner APIs</button> <button type="button" class="button secondary" data-action="ask" data-query="How does the platform use AI?" data-icon="brain-circuit">AI platform</button>
{{% endcolumn %}}

{{% column width="50%" %}}
{{% hint style="success" icon="gitbook" %}}
**A note from GitBook**

This first-draft demo applies the Evolve docs pattern to Blue Yonder: brand-forward homepage, persona-aware routes, product cards, assistant-ready summaries, partner/developer paths, changelog governance, and clear migration notes for a real documentation rollout.

<a href="?visitor.persona=executive" class="button secondary" data-icon="chart-line">Executive</a> <a href="?visitor.persona=planner" class="button secondary" data-icon="route">Planner</a> <a href="?visitor.persona=developer" class="button secondary" data-icon="code">Developer</a> <a href="?visitor.persona=partner" class="button secondary" data-icon="handshake-angle">Partner</a>
{{% endhint %}}
{{% endcolumn %}}
{{% endcolumns %}}

{{% if visitor.claims.unsigned.persona %}}

***

## <i class="fa-sparkle" style="color:$info;"></i> Picked for you

{{% endif %}}

{{% if visitor.claims.unsigned.persona === "executive" %}}
{{% hint style="info" icon="chart-line" %}}
**Executive path.** Start with the platform narrative, governance model, and outcomes dashboard.
{{% endhint %}}

{card_rows([
    ("brain-circuit", "Platform & AI overview", "How the common platform ties forecasting, execution, network signals, and AI recommendations together.", "https://app.gitbook.com/s/XSPACE_PLATFORM/"),
    ("diagram-project", "Decision orchestration", "Where recommendations, exceptions, and human approvals fit into supply chain operations.", "https://app.gitbook.com/s/XSPACE_PLATFORM/ai-decisioning/decision-orchestration.md"),
    ("shield-check", "Governance model", "Ownership, change requests, authenticated content, and audit-ready documentation controls.", "governance-model.md"),
])}
{{% endif %}}

{{% if visitor.claims.unsigned.persona === "planner" %}}
{{% hint style="info" icon="route" %}}
**Planner path.** Focus on demand, supply, inventory, and exception management workflows.
{{% endhint %}}

{card_rows([
    ("chart-line", "Supply Chain Planning", "Integrated planning, demand and supply, production scheduling, and inventory optimization.", "https://app.gitbook.com/s/XSPACE_SOLUTIONS/planning/supply-chain-planning.md"),
    ("triangle-exclamation", "Exception workspace", "A sample operating model for resolving disruptions with network context.", "https://app.gitbook.com/s/XSPACE_SOLUTIONS/workflows/exception-management.md"),
    ("clipboard-check", "Go-live checklist", "Readiness criteria before enabling planners, operators, and partners.", "https://app.gitbook.com/s/XSPACE_SOLUTIONS/workflows/go-live-checklist.md"),
])}
{{% endif %}}

{{% if visitor.claims.unsigned.persona === "developer" %}}
{{% hint style="info" icon="code" %}}
**Developer path.** Start with Connect, authentication, sandbox access, and API governance.
{{% endhint %}}

{card_rows([
    ("plug", "Blue Yonder Connect", "Partner APIs, connectors, certification, and data exchange patterns.", "https://app.gitbook.com/s/XSPACE_CONNECT/developers/blue-yonder-connect.md"),
    ("key", "Authentication patterns", "API keys, OAuth-style authorization, sandboxes, and environment separation.", "https://app.gitbook.com/s/XSPACE_CONNECT/developers/authentication.md"),
    ("webhook", "Events and webhooks", "How integration events should be documented for agents and humans.", "https://app.gitbook.com/s/XSPACE_CONNECT/developers/events-and-webhooks.md"),
])}
{{% endif %}}

{{% if visitor.claims.unsigned.persona === "partner" %}}
{{% hint style="info" icon="handshake-angle" %}}
**Partner path.** Position the hub as an authenticated partner experience for onboarding, certification, and co-selling.
{{% endhint %}}

{card_rows([
    ("handshake", "Partner onboarding", "Program overview, enablement checklist, and owner handoffs.", "https://app.gitbook.com/s/XSPACE_CONNECT/partners/partner-onboarding.md"),
    ("stamp", "Certification workflow", "Sandbox setup, validation evidence, and publishing requirements.", "https://app.gitbook.com/s/XSPACE_CONNECT/partners/certification-workflow.md"),
    ("life-ring", "Partner support", "Support escalation paths and operational runbooks.", "https://app.gitbook.com/s/XSPACE_CONNECT/partners/support.md"),
])}
{{% endif %}}

***

## One intelligent supply chain platform

{card_rows([
    ("brain-circuit", "Platform & AI", "Agentic supply chain, shared data foundation, extensibility, and AI decisioning routes.", "https://app.gitbook.com/s/XSPACE_PLATFORM/"),
    ("route", "Planning & Execution", "Planning, warehouse, transportation, order promising, commerce, and operational playbooks.", "https://app.gitbook.com/s/XSPACE_SOLUTIONS/"),
    ("plug", "Connect & Partners", "Developer portal, APIs, partner certification, and support workflows.", "https://app.gitbook.com/s/XSPACE_CONNECT/"),
    ("clipboard-list", "Review notes", "Assumptions, sources, and the strongest feedback areas for the sales team.", "review-notes.md"),
])}

{{% columns %}}
{{% column width="66.66666666666666%" %}}
## Demo route

1. Start on the homepage and show the Blue Yonder-branded search-first entry point.
2. Switch between executive, planner, developer, and partner personas.
3. Open Platform & AI to show strategic messaging, then jump to Planning & Execution for operator workflows.
4. Finish in Connect & Partners to show how GitBook can house public docs, partner docs, and authenticated implementation guidance in one site.
{{% endcolumn %}}

{{% column width="33.33333333333334%" %}}
#### What's new

{card_rows([
    ("sparkles", "2026.2 release path", "Sample release-note structure for platform, planning, and connector changes.", "https://app.gitbook.com/s/XSPACE_CONNECT/releases/release-notes.md"),
    ("robot", "AI assistant prompts", "Starter questions tailored to supply chain users and partner developers.", "#welcome-to-blue-yonder"),
])}
{{% endcolumn %}}
{{% endcolumns %}}
""",
    )
    write("home/SUMMARY.md", "# Table of contents\n\n* [Welcome to Blue Yonder](README.md)\n* [Governance model](governance-model.md)\n* [Review notes](review-notes.md)\n")
    write(
        "home/governance-model.md",
        """
---
description: A sample operating model for managing Blue Yonder documentation in GitBook.
icon: shield-check
---

# Governance model

Use this page to show how enterprise teams can move from fragmented product pages and partner portals to a governed docs hub.

{% stepper %}
{% step %}
## Own the source

Product documentation, partner guidance, API references, and release notes each have clear owners and review paths.
{% endstep %}

{% step %}
## Draft with change requests

Implementation teams can propose updates without publishing them directly. Reviewers approve content before it reaches customers or partners.
{% endstep %}

{% step %}
## Control visibility

Public content stays searchable. Partner playbooks, certification steps, and implementation-only content can be gated with authenticated access.
{% endstep %}

{% step %}
## Make it answerable

Pages are written with strong summaries, task names, and glossary terms so GitBook AI can answer supply-chain questions with evidence.
{% endstep %}
{% endstepper %}
""",
    )
    write(
        "home/review-notes.md",
        """
---
description: First-draft assumptions and feedback points for the Blue Yonder demo.
icon: clipboard-list
---

# Review notes

{% hint style="warning" %}
This is representative demo content based on Blue Yonder's public website and the Evolve demo pattern. It is not a migration of private Blue Yonder documentation.
{% endhint %}

## Assumptions

* The most useful sales motion is a unified product, developer, partner, and support documentation hub.
* Blue Yonder branding should feel corporate and operational: clean white surfaces, deep blue, bright accent blue, and supply-chain route imagery.
* The demo should show both public documentation and gated partner/developer material without needing real authentication data.

## Feedback areas

* Whether the IA should emphasize industry solutions, product families, or partner/developer workflows first.
* Which Blue Yonder product names and capabilities need to be exact before a customer-facing version.
* Whether the demo should add real OpenAPI specs for Connect APIs once those are available.
""",
    )

    write(
        "platform-ai/README.md",
        f"""
---
description: Platform services, agentic AI, data foundation, and extensibility for the Blue Yonder Platform.
icon: brain-circuit
cover: ../assets/blue-yonder-cover.svg
coverY: 0
layout:
  width: wide
---

# Platform & AI

Blue Yonder's platform story is about unifying planning, execution, commerce, and network signals so teams can make faster supply-chain decisions.

{card_rows([
    ("database", "Data foundation", "Shared operational data model for forecasting, fulfillment, transportation, labor, and delivery.", "foundation/data-cloud.md"),
    ("brain-circuit", "AI decisioning", "Predictive, generative, and agentic AI patterns for supply-chain decisions.", "ai-decisioning/agentic-supply-chain.md"),
    ("puzzle-piece", "Extensibility", "How teams extend workflows, connect third-party systems, and document custom journeys.", "foundation/extensibility.md"),
])}

{{% hint style="info" icon="gitbook-assistant" %}}
Each page starts with business context, then implementation notes, then agent-readable answers. That mirrors how real Blue Yonder users move from strategy to operations.
{{% endhint %}}
""",
    )
    write("platform-ai/SUMMARY.md", "# Table of contents\n\n* [Platform & AI](README.md)\n\n## Foundation\n\n* [Data cloud](foundation/data-cloud.md)\n* [Extensibility](foundation/extensibility.md)\n\n## AI decisioning\n\n* [Agentic supply chain](ai-decisioning/agentic-supply-chain.md)\n* [Decision orchestration](ai-decisioning/decision-orchestration.md)\n")
    write("platform-ai/foundation/data-cloud.md", page("Data cloud", "database", "Model planning, execution, commerce, and partner events as a shared source of truth for humans and agents.", ["Define canonical objects for orders, inventory, capacity, lanes, facilities, labor, and exceptions.", "Document ownership and freshness expectations for each source.", "Expose lineage so recommendations can be traced back to the signal that created them."]))
    write("platform-ai/foundation/extensibility.md", page("Extensibility", "puzzle-piece", "Use documented extension points to adapt Blue Yonder workflows without creating unmanaged knowledge drift.", ["Catalog approved integrations and custom journeys.", "Separate public extension concepts from gated implementation details.", "Keep examples reusable through variables, includes, and API-backed references."]))
    write("platform-ai/ai-decisioning/agentic-supply-chain.md", page("Agentic supply chain", "robot", "Position AI as an operational copilot for forecasting, disruption response, network optimization, and fulfillment decisions.", ["Summarize what each agent can decide, recommend, or escalate.", "Define the human approval points before actions affect inventory, labor, transport, or customer promises.", "Capture confidence, evidence, and rollback steps in every high-impact workflow."]))
    write("platform-ai/ai-decisioning/decision-orchestration.md", page("Decision orchestration", "diagram-project", "Show how recommendations move from signal to exception queue to approved operational change.", ["Sense: ingest network and operating signals.", "Prioritize: rank impact by service, cost, margin, and capacity.", "Act: route the change to planners, operators, partners, or automated execution."]))

    write(
        "planning-execution/README.md",
        f"""
---
description: Planning, warehouse, transportation, commerce, and operational workflows.
icon: route
cover: ../assets/blue-yonder-cover.svg
coverY: 0
layout:
  width: wide
---

# Planning & Execution

This space turns Blue Yonder's broad product story into task-oriented documentation for planners, operators, and implementation teams.

{card_rows([
    ("chart-line", "Supply Chain Planning", "Demand, supply, inventory, production planning, and order promising.", "planning/supply-chain-planning.md"),
    ("warehouse", "Warehouse and labor", "Operational playbooks for warehouse visibility, tasking, and labor planning.", "execution/warehouse-and-labor.md"),
    ("truck-fast", "Transportation", "Network design, carrier decisions, routing, and last-mile exception handling.", "execution/transportation.md"),
    ("triangle-exclamation", "Exception management", "A cross-functional runbook for disruptions and service-risk events.", "workflows/exception-management.md"),
])}
""",
    )
    write("planning-execution/SUMMARY.md", "# Table of contents\n\n* [Planning & Execution](README.md)\n\n## Planning\n\n* [Supply Chain Planning](planning/supply-chain-planning.md)\n* [Inventory operations](planning/inventory-operations.md)\n\n## Execution\n\n* [Warehouse and labor](execution/warehouse-and-labor.md)\n* [Transportation](execution/transportation.md)\n\n## Workflows\n\n* [Exception management](workflows/exception-management.md)\n* [Go-live checklist](workflows/go-live-checklist.md)\n")
    write("planning-execution/planning/supply-chain-planning.md", page("Supply Chain Planning", "chart-line", "Balance demand, supply, inventory, production constraints, and financial outcomes in one planning workflow.", ["Start with the planning horizon and business objective.", "Connect demand signals, inventory policy, capacity, and customer promise constraints.", "Use AI recommendations to compare tradeoffs before publishing a plan."]))
    write("planning-execution/planning/inventory-operations.md", page("Inventory operations", "boxes-stacked", "Document reorder, allocation, safety stock, and exception flows in a way planners can search and agents can answer.", ["Define policy thresholds and owner roles.", "Show how network visibility changes allocation decisions.", "Capture exception patterns and recommended next actions."]))
    write("planning-execution/execution/warehouse-and-labor.md", page("Warehouse and labor", "warehouse", "Connect warehouse work, labor plans, automation, and service-level outcomes.", ["Document facility setup and role-specific tasks.", "Tie labor plans to volume, wave, and exception forecasts.", "Keep troubleshooting paths close to operational workflows."]))
    write("planning-execution/execution/transportation.md", page("Transportation", "truck-fast", "Give transportation teams a single path from network plan to carrier execution and exception recovery.", ["Model lanes, capacity, carrier constraints, and customer promises.", "Document routing decisions and tendering states.", "Use examples that show service, cost, and sustainability tradeoffs."]))
    write("planning-execution/workflows/exception-management.md", page("Exception management", "triangle-exclamation", "A representative operating model for resolving disruptions with shared context.", ["Detect the exception and attach impacted orders, facilities, inventory, carriers, and customers.", "Recommend actions with confidence and tradeoff notes.", "Route approval to the right planner or operator, then publish the resolution."]))
    write("planning-execution/workflows/go-live-checklist.md", page("Go-live checklist", "clipboard-check", "A launch checklist for rolling out a new planning or execution workflow.", ["Confirm data sources, roles, and approval gates.", "Publish role-based training paths.", "Prepare support, release notes, and rollback guidance."]))

    write(
        "connect-partners/README.md",
        f"""
---
description: Developer environment, APIs, partner onboarding, certification, releases, and support.
icon: plug
cover: ../assets/blue-yonder-cover.svg
coverY: 0
layout:
  width: wide
---

# Connect & Partners

Use this space to show how Blue Yonder could combine public developer docs, partner certification, support runbooks, and release governance in one GitBook experience.

{card_rows([
    ("plug", "Blue Yonder Connect", "APIs, connectors, sandboxes, and partner integration routes.", "developers/blue-yonder-connect.md"),
    ("key", "Authentication", "Credential handling, environments, and permission boundaries.", "developers/authentication.md"),
    ("handshake", "Partner onboarding", "Enablement, certification, marketing, and support paths.", "partners/partner-onboarding.md"),
    ("clock-rotate-left", "Release notes", "Sample release-note format for platform and connector changes.", "releases/release-notes.md"),
])}
""",
    )
    write("connect-partners/SUMMARY.md", "# Table of contents\n\n* [Connect & Partners](README.md)\n\n## Developers\n\n* [Blue Yonder Connect](developers/blue-yonder-connect.md)\n* [Authentication](developers/authentication.md)\n* [Events and webhooks](developers/events-and-webhooks.md)\n\n## Partners\n\n* [Partner onboarding](partners/partner-onboarding.md)\n* [Certification workflow](partners/certification-workflow.md)\n* [Support](partners/support.md)\n\n## Releases\n\n* [Release notes](releases/release-notes.md)\n")
    write("connect-partners/developers/blue-yonder-connect.md", page("Blue Yonder Connect", "plug", "A developer-friendly route for APIs, connectors, sandboxes, and integration certification.", ["Start with the business process the integration supports.", "Show endpoint families, event types, and data ownership before code.", "Keep certification evidence and support handoffs in the same hub."]))
    write("connect-partners/developers/authentication.md", page("Authentication", "key", "Separate public concepts from gated credential handling and environment-specific setup.", ["Document sandbox, staging, and production boundaries.", "Define scopes, owners, rotation policy, and audit evidence.", "Keep secrets out of docs and link to secure vault workflows."]))
    write("connect-partners/developers/events-and-webhooks.md", page("Events and webhooks", "webhook", "Event-driven documentation should explain when events fire, who owns retries, and what downstream systems should do.", ["Name event producers and consumers.", "Include example payloads only after canonical schemas are available.", "Document replay, idempotency, and failure handling."]))
    write("connect-partners/partners/partner-onboarding.md", page("Partner onboarding", "handshake", "A hub for partner enablement, solution setup, certification, and co-selling materials.", ["Qualify the integration motion.", "Grant sandbox access and assign technical owners.", "Track certification tasks with clear approval steps."]))
    write("connect-partners/partners/certification-workflow.md", page("Certification workflow", "stamp", "Show the path from sandbox build to validated integration listing.", ["Run required scenario tests.", "Upload evidence and implementation notes.", "Approve support readiness before publishing."]))
    write("connect-partners/partners/support.md", page("Support", "life-ring", "Keep operational help close to partner docs so teams can resolve issues without searching multiple portals.", ["Define severity and owner routing.", "Link incidents to release notes and affected integrations.", "Capture recurring issues as docs updates."]))
    write("connect-partners/releases/release-notes.md", release_notes())


def page(title: str, icon: str, description: str, bullets: list[str]) -> str:
    rows = "\n".join(f"* {item}" for item in bullets)
    return f"""
---
description: {description}
icon: {icon}
---

# {title}

{description}

{{% hint style="info" icon="gitbook-assistant" %}}
Use the Assistant on this page to ask how this topic affects planners, operators, developers, and partners.
{{% endhint %}}

## What to document

{rows}

## Example structure

{{% tabs %}}
{{% tab title="Overview" %}}
Explain the business workflow, owner roles, and decision points.
{{% endtab %}}

{{% tab title="Implementation" %}}
Capture setup requirements, environments, dependencies, and validation criteria.
{{% endtab %}}

{{% tab title="Operations" %}}
Show monitoring, exception handling, support handoffs, and release-note impact.
{{% endtab %}}
{{% endtabs %}}
"""


def release_notes() -> str:
    return """
---
description: Sample release-note format for Blue Yonder platform and partner-facing changes.
icon: clock-rotate-left
layout:
  width: wide
---

# Release notes

{% updates %}
{% update title="2026.2 platform notes" description="Sample release note for the demo site." %}
Improved structure for agentic supply-chain workflows, including clearer exception routes and partner-facing implementation notes.
{% endupdate %}

{% update title="Connect certification checklist" description="Sample partner update." %}
Added a certification evidence checklist covering sandbox validation, support readiness, and release-note ownership.
{% endupdate %}
{% endupdates %}
"""


def git_commit_push() -> None:
    run(["git", "init"])
    run(["git", "branch", "-M", "main"], check=False)
    run(["git", "add", "."])
    run(["git", "commit", "-m", "Add Blue Yonder demo content"])
    view = subprocess.run(["gh", "repo", "view", f"{REPO_OWNER}/{REPO}"], cwd=ROOT, text=True, capture_output=True)
    if view.returncode != 0:
        run(["gh", "repo", "create", f"{REPO_OWNER}/{REPO}", "--public", "--source", ".", "--remote", "origin", "--push"])
    else:
        remote = subprocess.run(["git", "remote"], cwd=ROOT, text=True, capture_output=True)
        if "origin" not in remote.stdout.split():
            run(["git", "remote", "add", "origin", REPO_URL])
        run(["git", "push", "-u", "origin", "main"])


def replace_sentinels(space_ids: dict[str, str]) -> None:
    replacements = {item["sentinel"]: space_ids[item["key"]] for item in SPACES}
    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        original = text
        for old, new in replacements.items():
            text = text.replace(old, new)
        if text != original:
            md.write_text(text, encoding="utf-8")


def create_site() -> dict:
    title = "Blue Yonder Documentation Hub"
    basename = f"blue-yonder-docs-demo-{time.strftime('%Y%m%d-%H%M%S', time.gmtime())}"
    _, site = api("POST", f"/orgs/{ORG_ID}/sites", {"type": "ultimate", "title": title, "visibility": "share-link"})
    site_id = site["id"]
    api("PATCH", f"/orgs/{ORG_ID}/sites/{site_id}", {"title": title, "visibility": "share-link", "basename": basename})
    created: dict[str, Any] = {"org": ORG_ID, "site": site_id, "spaces": {}, "sections": {}, "site_spaces": {}, "basename": basename}
    for item in SPACES:
        _, space = api("POST", f"/orgs/{ORG_ID}/spaces", {"title": item["title"], "emoji": item["emoji"], "empty": True, "editMode": "live"})
        space_id = space["id"]
        _, section = api("POST", f"/orgs/{ORG_ID}/sites/{site_id}/sections", {"spaceId": space_id, "title": item["title"], "icon": item["icon"], "draft": False})
        section_id = section["id"]
        site_space_id = section["siteSpaces"][0]["id"]
        api("PATCH", f"/orgs/{ORG_ID}/sites/{site_id}/sections/{section_id}", {"path": item["path"], "description": item["description"], "draft": False, "defaultSiteSpace": site_space_id})
        created["spaces"][item["key"]] = space_id
        created["sections"][item["key"]] = section_id
        created["site_spaces"][item["key"]] = site_space_id
    api("PATCH", f"/orgs/{ORG_ID}/sites/{site_id}", {"defaultSiteSection": created["sections"]["HOME"], "defaultSiteSpace": created["site_spaces"]["HOME"]})
    write("gitbook-created.json", json.dumps(created, indent=2))
    return created


def import_spaces(created: dict) -> dict:
    results = {}
    for item in SPACES:
        status, _ = api(
            "POST",
            f"/spaces/{created['spaces'][item['key']]}/git/import",
            {
                "url": REPO_URL,
                "ref": "refs/heads/main",
                "repoProjectDirectory": item["folder"],
                "repoTreeURL": f"https://github.com/{REPO_OWNER}/{REPO}/tree/main",
                "repoCommitURL": f"https://github.com/{REPO_OWNER}/{REPO}/commit",
                "force": True,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            },
            expected=(204,),
        )
        results[item["key"]] = {"status": status, "space": created["spaces"][item["key"]], "folder": item["folder"]}
    write("gitbook-import-results.json", json.dumps(results, indent=2))
    return results


def customize(created: dict) -> dict:
    customization = {
        "title": "Blue Yonder Documentation Hub",
        "localizedTitle": {},
        "internationalization": {"locale": "en"},
        "styling": {
            "theme": "clean",
            "primaryColor": {"light": "#005EB8", "dark": "#5DB7FF"},
            "infoColor": {"light": "#2B72FF", "dark": "#86C5FF"},
            "successColor": {"light": "#00A6A6", "dark": "#46D6D0"},
            "warningColor": {"light": "#F4B000", "dark": "#FFD166"},
            "dangerColor": {"light": "#D64545", "dark": "#FF8A8A"},
            "tint": {"color": {"light": "#F4F8FB", "dark": "#061D49"}},
            "corners": "circular",
            "depth": "flat",
            "links": "accent",
            "font": "Inter",
            "monospaceFont": "IBMPlexMono",
            "icons": "regular",
            "background": "plain",
            "sidebar": {"background": "filled", "list": "default"},
            "codeTheme": {
                "default": {"light": "default-light", "dark": "default-dark"},
                "openapi": {"light": "default-light", "dark": "default-dark"},
            },
            "search": "prominent",
        },
        "header": {
            "preset": "default",
            "logo": {"light": LOGO, "dark": LOGO},
            "links": [
                {"title": "Platform", "to": {"kind": "space", "space": created["spaces"]["PLATFORM"]}, "style": "link", "links": [], "localizedTitle": {}},
                {"title": "Planning & Execution", "to": {"kind": "space", "space": created["spaces"]["SOLUTIONS"]}, "style": "link", "links": [], "localizedTitle": {}},
                {"title": "Connect", "to": {"kind": "space", "space": created["spaces"]["CONNECT"]}, "style": "link", "links": [], "localizedTitle": {}},
                {"title": "Blue Yonder", "to": {"kind": "url", "url": "https://blueyonder.com"}, "style": "button-secondary", "links": [], "localizedTitle": {}},
            ],
        },
        "favicon": {"icon": {"light": ICON, "dark": ICON}},
        "footer": {
            "logo": {"light": LOGO, "dark": LOGO},
            "groups": [
                {
                    "title": "Demo paths",
                    "localizedTitle": {},
                    "links": [
                        {"title": "Platform & AI", "to": {"kind": "space", "space": created["spaces"]["PLATFORM"]}, "localizedTitle": {}},
                        {"title": "Planning & Execution", "to": {"kind": "space", "space": created["spaces"]["SOLUTIONS"]}, "localizedTitle": {}},
                        {"title": "Connect & Partners", "to": {"kind": "space", "space": created["spaces"]["CONNECT"]}, "localizedTitle": {}},
                    ],
                },
                {
                    "title": "Sources",
                    "localizedTitle": {},
                    "links": [
                        {"title": "Source repo", "to": {"kind": "url", "url": f"https://github.com/{REPO_OWNER}/{REPO}"}, "localizedTitle": {}},
                        {"title": "Blue Yonder", "to": {"kind": "url", "url": "https://blueyonder.com"}, "localizedTitle": {}},
                    ],
                },
            ],
            "copyright": "Blue Yonder Documentation Hub demo - built for GitBook review.",
        },
        "themes": {"default": "light", "toggeable": True},
        "pdf": {"enabled": True},
        "feedback": {"enabled": True},
        "ai": {
            "mode": "assistant",
            "suggestions": [
                "How should a planner prepare for rollout?",
                "Where do partners find API and certification guidance?",
                "How does Blue Yonder Connect fit into the platform?",
                "What governance model should documentation owners use?",
            ],
        },
        "advancedCustomization": {"enabled": True},
        "trademark": {"enabled": True},
        "externalLinks": {"target": "self"},
        "pagination": {"enabled": True},
        "pageActions": {"externalAI": True, "markdown": True, "mcp": True, "items": ["assistant", "markdown", "external-ai", "mcp", "pdf"]},
        "git": {"showEditLink": False},
        "privacyPolicy": {"url": "https://blueyonder.com/privacy-policy"},
        "socialPreview": {"url": "https://edge.sitecorecloud.io/blueyonderie8e6-corporateefb0-prod6ccb-be06/media/project/blueyonder/shared/default-images/default-opengraph-image.png?h=360&iar=0&w=640"},
    }
    _, result = api("PUT", f"/orgs/{ORG_ID}/sites/{created['site']}/customization", customization)
    write("gitbook-customization-result.json", json.dumps(result, indent=2))
    return result


def publish(created: dict) -> dict:
    publish_status, publish_result = api("POST", f"/orgs/{ORG_ID}/sites/{created['site']}/publish")
    share_status, share = api("POST", f"/orgs/{ORG_ID}/sites/{created['site']}/share-links", {"name": "Blue Yonder demo review"})
    final = {
        "publish_status": publish_status,
        "publish": publish_result,
        "share_status": share_status,
        "share": share,
        "published_url": share.get("urls", {}).get("published", ""),
        "app_url": publish_result.get("urls", {}).get("app", ""),
        "preview_url": publish_result.get("urls", {}).get("preview", ""),
        "repo": f"https://github.com/{REPO_OWNER}/{REPO}",
    }
    write("gitbook-publish-share.json", json.dumps(final, indent=2))
    return final


def main() -> None:
    os.environ["GITBOOK_TOKEN"] = load_secret("GITBOOK_TOKEN")
    if not os.environ["GITBOOK_TOKEN"]:
        raise RuntimeError("Missing GITBOOK_TOKEN")
    scaffold()
    git_commit_push()
    created = create_site()
    replace_sentinels(created["spaces"])
    run(["git", "add", "."])
    run(["git", "commit", "-m", "Resolve GitBook space links"])
    run(["git", "push"])
    import_spaces(created)
    customize(created)
    final = publish(created)
    run(["git", "add", "."])
    run(["git", "commit", "-m", "Add GitBook publish artifacts"])
    run(["git", "push"])
    print(json.dumps(final, indent=2))


if __name__ == "__main__":
    main()
