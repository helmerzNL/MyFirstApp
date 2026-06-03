# DiscVault 26 Docs — GitHub Pages deployment-plan

## Korte conclusie

Gebruik voor deze site GitHub Pages vanaf `main` / repository root. De docs-site is bewust statisch gebouwd met HTML, CSS, relatieve links en lokale assets. Een GitHub Actions workflow voegt nu geen waarde toe en vraagt extra tokenrechten (`workflow`) die de huidige agent-token niet heeft.

Beste route:

1. Publiceer vanuit `main` → `/ (root)`.
2. Houd `CNAME` in de repo met exact `docs.discvault.eu`.
3. Gebruik GitHub Actions pas later als er een echte build-step komt, bijvoorbeeld minify, image pipeline, meertalige generator of docs-framework.

## Huidige statuscheck

Uitgevoerd op 2026-06-03:

- `https://docs.discvault.eu` geeft HTTP 200 terug.
- `http://docs.discvault.eu` geeft HTTP 200 terug.
- `https://helmerznl.github.io/MyFirstApp/` verwijst door naar `http://docs.discvault.eu/`.
- DNS-resolutie voor `docs.discvault.eu` loopt via Cloudflare-adressen.
- `CNAME` op `origin/main` bestaat en bevat `docs.discvault.eu`.
- De live site toont nog oude copy/titel; de DiscVault 26-update staat lokaal en op preview-branch `review/discvault-docs-preview`, maar moet nog naar `main` om live te worden.
- De GitHub CLI is niet ingelogd en er is geen `GH_TOKEN`/`GITHUB_TOKEN` in de shell. Daardoor kan de agent Pages-instellingen niet via de API beheren of controleren.

## Waarom branch/root beter is dan GitHub Actions

### Branch/root Pages

Voordelen:

- Past bij de huidige site: pure statische bestanden zonder build.
- Geen workflow-bestanden nodig.
- Geen extra `workflow`-scope nodig op de token.
- Minder bewegende delen: push naar `main` is genoeg.
- Makkelijk door Helmer handmatig te beheren via Settings > Pages.

Nadelen:

- Geen automatische build, lint of asset pipeline.
- Als later een framework wordt gebruikt, moet de route aangepast worden.

### GitHub Actions Pages

Voordelen:

- Geschikt zodra er een build-proces komt.
- Kan previews, HTML-validatie en asset-optimalisatie toevoegen.
- Scheidt bronbestanden en gepubliceerde output.

Nadelen voor nu:

- Huidige token mist `workflow`-rechten.
- Pages/deploy-workflows vragen extra GitHub-permissies en meer onderhoud.
- Overkill voor handgeschreven HTML/CSS.

## Handmatige actie voor Helmer in GitHub

Als Pages nog niet correct ingesteld staat:

1. Ga naar GitHub repository `helmerzNL/MyFirstApp`.
2. Open `Settings`.
3. Open `Pages`.
4. Kies bij `Build and deployment`:
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/ (root)`
5. Controleer `Custom domain`:
   - `docs.discvault.eu`
6. Klik `Save`.
7. Wacht tot GitHub de Pages-build heeft gepubliceerd.
8. Zet `Enforce HTTPS` pas aan wanneer GitHub aangeeft dat het certificaat klaar is.

Let op bij Cloudflare:

- Voor GitHub Pages certificate provisioning is `DNS only` vaak betrouwbaarder dan een geproxiede Cloudflare-record.
- Als HTTPS-provisioning blijft hangen: zet `docs.discvault.eu` tijdelijk op DNS-only, wacht tot GitHub HTTPS klaar is, en zet daarna pas eventueel Cloudflare proxy terug aan.
- De CNAME moet naar `helmerznl.github.io` wijzen als GitHub Pages direct de custom domain moet valideren.

## Tokenrechten als Henk/agent dit zelf moet beheren

Voor alleen content publiceren:

- Git push naar `helmerzNL/MyFirstApp` is genoeg.
- Klassieke PAT: `repo` voor private repo's; voor public repo's kan beperktere write-to-code toegang genoeg zijn.
- Fine-grained PAT: repository `helmerzNL/MyFirstApp` met `Contents: Read and write`.

Voor Pages-instellingen beheren via API:

- Fine-grained PAT: repository `helmerzNL/MyFirstApp` met Pages/Administration-rechten die Pages settings mogen lezen en wijzigen.
- Klassieke PAT: meestal `repo` plus admin/configure-rechten op de repository.
- De agent moet de token beschikbaar krijgen als `GH_TOKEN` of via `gh auth login`.

Voor GitHub Actions route:

- Fine-grained PAT: `Contents: Read and write`, `Actions: Read and write`, en recht om workflow-bestanden te wijzigen.
- Klassieke PAT: `repo` + `workflow`.
- Pas nodig als er echt een `.github/workflows/...` deploybestand komt.

## Publicatie-checklist

1. Merge/push de DiscVault 26-site naar `main`.
2. Controleer dat `CNAME` aanwezig blijft met `docs.discvault.eu`.
3. Controleer live HTML:
   - titel bevat `DiscVault 26`;
   - geen oude productnaam/copy zichtbaar;
   - CSS en screenshots laden via relatieve paden.
4. Controleer Pages in GitHub Settings:
   - Source `Deploy from a branch`;
   - branch `main`;
   - folder `/ (root)`;
   - custom domain `docs.discvault.eu`.
5. Controleer DNS/HTTPS:
   - `https://docs.discvault.eu` geeft 200;
   - GitHub Pages meldt certificate/HTTPS klaar;
   - bij Cloudflare-problemen tijdelijk DNS-only gebruiken.

## Wanneer alsnog naar GitHub Actions overstappen

Stap pas over op Actions als één van deze dingen nodig wordt:

- automatische HTML/CSS-validatie;
- screenshot- of image-optimalisatie;
- vertaalbuild voor meerdere talen;
- gegenereerde navigatie/search index;
- docs-framework zoals Astro, VitePress, Docusaurus of MkDocs.

Tot die tijd is `main` / root de simpelste en robuustste deploy-route.
