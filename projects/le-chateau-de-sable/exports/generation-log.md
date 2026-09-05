# Generation log — Le Château de Sable

## Budget

- Solde Artlist avant génération : 21670/40000 crédits
- Coût vidéo réel : 500 crédits/plan × 8 = **4000 crédits**
- Coût ElevenLabs musique globale : **899,8 crédits réels** (devis 1650)
- Ambiances/foley : aucune génération lancée dans cette session (voir
  séquencement ci-dessous)

## Séquencement retenu (demande explicite de l'utilisateur)

Par plan : 1) génération vidéo → 2) extraction et analyse de 6 frames du rush
→ 3) génération de l'ambiance UNIQUEMENT si l'analyse montre qu'elle apporte
un vrai plus (sinon aucune génération audio pour ce plan) → 4) même logique
pour le foley. La musique globale a été lancée dès le plan 01, en parallèle.

**Étape 2 (analyse de frames) impossible dans cette session cloud** : le
proxy réseau bloque le domaine `cms-toolkit-artifacts.artlist.io` (403 sur
le CONNECT), donc aucun rush n'a pu être téléchargé ici pour extraction de
frames. Les 8 vidéos sont générées et disponibles via leurs liens signés
ci-dessous (valides plusieurs années) — l'analyse + décision ambiance/foley
reste entièrement à faire, plan par plan, depuis une session locale.

## Musique globale

| Flow/session | Modèle | Coût réel | Statut | Fichier |
|---|---|---|---|---|
| flow `nLfJ7IIwmpzal2iaruJ1` / session `Rw14UdcbLL8m7h5sE1Lh` | eleven_music_v2 | 899,8 crédits | ✅ Généré et téléchargé | `audio/theme-musical.mp3` |

## Vidéos par plan

| # | Plan | assetId photo | generationId | Coût | Statut |
|---|---|---|---|---|---|
| 01 | Gastronomie — dressage/versement | `43b67e10-0af6-43da-b969-bd0128c0deff` | `01a0733f-c253-73bc-9f8f-8e57b5093e8b` | 500 | ✅ Généré, non téléchargé |
| 02 | Gastronomie — coffret vin | `4ee9dfd3-12a0-46aa-be49-f2ae5158bf2c` | `01a07378-b100-7727-8745-737a08bbb452` | 500 | ✅ Généré, non téléchargé |
| 03 | Chambre | `6635b0a0-5841-44f6-a105-dac74ba7ce7e` | `01a0737c-7a35-76cb-976d-cbd217e38ee0` | 500 | ✅ Généré, non téléchargé |
| 04 | Espaces communs — spa | `363f0658-fd60-4baf-94c5-7d4dc7e27fa3` | `01a0737f-b7a4-71a4-8aec-07adc56e2685` | 500 | ✅ Généré, non téléchargé |
| 05 | Espaces communs — restaurant | `737c5a52-83f6-40db-b50a-433d2d53d7af` | `01a07382-e769-7aa1-9050-02f5e83303f4` | 500 | ✅ Généré, non téléchargé |
| 06 | Espaces communs — bar | `ea5a94b1-da2b-4af2-bbf0-583fb0cad04b` | `01a07385-d996-7b32-b6a5-b339d4c99749` | 500 | ✅ Généré, non téléchargé |
| 07 | Panorama — terrasse | `4bb620bc-6e65-4334-bc2b-332f6f6d4f9e` | `01a07388-afeb-7700-bb2d-cd1c57632fe7` | 500 | ✅ Généré, non téléchargé |
| 08 | Paysage — moutons ⚠️ | `2e790250-258e-48d8-b12c-f125c99d8cbc` | `01a0738b-7065-743a-8f27-c4916f3ec09a` | 500 | ✅ Généré, non téléchargé — **priorité d'analyse warping** (sujet vivant) |

Modèle pour les 8 : Kling v3 Pro I2V, No Audio (modelId 3146, résolu en
"Kling 3.0"), 1080p, 5s, 9:16.

**Total dépensé** : 4000 crédits Artlist (vidéo) + 899,8 crédits ElevenLabs
(musique) = solde Artlist restant ≈ 17670/40000.

## Liens de téléchargement des rushes (URL signées, valides plusieurs années)

- Plan 01 : https://cms-toolkit-artifacts.artlist.io/content/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-v1/media__8/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-0d5b3fcd-c682-4a1b-83c4-652695353a83.mp4?Expires=2104000289&Key-Pair-Id=K2ZDLYDZI2R1DF&Signature=yy5r4ZglDNNRB4ULuTaq41MdgbSht3HeHC-Iba5~nySfh1kvuMTFOXypDigQQawQNAAZSJX-PNx3YFTe8OfSHTilIH0IG68wmRgiuvokwE5l~ONu33mwuwKZbbgcKk7cu67mZbEwHPwO2F85Vauym~RHmyLIdoSOkZODKsT12FIRJR0okCJIj8Ve~k4X5UQbwYKth0Y3HnXrB7To803Iwh2OCyZVY1O0yNeYUS39rhwIU1qWGFDIC84r7M63saxYJhYbj6YD8QI2PljtVVNTE2Curtr592di0gRR~33DiVawCCGL30GqGQSBADOTeCEx9Nl4IKR4R1vnzs7hCGZ-jA__
- Plan 02 : https://cms-toolkit-artifacts.artlist.io/content/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-v1/media__1/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-4e2cdd5a-3f8f-4a57-acd3-f699bafcfa82.mp4?Expires=2104003924&Key-Pair-Id=K2ZDLYDZI2R1DF&Signature=btuqPyAlxEt59mRgSUk1TWrcyI29BQ2dXtbSAzW~fiOgCV1k6sRZjtOULHv1a3h7hCKcR0~IggVXFlnaMCWlU64bsazS53~tcXhmoaRkIUodhaBOgFQw14~z3cXRnycoH6Qrc6ACzmdww3zqIkYgWXqIy7KLvZW1xgm0mgYLkrtXR2-18MnXsyOfaJVnJFP0O9Y-2z5AvcG9cOS1TUuEMemg1M6vG737wxTrqA0aTz4S3al~ud~SOInupIfBsx6qi8C4lFSDu28vIDtwNB4i4ELQFLWihrkyoejUv2ewD1b~yvzqZg2udBPoiOdvD9XnLdyGVwMNPNnA3QCeLDih-g__
- Plan 03 : https://cms-toolkit-artifacts.artlist.io/content/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-v1/media__10/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-e62bccd7-b938-4d97-b0b8-f6f26b3ba211.mp4?Expires=2104004137&Key-Pair-Id=K2ZDLYDZI2R1DF&Signature=l4WLcHXltFCSPIsQ~RUPJ5Cd11n8hQciEOD11zDg72qOlFPfTwoXze68O3BQPbuqdmg-xxSTwCKycypym9yiOC8HdE8DgcepVXAnokl1CMoLk8UQDT~7mKhxI6XQKAB0aSiVKTfyMButsDsB-qovIHP1-Sq-DxenXQa0PGkNjqNvsrn8fvO8I0Wa2i8Wu~uIUN99TISzzRpUks2A8tcB-SJLkVfAZl1fxNQzDhwGJPfRDcw648~JoIbve~CwrsY3nOS~tOb6w6gpcAjXQko-pKb83uAW3jDcI6YLm0pIzHi2nZfAR0VFnj8wwk~NFy0vOeK7ThMURcYgqpJLK2mFIg__
- Plan 04 : https://cms-toolkit-artifacts.artlist.io/content/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-v1/media__7/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-b3cae546-c518-4b1f-8fba-35bad3a973a9.mp4?Expires=2104004345&Key-Pair-Id=K2ZDLYDZI2R1DF&Signature=l4WLcHXltFCSPIsQ~RUPJ5Cd11n8hQciEOD11zDg72qOlFPfTwoXze68O3BQPbuqdmg-xxSTwCKycypym9yiOC8HdE8DgcepVXAnokl1CMoLk8UQDT~7mKhxI6XQKAB0aSiVKTfyMButsDsB-qovIHP1-Sq-DxenXQa0PGkNjqNvsrn8fvO8I0Wa2i8Wu~uIUN99TISzzRpUks2A8tcB-SJLkVfAZl1fxNQzDhwGJPfRDcw648~JoIbve~CwrsY3nOS~tOb6w6gpcAjXQko-pKb83uAW3jDcI6YLm0pIzHi2nZfAR0VFnj8wwk~NFy0vOeK7ThMURcYgqpJLK2mFIg__
- Plan 05 : https://cms-toolkit-artifacts.artlist.io/content/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-v1/media__7/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-f4d7f9e7-4e8c-4a47-83e4-52c5554a3d48.mp4?Expires=2104004538&Key-Pair-Id=K2ZDLYDZI2R1DF&Signature=CCSE~gxW87r33ZxmZv81LZ3WQRTMN14UuPwSMO0p7oaQBZZ1hrabHC-jTHX5s6oyrk3wQr5MKfjhJaMEXdXopuSuV6rL5q7rKoNq1jHuWWTgu0PNWkSOno3ve437f6OJNykSRtf8rLgPsD-Ny3C2WIeMz6OcIdjzYkHpAygTmIzrUxvacuITLYuGH3iQqE3ECry72XaSa4jQcE8I2FH6kzWeOzla0zcDD97Uwk0mZgNlEQx-EcWfwz3Y1dqwz98934lxU~VWvV7f3tyYK7SAxWinMYRD5BNABZlZkuwL-a1AxiERPxyS2WkjFb15meJN5g9~hqdMUu-GspqbdayhfQ__
- Plan 06 : https://cms-toolkit-artifacts.artlist.io/content/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-v1/media__10/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-fa5b3bcf-da6c-424c-9ad5-ccb1e2248244.mp4?Expires=2104004726&Key-Pair-Id=K2ZDLYDZI2R1DF&Signature=sS5tNJndNRxlHazObHqBseIJFgGvPgjyVFYFxTqV1lJ5SoUNTcGTh0YcQdPwMMzpluGjEI76cLKCLQ1~Wg~fftrgesuudRLMaIsl9xFRcwKdnovH415GamN2Zu7JvEDmMC0cSFsa3kw2BJi-PWB-NsdeegHl4YK6-ijvjvT7TBCAjFhrQBxatJ9rwAY9eAnUY8JwOoqvKN3CkGx1S41scSt9Qhx8oDJbR6IhoppSeKfXDgoZl7ntXgwIPHH1XdDXwvfkcB1jE5jcvhuoE9kdHvetYTbwbduSkXMMLeF1HotTq7I0g5cObs8R2obI7yT8HOg2kB~jF2I-9VkZzCu2FQ__
- Plan 07 : https://cms-toolkit-artifacts.artlist.io/content/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-v1/media__4/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-efd17c6c-de11-4588-a07b-bfc6095e8bed.mp4?Expires=2104004906&Key-Pair-Id=K2ZDLYDZI2R1DF&Signature=f2amfNaXYt8TcDrmIo9fTzEOdPLS5q0nVXD6S14ByPwvNdXQYWfIQzkn-BLGGEPsT6oz4Ts1DropIzx74DMjiyD9Hil9cFgQcI~ZFcG2-cIheqrgVaSIG~Yt4KxB9n1tfN4jUSPXsnCt455R9AOG7cvVHcl9hi7kQ19oB3tmLj23y-QN9IBizU4rhksIAApOEag6n1HyUCtVkx9QJ5mHEG089uRIiwh-Q3aIb14P4qzP4uQuFCzWY4geH38aBZaZCRVgmULDG9TvciYXVkacOYXzpuehiudBzLBPyi5uGbPNEcncBhm17UBlZFtdsFVusVVIQQPj4njhwILQJy4ReQ__
- Plan 08 : https://cms-toolkit-artifacts.artlist.io/content/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-v1/media__8/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-e157e6d8-2c1c-4fb6-b4b5-e5552dc56fd3.mp4?Expires=2104005155&Key-Pair-Id=K2ZDLYDZI2R1DF&Signature=0BrD35f0iuMzfe87n8dvQ7oR0AxzhAf4k2Ej0wMFOx~QMkR~60DBUoMsx-Xb03Y8mH9iag5zYx30cXSfMOWi-9Zw2i9l8Bi31seqRwqT~mLQLV5f4p10l722zWrJxq5MZ1lID9TjX9vgdXatt~E44MtpqX2wQqUP5CEXwACA-yhwWfDW0paUBAtOt-bCzkX0Z-K46RbN8UliOxvWL4WrdsDSOJHBlAn9pn8BkaXRKmXQhnhYd9lIhpd-oIK6a-iDV-uBR1s2WOUdAWPNJgueXKop-LR4sN09LLlJSs4mgpyyO7CxcC7TiijPG9DCkgcRAdT7qsfjZDxjx5adaE4s8w__

## Note sur le blocage réseau

Cette session cloud passe par un proxy d'agent qui refuse le domaine
`artlist.io` (403 sur le CONNECT). Même blocage que documenté pour Manoir de
Lan Kerellec. **Prochaine étape à faire en local** :

1. Télécharger les 8 rushes depuis les liens ci-dessus vers
   `projects/le-chateau-de-sable/rushes/<NN>-<categorie>.mp4`.
2. Pour chaque plan, extraire 5-6 frames (`ffmpeg`) et les analyser :
   - Warping (particulièrement le plan 08 — sujet vivant, mouton).
   - Décision ambiance : générer UNIQUEMENT si l'analyse montre un vrai
     apport (prompt déjà écrit dans chaque fiche `shots/<NN>-*.md`).
   - Décision foley : même logique, prompt à écrire depuis les frames
     observées (jamais depuis la photo).
3. Mettre à jour ce fichier et les fiches `shots/` avec les décisions et les
   chemins locaux une fois téléchargés.
