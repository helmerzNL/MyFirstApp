# DiscVault 26 Docs

Statische documentatie-website voor DiscVault 26, bedoeld voor GitHub Pages zonder build-step.

## Pagina's

- `index.html` — overzicht en belangrijkste workflows
- `installatie.html` — Docker, Unraid, ports, volumes en env-vars
- `gebruikershandleiding.html` — toevoegen, importeren, zoeken, details, watchlist en history
- `beheer.html` — passkeys, invite-only, groups, backups, logs en push
- `mcp-ai.html` — MCP-clientconfig, persoonlijke API-keys en user-scoping
- `developers.html` — architectuur, runtime en publieke API-samenvatting
- `faq.html` — korte probleemoplossing en updatechecklist

## Lokaal bekijken

```bash
python3 -m http.server 8080
```

Daarna: http://localhost:8080

## GitHub Pages

De site gebruikt alleen statische HTML, CSS en relatieve links. Aanbevolen publicatie-route: GitHub Pages vanuit `main` en `/ (root)`, met `CNAME` op `docs.discvault.eu`.

Zie `DEPLOYMENT.md` voor de permissiecheck, DNS/HTTPS-notities en het stappenplan voor Settings > Pages.

## Assets

Geselecteerde screenshots staan in `assets/images/` en zijn gekopieerd uit de DiscVault productrepo. Publiceer geen secrets of echte API-sleutels in screenshots of codevoorbeelden.
