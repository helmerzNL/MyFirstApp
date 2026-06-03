# Inhoudelijke review DiscVault 26 docs-site

Review uitgevoerd tegen `/home/hermes/projects/github/DiscVault` en de huidige docs-site in `/home/hermes/projects/github/MyFirstApp`.

## Gecontroleerd

- Naamgeving: zichtbare site gebruikt DiscVault 26 en vermijdt oude productnamen/historische context als publiek verhaal.
- Kernonderwerpen: MCP, passkeys/WebAuthn, Docker/Unraid, users/groups, backups, watchlist/history en PWA-scope.
- Technische consistentie: poorten 6080/6090, `/data`, `/mcp`, `/mcp-health`, `RP_ID`, `RP_ORIGIN(S)`, `JWT_SECRET`, optionele OMDb/TMDb keys.
- Meertaligheid: de site heeft nu echte statische HTML-subfolders voor dezelfde 11 locales als discvault.eu: nl, en, de, fr, es, it, pt, da, no, fi, sv.
- Links/assets: lokale HTML-links en afbeeldingen resolve-en zonder ontbrekende bestanden.

## Direct gepatcht

- Generator aangepast zodat topicpagina’s geen hardcoded Engelse uitleg meer tonen in alle niet-Engelse talen.
- Gegenereerde HTML opnieuw opgebouwd voor 11 talen × 7 pagina’s plus root-taalkeuze.
- Root en oude top-level pagina’s functioneren als redirects/taalkeuze, zodat GitHub Pages zonder build-step kan publiceren.
- PWA-copy blijft afgezwakt: app-shell/leesfallback kan cachen, schrijfacties vereisen backend.
- MCP-copy blijft user-scoped: persoonlijke API-keys zijn het standaardverhaal, geen globale admin-sleutel als publieke route.

## Reviewbevindingen

- Sterk: de docs-site voldoet nu structureel aan de 11-talen-eis met echte HTML per taal en hreflang-alternates.
- Sterk: DiscVault 26 is consequent de publieke naam; historische implementatiecontext wordt niet uitgelegd.
- Sterk: de belangrijkste veiligheidsnuances staan erin: self-hosted, PWA niet volledig offline, MCP per gebruiker.
- Aandachtspunt: de meertalige subpagina’s zijn inhoudelijk nog compact. Ze noemen de juiste onderwerpen, maar missen nog de rijkere screenshots/quickstarts uit de eerdere Nederlandse basis.
- Aandachtspunt: Docker/Unraid-quickstart met exacte `docker run`, env-vars en backup/restore-stappen verdient in een volgende contentronde meer detail per taal.
- Aandachtspunt: GitHub Pages staat nog handmatig uit door ontbrekende Pages-adminrechten; dit blijft buiten de inhoudelijke docs-review.

## Concrete vervolgstappen

- Voeg per taal een uitgebreidere installatiepagina toe met poorten 6080/6090, `/data`, `RP_ID`, `RP_ORIGIN(S)`, `JWT_SECRET`, OMDb/TMDb en Unraid Community Applications.
- Voeg per taal een MCP-voorbeeldconfig toe met `Authorization: Bearer <personal-api-key>` en expliciete user-scope.
- Voeg screenshots terug in de topicpagina’s waar dat de uitleg helpt: collectie, passkeys/security, group management, backup, MCP activity.
- Pas pas daarna GitHub Pages/custom domain aan zodra de PAT/Pages-permissies beschikbaar zijn.
