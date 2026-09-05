# Generation log — Le Château de Sable

## Budget

- Solde Artlist avant génération : 21670/40000 crédits
- Devis vidéo (Kling v3 Pro 1080p, 5s, sans audio) : 500 crédits/plan × 8 = 4000 crédits
- Devis ElevenLabs ambiance : ~55 crédits/plan (estimation, coût réel souvent inférieur)
- Devis ElevenLabs musique globale (24s) : ~1650 crédits estimés, **899,8 crédits réels**

## Séquencement retenu (demande explicite de l'utilisateur)

Par plan : 1) génération vidéo → 2) extraction et analyse de 6 frames du rush →
3) génération de l'ambiance UNIQUEMENT si l'analyse montre qu'elle apporte un
vrai plus (sinon aucune génération audio pour ce plan) → 4) même logique pour
le foley. La musique globale peut être lancée dès le premier plan, en
parallèle.

## Musique globale

| Flow/session | Modèle | Coût réel | Statut | Fichier |
|---|---|---|---|---|
| flow `nLfJ7IIwmpzal2iaruJ1` / session `Rw14UdcbLL8m7h5sE1Lh` | eleven_music_v2 | 899,8 crédits | ✅ Généré et téléchargé | `audio/theme-musical.mp3` |

## Plan 01 — Gastronomie (dressage/versement)

| Étape | Détail |
|---|---|
| Photo source | `photos-source/01-gastronomie-dessert-macro.jpg` |
| assetId Artlist | `43b67e10-0af6-43da-b969-bd0128c0deff` |
| Modèle vidéo | Kling v3 Pro I2V, No Audio (modelId 3146, résolu en "Kling 3.0"), 1080p, 5s, 9:16 |
| generationId | `01a0733f-c253-73bc-9f8f-8e57b5093e8b` |
| Coût | 500 crédits |
| Statut | ✅ Généré — **non téléchargé** (proxy réseau de la session bloque `cms-toolkit-artifacts.artlist.io`, voir note ci-dessous) |
| Analyse frames (warping + foley) | **En attente** — nécessite le fichier vidéo local, impossible à récupérer dans cet environnement cloud |
| Ambiance | **En attente** — décision conditionnée à l'analyse des frames (voir ci-dessus), non générée dans cette session |

**Lien de téléchargement du rush** (URL signée, valide plusieurs années) :

https://cms-toolkit-artifacts.artlist.io/content/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-v1/media__8/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-0d5b3fcd-c682-4a1b-83c4-652695353a83.mp4?Expires=2104000289&Key-Pair-Id=K2ZDLYDZI2R1DF&Signature=yy5r4ZglDNNRB4ULuTaq41MdgbSht3HeHC-Iba5~nySfh1kvuMTFOXypDigQQawQNAAZSJX-PNx3YFTe8OfSHTilIH0IG68wmRgiuvokwE5l~ONu33mwuwKZbbgcKk7cu67mZbEwHPwO2F85Vauym~RHmyLIdoSOkZODKsT12FIRJR0okCJIj8Ve~k4X5UQbwYKth0Y3HnXrB7To803Iwh2OCyZVY1O0yNeYUS39rhwIU1qWGFDIC84r7M63saxYJhYbj6YD8QI2PljtVVNTE2Curtr592di0gRR~33DiVawCCGL30GqGQSBADOTeCEx9Nl4IKR4R1vnzs7hCGZ-jA__

**Note sur le blocage réseau** : cette session cloud passe par un proxy
d'agent qui refuse les domaines `artlist.io` (403 sur le CONNECT). Ce n'est
pas propre à ce plan — le même blocage a été documenté pour Manoir de Lan
Kerellec (`projects/manoir-de-lan-kerellec/exports/generation-log.md`).
Pour poursuivre l'analyse (warping + décision ambiance/foley), utiliser la
session Claude Code **locale** de l'utilisateur (sans cette restriction
réseau) : télécharger le rush depuis le lien ci-dessus vers
`projects/le-chateau-de-sable/rushes/01-gastronomie-dessert-macro.mp4`, puis
relancer le skill `realisateur-ia` à partir de l'étape 3 pour ce plan.

## Total dépensé dans cette session

- Artlist : 500 crédits (1 plan vidéo)
- ElevenLabs : 899,8 crédits (musique globale)
- **Reste 7 plans vidéo à traiter**, chacun suivant le même séquencement.
