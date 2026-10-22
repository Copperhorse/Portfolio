# Portfolio

Single-page portfolio for M. Ahmad Siddiqui: plain HTML and CSS, no build step.

- `index.html`: the site. Images live in `data/`.
- `resume/resume.html`: resume source. `python resume/build.py` renders it to `data/Ahmad_Siddiqui_Resume.pdf` and a copy at `data/Resume.pdf` (the older, shared URL). Needs `playwright` with Chromium.
- `resume/resume.tex`: the same resume for Overleaf.
- `designs/`: the same content in several designs (Paper, Terminal, Editorial, Bento), kept as references for future sites.
  `designs/index.html` compares them; `python designs/build.py` regenerates the pages from `designs/content.py`
  (needs `jinja2`). The live `index.html` is the Bento design.

## Hosting and analytics

Served from GitHub Pages, which has no built-in analytics. On Vercel, turn on **Web Analytics** for the project
(Project → Analytics → Enable); `index.html` already loads `/_vercel/insights/script.js` on any host that is not
GitHub Pages or localhost, so page views and visitors appear once it is deployed there.
