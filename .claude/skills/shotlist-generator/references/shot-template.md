# Gabarit d'un plan

Utilise cette structure pour chaque fichier `projects/<slug>/shots/<NN>-<nom>.md` :

```markdown
# Plan <NN> — <Nom court du plan>

**Catégorie** : <gastronomie | panorama | chambre | espaces communs | paysage | outro>
**Photo source** : <nom de fichier ou description>
**Durée** : 4-5s

## Prompt caméra (Runway / Kling)

<Prompt en langage naturel, prêt à coller. Doit préciser :
 le sujet, le mouvement de caméra (push-in lent / léger pan), et les éléments
 architecturaux/structurels à verrouiller (fixed, no distortion).>

## Intention

<1-2 phrases : ce que ce plan doit faire ressentir, et pourquoi il est à cette
 place dans la séquence.>

## Sound design

À compléter par le skill `sound-design` — ne pas improviser ici.
```

## Exemple — Castel Beau Site

Référence de qualité, 4 étoiles, positionnement "gastronomie + panorama côtier
breton". Cinq plans + outro :

1. **La Gastronomie (macro)** — Découpe d'un fromage affiné au restaurant.
   Prompt type : *"Macro shot of a hand slicing a ripened cheese wheel with a
   thin blade on a wooden board, extremely slow and deliberate motion, shallow
   depth of field, warm restaurant lighting, camera locked static with a very
   slight push-in, no distortion on the blade or board edges."*

2. **Le Panorama Côtier (extérieur)** — Balcon surplombant la crique et le
   château de Costaérès. Prompt type : *"Slow cinematic push-in from a hotel
   balcony overlooking a rocky cove and a distant château on the water, railing
   and balcony structure locked and static, gentle sea haze, golden hour light."*

3. **La Chambre Prestige (intérieur)** — Chambre lumineuse face à la mer avec
   verrière. Prompt type : *"Very slow push-in inside a bright hotel room facing
   the sea through a glass veranda, soft natural light reflections on the floor,
   walls and window frame completely locked, no warping, calm and static feel."*

4. **Les Espaces Communs (lounge)** — Bibliothèque et table en bois massif.
   Prompt type : *"Gentle pan across a hotel lounge library with a solid wood
   table, warm wood textures in focus, architectural lines and shelving locked,
   slow and minimal camera drift only."*

5. **Le Territoire (paysage)** — Phare de Men Ruz et rochers de granit rose.
   Prompt type : *"Slow push-in toward a lighthouse on pink granite rocks by the
   ocean, rock formations and lighthouse structure locked and static, ocean swell
   motion only in the water, overcast dramatic sky."*

6. **Outro de marque** — Révélation du logo officiel avec ses 4 étoiles, fondu
   lent sur fond neutre (voir skill `montage-capcut` pour les paramètres exacts
   de keyframes et de timing).

Ce cas sert de barème : si un nouveau projet produit des plans nettement moins
spécifiques que ceux-ci (verbes vagues, pas de mention explicite des éléments à
verrouiller), retravaille le prompt avant de le livrer.
