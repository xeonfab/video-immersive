---
name: montage-capcut
description: Génère la feuille de montage (EDL) détaillée pour assembler dans CapCut les rushes d'une vidéo immersive hôtelière — ordre des plans, transitions, niveaux de mix audio en dB, et keyframes précis pour la révélation du logo en outro. Utilise ce skill quand l'utilisateur veut monter, assembler, mixer, ou finaliser une séquence après que les plans vidéo et les sons/musique ont été générés — que ce soit pour préparer le montage dans CapCut ou vérifier une checklist avant livraison au client. Ne génère pas de vidéo ni d'audio lui-même : produit le plan d'exécution que l'utilisateur suit manuellement dans CapCut.
---

# Montage & feuille de montage CapCut

## Objectif

Une fois les rushes vidéo (Runway/Kling) et les sons (ElevenLabs) prêts, ce skill
transforme la shot-list en feuille de montage exécutable : l'ordre exact, chaque
transition, chaque niveau de mix, et les paramètres de keyframes pour l'outro logo
— de sorte que le montage dans CapCut soit une exécution mécanique, pas une suite
de décisions créatives improvisées au dernier moment.

## Étape 0 — Vérifier que les rushes existent

Lis `projects/<slug>/exports/shotlist.md` et `projects/<slug>/exports/sound-design.md`.
Si l'un des deux manque, dis-le à l'utilisateur plutôt que d'inventer un montage
sur des plans qui n'ont pas encore de sound design défini — le mix dépend
directement des couches audio prévues à l'étape précédente.

## Étape 1 — Transitions

Règle par défaut, à appliquer uniformément sauf demande contraire : **cut franc**
entre deux plans qui se suivent dans la même veine (ex: deux plans d'ambiance
similaire), ou **fondu croisé court de 0,3 à 0,5 seconde** quand l'ambiance
change nettement (ex: passage d'un intérieur feutré à un extérieur venteux). Ne
jamais utiliser de transition plus longue ou plus "créative" (glitch, wipe...) —
ça casse le registre haut de gamme et sobre du studio.

## Étape 2 — Hiérarchie du mix audio

Reprend les repères posés par le skill `sound-design` et les rend actionnables
plan par plan :

- **Musique globale (24s)** : -12 à -15 dB, soit environ 20-30% du volume perçu,
  constante sur toute la durée sauf le fade-out final.
- **Ambiances et foley** : 100%, sans réduction — ce sont eux qui font le
  réalisme, jamais la musique.
- Si deux plans consécutifs ont des ambiances qui se chevauchent mal au cut
  (ex: mer forte puis silence intérieur), prévois un micro-fondu de 0,2-0,3s sur
  l'ambiance sortante pour éviter une coupure sèche perceptible à l'oreille.

## Étape 3 — Révélation du logo (outro)

Paramètres fixes du studio, à appliquer tels quels sauf demande explicite de
l'utilisateur de s'en écarter :

- **Fondu d'apparition** : 1,5 à 2 secondes, lent.
- **Fond** : neutre uni, ou surimpression blanche sur le dernier plan filmé selon
  ce qui a été noté dans la fiche outro de la shot-list.
- **Micro-zoom** : de 100% à 103% sur la durée du fondu, via keyframes CapCut —
  jamais plus, un zoom plus marqué se voit et casse la sobriété recherchée.
- Décris les keyframes en position/échelle explicites (ex: "keyframe 1 à 0s :
  scale 100%, opacity 0% — keyframe 2 à 1,8s : scale 103%, opacity 100%") pour
  que l'exécution dans CapCut ne demande aucune interprétation.

## Étape 4 — Livrer

Écris la feuille de montage dans `projects/<slug>/exports/montage-edl.md` avec,
dans l'ordre : la liste des plans avec leur durée, la transition qui les relie,
les niveaux de mix par piste, puis la section outro avec ses keyframes détaillés.
Termine par une checklist courte (5-8 points) que l'utilisateur peut cocher
pendant qu'il monte dans CapCut, pour repérer vite un oubli (ex: "musique bien
en retrait sur tous les plans ?", "logo lisible sur fond neutre ?").
