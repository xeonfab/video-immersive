# Sélection des photos source — Manoir de Lan Kerellec

Source : dossier Google Drive `manoirdelankerellec - Photos Instagram - 120j`
(id `1ifV7pGafsp1t22aL76uADqy5x0tDqxMK`, sous `Videos_immersives`).

## Chiffres

- **33 photos** analysées au total.
- **1 écartée** au pré-filtrage technique automatique : résolution trop faible
  (862px sur le plus petit côté, en dessous du seuil de 1080px).
- **32 candidates** passées en revue visuelle.
- **8 retenues**, réparties sur 4 catégories (2 par catégorie) plutôt que sur
  les 5 types habituels — le compte Instagram de l'établissement ne montre
  quasiment aucun grand paysage/territoire distinct des plans "panorama
  côtier" déjà couverts par la catégorie paysage ci-dessous, donc j'ai
  fusionné panorama et paysage plutôt que de forcer une 5ᵉ catégorie faible.

## Sélection retenue

| # | Fichier | Catégorie | Pourquoi |
|---|---|---|---|
| 01 | gastronomie-dessert | Gastronomie (macro) | Dessert gastronomique très soigné, geste net de versement de sauce, un seul sujet d'attention — parfait pour un push-in lent. |
| 02 | gastronomie-tourteau | Gastronomie (macro) | Main tenant un tourteau au-dessus d'une bisque, geste fort et identitaire (pêche/fruits de mer bretons). Deuxième plan gastronomie plutôt qu'un seul : l'établissement est visiblement très centré cuisine (nombreuses photos de plats et de chefs), ça mérite d'être représenté deux fois. |
| 03 | paysage-rochers | Paysage / territoire | Rochers de granit rose et ajoncs jaunes — l'identité géographique la plus forte du lieu (Côte de Granit Rose). |
| 04 | paysage-vague | Paysage / territoire | Vague dorée sur le sable en contre-jour, texture d'eau très cinématique, registre différent du plan 03 (minéral vs liquide). |
| 05 | chambre-miroirs | Chambre / intérieur | Reflet de chambre dans des miroirs anciens, avec le livre "Manoir de Lan Kerellec" posé sur la table — identité de marque visible sans être un logo forcé. |
| 06 | chambre-fenetre-ovale | Chambre / intérieur | Fenêtre ovale ouverte sur la mer, cadre architectural distinctif, différent du plan 05 (chambre vécue vs vue depuis la chambre). |
| 07 | espaces-communs-restaurant | Espaces communs | Salle du restaurant avec sa maquette de voilier suspendue au plafond — le plan le plus emblématique et mémorable du dossier. |
| 08 | espaces-communs-terrasse | Espaces communs | Table dressée en terrasse avec vue mer et verres à vin, élégant, bon plan de clôture avant l'outro logo. |

## Écartées malgré une bonne qualité — et pourquoi

Cinq photos par ailleurs très réussies ont été écartées uniquement pour un
motif précis, pas pour un manque de qualité :

- **2 photos avec texte superposé** ("Sunset Diaries", "Summer Diaries") —
  inutilisables telles quelles, l'IA figerait le texte dans l'animation.
- **5 portraits nets du personnel/chefs** (le chef Simon Cédric en jardin, un
  chef en cuisine, un chef tenant des araignées de mer, une employée faisant
  un lit, une femme souriante en salle) — visages nets et identifiables,
  inadaptés à l'animation image-to-video (l'IA anime mal les visages humains,
  effet "uncanny" quasi systématique) plutôt qu'un problème de droit à
  l'image ici puisqu'il s'agit du personnel de l'établissement, pas de
  clients.
- **1 détail vestimentaire** (nœud papillon en bois) — hors des 5 catégories
  narratives du studio, pas de sujet d'attention clair pour un plan seul.

Quelques bonnes candidates non retenues faute de place (redondantes avec une
photo déjà choisie) : `05-05` et `05-27` (panorama côtier, proches de
`paysage-rochers`), `07-24` et `06-09` (chambre, proches de
`chambre-miroirs`).

## Prochaine étape

`shotlist-generator` peut être lancé directement pour le Manoir de Lan
Kerellec : il lira `projects/manoir-de-lan-kerellec/photos-source/`
automatiquement.
