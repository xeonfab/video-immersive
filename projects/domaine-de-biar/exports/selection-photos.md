# Sélection photos — Domaine de Biar

Source : dossier Google Drive `domainedebiar`
(id `10u9c8sE2UZRufuR7ivIqmkA9U4nCzv3Y`, https://drive.google.com/drive/folders/10u9c8sE2UZRufuR7ivIqmkA9U4nCzv3Y)

> Point d'attention studio : ce dossier n'est pas placé à l'intérieur du dossier
> parent standard `Videos_immersives`
> (id `1kDhEW9gV4UbEUG18eX8WVYeH7pJdtDqm`) comme le veut la convention pour les
> autres établissements. Ça n'a pas bloqué le traitement, mais ce serait bien
> de le déplacer/harmoniser à l'occasion.

## 1. Volume traité

- **99 fichiers .jpg** rapatriés depuis le dossier Drive vers
  `.drive-download/` (dossier temporaire, supprimé une fois la sélection
  faite).
- **Pré-filtrage technique** (`prefilter_photos.py --min-side 1080`) :
  - **71 candidats** retenus (résolution ≥ 1080 px sur le plus petit côté).
  - **28 écartés**, tous pour la même raison groupée : résolution trop
    faible (28 fichiers entre 480 px et 939 px de petit côté — probablement
    des exports basse résolution ou des miniatures Instagram).
- **Doublons visuels stricts** : sur les 71 candidats, 35 paires étaient des
  doublons pixel-identiques (deux noms de fichiers Drive différents,
  contenu binaire rigoureusement identique — confirmé par hash MD5). Cela
  ramène le pool réellement distinct à **36 photos uniques**, toutes revues
  visuellement une par une selon les 4 axes du skill (netteté/lisibilité,
  catégorie de plan, attractivité, adéquation à l'animation IA).

## 2. Écartées à la revue visuelle (au-delà du pré-filtrage technique)

- **2 photos avec client identifiable au premier plan**, exclues
  systématiquement malgré une qualité par ailleurs excellente (cf. règle
  droit à l'image du skill) :
  - `2026-01-21_...` — spa, personne allongée en peignoir, visage visible de
    près.
  - `2026-08-10_...` — piscine, femme en peignoir lisant, visage net de
    profil.
  - `2026-08-06_...` — jardin, couple sur transats, visages reconnaissables
    à distance moyenne.
- Plusieurs photos de détails décoratifs (portail en fer forgé, vase de
  fleurs séchées, feuille de palmier, niche/bureau) ont été jugées correctes
  mais moins fortes commercialement que les candidates finalement retenues —
  elles ne sont pas défaut techniques, simplement dépassées par de meilleures
  options dans leur catégorie.

## 3. Sélection finale — 8 photos

Copiées dans `projects/domaine-de-biar/photos-source/`, dans l'ordre
narratif proche → loin → intime → collectif → grand angle.

| # | Fichier | Catégorie | Attractivité | Raison de sélection |
|---|---|---|---|---|
| 01 | `01-gastronomie-macro.jpg` | Gastronomie (macro) | 9/10 | Plat signature (poulpe, condiments colorés, dressage arty) — sujet net et centré, idéal pour un léger push-in, aucune personne dans le cadre. |
| 02 | `02-gastronomie-macro.jpg` | Gastronomie (macro) | 8.5/10 | Dessert tiramisu en verre à cocktail, fleurs comestibles, lumière douce — apporte la diversité salé/sucré dans la catégorie gastronomie. |
| 03 | `03-chambre-interieur.jpg` | Chambre / intérieur | 8.5/10 | Salle de bain avec baignoire îlot, rideaux amples, carrelage écailles de poisson — matière et lumière naturelle qualitative, aucun élément parasite. |
| 04 | `04-chambre-interieur.jpg` | Chambre / intérieur | 8/10 | Tête de lit bois brut + coussin brodé (colombe), ambiance chaleureuse et épurée — bon contraste avec la salle de bain (n°03). |
| 05 | `05-espaces-communs.jpg` | Espaces communs | 9.5/10 | Salon rond, fauteuils crème sculpturaux, moulures d'époque, vue jardin par de grandes portes-fenêtres — photo la plus qualitative du lot, plan large mais sujet net, aucune personne. |
| 06 | `06-paysage-territoire.jpg` | Paysage / territoire | 8.5/10 | Paon perché sur une cheminée en pierre au petit matin — image distinctive et mémorable, incarne le caractère "domaine" du lieu mieux qu'un simple plan de parc. |
| 07 | `07-panorama-exterieur.jpg` | Panorama extérieur | 8.5/10 | Façade du château avec arcades et arbres à agrumes en pots, lumière de fin de journée — bonne transition entre intérieur et extérieur avant le plan large final. |
| 08 | `08-panorama-exterieur.jpg` | Panorama extérieur | 9.5/10 | Plan large du château à l'heure bleue, éclairage architectural, terrasse et pelouse éclairée par des spots au sol — plan de clôture idéal, grand angle, aucune personne identifiable. |

Répartition : Gastronomie macro (2) · Chambre/intérieur (2) · Espaces communs
(1) · Paysage/territoire (1) · Panorama extérieur (2) — conforme à la cible
1-2 par catégorie du skill, les 5 catégories sont couvertes.

## 4. Meilleures candidates non retenues

- `2026-06-04_...` — pièce montée (wedding cake) posée devant la façade du
  château, très belle double lecture gastronomie/architecture, écartée
  uniquement pour ne pas déséquilibrer la répartition (aurait fait un 3e
  plan gastronomie ou un 3e panorama).
- `2026-01-07_...` — arcades en pierre sculptée avec escalier éclairé en
  fond, ambiance très cinématographique pour les espaces communs ; solide
  alternative à la photo n°05 si le client préfère une ambiance plus sombre
  et patrimoniale qu'un salon lumineux.
- `2025-11-20_...` — pièce de bœuf grillée vue de dessus, éclairage
  dramatique en clair-obscur ; alternative forte à la photo n°01 si le
  client souhaite un plat plus "signature bistronomie" qu'un dressage
  d'auteur.

## 5. Miroir Google Drive

Un sous-dossier **"Sélection vidéo - 8 photos"** a été créé dans le dossier
Drive de l'hôtel et contient une copie des 8 photos retenues, renommées à
l'identique de `photos-source/` :
https://drive.google.com/drive/folders/1yY0JeiTiUtrjMPl_PXNuOQhKhR1rDwnw

## 6. Étape suivante

Le skill `shotlist-generator` peut être lancé directement pour ce projet —
il lira `projects/domaine-de-biar/photos-source/` sans qu'il soit nécessaire
de relister les photos.
