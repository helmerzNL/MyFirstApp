# DiscVault 26 Docs - informatiearchitectuur

## Doelgroep

- Self-hosters en Unraid-gebruikers die DiscVault willen installeren, updaten en beheren.
- Fysieke media collectors die willen begrijpen hoe collectiebeheer, import, metadata, watchlist en groepen werken.
- Admins die gebruikers, passkeys, invite-only registratie, backups, logs, push-notificaties en MCP/API-sleutels beheren.
- Developers/integrators die API, MCP, MovieVault-koppeling en container-runtime globaal moeten begrijpen zonder interne data-contracten te publiceren.

## Navigatievoorstel

Houd fase 2 statisch en GitHub Pages-vriendelijk, zonder build-step. Splits de huidige single-page site naar kleine HTML-pagina's zodra de content groter wordt:

1. `index.html` - landing/overzicht: wat is DiscVault 26, belangrijkste flows, links naar install/guides.
2. `installatie.html` - Docker, Unraid, ports, volumes, env-vars, updatebeleid, Pages-note.
3. `gebruikershandleiding.html` - collectie, zoeken/filteren, toevoegen, importeren, bulk refresh, movie detail, watchlist/history, groups.
4. `beheer.html` - passkeys, invite-only, user/group management, backups/restore, logs, settings, push notifications.
5. `mcp-ai.html` - persoonlijke API keys, MCP endpoint, clientconfig, tool-overzicht, user-scoping en veiligheid.
6. `developers.html` - architectuur, repo-layout, API-samenvatting, frontend/backend/MCP-componenten, contracts die openbaar mogen worden genoemd.
7. `faq.html` - korte probleemoplossing: login/passkeys, metadata keys, reverse proxy, Unraid, backups, MCP-connectie.

Als coder het klein wil houden: behoud één pagina, maar gebruik dezelfde structuur als secties met duidelijke anchors en cards.

## Pagina-indeling

- Bovenaan: consistente header met logo, korte tagline, hoofdnav en GitHub-link.
- Per pagina: hero/introtekst, 3-5 kernkaarten, daarna stap-voor-stap secties met screenshots.
- Gebruik callouts:
  - `Belangrijk` voor RP_ID/RP_ORIGIN, data-volume, secrets en admin-only acties.
  - `Tip` voor Unraid, metadata API keys, PWA/offline gebruik.
  - `Niet publiceren` voor interne DB-details: verwijs naar UI/API/backups i.p.v. tabellen/migraties.
- Onder elke guide: “Bronnen in repo” met bestandslinks en “Nog nodig van writer/coder”.

## Eerst te schrijven onderwerpen

1. Installatie en quickstart: Docker-run, Unraid-verwijzing, `/data` volume, ports 6080/6090, `TZ`, `RP_ID`, `RP_ORIGIN`, optionele metadata keys.
2. Dagelijks gebruik: collectie bekijken, zoeken/filteren, handmatig toevoegen, import-flow, bulk metadata refresh, movie detail.
3. Account/admin: passkeys, invite-only registratie, users/groups, backups/restore, logs.
4. AI/MCP: persoonlijke API-key in profiel, `http://<host>:6080/mcp`, Bearer token config, beschikbare tools en user-scoping.
5. Developer-overzicht: `app/backend`, `app/frontend`, `app/mcp-server`, all-in-one container, API-samenvatting, contractdocs.

## Screenshots die gebruikt moeten worden

Gebruik primair bestaande assets uit `/home/hermes/projects/github/DiscVault/website/images/` of `/home/hermes/projects/github/DiscVault/screenshots/desktop/`:

- Overzicht/landing: `Desktop_collection_collection.png`, `mobile_collection.jpeg`.
- Zoeken/filteren: `Desktop_search.png`, `Desktop_more_options.png`.
- Movie detail: `Desktop_movie_detail_01.png`, `Desktop_movie_detail_hdr_dolbyvision.png`, `Desktop_movie_detail_watch_history.png`, eventueel `Desktop_movie_detail_02_nl.png`.
- Toevoegen/importeren: `Desktop_add_manual_01.png`, `Desktop_add_manual_02.png`, `Desktop_add_import_01.png`, `Desktop_add_import_02.png`, `Desktop_add_import_03.png`, `Desktop_collection_bulk_refreh*.png`.
- Watchlist/history: `Desktop_watchlist.png`, `Desktop_watch_history.png`.
- Profiel/MCP: `Desktop_profile_api_keys.png`, `Desktop_profile_mcp_activity.png`, `Desktop_profile_security.png`, `Desktop_profile_push_notifications.png`.
- Admin/beheer: `Admin_Desktop_security_user_mgmt.png`, `Admin_Desktop_security_invite_only.png`, `Admin_Desktop_security_group_mgmt.png`, `Admin_Desktop_backup.png`, `Admin_Desktop_logfiles.png`, `Admin_Desktop_advanced.png`.
- Installatie/Unraid: `discvault_available_in_unraid_community_applications.png`.

Coder: kopieer alleen de gekozen screenshots naar `MyFirstApp/assets/` of `MyFirstApp/images/` zodat de docs-site zelfstandig via GitHub Pages werkt.

## Bronbestanden voor writer/coder

- Productoverzicht en featurelijst: `/home/hermes/projects/github/DiscVault/README.md`.
- App/dev/runtime uitleg: `/home/hermes/projects/github/DiscVault/app/README.md`.
- All-in-one container endpoints: `/home/hermes/projects/github/DiscVault/app/deploy/all-in-one/README.md`.
- Unraid details: `/home/hermes/projects/github/DiscVault/app/deploy/unraid/README.md` en `PUBLISH.md`.
- Frontend flows/labels: `/home/hermes/projects/github/DiscVault/app/frontend/index.html`, `app/frontend/js/app.js`, `collection.js`, `import.js`, `settings.js`, `auth.js`, `social.js`, `i18n/translations.json`.
- Backend/API: `/home/hermes/projects/github/DiscVault/app/backend/app.py`, `settings/routes.py`, `push/routes.py`, `config.py`, `db.py`.
- MCP details: `/home/hermes/projects/github/DiscVault/app/mcp-server/server.py` en het MCP-hoofdstuk in `app/README.md`.
- Openbare contracten: `/home/hermes/projects/github/DiscVault/docs/contracts/*.md`, vooral `MOBILE_API_CONTRACT.md`, `PASSKEY_AUTH_IMPLEMENTATION_CONTRACT.md`, `AUTH_AND_INVITES_UI_CONTRACT.md`, `MOVIEVAULT_INTEGRATION_CONTRACT.md`.
- Let op: `CONTAINER_SCHEMA.md` zegt expliciet dat genormaliseerde opslag/migratiedetails niet gepubliceerd moeten worden.

## Expliciet nodig van writer

- Nederlandse microcopy per pagina: korte intro, stappen, waarschuwingen en FAQ-antwoorden.
- Heldere uitleg voor niet-developers van passkeys, invite-only, `/data` volume, backups en metadata API keys.
- Screenshot-bijschriften in NL, met focus op “wat zie ik en wat doe ik hier?”.
- Meertalige contentmatrix voor dezelfde 11 talen als DiscVault: zie `docs-i18n-content-matrix.md` en machineleesbare bron `i18n-content.json`.

## Expliciet nodig van coder

- Kies single-page anchors of meerdere statische HTML-pagina's; geen build-step tenzij noodzakelijk.
- Maak `assets/` of `images/` aan en kopieer geselecteerde screenshots uit de DiscVault repo.
- Bouw nav, responsive screenshot cards, callouts en bronlinks.
- Houd GitHub Pages simpel: relatieve links, geen server-side routing, geen secrets, geen workflow/Pages-admin acties met huidige PAT.
- Commit lokaal in MyFirstApp; push pas na finale check.
