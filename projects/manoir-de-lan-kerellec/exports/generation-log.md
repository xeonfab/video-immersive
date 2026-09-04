# Journal de génération — Manoir de Lan Kerellec

## Vidéo (Artlist)

| # | Plan | Photo (assetId) | Modèle | Réglages | Coût | generationId | Statut |
|---|---|---|---|---|---|---|---|
| 01 | Gastronomie — dessert | `be989e0d-9588-4fc0-ad29-eac09853b0f7` | Kling v3 Pro I2V, No Audio (modelId 3146, résolu en "Kling 3.0") | 1080p, 5s, audio off | 500 crédits | `01a06c50-6521-7aa6-aebb-c364e28334cc` | ✅ Généré — **non téléchargé** (proxy réseau de la session bloque les domaines Artlist, voir note ci-dessous) |

**Lien de téléchargement du rush** (URL signée, valide plusieurs années) :
https://cms-toolkit-artifacts.artlist.io/content/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-v1/media__9/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-5c6274a5-1d28-46c5-9a13-62829ed730b1.mp4?Expires=2103883714&Key-Pair-Id=K2ZDLYDZI2R1DF&Signature=PLdD-ZAMsmolzBflImhM3mBC5JIipoTaFRzrqjGNy4gUXWcAtA7dLX4amVlb7dQ4FzDX4q0cQpBWrQBgOoAxUqTSDtmNaFK7CvS~UIJ-czip9xFUBD3grDJtzkzNnsSm8hKorPWovmLgDu194f~Yg07Bt0O4AKF~Zf5aGyZ101GMi9QtJXcoqy9Yvsm0JbBFCEWIjDp5Qi6ftbKzUeDKTruTNXxkGx4rAu-b0bitaopqPT~bq80qg04tKuRL0X9udBH9IIElrMCWTaerKAYSZRwFfWDwUocCvg-NZ~GZVj9meUScI-4YcegufddAvGlr~XPrcwWum3hEdhl8F621Ug__

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

Pas encore lancés — ce premier run de test portait uniquement sur la vidéo
du plan 01.

## Total dépensé

- Artlist : 500 crédits (solde restant : 2 770 / 3 270)
- ElevenLabs : 0
