# Sound design — Domaine de Biar

**Positionnement** : château champêtre chic, près de Montpellier — élégance
patrimoniale + nature (parc, agrumes, piscine), ambiance chillout haut de gamme.

> Cette passe couvre uniquement le thème musical global (24s), à la demande du
> client. Les ambiances de fond par plan restent à écrire — section réservée
> ci-dessous, plans non complétés dans `shots/`.

## Thème musical global (24 secondes)

Un seul morceau pour toute la séquence — instrumental, jamais de voix.

**Prompt ElevenLabs (music, `eleven_music_v2`)** :

> Instrumental chillout theme for an upscale French château hotel, warm acoustic
> guitar and soft felt piano over a light string pad, gentle and understated,
> no percussion or only a very soft brushed texture, steady unchanging tempo
> throughout, elegant and pastoral mood — refined countryside rather than
> beach or urban lounge, natural fade-out over the last 2-3 seconds, 24 seconds
> total, continuous and non-repetitive, no vocals, no drums.

**Généré** (ElevenLabs `eleven_music_v2`) le 07/09/2026 — coût réel 899,8 crédits
(~0,16 $, devis initial 1650 crédits), durée confirmée 24,0s.
Fichier local : `projects/domaine-de-biar/audio/theme-musical.mp3`.

**Caractéristiques imposées** :
- Style : instrumental acoustique/chillout haut de gamme, ton pastoral-patrimonial
  (cohérent avec les photos château + parc + agrumes, pas une ambiance "plage").
- Tempo : stable du début à la fin, aucune montée dramatique.
- Durée : 24 secondes pile, résolution en fondu naturel sur les 2-3 dernières
  secondes plutôt qu'une coupe franche.

## Repères de mixage (à transmettre à `montage-capcut`)

- Musique en retrait : -12 à -15 dB / 20-30% de volume perçu.
- Ambiances de plan (à écrire) et foley (décidé dans `realisateur-ia` sur les
  rushes réels) : 100%.
- Cette hiérarchie fait qu'on entend "un vrai lieu" plutôt qu'"une musique avec
  des images dessus" — ne pas la renverser au mix.

## Ambiances par plan

Non traitées dans cette passe — à compléter plan par plan (`shots/01-*.md` à
`08-*.md`) avant le montage final, sur le même principe que `references/prompt-patterns.md`.

## Étape suivante

Le foley de chaque plan se décide dans `realisateur-ia`, une fois les rushes
regardés (déjà générés pour ce projet, cf. `exports/generation-log.md`) — pas ici.
