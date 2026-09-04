---
name: selection-photos
description: Analyse les photos brutes extraites du compte Instagram d'un hôtel — dossier local, OU dossier Google Drive alimenté par un scénario Make (Apify Instagram Scraper → Google Drive), typiquement "Apify → 30 dernieres photos → Google Drive" — et sélectionne les 8 meilleures pour la production vidéo : format/résolution technique, diversité des plans, attractivité, adéquation à l'animation par IA (image-to-video). Utilise ce skill dès que l'utilisateur a des photos Instagram à trier, un scénario Make/Apify qui vient de tourner, ou demande "sélectionne les meilleures photos", "quelles photos on garde pour la vidéo", "j'ai extrait les photos via Apify", "trie ce dossier de photos", "le scénario Make a tourné, trie les photos". Alimente directement shotlist-generator : les 8 photos retenues sont copiées dans projects/<slug>/photos-source/ pour que ce skill les récupère automatiquement, sans que l'utilisateur ait à les lister manuellement.
---

# Sélection des photos source — depuis un scrape Instagram

## Objectif

Un scrape Apify d'un compte Instagram ramène souvent 30 à 300 photos, de qualité
et de pertinence très inégales (stories, reposts, photos de plats en table
d'hôtes, selfies de clients, captures d'écran). Ce skill fait le tri : il
identifie les 8 photos qui donneront les meilleurs résultats une fois animées en
vidéo, et les prépare pour que `shotlist-generator` les récupère sans étape
manuelle.

Ce skill ne scrape pas Instagram lui-même — il part du principe que le
téléchargement a déjà eu lieu, via l'une de ces deux sources :

- **Dossier local** — un dossier de photos déjà présent sur la machine.
- **Dossier Google Drive** — le cas courant côté studio : le scénario Make
  `Apify → 30 dernieres photos → Google Drive (<slug>)` lance l'actor Apify
  Instagram Scraper sur l'URL du compte et dépose les photos dans un dossier
  Drive nommé `"<slug> - Photos Instagram - 30 dernieres"`, avec des fichiers
  `YYYY-MM-DD_<hash>.jpg`. Ce skill sait lire ce dossier directement via les
  outils Google Drive (search_files / download_file_content) sans que
  l'utilisateur ait à synchroniser ou télécharger quoi que ce soit à la main.

## Étape 0 — Localiser la source et le projet

Détermine d'abord d'où viennent les photos, dans cet ordre de préférence :

1. Si l'utilisateur donne un chemin de dossier local, utilise-le directement
   (voir Étape 1).
2. Sinon, cherche un dossier Google Drive nommé `"<slug ou nom hôtel> - Photos
   Instagram"` (recherche partielle) via `search_files`. Si trouvé, c'est la
   source — passe à la procédure Drive ci-dessous. C'est le cas le plus
   fréquent une fois le scénario Make en place.
3. Sinon, demande explicitement à l'utilisateur où se trouvent les photos —
   ne suppose jamais un chemin.

Si un projet `projects/<slug>/` existe déjà pour cet hôtel, note la source
retenue dans son `config.yaml` (`photos.dossier_brut` pour un dossier local,
`photos.google_drive_folder` pour le nom/ID du dossier Drive) pour ne pas avoir
à la redemander la prochaine fois. Si le projet n'existe pas encore, propose de
le créer (`python3 scripts/new_project.py "<Nom>"`) avant de continuer.

### Procédure spécifique — source Google Drive

Le pré-filtrage (Étape 1) et la revue visuelle (Étape 2) ont besoin de fichiers
locaux — ils ne peuvent pas lire les photos directement depuis Drive. Rapatrie
donc d'abord chaque photo dans un dossier temporaire local
(`projects/<slug>/.drive-download/`, à ne jamais committer) :

1. `search_files` avec `parentId = '<id du dossier Drive>'` pour lister tous
   les fichiers image du dossier.
2. Pour chaque fichier, `download_file_content` avec son `fileId` — l'outil
   renvoie le contenu encodé en base64.
3. Écris ce contenu base64 dans un fichier temporaire (`Write`), puis décode-le
   en binaire avec `base64 -d fichier.b64 > projects/<slug>/.drive-download/<nom>.jpg`
   (Bash) — c'est le point de passage obligé, il n'existe pas de moyen d'écrire
   un fichier binaire directement depuis le contenu base64 renvoyé par l'outil.
4. Une fois tous les fichiers rapatriés, poursuis normalement à partir de
   l'Étape 1 en pointant le pré-filtrage sur `projects/<slug>/.drive-download/`.

Sur un dossier de 30 photos (le volume typique de ce scénario Make), ça reste
gérable en une série d'appels ; au-delà de 100-150 photos, dis-le à
l'utilisateur avant de te lancer — le coût en appels d'outils devient
significatif et il peut préférer réduire le `resultsLimit` côté Apify plutôt
que de tout rapatrier.

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
- Si la source était Google Drive, supprime `projects/<slug>/.drive-download/`
  une fois les 8 photos copiées dans `photos-source/` — c'était un dossier de
  passage, pas un livrable, et il ne doit pas s'accumuler à chaque run.
