---
name: sound-design
description: Génère l'habillage sonore complet d'une vidéo immersive hôtelière — prompts ElevenLabs Text-to-Sound pour les ambiances et le foley de chaque plan, plus la structure du thème musical de 24 secondes. Utilise ce skill dès que l'utilisateur parle de sound design, bruitages, ambiances sonores, foley, musique d'ambiance, ou de "sonoriser" une shot-list déjà écrite — pour un hôtel, un plan précis, ou toute la séquence. Fonctionne à partir des fiches de plan produites par shotlist-generator ; complète chaque fiche avec sa section Sound design plutôt que de partir de zéro.
---

# Sound design — vidéo immersive hôtelière

## Objectif

Un plan vidéo sans son ne vend rien : c'est le sound design qui fait la différence
entre "jolie animation" et "je m'y crois". Ce skill produit deux livrables par
projet : les prompts ElevenLabs pour chaque plan (ambiance + foley), et la
structure du thème musical global de 24 secondes qui unifie la séquence.

## Étape 0 — Repérer les plans à sonoriser

Lis les fiches dans `projects/<slug>/shots/`. Si elles n'existent pas, invite
l'utilisateur à d'abord passer par le skill `shotlist-generator` — le sound design
sans plan écrit part dans tous les sens et perd le lien avec l'intention de chaque
image.

## Étape 1 — Deux couches par plan, jamais confondues

Chaque plan reçoit exactement deux couches sonores, qui répondent à des logiques
différentes :

1. **Ambiance d'arrière-plan** — continue sur toute la durée du plan (mer, brise,
   tonalité feutrée d'intérieur, silence habité...). Elle porte l'atmosphère.
2. **Foley / bruitage d'impact** — ponctuel et précis, synchronisé sur un geste
   visible dans le plan (tranchant d'une lame, cliquetis, pas sur le bois). Il
   porte le réalisme. Un plan large sans geste (panorama, paysage) n'a souvent
   pas de foley du tout — ne force pas un bruitage là où rien ne bouge à l'image,
   ça sonne artificiel.

Pour chaque couche, écris un prompt ElevenLabs Text-to-Sound descriptif et
spécifique (matière, distance, intensité), voir `references/prompt-patterns.md`
pour des formulations qui marchent bien avec ce modèle. Un prompt vague ("bruit de
mer") donne un rendu générique ; un prompt qui précise texture et proximité
("close, soft rolling shoreline waves with light foam hiss, no wind") donne un
rendu exploitable au mix.

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
audio que le montage devra respecter, pour que rien ne se perde entre les deux
étapes : musique en retrait (-12 à -15 dB / 20-30% de volume perçu), foley et
ambiances à 100%. C'est cette hiérarchie qui fait qu'on entend "un vrai lieu"
plutôt qu'"une musique avec des images dessus".

## Étape 4 — Livrer

Complète la section `## Sound design` de chaque fichier `projects/<slug>/shots/<NN>-*.md`
avec les prompts ambiance + foley (ou l'absence assumée de foley). Écris le thème
musical global dans `projects/<slug>/exports/sound-design.md`, avec un tableau
récapitulatif de tous les prompts du projet pour que quelqu'un puisse lancer
toutes les générations ElevenLabs sans revenir consulter chaque fiche.

Si les outils MCP ElevenLabs/Artlist sont disponibles dans la session et que
l'utilisateur demande explicitement de générer (pas seulement de préparer les
prompts), génère réellement les sons/la musique à partir de ces prompts plutôt
que de t'arrêter à l'écrit — mais ne le fais jamais sans demande explicite, la
génération a un coût.
