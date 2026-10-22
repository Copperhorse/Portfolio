"""Render resume/resume.html to data/Ahmad_Siddiqui_Resume.pdf (needs: pip install playwright && playwright install chromium)."""
from pathlib import Path

from playwright.sync_api import sync_playwright

here = Path(__file__).resolve().parent
out = here.parent / "data" / "Ahmad_Siddiqui_Resume.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto((here / "resume.html").as_uri())
    page.pdf(path=str(out), prefer_css_page_size=True, print_background=True)
    browser.close()
print("wrote", out)
