# Sound design — Le Château de Sable

Positionnement (`config.yaml`) : ambiance "chillout haut de gamme", mots-clés
sérénité/authenticité/vue mer. Territoire breton (granit, moutons noirs,
lande) — le thème musical et les ambiances évitent tout marqueur trop
identifiable qui trahirait un genre précis, pour rester cohérents avec un
positionnement 4 étoiles discret.

## Thème musical global (24s, un seul morceau pour toute la séquence)

> Instrumental chillout haut de gamme, guitare acoustique fingerstyle légère
> et nappes discrètes de piano/synthé doux, tempo stable autour de 70-80 BPM
> sans accélération ni pic dramatique, ambiance sereine et minérale évoquant
> le littoral et la pierre plutôt qu'un style touristique générique, texture
> chaleureuse et épurée, fondu de sortie naturel sur les 2-3 dernières
> secondes, 24 secondes exactement, aucune voix.

## Tableau récapitulatif des ambiances par plan

| # | Plan | Prompt ambiance ElevenLabs (Text-to-Sound) |
|---|---|---|
| 01 | Gastronomie (dressage) | "Close outdoor garden room tone in bright daylight, faint distant lawn breeze, no birds, no wind gusts, quiet and intimate feel, continuous loopable texture." |
| 02 | Gastronomie (coffret vin) | "Close outdoor stone terrace room tone in soft daylight, very faint distant coastal breeze, no wind gusts, no birds, quiet and mineral feel, continuous loopable texture." |
| 03 | Chambre | "Subtle indoor room tone, very quiet, faint distant fabric rustle, no HVAC hum, no footsteps, near-silence with texture." |
| 04 | Espaces communs (spa) | "Very quiet spa treatment room tone, faint distant water trickle, no voices, no music, warm enclosed feel, near-silence with texture." |
| 05 | Espaces communs (restaurant) | "Warm indoor restaurant room tone, faint distant glass clink, no voices, no music, cozy enclosed room feel, near-silence with texture." |
| 06 | Espaces communs (bar) | "Warm indoor bar room tone in the evening, faint distant ice clink, no voices, no music, cozy enclosed feel, near-silence with texture." |
| 07 | Panorama (terrasse) | "Open moorland terrace ambience, steady gentle breeze across grass at moderate distance, faint fabric flutter, no birds, no voices, continuous loopable texture." |
| 08 | Paysage (moutons) | "Open countryside meadow ambience, steady light wind across grass at moderate distance, faint distant sheep bleat, no traffic, no voices, continuous loopable texture." |

Le foley (bruitage ponctuel synchronisé sur un geste) n'est pas décidé ici —
voir la section Sound design de chaque fiche `shots/<NN>-*.md` pour l'état
d'attente par plan. La décision se prend dans `realisateur-ia`, sur le rush
vidéo réellement généré, pas sur la photo source.

## Repères de mixage (à appliquer dans `montage-capcut`)

- Musique : en retrait, -12 à -15 dB (20-30% de volume perçu) — jamais au
  premier plan.
- Ambiances de plan et foley (une fois décidé) : à 100%, c'est ce qui vend le
  sentiment de "vrai lieu" plutôt que "musique avec des images dessus".

## Prochaine étape

Le foley de chaque plan se décide dans `realisateur-ia`, une fois les rushes
vidéo générés — pas avant. `realisateur-ia` peut maintenant être lancé pour
la génération vidéo (Artlist) et sonore (ElevenLabs) des 8 plans.
