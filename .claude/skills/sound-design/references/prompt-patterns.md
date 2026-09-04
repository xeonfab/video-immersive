# Formulations de prompts ElevenLabs Text-to-Sound qui marchent bien

Le modèle répond mieux à des prompts qui précisent : matière → action → distance
au micro → absence explicite de ce qu'on ne veut pas. Éviter les adjectifs vagues
("joli", "agréable") qui ne décrivent rien d'audible.

## Ambiances (continues)

- Mer / littoral : *"Close, soft rolling shoreline waves with light foam hiss,
  gentle sea breeze, no wind gusts, no seagulls, continuous loopable texture."*
- Intérieur feutré (chambre) : *"Subtle indoor room tone, very quiet, faint
  distant fabric rustle, no HVAC hum, no footsteps, near-silence with texture."*
- Lounge / bibliothèque : *"Warm indoor ambience, faint wood creak, distant soft
  page turn, no voices, no music, cozy enclosed room feel."*
- Grand paysage (phare, littoral rocheux) : *"Distant ocean swell against rocks,
  low rumble, occasional spray hiss, steady wind at moderate distance, no birds."*

## Foley (ponctuels, synchronisés)

- Découpe alimentaire : *"Single knife slicing through a firm aged cheese wheel,
  clean crisp cut, subtle blade-on-wood contact at the end, close mic, no reverb."*
- Cliquetis léger (couverts, verre) : *"Light single clink of fine cutlery on
  porcelain, short and precise, close and dry, no room tone."*
- Pas sur bois : *"Single soft footstep on a solid wood floor, close and dry,
  no reverb tail, natural weight."*

## Ce qui ne marche pas

- Décrire une émotion plutôt qu'un son ("apaisant", "luxueux") : le modèle n'a
  rien à convertir en audio, il improvise et le résultat dérive du prompt.
- Cumuler plus de deux événements sonores dans un même prompt de foley : ça finit
  en bouillie, un seul geste = un seul prompt.
- Oublier la distance au micro ("close" vs "distant") : par défaut le modèle
  choisit une distance moyenne qui sonne générique.
