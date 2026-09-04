# Critères de sélection détaillés

## 1. Format & lisibilité technique

Le pré-filtrage automatique (`prefilter_photos.py`) élimine déjà les
résolutions trop faibles et les ratios extrêmes. Ce qui reste à juger à l'œil :

- **Netteté réelle** : une photo peut être en haute résolution et pourtant
  floue (flou de bougé, mise au point ratée). Regarder les bords nets d'un
  élément fixe (cadre, mobilier, ligne architecturale).
- **Texte ou stickers superposés** : légendes Instagram, logos de réutilisation,
  dates de story incrustées — inutilisables tels quels, l'IA les fige dans
  l'animation.
- **Collage multi-images** : carrousels compilés en une seule image, avant/
  après, grilles — l'image-to-video a besoin d'un seul sujet cohérent.
- **Filtre Instagram trop appuyé** : une teinte artificielle uniforme (sépia
  fort, vignettage lourd) dénature les couleurs réelles de l'établissement et
  produira une vidéo qui ne matche plus rien une fois comparée à la réalité —
  préférer une photo moins retouchée mais fidèle.

## 2. Catégories de plan

Reprend exactement la typologie de `shotlist-generator`
(`.claude/skills/shotlist-generator/references/categories.md`) :

- Gastronomie (macro)
- Panorama côtier / extérieur
- Chambre / intérieur prestige
- Espaces communs (lounge, bibliothèque, restaurant vide)
- Paysage / territoire

## Répartition cible {#repartition-cible}

Pour 8 photos, viser un équilibre proche de :

| Catégorie | Nombre cible |
|---|---|
| Gastronomie (macro) | 1-2 |
| Panorama extérieur | 1-2 |
| Chambre / intérieur | 1-2 |
| Espaces communs | 1-2 |
| Paysage / territoire | 1-2 |

Ce n'est pas une règle rigide — si le compte Instagram de l'hôtel n'a
quasiment que des photos d'extérieur, mieux vaut le signaler et proposer une
séquence plus courte (4-5 plans) que de forcer 2 catégories vides avec des
photos hors-sujet.

## 3. Attractivité

Juge la valeur commerciale de la photo pour ce format précis, pas sa qualité
Instagram en absolu :

- Lumière naturelle qualitative (golden hour, lumière douce diffuse) plutôt
  que lumière artificielle dure ou plein soleil écrasant.
- Matière et texture visibles et identifiables (bois, granit, lin, verre) —
  ce sont elles qui portent le sound design ensuite.
- Une photo "propre" (peu d'éléments parasites au cadre : câbles, poubelles,
  objets du quotidien visibles) plutôt qu'une photo simplement bien exposée.

## 4. Adéquation à l'animation IA

- Sujet net avec de l'espace autour pour un léger push-in sans sortir du cadre
  ni couper un élément important.
- Pas de mouvement figé à mi-course (personne captée en plein geste, eau en
  éclaboussure) — l'IA anime à partir d'un instant, pas d'une trajectoire, et
  un geste figé "reprend" de façon peu naturelle.
- Pas plusieurs sujets qui devraient bouger de façon indépendante et
  incohérente une fois animés (ex: deux personnes à des distances différentes
  de la caméra).
- **Écarter systématiquement** toute photo où des clients sont identifiables
  au premier plan, animée ou non — risque de droit à l'image en usage
  commercial, à signaler à l'utilisateur si la photo est par ailleurs
  excellente, pour qu'il tranche en connaissance de cause plutôt que de la
  voir disparaître sans explication.
