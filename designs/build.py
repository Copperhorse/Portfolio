"""Render every design in designs/templates/*.html.j2 from content.py into designs/<name>.html.

    python designs/build.py
"""
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

import content

here = Path(__file__).resolve().parent
env = Environment(loader=FileSystemLoader(here / "templates"), autoescape=select_autoescape(["html", "j2"]))

for tpl in sorted((here / "templates").glob("*.html.j2")):
    name = tpl.name.removesuffix(".html.j2")
    html = env.get_template(tpl.name).render(
        P=content.PROFILE, PROJECTS=content.PROJECTS, ALSO=content.ALSO,
        EXPERIENCE=content.EXPERIENCE, SKILLS=content.SKILLS, ABOUT=content.ABOUT,
    )
    (here / f"{name}.html").write_text(html, encoding="utf-8")
    print("wrote", f"designs/{name}.html", f"({len(html):,} bytes)")
