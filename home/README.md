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

{% columns %}
{% column width="50%" %}
Plan, execute, and adapt across the end-to-end supply chain with one documentation hub for business users, implementation teams, developers, and partners.

<button type="button" class="button primary" data-action="ask" data-icon="gitbook-assistant">Ask the Blue Yonder docs</button>

<button type="button" class="button secondary" data-action="ask" data-query="How do I prepare for a planning rollout?" data-icon="route">Planning rollout</button> <button type="button" class="button secondary" data-action="ask" data-query="Where do partners find API guidance?" data-icon="plug">Partner APIs</button> <button type="button" class="button secondary" data-action="ask" data-query="How does the platform use AI?" data-icon="brain-circuit">AI platform</button>
{% endcolumn %}

{% column width="50%" %}
{% hint style="success" icon="gitbook" %}
**A note from GitBook**

This first-draft demo applies the Evolve docs pattern to Blue Yonder: brand-forward homepage, persona-aware routes, product cards, assistant-ready summaries, partner/developer paths, changelog governance, and clear migration notes for a real documentation rollout.

<a href="?visitor.persona=executive" class="button secondary" data-icon="chart-line">Executive</a> <a href="?visitor.persona=planner" class="button secondary" data-icon="route">Planner</a> <a href="?visitor.persona=developer" class="button secondary" data-icon="code">Developer</a> <a href="?visitor.persona=partner" class="button secondary" data-icon="handshake-angle">Partner</a>
{% endhint %}
{% endcolumn %}
{% endcolumns %}

{% if visitor.claims.unsigned.persona %}

***

## <i class="fa-sparkle" style="color:$info;"></i> Picked for you

{% endif %}

{% if visitor.claims.unsigned.persona === "executive" %}
{% hint style="info" icon="chart-line" %}
**Executive path.** Start with the platform narrative, governance model, and outcomes dashboard.
{% endhint %}

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><h3><i class="fa-brain-circuit" style="color:$primary;"></i></h3></td><td><strong>Platform & AI overview</strong></td><td>How the common platform ties forecasting, execution, network signals, and AI recommendations together.</td><td><a href="https://app.gitbook.com/s/H7GIqXk9SW38FaGyX3Mc/">platform-ai-overview</a></td></tr>
<tr><td><h3><i class="fa-diagram-project" style="color:$primary;"></i></h3></td><td><strong>Decision orchestration</strong></td><td>Where recommendations, exceptions, and human approvals fit into supply chain operations.</td><td><a href="https://app.gitbook.com/s/H7GIqXk9SW38FaGyX3Mc/ai-decisioning/decision-orchestration.md">decision-orchestration</a></td></tr>
<tr><td><h3><i class="fa-shield-check" style="color:$primary;"></i></h3></td><td><strong>Governance model</strong></td><td>Ownership, change requests, authenticated content, and audit-ready documentation controls.</td><td><a href="governance-model.md">governance-model</a></td></tr>
</tbody></table>
{% endif %}

{% if visitor.claims.unsigned.persona === "planner" %}
{% hint style="info" icon="route" %}
**Planner path.** Focus on demand, supply, inventory, and exception management workflows.
{% endhint %}

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><h3><i class="fa-chart-line" style="color:$primary;"></i></h3></td><td><strong>Supply Chain Planning</strong></td><td>Integrated planning, demand and supply, production scheduling, and inventory optimization.</td><td><a href="https://app.gitbook.com/s/LcqiTNteUHkzjiTOUr8c/planning/supply-chain-planning.md">supply-chain-planning</a></td></tr>
<tr><td><h3><i class="fa-triangle-exclamation" style="color:$primary;"></i></h3></td><td><strong>Exception workspace</strong></td><td>A sample operating model for resolving disruptions with network context.</td><td><a href="https://app.gitbook.com/s/LcqiTNteUHkzjiTOUr8c/workflows/exception-management.md">exception-workspace</a></td></tr>
<tr><td><h3><i class="fa-clipboard-check" style="color:$primary;"></i></h3></td><td><strong>Go-live checklist</strong></td><td>Readiness criteria before enabling planners, operators, and partners.</td><td><a href="https://app.gitbook.com/s/LcqiTNteUHkzjiTOUr8c/workflows/go-live-checklist.md">go-live-checklist</a></td></tr>
</tbody></table>
{% endif %}

{% if visitor.claims.unsigned.persona === "developer" %}
{% hint style="info" icon="code" %}
**Developer path.** Start with Connect, authentication, sandbox access, and API governance.
{% endhint %}

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><h3><i class="fa-plug" style="color:$primary;"></i></h3></td><td><strong>Blue Yonder Connect</strong></td><td>Partner APIs, connectors, certification, and data exchange patterns.</td><td><a href="https://app.gitbook.com/s/EBF0LyiZSa2gJV3j6pkd/developers/blue-yonder-connect.md">blue-yonder-connect</a></td></tr>
<tr><td><h3><i class="fa-key" style="color:$primary;"></i></h3></td><td><strong>Authentication patterns</strong></td><td>API keys, OAuth-style authorization, sandboxes, and environment separation.</td><td><a href="https://app.gitbook.com/s/EBF0LyiZSa2gJV3j6pkd/developers/authentication.md">authentication-patterns</a></td></tr>
<tr><td><h3><i class="fa-webhook" style="color:$primary;"></i></h3></td><td><strong>Events and webhooks</strong></td><td>How integration events should be documented for agents and humans.</td><td><a href="https://app.gitbook.com/s/EBF0LyiZSa2gJV3j6pkd/developers/events-and-webhooks.md">events-and-webhooks</a></td></tr>
</tbody></table>
{% endif %}

{% if visitor.claims.unsigned.persona === "partner" %}
{% hint style="info" icon="handshake-angle" %}
**Partner path.** Position the hub as an authenticated partner experience for onboarding, certification, and co-selling.
{% endhint %}

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><h3><i class="fa-handshake" style="color:$primary;"></i></h3></td><td><strong>Partner onboarding</strong></td><td>Program overview, enablement checklist, and owner handoffs.</td><td><a href="https://app.gitbook.com/s/EBF0LyiZSa2gJV3j6pkd/partners/partner-onboarding.md">partner-onboarding</a></td></tr>
<tr><td><h3><i class="fa-stamp" style="color:$primary;"></i></h3></td><td><strong>Certification workflow</strong></td><td>Sandbox setup, validation evidence, and publishing requirements.</td><td><a href="https://app.gitbook.com/s/EBF0LyiZSa2gJV3j6pkd/partners/certification-workflow.md">certification-workflow</a></td></tr>
<tr><td><h3><i class="fa-life-ring" style="color:$primary;"></i></h3></td><td><strong>Partner support</strong></td><td>Support escalation paths and operational runbooks.</td><td><a href="https://app.gitbook.com/s/EBF0LyiZSa2gJV3j6pkd/partners/support.md">partner-support</a></td></tr>
</tbody></table>
{% endif %}

***

## One intelligent supply chain platform

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><h3><i class="fa-brain-circuit" style="color:$primary;"></i></h3></td><td><strong>Platform & AI</strong></td><td>Agentic supply chain, shared data foundation, extensibility, and AI decisioning routes.</td><td><a href="https://app.gitbook.com/s/H7GIqXk9SW38FaGyX3Mc/">platform-ai</a></td></tr>
<tr><td><h3><i class="fa-route" style="color:$primary;"></i></h3></td><td><strong>Planning & Execution</strong></td><td>Planning, warehouse, transportation, order promising, commerce, and operational playbooks.</td><td><a href="https://app.gitbook.com/s/LcqiTNteUHkzjiTOUr8c/">planning-execution</a></td></tr>
<tr><td><h3><i class="fa-plug" style="color:$primary;"></i></h3></td><td><strong>Connect & Partners</strong></td><td>Developer portal, APIs, partner certification, and support workflows.</td><td><a href="https://app.gitbook.com/s/EBF0LyiZSa2gJV3j6pkd/">connect-partners</a></td></tr>
<tr><td><h3><i class="fa-clipboard-list" style="color:$primary;"></i></h3></td><td><strong>Review notes</strong></td><td>Assumptions, sources, and the strongest feedback areas for the sales team.</td><td><a href="review-notes.md">review-notes</a></td></tr>
</tbody></table>

{% columns %}
{% column width="66.66666666666666%" %}
## Demo route

1. Start on the homepage and show the Blue Yonder-branded search-first entry point.
2. Switch between executive, planner, developer, and partner personas.
3. Open Platform & AI to show strategic messaging, then jump to Planning & Execution for operator workflows.
4. Finish in Connect & Partners to show how GitBook can house public docs, partner docs, and authenticated implementation guidance in one site.
{% endcolumn %}

{% column width="33.33333333333334%" %}
#### What's new

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><h3><i class="fa-sparkles" style="color:$primary;"></i></h3></td><td><strong>2026.2 release path</strong></td><td>Sample release-note structure for platform, planning, and connector changes.</td><td><a href="https://app.gitbook.com/s/EBF0LyiZSa2gJV3j6pkd/releases/release-notes.md">2026-2-release-path</a></td></tr>
<tr><td><h3><i class="fa-robot" style="color:$primary;"></i></h3></td><td><strong>AI assistant prompts</strong></td><td>Starter questions tailored to supply chain users and partner developers.</td><td><a href="#welcome-to-blue-yonder">ai-assistant-prompts</a></td></tr>
</tbody></table>
{% endcolumn %}
{% endcolumns %}
