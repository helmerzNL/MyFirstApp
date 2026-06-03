#!/usr/bin/env python3
"""Generate the static multilingual DiscVault 26 docs site.

The generated HTML is committed so GitHub Pages can serve it without a build step.
Run manually after editing i18n-content.json or this template.
"""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "i18n-content.json").read_text(encoding="utf-8"))
CONTENT = DATA["content"]
LANGS = DATA["meta"]["languages"]

PAGE_SLUGS = {
    "nl": {"index": "index.html", "install": "installatie.html", "guide": "gebruikershandleiding.html", "admin": "beheer.html", "mcp": "mcp-ai.html", "developers": "developers.html", "faq": "faq.html"},
    "en": {"index": "index.html", "install": "installation.html", "guide": "user-guide.html", "admin": "admin.html", "mcp": "mcp-ai.html", "developers": "developers.html", "faq": "faq.html"},
    "de": {"index": "index.html", "install": "installation.html", "guide": "benutzerhandbuch.html", "admin": "verwaltung.html", "mcp": "mcp-ki.html", "developers": "entwickler.html", "faq": "faq.html"},
    "fr": {"index": "index.html", "install": "installation.html", "guide": "guide-utilisateur.html", "admin": "administration.html", "mcp": "mcp-ia.html", "developers": "developpeurs.html", "faq": "faq.html"},
    "es": {"index": "index.html", "install": "instalacion.html", "guide": "guia-usuario.html", "admin": "administracion.html", "mcp": "mcp-ia.html", "developers": "desarrolladores.html", "faq": "faq.html"},
    "it": {"index": "index.html", "install": "installazione.html", "guide": "guida-utente.html", "admin": "gestione.html", "mcp": "mcp-ia.html", "developers": "sviluppatori.html", "faq": "faq.html"},
    "pt": {"index": "index.html", "install": "instalacao.html", "guide": "guia-utilizacao.html", "admin": "administracao.html", "mcp": "mcp-ia.html", "developers": "programadores.html", "faq": "faq.html"},
    "da": {"index": "index.html", "install": "installation.html", "guide": "brugervejledning.html", "admin": "administration.html", "mcp": "mcp-ai.html", "developers": "udviklere.html", "faq": "faq.html"},
    "no": {"index": "index.html", "install": "installasjon.html", "guide": "brukerveiledning.html", "admin": "administrasjon.html", "mcp": "mcp-ai.html", "developers": "utviklere.html", "faq": "faq.html"},
    "fi": {"index": "index.html", "install": "asennus.html", "guide": "kayttoohje.html", "admin": "hallinta.html", "mcp": "mcp-ai.html", "developers": "kehittajat.html", "faq": "ukk.html"},
    "sv": {"index": "index.html", "install": "installation.html", "guide": "anvandarguide.html", "admin": "administration.html", "mcp": "mcp-ai.html", "developers": "utvecklare.html", "faq": "faq.html"},
}

UI = {
    "nl": {"skip": "Spring naar inhoud", "home": "Docs home", "langs": "Beschikbare talen", "source": "Broncode", "product": "Productwebsite", "plan": "Docs-plan", "footer": "Statische GitHub Pages-site zonder build-step. Relatieve links, lokale screenshots en geen secrets.", "fallback": "Als je taal niet beschikbaar is, valt de site terug op Nederlands of Engels.", "github_pages": "Geschikt voor GitHub Pages en een later custom domain; HTTPS voor docs.discvault.eu wordt nog niet geclaimd.", "open": "Open deze pagina"},
    "en": {"skip": "Skip to content", "home": "Docs home", "langs": "Available languages", "source": "Source code", "product": "Product website", "plan": "Docs plan", "footer": "Static GitHub Pages site without a build step. Relative links, local screenshots and no secrets.", "fallback": "If a language is unavailable, the site falls back to Dutch or English.", "github_pages": "Ready for GitHub Pages and a later custom domain; HTTPS for docs.discvault.eu is not claimed yet.", "open": "Open this page"},
}

def ui(lang: str, key: str) -> str:
    return UI.get(lang, UI["en"])[key]

def esc(value: str) -> str:
    return html.escape(value, quote=True)

def page_url(lang: str, page: str, from_lang: str | None = None) -> str:
    prefix = "" if from_lang is None else f"../{lang}/"
    if lang == from_lang:
        prefix = ""
    return prefix + PAGE_SLUGS[lang][page]

def nav(lang: str, page: str) -> str:
    labels = CONTENT[lang]["nav"]
    items = [("index", labels["overview"]), ("install", labels["install"]), ("guide", labels["guide"]), ("admin", labels["admin"]), ("mcp", labels["mcp"]), ("developers", labels["developers"]), ("faq", labels["faq"])]
    return "\n".join(
        f'<a href="{esc(page_url(lang, key, lang))}" class="{"active" if key == page else ""}">{esc(label)}</a>'
        for key, label in items
    )

def language_menu(lang: str, page: str) -> str:
    links = []
    for code in LANGS:
        name = CONTENT[code]["languageName"]
        current = ' aria-current="true"' if code == lang else ""
        links.append(f'<a href="{esc(page_url(code, page, lang))}" hreflang="{code}" lang="{code}"{current}>{esc(name)}</a>')
    return "\n".join(links)

def hreflangs(page: str) -> str:
    return "\n".join(f'  <link rel="alternate" hreflang="{code}" href="../{code}/{PAGE_SLUGS[code][page]}">' for code in LANGS)

def layout(lang: str, page: str, title: str, description: str, body: str) -> str:
    c = CONTENT[lang]
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)} · DiscVault 26 Docs</title>
  <meta name="description" content="{esc(description)}">
  <link rel="stylesheet" href="../styles.css">
{hreflangs(page)}
</head>
<body>
  <a class="skip-link" href="#content">{esc(ui(lang, "skip"))}</a>
  <header class="site-header">
    <a class="brand" href="{esc(page_url(lang, "index", lang))}" aria-label="DiscVault 26 {esc(ui(lang, "home"))}">
      <span class="brand-mark">DV</span>
      <span><strong>DiscVault 26</strong><small>Docs</small></span>
    </a>
    <nav class="nav" aria-label="Main navigation">{nav(lang, page)}</nav>
    <div class="header-actions">
      <details class="language-menu">
        <summary>{esc(c["languageName"])}</summary>
        <div class="language-list" aria-label="{esc(ui(lang, "langs"))}">
          {language_menu(lang, page)}
        </div>
      </details>
      <a class="github-link" href="https://github.com/helmerzNL/DiscVault" rel="noreferrer">GitHub</a>
    </div>
  </header>
  <main id="content">
{body}
  </main>
  <footer class="site-footer">
    <div>
      <strong>DiscVault 26 Docs</strong>
      <p>{esc(ui(lang, "footer"))}</p>
    </div>
    <div class="footer-links">
      <a href="https://github.com/helmerzNL/DiscVault" rel="noreferrer">{esc(ui(lang, "source"))}</a>
      <a href="https://discvault.eu" rel="noreferrer">{esc(ui(lang, "product"))}</a>
      <a href="../docs-plan.md">{esc(ui(lang, "plan"))}</a>
    </div>
  </footer>
</body>
</html>
'''

def card(title: str, text: str, href: str | None = None, link: str | None = None) -> str:
    anchor = f'<a href="{esc(href)}">{esc(link or title)} →</a>' if href else ""
    return f'<article class="card"><h3>{esc(title)}</h3><p>{esc(text)}</p>{anchor}</article>'

def index_body(lang: str) -> str:
    c = CONTENT[lang]; s = c["sections"]; core = c["core"]
    return f'''    <section class="hero">
      <div class="hero-copy">
        <p class="eyebrow">{esc(c["hero"]["eyebrow"])}</p>
        <h1>{esc(c["hero"]["title"])}</h1>
        <p class="lead">{esc(c["hero"]["lead"])}</p>
        <div class="actions">
          <a class="button primary" href="{esc(page_url(lang, "install", lang))}">{esc(c["hero"]["primaryCta"])}</a>
          <a class="button" href="{esc(page_url(lang, "guide", lang))}">{esc(c["hero"]["secondaryCta"])}</a>
        </div>
        <ul class="pill-list" aria-label="DiscVault 26"><li>Docker & Unraid</li><li>Passkeys</li><li>Watchlist</li><li>Backups</li><li>MCP</li><li>PWA</li></ul>
      </div>
      <div class="hero-visual">
        <figure class="shot browser-frame"><img src="../assets/images/Desktop_collection_collection.webp" alt="DiscVault collection overview"><figcaption>{esc(s["useBody"])}</figcaption></figure>
        <figure class="shot"><img src="../assets/images/mobile_collection.webp" alt="DiscVault mobile collection view"><figcaption>Responsive PWA.</figcaption></figure>
      </div>
    </section>
    <section class="section">
      <div class="section-heading"><p class="eyebrow">{esc(s["workflowsEyebrow"])}</p><h2>{esc(s["workflowsTitle"])}</h2><p class="lead">{esc(s["workflowsLead"])}</p></div>
      <div class="grid three">
        {card(s["installTitle"], s["installBody"], page_url(lang, "install", lang), c["nav"]["install"])}
        {card(s["useTitle"], s["useBody"], page_url(lang, "guide", lang), c["nav"]["guide"])}
        {card(s["adminTitle"], s["adminBody"], page_url(lang, "admin", lang), c["nav"]["admin"])}
      </div>
    </section>
    <section class="section split">
      <div><p class="eyebrow">{esc(s["architectureEyebrow"])}</p><h2>{esc(s["architectureTitle"])}</h2></div>
      <div class="stack">
        <div class="flow-row"><strong>Frontend/PWA</strong><span>Responsive webapp met cached app-shell en beperkte offline leesfallback; wijzigingen schrijven vereist backend-connectiviteit.</span></div>
        <div class="flow-row"><strong>API</strong><span>Routes voor films, imports, watchlist, auth, groups, settings, backups en push.</span></div>
        <div class="flow-row"><strong>Data & assets</strong><span>Persistente data in <code>/data</code>: collectiedata, posters, avatars, profielen en backups.</span></div>
        <div class="flow-row"><strong>MCP</strong><span>Streamable HTTP endpoint via <code>/mcp</code>, bij voorkeur met persoonlijke API-key per gebruiker.</span></div>
      </div>
    </section>
    <section class="section" id="languages">
      <div class="section-heading"><p class="eyebrow">{esc(s["languagesEyebrow"])}</p><h2>{esc(s["languagesTitle"])}</h2><p class="lead">{esc(s["languagesLead"])} {esc(ui(lang, "fallback"))}</p></div>
      <ul class="language-grid" aria-label="{esc(ui(lang, "langs"))}">{''.join(f'<li class="{"active" if code == lang else ""}"><a href="{esc(page_url(code, "index", lang))}" hreflang="{code}">{esc(CONTENT[code]["languageName"])}</a></li>' for code in LANGS)}</ul>
    </section>
    <section class="section">
      <div class="section-heading"><p class="eyebrow">{esc(s["scopeEyebrow"])}</p><h2>{esc(s["scopeTitle"])}</h2></div>
      <div class="grid three">
        <article class="callout warning"><h3>{esc(core["selfHostedTitle"])}</h3><p>{esc(core["selfHostedBody"])}</p></article>
        <article class="callout warning"><h3>{esc(core["pwaTitle"])}</h3><p>{esc(core["pwaBody"])}</p></article>
        <article class="callout warning"><h3>{esc(core["mcpTitle"])}</h3><p>{esc(core["mcpBody"])}</p></article>
      </div>
    </section>'''

def topic_body(lang: str, page: str) -> str:
    c = CONTENT[lang]; s = c["sections"]; core = c["core"]; n = c["nav"]
    page_data = {
        "install": (n["install"], s["installBody"], [("Docker / Unraid", s["installBody"]), ("Passkeys / RP_ID", s["adminBody"]), ("GitHub Pages", ui(lang, "github_pages"))]),
        "guide": (n["guide"], s["useBody"], [(s["useTitle"], s["useBody"]), ("Watchlist & history", s["useBody"]), ("PWA", core["pwaBody"])]),
        "admin": (n["admin"], s["adminBody"], [(core["selfHostedTitle"], core["selfHostedBody"]), ("Passkeys & invites", s["adminBody"]), ("Backups & restore", s["adminBody"])]),
        "mcp": (n["mcp"], core["mcpBody"], [(core["mcpTitle"], core["mcpBody"]), ("Endpoint /mcp", core["mcpBody"]), ("User scope", core["mcpBody"])]),
        "developers": (n["developers"], s["workflowsLead"], [(s["architectureTitle"], s["installBody"]), (s["languagesTitle"], s["languagesLead"]), (s["scopeTitle"], f"{core['selfHostedBody']} {core['mcpBody']}")]),
        "faq": (n["faq"], s["scopeTitle"], [(core["selfHostedTitle"], core["selfHostedBody"]), (core["pwaTitle"], core["pwaBody"]), (core["mcpTitle"], core["mcpBody"]), (s["languagesTitle"], "nl, en, de, fr, es, it, pt, da, no, fi, sv")]),
    }[page]
    title, lead, cards = page_data
    return f'''    <section class="page-hero">
      <p class="eyebrow">DiscVault 26 Docs</p>
      <h1>{esc(title)}</h1>
      <p class="lead">{esc(lead)}</p>
      <div class="actions"><a class="button" href="{esc(page_url(lang, "index", lang))}">{esc(n["overview"])}</a><a class="button primary" href="{esc(page_url(lang, "faq", lang))}">{esc(n["faq"])}</a></div>
    </section>
    <section class="section">
      <div class="grid three">
        {''.join(card(t, b) for t, b in cards)}
      </div>
    </section>
    <section class="section split">
      <div><p class="eyebrow">{esc(s["scopeEyebrow"])}</p><h2>{esc(s["scopeTitle"])}</h2></div>
      <div class="stack">
        <div class="flow-row"><strong>{esc(core["selfHostedTitle"])}</strong><span>{esc(core["selfHostedBody"])}</span></div>
        <div class="flow-row"><strong>{esc(core["pwaTitle"])}</strong><span>{esc(core["pwaBody"])}</span></div>
        <div class="flow-row"><strong>{esc(core["mcpTitle"])}</strong><span>{esc(core["mcpBody"])}</span></div>
      </div>
    </section>'''

def root_index() -> str:
    lang_links = "\n".join(f'<a class="button" href="{code}/index.html" hreflang="{code}" lang="{code}">{esc(CONTENT[code]["languageName"])}</a>' for code in LANGS)
    return f'''<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>DiscVault 26 Docs</title>
  <meta name="description" content="Meertalige DiscVault 26 documentatie in dezelfde 11 talen als DiscVault.">
  <link rel="stylesheet" href="./styles.css">
  <link rel="canonical" href="./nl/index.html">
  <script>
    (function () {{
      var supported = {json.dumps(LANGS)};
      var preferred = (navigator.languages || [navigator.language || 'nl'])
        .map(function (lang) {{ return String(lang).slice(0, 2).toLowerCase(); }})
        .find(function (lang) {{ return supported.indexOf(lang) !== -1; }});
      window.location.replace('./' + (preferred || 'nl') + '/index.html');
    }})();
  </script>
</head>
<body>
  <main id="content">
    <section class="hero single">
      <div class="hero-copy">
        <p class="eyebrow">DiscVault 26 Docs</p>
        <h1>Kies je taal</h1>
        <p class="lead">Deze statische GitHub Pages-site is beschikbaar in dezelfde 11 talen als DiscVault. Zonder JavaScript kun je hieronder handmatig kiezen; met JavaScript word je doorgestuurd naar je browsertaal met fallback naar Nederlands.</p>
        <div class="actions">{lang_links}</div>
      </div>
    </section>
  </main>
</body>
</html>
'''

# Remove old generated language HTML files only in known language dirs.
for code in LANGS:
    (ROOT / code).mkdir(exist_ok=True)

for code in LANGS:
    c = CONTENT[code]
    pages = {
        "index": (c["nav"]["overview"], c["hero"]["lead"], index_body(code)),
        "install": (c["nav"]["install"], c["sections"]["installBody"], topic_body(code, "install")),
        "guide": (c["nav"]["guide"], c["sections"]["useBody"], topic_body(code, "guide")),
        "admin": (c["nav"]["admin"], c["sections"]["adminBody"], topic_body(code, "admin")),
        "mcp": (c["nav"]["mcp"], c["core"]["mcpBody"], topic_body(code, "mcp")),
        "developers": (c["nav"]["developers"], "DiscVault 26 developer documentation.", topic_body(code, "developers")),
        "faq": (c["nav"]["faq"], "DiscVault 26 FAQ.", topic_body(code, "faq")),
    }
    for page, (title, desc, body) in pages.items():
        (ROOT / code / PAGE_SLUGS[code][page]).write_text(layout(code, page, title, desc, body), encoding="utf-8")

(ROOT / "index.html").write_text(root_index(), encoding="utf-8")
print(f"Generated {len(LANGS) * 7 + 1} HTML files for {', '.join(LANGS)}")
