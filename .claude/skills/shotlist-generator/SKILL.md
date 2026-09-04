---
name: shotlist-generator
description: Génère la shot-list complète (prompts caméra image-to-video, structure narrative, durées) d'une vidéo immersive hôtelière à partir des photos disponibles et du positionnement de l'établissement. Utilise ce skill dès que l'utilisateur veut préparer, planifier ou lancer une production vidéo pour un hôtel — que ce soit un nouveau prospect, un client signé, ou une simple demande de "prépare la vidéo pour [hôtel]", "shot-list", "quels plans on fait", "prompts Runway/Kling". S'appuie sur le cas de référence Castel Beau Site (5 plans : gastronomie macro, panorama côtier, chambre prestige, espaces communs, paysage, outro logo).
---

# Générateur de shot-list — vidéo immersive hôtelière

## Objectif

Transformer une photothèque d'hôtel en une shot-list de production prête à l'emploi :
chaque plan a un prompt caméra précis (mouvement, verrouillage des structures fixes),
une durée, et un pont vers le sound design associé (le skill `sound-design` complète
chaque plan ensuite).

Le format cible n'est jamais une liste vague de "belles idées" : chaque plan doit
pouvoir être collé tel quel dans Runway Gen-3 ou Kling par quelqu'un qui n'a pas
participé à la réflexion.

## Étape 0 — Localiser ou créer le projet

Si un dossier `projects/<slug>/` existe déjà pour cet hôtel, lis `config.yaml` pour
récupérer le positionnement (ambiance, mots-clés, catégorie). Sinon, propose de le
créer avec `python3 scripts/new_project.py "<Nom de l'hôtel>"` puis demande les
informations manquantes (catégorie, ambiance, mots-clés) plutôt que de les inventer —
elles conditionnent le ton de tous les plans.

## Étape 1 — Inventorier les photos disponibles

Vérifie d'abord si `projects/<slug>/photos-source/` existe et contient des
photos : c'est le dossier alimenté par le skill `selection-photos` (sélection
des 8 meilleures photos depuis un scrape Instagram/Apify), déjà nommées et
classées par catégorie dans l'ordre narratif — utilise-les directement sans
redemander à l'utilisateur. S'il n'existe pas et que l'utilisateur dispose d'un
dossier de photos brutes issu d'Instagram, propose d'abord de passer par
`selection-photos` plutôt que de trier manuellement ici.

Seulement si aucune des deux situations ne s'applique, demande la liste des
photos (ou le dossier) directement. Pour chaque photo utilisable, identifie sa
catégorie narrative — voir `references/categories.md` pour la typologie complète
(gastronomie, extérieur/panorama, chambre, espaces communs, paysage/territoire).
Un projet de démonstration tient en 4-6 plans + un outro logo ; ne dépasse pas ce
format sans que l'utilisateur le demande, la valeur du studio est la régularité
de contenus courts, pas des films longs.

## Étape 2 — Écrire chaque plan

Utilise `references/shot-template.md` comme structure pour chaque plan. Les
invariants techniques, non négociables car ils évitent les défauts les plus visibles
de l'image-to-video (warping architectural, mouvements de caméra qui cassent
l'immersion) :

- **Durée** : 4 à 5 secondes par plan.
- **Mouvement de caméra** : lent et cinématique uniquement — push-in ou léger pan.
  Jamais de mouvement complexe (whip pan, zoom rapide, rotation) : le modèle
  image-to-video déforme les structures architecturales fixes (murs, poutres,
  lignes de toit) dès que le mouvement est trop ample ou trop rapide.
  Nomme explicitement dans le prompt les éléments fixes à verrouiller.
- **Un seul sujet d'attention par plan** — un geste, un point de vue, une texture.
  Ne décris jamais deux mouvements différents dans le même prompt.

Écris chaque prompt caméra directement en langage naturel descriptif (comme pour
Runway/Kling), pas en jargon technique interne — c'est ce texte qui part tel quel
dans l'outil de génération.

## Étape 3 — Construire la structure narrative

Ordonne les plans pour raconter une expérience client, pas un inventaire de pièces.
Le cas Castel Beau Site est le gabarit de référence (voir
`references/shot-template.md#exemple-castel-beau-site`) : on part du détail sensoriel
(gastronomie macro) pour ouvrir vers l'extérieur (panorama), puis l'intime (chambre),
le collectif (espaces communs), et le grand paysage (territoire), avant de refermer
sur la marque (outro logo). Cette respiration — proche → loin → intime → collectif →
grand angle → marque — fonctionne pour la plupart des hôtels indépendants ; adapte
l'ordre aux photos réellement disponibles plutôt que de forcer ce gabarit.

## Étape 4 — Outro de marque

Toujours prévoir un plan de fermeture dédié au logo (voir `references/shot-template.md`
pour les specs de révélation — elles sont détaillées mais appliquées dans le skill
`montage-capcut`, pas ici). Ici, note simplement le fond retenu (neutre ou
surimpression blanche) et si un fichier logo est disponible dans `config.yaml`.

## Étape 5 — Livrer

Écris le résultat dans `projects/<slug>/shots/<NN>-<nom-du-plan>.md` (un fichier par
plan, numéroté dans l'ordre narratif) et un récapitulatif
`projects/<slug>/exports/shotlist.md` qui liste tous les plans avec leur prompt complet,
prêt à copier-coller dans l'outil de génération. Termine toujours en signalant à
l'utilisateur que le sound design de chaque plan reste à faire — invite-le à enchaîner
avec le skill `sound-design` plutôt que de l'improviser ici.
