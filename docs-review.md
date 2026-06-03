# Inhoudelijke review DiscVault 26 docs-site

Review uitgevoerd tegen `/home/hermes/projects/github/DiscVault` en de huidige docs-site in `/home/hermes/projects/github/MyFirstApp`.

## Gecontroleerd

- Naamgeving: zichtbare site gebruikt DiscVault 26 en vermijdt DiscVault Next/legacy als publiek verhaal.
- Kernonderwerpen: MCP, passkeys/WebAuthn, Docker/Unraid, users/groups, backups, watchlist/history en PWA-scope.
- Technische consistentie: poorten 6080/6090, `/data`, `/mcp`, `/mcp-health`, `RP_ID`, `RP_ORIGIN(S)`, `JWT_SECRET`, optionele OMDb/TMDb keys.
- Meertaligheid: taalkiezer bevat dezelfde 11 locales als discvault.eu: nl, en, de, fr, es, it, pt, da, no, fi, sv.
- Links/assets: lokale HTML-links en afbeeldingen resolve-en zonder ontbrekende bestanden.

## Direct gepatcht

- Docker quickstart aangevuld met OMDb/TMDb placeholders, `JWT_SECRET` en lowercase GHCR image-naam.
- Passkey-uitleg aangescherpt met `RP_ORIGINS` en productie-waarschuwing rond secrets.
- PWA-copy afgezwakt: app-shell/leesfallback kan cachen, schrijfacties vereisen backend.
- MemberGroups-copy verduidelijkt: gedeelde views/uitnodigingen, geen real-time co-editing claim.
- MCP-copy aangescherpt: persoonlijke API-keys/user-scope, huidige tools kunnen zoeken/lezen/toevoegen/lijsten ophalen; geen globale admin-sleutel als standaardpad.
- Developers-pagina aangevuld met optionele directe MCP-poort 6090.

## Open verbeterpunten voor volgende fase

- Echte 11-talige docs ontbreken nog. De taalkiezer en locale-lijst zijn aanwezig, maar de pagina’s zelf zijn nog Nederlandse brontekst. Voor publicatie per taal zijn `/en/`, `/de/`, `/fr/`, `/es/`, `/it/`, `/pt/`, `/da/`, `/no/`, `/fi/`, `/sv/` of een client-side vertaalmechanisme nodig.
- Overweeg een korte aparte pagina “Releasekanalen en updates” als Unraid/GHCR publicatie definitief is, zodat `latest/stable/beta` minder verspreid staat.
- Als API-contracten later publiek worden, link dan alleen naar bewust gepubliceerde contractdocs; nu blijft de developers-pagina terecht hoog-over.
- GitHub Pages staat nog handmatig uit door ontbrekende Pages-adminrechten; dit blijft buiten de inhoudelijke docs-review.
