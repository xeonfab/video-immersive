# Sélection des photos source — Le Château de Sable

**Source** : Google Drive, dossier `lechateaudesable - Photos Instagram - 25 dernieres`
(id `1VzDDBWa770635g_d0ZusIDKiQJK54RIr`, dans `Videos_immersives`)

## Bilan du tri

- **24** photos rapatriées depuis Drive
- **7** écartées au pré-filtrage technique (résolution insuffisante, < 1080px sur le
  plus petit côté) :
  - `2026-01-21_5f95cb25...` (977px)
  - `2026-02-05_e5115cf6...` (960px)
  - `2026-02-21_ef6f2352...` (960px)
  - `2026-03-18_7a6e3e6f...` (721px)
  - `2026-03-26_107c1bec...` (912px)
  - `2026-03-26_82a94b2c...` (540px)
  - `2026-08-15_a38f4aa4...` (1026px)
- **17** candidats techniquement valides passés en revue visuelle
- **4** écartées en revue visuelle malgré une résolution correcte :
  - `2025-06-29...` et `2025-12-20...` (portrait chef) et `2026-04-10...`
    (portrait réceptionniste) — visages nets et identifiables, risque d'usage
    commercial de l'image d'une personne sans consentement
  - `2025-11-28...` — montage collage 4 images + texte "PORSPODER", hors
    format pour une animation image-to-video
  - `2025-07-19...` — festival de cerfs-volants, ciel chargé et scène trop
    chaotique, hors-catégorie
- **8** retenues pour la vidéo (voir tableau ci-dessous)

## Sélection finale

| # | Fichier | Catégorie | Description | Raison de sélection |
|---|---|---|---|---|
| 01 | `01-gastronomie-dessert-chocolat.jpg` | Gastronomie | Dessert chocolat/cerises, vue plongeante sur table bois, quenelle et coulis | Meilleur candidat gastronomie du dossier — composition épurée, forte lisibilité, sujet net et centré, idéal pour un léger zoom |
| 02 | `02-gastronomie-coffret-vin.jpg` | Gastronomie | Coffret de vin (Brumont Montus) et verre, posé sur un rocher de granit | Complète le plan dessert par une note terroir/œnologie, ancrage minéral local |
| 03 | `03-interieur-fauteuil-cosy.jpg` | Intérieur | Gros plan sur un fauteuil beige, bougie et guirlande lumineuse en arrière-plan | Substitut "chambre" — aucune photo de chambre n'était disponible dans ce dossier (voir note ci-dessous), cette image porte une ambiance intime et chaleureuse |
| 04 | `04-espaces-communs-spa.jpg` | Espaces communs | Salle de soins/massage, lumière tamisée, ambiance zen | Espace bien-être, différenciant fort pour un 4 étoiles, aucun visage |
| 05 | `05-espaces-communs-restaurant.jpg` | Espaces communs | Salle de restaurant, lumière dorée de fin de journée | Meilleure lumière naturelle de tout le dossier, sujet net, aucun visage |
| 06 | `06-espaces-communs-bar.jpg` | Espaces communs | Flatlay bar : cocktail, menthe, tonic, limoncello | Ambiance bar/apéritif, composition graphique forte, texture et couleurs vives |
| 07 | `07-panorama-terrasse.jpg` | Panorama/extérieur | Terrasse en hauteur, vue sur la lande et l'horizon, chapeau et magazine | Seule vue extérieure/panoramique nette du dossier, respiration après les plans intérieurs |
| 08 | `08-paysage-territoire-moutons.jpg` | Paysage/territoire | Moutons noirs (race locale) dans un pré clos de pierre | Ancrage territoire fort et différenciant — ⚠️ à surveiller en image-to-video : sujet vivant, mouvement de tête/regard imprévisible, prévoir un prompt caméra très contraint (push-in minimal, pas d'animation sur l'animal lui-même) |

### Note — catégorie "chambre" absente

Aucune des 24 photos rapatriées ne montre l'intérieur d'une chambre. Le plan
03 (fauteuil) sert de substitut le plus proche en attendant que le compte
Instagram publie ou que l'hôtel fournisse une photo de chambre dédiée — à
signaler à l'utilisateur avant de lancer `shotlist-generator`.

## Meilleures candidates non retenues

- `2026-04-03_d46292e5...` (sculpture chocolat pieuvre sur galets) — très
  proche en composition du plan 02 (assiette/objet posé sur pierre), écartée
  pour éviter la redondance visuelle
- `2026-06-07_b3504d98...` (salle de restaurant, tables dressées) — bonne
  photo mais redondante avec le plan 05, lumière moins qualitative
- `2025-07-05_cc64ae76...` (moutons noirs, vue plus large) — alternative au
  plan 08 si le gros plan retenu s'avère trop difficile à animer

## Prochaine étape

`shotlist-generator` peut être lancé directement — il lira
`projects/le-chateau-de-sable/photos-source/` sans qu'il soit nécessaire de
relister les photos.
