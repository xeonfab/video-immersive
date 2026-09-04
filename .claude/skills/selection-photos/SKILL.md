---
name: selection-photos
description: Analyse un dossier local de photos brutes extraites du compte Instagram d'un hôtel (typiquement via un scraper Apify) et sélectionne les 8 meilleures pour la production vidéo — en évaluant format/résolution technique, diversité des plans, attractivité et adéquation à l'animation par IA (image-to-video). Utilise ce skill dès que l'utilisateur a un dossier de photos Instagram téléchargées à trier, ou demande "sélectionne les meilleures photos", "quelles photos on garde pour la vidéo", "j'ai extrait les photos via Apify", "trie ce dossier de photos". Alimente directement shotlist-generator : les 8 photos retenues sont copiées dans projects/<slug>/photos-source/ pour que ce skill les récupère automatiquement, sans que l'utilisateur ait à les lister manuellement.
---

# Sélection des photos source — depuis un scrape Instagram

## Objectif

Un scrape Apify d'un compte Instagram ramène souvent 50 à 300 photos, de qualité
et de pertinence très inégales (stories, reposts, photos de plats en table
d'hôtes, selfies de clients, captures d'écran). Ce skill fait le tri : il
identifie les 8 photos qui donneront les meilleurs résultats une fois animées en
vidéo, et les prépare pour que `shotlist-generator` les récupère sans étape
manuelle.

Ce skill ne scrape pas Instagram lui-même — il part du principe que le
téléchargement (Apify ou autre) a déjà eu lieu et que les fichiers sont dans un
dossier local.

## Étape 0 — Localiser le dossier source et le projet

Demande le chemin du dossier de photos brutes s'il n'est pas fourni. Si un
projet `projects/<slug>/` existe pour cet hôtel, note ce chemin dans son
`config.yaml` (section `photos.dossier_brut`) pour ne pas avoir à le redemander
la prochaine fois. Si le projet n'existe pas encore, propose de le créer
(`python3 scripts/new_project.py "<Nom>"`) avant de continuer.

## Étape 1 — Pré-filtrage technique automatique

Un tri visuel manuel sur 200 photos gaspille du temps et du contexte. Lance
d'abord le pré-filtrage déterministe :

```bash
python3 .claude/skills/selection-photos/scripts/prefilter_photos.py <dossier> --min-side 1080
```

Ce script (pure Python, sans dépendance) lit les dimensions réelles de chaque
image et écarte automatiquement, avant toute lecture visuelle :

- les fichiers illisibles/corrompus,
- les résolutions trop faibles (par défaut < 1080px sur le plus petit côté —
  en dessous, l'image-to-video amplifie le flou et les artefacts de
  compression au lieu de les masquer),
- les ratios extrêmes (par défaut > 2,2:1 — bannières, captures d'écran
  découpées, montages).

Il renvoie un JSON `{"candidates": [...], "rejected": [...]}`, les candidats
triés par résolution décroissante. Garde ce rejet technique traçable dans le
rapport final (Étape 4) plutôt que de le passer sous silence — ça rassure
l'utilisateur sur le fait que le tri n'a pas juste "disparu" des photos.

## Étape 2 — Revue visuelle des candidats survivants

Sur les candidats qui passent le pré-filtrage (en général 20 à 60 photos selon
la taille du compte), lis chaque image avec l'outil Read et évalue-la sur les
quatre axes détaillés dans `references/criteres-selection.md` :

1. **Format & lisibilité technique** (au-delà de la résolution déjà filtrée) —
   netteté réelle, absence de flou de bougé, absence de texte/stickers Instagram
   superposés, absence de collage multi-images.
2. **Catégorie de plan** — classe chaque photo dans une des catégories du
   skill `shotlist-generator` (gastronomie macro, panorama extérieur, chambre/
   intérieur, espaces communs, paysage/territoire) pour pouvoir ensuite
   maximiser la diversité plutôt que la simple qualité individuelle.
3. **Attractivité** — composition, lumière naturelle qualitative, matière et
   texture visibles, capacité à donner envie de réserver. Pas "jolie photo"
   en général mais une valeur commerciale concrète pour ce format vidéo précis.
4. **Adéquation à l'animation IA** — un sujet net avec un espace de respiration
   pour un léger push-in, pas de mouvement figé à mi-course (ex: personne
   captée en plein geste flou), pas de multiples sujets qui bougeraient de
   façon incohérente une fois animés. Écarte aussi toute photo où des clients
   sont identifiables au premier plan — un usage commercial de leur image sans
   consentement est un vrai risque pour le client, pas un détail esthétique.

## Étape 3 — Composer la sélection finale de 8 photos

Ne prends pas simplement les 8 meilleures notes brutes : équilibre les
catégories. Vise à couvrir un maximum des cinq catégories (voir
`references/criteres-selection.md#repartition-cible`) — une sélection de 8
photos de chambres, aussi réussies soient-elles individuellement, produira une
vidéo monotone. Si une catégorie manque totalement dans le dossier source
(pas de photo de gastronomie par exemple), dis-le à l'utilisateur plutôt que de
forcer une photo hors-sujet dans cette catégorie.

## Étape 4 — Livrer

- Copie (ne déplace jamais l'original) les 8 photos retenues dans
  `projects/<slug>/photos-source/`, renommées `01-<categorie>.jpg`,
  `02-<categorie>.jpg`, etc. dans l'ordre narratif attendu par
  `shotlist-generator` (proche → loin → intime → collectif → grand angle).
- Écris `projects/<slug>/exports/selection-photos.md` avec : le nombre total
  de photos analysées, le nombre écarté au pré-filtrage technique (avec raison
  groupée), un tableau des 8 retenues (catégorie, note d'attractivité, raison
  de sélection), et une courte liste des meilleures candidates non retenues
  (2-3 suffisent) au cas où l'utilisateur voudrait challenger un choix.
- Termine en indiquant explicitement que `shotlist-generator` peut maintenant
  être lancé directement — il lira `projects/<slug>/photos-source/` sans que
  l'utilisateur ait à relister les photos.
