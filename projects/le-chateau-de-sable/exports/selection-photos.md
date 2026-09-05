# Sélection des photos source — Le Château de Sable

**Source** : Google Drive, dossier `lechateaudesable - Photos Instagram - 25 dernieres`
(id `1VzDDBWa770635g_d0ZusIDKiQJK54RIr`, dans `Videos_immersives`)

> **Mise à jour** : sélection revue après une modification manuelle par
> l'utilisateur du dossier miroir Drive "Sélection vidéo - 8 photos" — 4
> nouvelles photos ajoutées directement, dont une vraie photo de chambre qui
> comblait le trou signalé dans la version précédente de ce rapport. Voir
> détail ci-dessous.

## Bilan du tri (lot initial, 24 photos)

- **24** photos rapatriées depuis Drive
- **7** écartées au pré-filtrage technique (résolution insuffisante, < 1080px
  sur le plus petit côté)
- **17** candidats techniquement valides passés en revue visuelle
- **4** écartées en revue visuelle : 2 portraits identifiables (chef,
  réceptionniste), 1 collage multi-images, 1 scène hors-catégorie (festival
  de cerfs-volants)

## Ajustement manuel du dossier miroir Drive

L'utilisateur a directement modifié le dossier "Sélection vidéo - 8 photos" :
retrait de 5 photos du premier passage (dessert chocolat, coffret vin,
fauteuil cosy, spa, bar), ajout de 4 nouvelles photos hors du lot des 24
initiales :

| Fichier | Verdict | Raison |
|---|---|---|
| `2025-01-29_07e651aa...` | **Retenue** | Chambre lumineuse (lit king size, terrasse vitrée, bureau) — comble la catégorie "chambre", absente du premier passage |
| `2025-02-22_917181fb...` | **Retenue** | Main versant une sauce sur un dessert (mousse, œufs de saumon), geste net et propre, aucun visage |
| `2018-01-23_e540a19b...` | Écartée | 720×900px — bien sous le seuil technique (1080px), risque fort d'artefacts en image-to-video |
| `2026-02-05_e5115cf6...` | Écartée | 960px — déjà écartée au pré-filtrage du lot initial pour la même raison |

Les 2 photos sous le seuil de résolution ont été retirées après validation
explicite de l'utilisateur ; la sélection a été complétée en réintégrant les
meilleures candidates du premier passage (coffret de vin, spa, restaurant,
bar, terrasse, moutons) pour revenir à 8 photos, désormais avec un vrai plan
chambre.

## Sélection finale (mise à jour)

| # | Fichier | Catégorie | Description | Raison de sélection |
|---|---|---|---|---|
| 01 | `01-gastronomie-dessert-macro.jpg` | Gastronomie | Main versant une sauce sombre sur un dessert (mousse, œufs de saumon/groseille), table en extérieur | Geste de dressage net, aucun visage, bon candidat pour un foley de liquide versé |
| 02 | `02-gastronomie-coffret-vin.jpg` | Gastronomie | Coffret de vin (Brumont Montus) et verre, posé sur un rocher de granit | Ancrage terroir/minéral, complète le plan dessert |
| 03 | `03-chambre.jpg` | Chambre | Chambre lumineuse, lit king size, terrasse vitrée en arrière-plan, bureau et TV | Plan chambre manquant dans la version précédente — ajout de l'utilisateur, très bon candidat (sujet net, aucune personne) |
| 04 | `04-espaces-communs-spa.jpg` | Espaces communs | Salle de soins/massage, lumière tamisée | Espace bien-être différenciant, aucun visage |
| 05 | `05-espaces-communs-restaurant.jpg` | Espaces communs | Salle de restaurant, lumière dorée de fin de journée | Meilleure lumière naturelle du dossier |
| 06 | `06-espaces-communs-bar.jpg` | Espaces communs | Flatlay bar : cocktail, menthe, tonic, limoncello | Ambiance bar/apéritif, composition graphique forte |
| 07 | `07-panorama-terrasse.jpg` | Panorama/extérieur | Terrasse en hauteur, vue sur la lande et l'horizon | Seule vue extérieure/panoramique nette du dossier |
| 08 | `08-paysage-territoire-moutons.jpg` | Paysage/territoire | Moutons noirs (race locale) dans un pré clos de pierre | Ancrage territoire fort — ⚠️ sujet vivant, prévoir un prompt caméra très contraint |

## Meilleures candidates non retenues

- `2026-04-03_d46292e5...` (sculpture chocolat pieuvre sur galets) — redondante
  avec le plan 02
- `2026-06-07_b3504d98...` (salle de restaurant, tables dressées) — redondante
  avec le plan 05
- `03-interieur-fauteuil-cosy` (ancien substitut chambre) — plus nécessaire,
  remplacé par une vraie photo de chambre

## Prochaine étape

`shotlist-generator` a été relancé sur cette nouvelle composition — les
fiches de plan dans `shots/` reflètent cette version, pas la précédente.
