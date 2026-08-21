---
description: Event-driven documentation should explain when events fire, who owns retries, and what downstream systems should do.
icon: webhook
---

# Events and webhooks

Event-driven documentation should explain when events fire, who owns retries, and what downstream systems should do.

{% hint style="info" icon="gitbook-assistant" %}
Use the Assistant on this page to ask how this topic affects planners, operators, developers, and partners.
{% endhint %}

## What to document

* Name event producers and consumers.
* Include example payloads only after canonical schemas are available.
* Document replay, idempotency, and failure handling.

## Example structure

{% tabs %}
{% tab title="Overview" %}
Explain the business workflow, owner roles, and decision points.
{% endtab %}

{% tab title="Implementation" %}
Capture setup requirements, environments, dependencies, and validation criteria.
{% endtab %}

{% tab title="Operations" %}
Show monitoring, exception handling, support handoffs, and release-note impact.
{% endtab %}
{% endtabs %}
