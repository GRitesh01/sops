#!/usr/bin/env python3
"""Generate the StrategicOps static site.

Usage (from the project root):  python3 build/build.py
Writes index.html, pages/*.html, sitemap.xml and robots.txt.
Edit shared header/footer/metadata in build/common.py and content in build/*.py,
then re-run to keep every page consistent.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from common import PAGES, SITE  # noqa: E402
import pages_home, pages_services, pages_other  # noqa: E402

BUILDERS = {
    "home": pages_home.build_home,
    "about": pages_other.build_about,
    "services": pages_services.build_services,
    "consulting": lambda: pages_services.build_service("consulting"),
    "agents": lambda: pages_services.build_service("agents"),
    "multi": lambda: pages_services.build_service("multi"),
    "automation": lambda: pages_services.build_service("automation"),
    "enterprise": lambda: pages_services.build_service("enterprise"),
    "integration": lambda: pages_services.build_service("integration"),
    "solutions": pages_other.build_solutions,
    "industries": pages_other.build_industries,
    "technology": pages_other.build_technology,
    "process": pages_other.build_process,
    "cases": pages_other.build_cases,
    "insights": pages_other.build_insights,
    "contact": pages_other.build_contact,
    "consultation": pages_other.build_consultation,
    "privacy": pages_other.build_privacy,
    "terms": pages_other.build_terms,
    "cookies": pages_other.build_cookies,
}


def main():
    os.makedirs(os.path.join(ROOT, "pages"), exist_ok=True)
    for key, fn in BUILDERS.items():
        path = os.path.join(ROOT, PAGES[key][0])
        with open(path, "w", encoding="utf-8") as f:
            f.write(fn())
    urls = ""
    for key, (p, _) in PAGES.items():
        loc = SITE["base_url"] + "/" + ("" if p == "index.html" else p)
        pri = "1.0" if key == "home" else ("0.3" if key in ("privacy", "terms", "cookies") else "0.8")
        urls += "  <url><loc>%s</loc><priority>%s</priority></url>\n" % (loc, pri)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE["base_url"])
    print("Built %d pages." % len(BUILDERS))


if __name__ == "__main__":
    main()
