---
name: sound-design
description: Génère l'ambiance sonore de fond de chaque plan d'une vidéo immersive hôtelière (prompts ElevenLabs Text-to-Sound) et la structure du thème musical de 24 secondes. Utilise ce skill dès que l'utilisateur parle d'ambiance sonore, de musique d'ambiance, ou de "sonoriser" une shot-list déjà écrite — pour un hôtel, un plan précis, ou toute la séquence. Fonctionne à partir des fiches de plan produites par shotlist-generator ; complète chaque fiche avec sa section Sound design plutôt que de partir de zéro. Ne décide plus du foley (bruitage d'impact synchronisé sur un geste) — cette décision et son prompt exact se font désormais après génération vidéo, sur le rush réel, dans le skill realisateur-ia : la photo statique ne dit pas fidèlement quel geste l'IA va animer.
---

# Sound design — vidéo immersive hôtelière

## Objectif

Un plan vidéo sans son ne vend rien : c'est le sound design qui fait la différence
entre "jolie animation" et "je m'y crois". Ce skill produit deux livrables par
projet : le prompt d'ambiance ElevenLabs de chaque plan, et la structure du thème
musical global de 24 secondes qui unifie la séquence.

Il ne s'occupe **pas** du foley (bruitage d'impact synchronisé sur un geste
précis — tranchant d'une lame, versement, pas). Ce choix a changé : deviner le
foley depuis la photo statique suppose que l'IA va animer exactement le geste
qu'on imagine, ce qui n'est pas fiable. La décision ("y a-t-il un geste assez
net dans le rush pour mériter un bruitage ?") et le prompt exact se font
maintenant dans `realisateur-ia`, une fois la vidéo réellement générée — voir
sa section "Sound design par plan". Ne réintroduis pas de foley ici.

## Étape 0 — Repérer les plans à sonoriser

Lis les fiches dans `projects/<slug>/shots/`. Si elles n'existent pas, invite
l'utilisateur à d'abord passer par le skill `shotlist-generator` — le sound design
sans plan écrit part dans tous les sens et perd le lien avec l'intention de chaque
image.

## Étape 1 — L'ambiance d'arrière-plan de chaque plan

Une seule couche à écrire ici : l'ambiance de fond, continue sur toute la durée
du plan (mer, brise, tonalité feutrée d'intérieur, silence habité...). Elle porte
l'atmosphère du lieu — contrairement au foley, elle ne dépend pas du geste
précis que l'IA va animer, donc elle reste fiable à écrire depuis la photo et
l'intention du plan.

Écris un prompt ElevenLabs Text-to-Sound descriptif et spécifique (matière,
distance, intensité), voir `references/prompt-patterns.md` pour des formulations
qui marchent bien avec ce modèle. Un prompt vague ("bruit de mer") donne un rendu
générique ; un prompt qui précise texture et proximité ("close, soft rolling
shoreline waves with light foam hiss, no wind") donne un rendu exploitable au mix.

## Étape 2 — Le thème musical global (24 secondes)

Un seul morceau pour toute la séquence, pas un par plan. Caractéristiques à
respecter :

- **Style** : instrumental acoustique/chillout haut de gamme — jamais de voix,
  jamais de motif trop identifiable qui distrairait de l'image.
- **Tempo** : stable du début à la fin, pas d'accélération dramatique — la
  vidéo vend une sérénité, pas une tension.
- **Durée** : 24 secondes pile, avec une résolution en fondu naturel (fade-out)
  sur les 2-3 dernières secondes plutôt qu'une coupe franche.

Écris ce prompt musical en t'appuyant sur le champ `positionnement.ambiance` du
`config.yaml` du projet (ex: "chillout haut de gamme", "épuré minéral") pour que
le thème colle à l'identité de l'hôtel plutôt qu'à un défaut générique.

## Étape 3 — Repères de mixage (à transmettre, pas à exécuter ici)

Ce skill écrit les prompts et la structure ; le mix lui-même se fait dans
`montage-capcut`. Note quand même dans le livrable les repères de hiérarchie
audio que le montage devra respecter, pour que rien ne se perde entre les
étapes : musique en retrait (-12 à -15 dB / 20-30% de volume perçu), ambiances
et foley (décidé plus tard par `realisateur-ia`) à 100%. C'est cette
hiérarchie qui fait qu'on entend "un vrai lieu" plutôt qu'"une musique avec
des images dessus".

## Étape 4 — Livrer

Complète la section `## Sound design` de chaque fichier `projects/<slug>/shots/<NN>-*.md`
avec le prompt d'ambiance (le foley y sera ajouté plus tard par
`realisateur-ia`, une fois le rush généré). Écris le thème musical global dans
`projects/<slug>/exports/sound-design.md`, avec un tableau récapitulatif de
tous les prompts d'ambiance du projet pour que quelqu'un puisse lancer toutes
les générations ElevenLabs sans revenir consulter chaque fiche.

Si l'outil MCP ElevenLabs est disponible dans la session et que l'utilisateur
demande explicitement de générer (pas seulement de préparer les prompts),
génère réellement les ambiances/la musique à partir de ces prompts plutôt que
de t'arrêter à l'écrit — mais ne le fais jamais sans demande explicite, la
génération a un coût. Termine en rappelant que le foley de chaque plan se
décide dans `realisateur-ia`, après génération de la vidéo.
