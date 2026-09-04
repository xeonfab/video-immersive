# Journal de génération — Manoir de Lan Kerellec

## Vidéo (Artlist)

| # | Plan | Photo (assetId) | Modèle | Réglages | Coût | generationId | Statut |
|---|---|---|---|---|---|---|---|
| 01 | Gastronomie — dessert | `be989e0d-9588-4fc0-ad29-eac09853b0f7` | Kling v3 Pro I2V, No Audio (modelId 3146, résolu en "Kling 3.0") | 1080p, 5s, audio off | 500 crédits | `01a06c50-6521-7aa6-aebb-c364e28334cc` | ✅ Généré — **non téléchargé** (proxy réseau de la session bloque les domaines Artlist, voir note ci-dessous) |
| 02 | Gastronomie — tourteau | `5863f42c-1f7c-4ebd-bd4f-03ee8c4c2130` | Kling v3 Pro I2V, No Audio (modelId 3146) | 1080p, 5s, audio off | 500 crédits | `01a06c63-e5dd-74cf-ab4f-82510637ce90` | ✅ Généré — **non téléchargé** (même blocage) |

**Liens de téléchargement des rushes** (URL signées, valides plusieurs années) :
- Plan 01 : https://cms-toolkit-artifacts.artlist.io/content/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-v1/media__9/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-5c6274a5-1d28-46c5-9a13-62829ed730b1.mp4?Expires=2103883714&Key-Pair-Id=K2ZDLYDZI2R1DF&Signature=PLdD-ZAMsmolzBflImhM3mBC5JIipoTaFRzrqjGNy4gUXWcAtA7dLX4amVlb7dQ4FzDX4q0cQpBWrQBgOoAxUqTSDtmNaFK7CvS~UIJ-czip9xFUBD3grDJtzkzNnsSm8hKorPWovmLgDu194f~Yg07Bt0O4AKF~Zf5aGyZ101GMi9QtJXcoqy9Yvsm0JbBFCEWIjDp5Qi6ftbKzUeDKTruTNXxkGx4rAu-b0bitaopqPT~bq80qg04tKuRL0X9udBH9IIElrMCWTaerKAYSZRwFfWDwUocCvg-NZ~GZVj9meUScI-4YcegufddAvGlr~XPrcwWum3hEdhl8F621Ug__
- Plan 02 : https://cms-toolkit-artifacts.artlist.io/content/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-v1/media__9/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-cf342f26-c8b5-49a3-89dc-7d7aa4b90b9c.mp4?Expires=2103885054&Key-Pair-Id=K2ZDLYDZI2R1DF&Signature=XMiMTPN9rqYrI0TAfjdSWc2D4XLr4GxzSMEUUEWiY~eqqKokp1yeFtBz4496nqRu6KOP47T~7EMm64e~HBqeUIBGT~IrX0Bh7Cz7GAUhgDz-NLQ7luYGS7r0bd0AhQDnYtdCp7jIMaP-t93hmydngUAvkqHaDXs8KXdyzLXcdBW7HS4jPBAVd8x-lHuku3Wk-i~e1-nsIWrFf4ronHtbGHOKyKHrpgaKoXMSeA7e~ox8Mvd~6xmlDGD-PfJPpn3N7G1DYeJaDEPwAhi6eRxz4yV3kbj7I5Tk6cTfMaGDnAjSnVAHyEwadWNEznvxqbfZyC~fvfVSd5fdsRzGvXdTqA__

**Plan 02 — foley en attente d'analyse.** Le nouveau workflow (Étape 3 de
`realisateur-ia`) décide du foley en observant des frames extraites du rush
réel — impossible ici sans accès local au fichier vidéo (même blocage réseau
que le téléchargement). Dès que le rush du plan 02 est récupérable localement
(téléchargement manuel via le lien ci-dessus, ou session locale), relancer
l'analyse pour compléter/écarter le foley avant de considérer ce plan terminé.

## Note technique — téléchargement bloqué dans cette session

Cette session Claude Code tourne dans un environnement cloud dont le proxy
réseau applique une liste blanche de domaines sortants. Les domaines Artlist
(`mcp.artlist.io`, `cms-toolkit-artifacts.artlist.io`) n'y figurent pas — le
`curl` de téléchargement du rush a échoué avec un 403 (`connect_rejected`,
politique d'egress, pas un problème de certificat ou de configuration). Le
skill `realisateur-ia` a été mis à jour pour documenter ce cas : sur une
machine locale (Claude Code hors sandbox web), ce téléchargement devrait
fonctionner normalement.

## Sons & musique (ElevenLabs)

| # | Couche | Modèle | Durée générée | Coût réel | flow_id / session_id | Chemin local | Statut |
|---|---|---|---|---|---|---|---|
| 01 | Ambiance | eleven_text_to_sound_v2 | 2s | ~16,7 crédits | `E8umXzSjy3Y0e92ZE3WZ` / `mhpzJVtSZ8aJJJUy5UD2` | `audio/01-ambiance.mp3` | ✅ Généré et téléchargé |
| 01 | Foley (versement) | eleven_text_to_sound_v2 | 14s | ~16,7 crédits | `zslGZi79ns9CqmgNz1RJ` / `2C3YtewYN0UqsSfafBj8` | `audio/01-foley.mp3` | ✅ Généré et téléchargé — à couper sur le geste au montage (généré plus long que les 4-5s du plan, pas de réglage de durée exposé sur ce modèle) |
| 02 | Ambiance | eleven_text_to_sound_v2 | 18s | ~16,7 crédits | `h0pccFxtuHEu1L31s0XW` / `1fPoktv2mKOHfjHiX5L8` | `audio/02-ambiance.mp3` | ✅ Généré et téléchargé |
| 02 | Foley | — | — | — | — | — | ⏸️ En attente — décision impossible sans accès local au rush (voir note ci-dessus) |

Contrairement à Artlist, les domaines de stockage ElevenLabs
(`storage.googleapis.com`) passent le proxy réseau de cette session — le
téléchargement a fonctionné directement, sans la limitation notée ci-dessus
pour les rushes vidéo.

Le coût réel (~16,7 crédits/génération) est très inférieur au devis initial
(55 crédits) — `estimate_only` semble majorer par prudence, pas un problème,
juste une note pour ne pas se fier au devis à la décimale près.

Musique d'ambiance générale : pas encore lancée.

## Total dépensé

- Artlist : 1000 crédits (solde restant : 2 270 / 3 270)
- ElevenLabs : ~50 crédits (ambiance + foley plan 01, ambiance plan 02)
