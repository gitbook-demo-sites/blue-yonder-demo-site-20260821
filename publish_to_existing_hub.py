from __future__ import annotations

import json
import os
import subprocess
import time

import build_demo


ORG_ID = build_demo.ORG_ID
SITE_ID = "site_A713M"

TARGET_SPACES = {
    "HOME": {
        "space": "UgQSOGhsXFfAeWpSX20A",
        "section": "sitesc_sQQhJ",
        "site_space": "sitesp_xHuAH",
        "folder": "home",
        "title": "Home",
        "path": "home",
        "description": "Blue Yonder-style entry point, persona routes, and demo review notes.",
        "icon": "house",
        "emoji": "1f3e0",
    },
    "PLATFORM": {
        "space": "H7GIqXk9SW38FaGyX3Mc",
        "section": "sitesc_4LLNC",
        "site_space": "sitesp_EyaiY",
        "folder": "platform-ai",
        "title": "Platform & AI",
        "path": "platform-ai",
        "description": "Agentic supply chain, platform services, extensibility, and decision intelligence.",
        "icon": "brain-circuit",
        "emoji": "1f9e0",
    },
    "SOLUTIONS": {
        "space": "LcqiTNteUHkzjiTOUr8c",
        "section": "sitesc_S229A",
        "site_space": "sitesp_svBIF",
        "folder": "planning-execution",
        "title": "Planning & Execution",
        "path": "planning-execution",
        "description": "Planning, warehouse, transportation, commerce, and operational workflows.",
        "icon": "route",
        "emoji": "1f5fa",
    },
    "CONNECT": {
        "space": "EBF0LyiZSa2gJV3j6pkd",
        "section": "sitesc_gVV8D",
        "site_space": "sitesp_4YlT6",
        "folder": "connect-partners",
        "title": "Connect & Partners",
        "path": "connect-partners",
        "description": "Developer environment, APIs, partner onboarding, release governance, and support.",
        "icon": "plug",
        "emoji": "1f50c",
    },
    "HELP": {
        "space": "m3QbZzRKTUSYEJM3D4oQ",
        "section": "sitesc_zwwgT",
        "site_space": "sitesp_SlXLp",
        "folder": "help-center",
        "title": "Help Center",
        "path": "help-center",
        "description": "Support routes, common questions, and escalation guidance.",
        "icon": "life-ring",
        "emoji": "1f6df",
    },
}


def write_help_center() -> None:
    build_demo.write("help-center/.gitbook.yaml", build_demo.gitbook_yaml())
    build_demo.write("help-center/.gitbook/vars.yaml", build_demo.vars_yaml())
    build_demo.write(
        "help-center/README.md",
        """
---
description: Common questions, support routes, and escalation guidance for the Blue Yonder demo hub.
icon: life-ring
layout:
  width: wide
---

# Help Center

Give customers, partners, and implementation teams a single place to resolve common questions before opening a ticket.

<button type="button" class="button primary" data-action="ask" data-icon="gitbook-assistant">Ask support</button>

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><h3><i class="fa-circle-question" style="color:$primary;"></i></h3></td><td><strong>Common questions</strong></td><td>Planning, Connect, partner access, and documentation governance questions.</td><td><a href="common-questions.md">common-questions</a></td></tr>
<tr><td><h3><i class="fa-triangle-exclamation" style="color:$primary;"></i></h3></td><td><strong>Escalation paths</strong></td><td>How support, implementation, partner, and product teams route issues.</td><td><a href="escalation-paths.md">escalation-paths</a></td></tr>
<tr><td><h3><i class="fa-magnifying-glass-chart" style="color:$primary;"></i></h3></td><td><strong>AI answer quality</strong></td><td>How to improve answerability with summaries, glossary terms, and page ownership.</td><td><a href="ai-answer-quality.md">ai-answer-quality</a></td></tr>
</tbody></table>
""",
    )
    build_demo.write("help-center/SUMMARY.md", "# Table of contents\n\n* [Help Center](README.md)\n* [Common questions](common-questions.md)\n* [Escalation paths](escalation-paths.md)\n* [AI answer quality](ai-answer-quality.md)\n")
    build_demo.write("help-center/common-questions.md", build_demo.page("Common questions", "circle-question", "Representative support questions for a Blue Yonder documentation hub.", ["Which route should planners start with?", "Where do partners find Connect certification guidance?", "How do teams request documentation changes?", "Which content should be public versus authenticated?"]))
    build_demo.write("help-center/escalation-paths.md", build_demo.page("Escalation paths", "triangle-exclamation", "A simple routing model for product, implementation, partner, and support issues.", ["Route implementation blockers to the project owner.", "Route partner certification issues to partner operations.", "Route stale or unclear docs to the content owner through a change request."]))
    build_demo.write("help-center/ai-answer-quality.md", build_demo.page("AI answer quality", "magnifying-glass-chart", "Guidelines for making supply-chain content easier for AI agents to answer from.", ["Lead with direct summaries.", "Name roles, systems, and operational states consistently.", "Keep examples close to the page they support.", "Avoid burying important constraints in PDFs or gated files only."]))


def git_commit_push(message: str) -> None:
    subprocess.run(["git", "add", "."], cwd=build_demo.ROOT, check=True)
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=build_demo.ROOT)
    if diff.returncode != 0:
        subprocess.run(["git", "commit", "-m", message], cwd=build_demo.ROOT, check=True)
    subprocess.run(["git", "push"], cwd=build_demo.ROOT, check=True)


def main() -> None:
    os.environ["GITBOOK_TOKEN"] = build_demo.load_secret("GITBOOK_TOKEN")
    build_demo.os.environ["GITBOOK_TOKEN"] = os.environ["GITBOOK_TOKEN"]

    build_demo.scaffold()
    write_help_center()
    build_demo.replace_sentinels({key: value["space"] for key, value in TARGET_SPACES.items()})
    git_commit_push("Target existing Blue Yonder hub")

    created = {"org": ORG_ID, "site": SITE_ID, "spaces": {}, "sections": {}, "site_spaces": {}, "basename": "blue-yonder-hub"}
    for key, item in TARGET_SPACES.items():
        build_demo.api("PATCH", f"/spaces/{item['space']}", {"title": item["title"], "emoji": item["emoji"]})
        build_demo.api(
            "PATCH",
            f"/orgs/{ORG_ID}/sites/{SITE_ID}/sections/{item['section']}",
            {"title": item["title"], "path": item["path"], "description": item["description"], "icon": item["icon"], "draft": False, "defaultSiteSpace": item["site_space"]},
        )
        created["spaces"][key] = item["space"]
        created["sections"][key] = item["section"]
        created["site_spaces"][key] = item["site_space"]

    build_demo.api(
        "PATCH",
        f"/orgs/{ORG_ID}/sites/{SITE_ID}",
        {
            "title": "Blue Yonder HUB",
            "visibility": "share-link",
            "basename": "blue-yonder-hub",
            "defaultSiteSection": TARGET_SPACES["HOME"]["section"],
            "defaultSiteSpace": TARGET_SPACES["HOME"]["site_space"],
        },
    )

    imports = {}
    for key, item in TARGET_SPACES.items():
        status, _ = build_demo.api(
            "POST",
            f"/spaces/{item['space']}/git/import",
            {
                "url": build_demo.REPO_URL,
                "ref": "refs/heads/main",
                "repoProjectDirectory": item["folder"],
                "repoTreeURL": f"https://github.com/{build_demo.REPO_OWNER}/{build_demo.REPO}/tree/main",
                "repoCommitURL": f"https://github.com/{build_demo.REPO_OWNER}/{build_demo.REPO}/commit",
                "force": True,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            },
            expected=(204,),
        )
        imports[key] = {"status": status, "space": item["space"], "folder": item["folder"]}

    build_demo.write("gitbook-existing-hub-imports.json", json.dumps(imports, indent=2))
    build_demo.customize(created)
    final = build_demo.publish(created)
    build_demo.write("gitbook-existing-hub-publish.json", json.dumps(final, indent=2))
    git_commit_push("Publish existing Blue Yonder hub")
    print(json.dumps(final, indent=2))


if __name__ == "__main__":
    main()
