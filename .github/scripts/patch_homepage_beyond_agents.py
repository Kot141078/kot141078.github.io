from pathlib import Path

HOME = Path("index.html")
WORKFLOW = Path(".github/workflows/add-beyond-agents-home-entry.yml")
SCRIPT = Path(".github/scripts/patch_homepage_beyond_agents.py")

text = HOME.read_text(encoding="utf-8")

hero_old = """        <div class=\"section-links home-hero-actions\" aria-label=\"Primary homepage actions\">
          <a href=\"./start-here/\">Start here</a>
        <a href=\"./vision/\">Vision</a>
          <a href=\"./what-is-running/\">What is running</a>
          <a href=\"./publications/\">Publications</a>
          <a class=\"secondary-action\" href=\"./install-c/\">How to install c</a>
        </div>"""

hero_new = """        <div class=\"section-links home-hero-actions\" aria-label=\"Primary homepage actions\">
          <a href=\"./start-here/\">Start here</a>
          <a href=\"./beyond-agents/\">Beyond Agents</a>
          <a href=\"./vision/\">Vision</a>
          <a href=\"./what-is-running/\">What is running</a>
          <a href=\"./publications/\">Publications</a>
          <a class=\"secondary-action\" href=\"./install-c/\">How to install c</a>
        </div>"""

if 'href="./beyond-agents/">Beyond Agents</a>' not in text:
    if hero_old not in text:
        raise SystemExit("Expected homepage hero action block was not found")
    text = text.replace(hero_old, hero_new, 1)

explore_anchor = """          <article class=\"card route-card\"><h3>Vision</h3><p>Future-facing authorial statement separating forecasts, normative direction, and already-public work.</p><div class=\"section-links\"><a href=\"./vision/\">Open Vision</a></div></article>"""

beyond_card = """          <article class=\"card route-card\"><h3>Beyond Agents</h3><p>A dated public development timeline from agentic task execution to <code>c</code> as the continuity-bearing layer above replaceable models, agents, tools, and swarms.</p><div class=\"section-links\"><a href=\"./beyond-agents/\">Open Beyond Agents timeline</a></div></article>"""

if beyond_card not in text:
    if explore_anchor not in text:
        raise SystemExit("Expected Explore / Vision card was not found")
    text = text.replace(explore_anchor, beyond_card + "\n" + explore_anchor, 1)

HOME.write_text(text, encoding="utf-8")

# Remove the one-time machinery in the same commit that applies the patch.
if WORKFLOW.exists():
    WORKFLOW.unlink()
if SCRIPT.exists():
    SCRIPT.unlink()
