# Feuille de montage (EDL) — Castel Beau Site

## Ordre des plans et transitions

| Ordre | Plan | Durée | Transition vers le suivant |
|---|---|---|---|
| 1 | 01 — Gastronomie | 4-5s | Fondu croisé court (0,3-0,5s) — ambiance intérieure feutrée → extérieur venteux |
| 2 | 02 — Panorama Côtier | 4-5s | Cut franc — les deux plans suivants restent en registre "vue mer" |
| 3 | 03 — Chambre Prestige | 4-5s | Fondu croisé court (0,3-0,5s) — silence intérieur → ambiance lounge |
| 4 | 04 — Espaces Communs | 4-5s | Fondu croisé court (0,3-0,5s) — intérieur → grand large |
| 5 | 05 — Territoire | 4-5s | Fondu croisé vers outro (1,5-2s, cf. ci-dessous) |
| 6 | 06 — Outro logo | ~2s | — |

## Mix audio

- **Musique (thème 24s)** : -12 à -15 dB sur toute la timeline, fade-out sur les
  2-3 dernières secondes (calé sur le fondu du logo).
- **Ambiances/foley par plan** : 100%, pas de réduction.
- Micro-fondu de 0,2-0,3s sur l'ambiance sortante entre le plan 02 (mer, forte)
  et le plan 03 (intérieur, quasi-silencieux) pour éviter une coupure sèche à
  l'oreille.

## Outro logo — keyframes

- Fond : surimpression blanche sur le dernier plan filmé (05 — Territoire), à
  défaut de fichier logo dédié fourni.
- Keyframe 1 à 0s (début du fondu) : scale 100%, opacity 0%.
- Keyframe 2 à 1,8s (fin du fondu) : scale 103%, opacity 100%.
- Durée totale du fondu : 1,8s (dans la fourchette 1,5-2s).

## Checklist avant livraison

- [ ] Musique bien en retrait (-12/-15 dB) sur tous les plans ?
- [ ] Aucun foley qui déborde sur le plan suivant ?
- [ ] Transitions cohérentes avec le tableau ci-dessus (pas de fondu long, pas de wipe/glitch) ?
- [ ] Logo lisible et centré sur fond neutre ?
- [ ] Fade-out musical synchronisé avec la fin du fondu logo ?
- [ ] Export sans filigrane, sans mention "spécimen" ?
- [ ] Durée totale cohérente (5 plans × 4-5s + ~2s outro ≈ 22-27s) ?
