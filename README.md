# Studio Vidéo Immersive — Hôtellerie de Prestige

Pipeline de production automatisé pour transformer les photothèques d'hôtels 4/5 étoiles
en séquences vidéo cinématiques habillées d'un sound design sur-mesure — sans logistique
sur place — plus les outils de prospection commerciale associés.

## Vision

Les hôtels indépendants haut de gamme ont des photos superbes mais peu de vidéo régulière
pour Instagram, les campagnes sponsorisées et leur site web. On transforme leurs photos
existantes en clips cinématiques (image-to-video + sound design + musique + montage),
sans mobiliser un vidéaste sur place.

## Le pipeline (4 étapes)

```
[ Scrape Instagram (Apify) ]
     ↓
0. Sélection des 8 meilleures photos           → skill: selection-photos
     ↓
[ Photo HD ]
     ↓
1. Prompts caméra image-to-video               → skill: shotlist-generator
     ↓
2. Prompts sound design + thème musical         → skill: sound-design
     ↓
3. Génération réelle vidéo (Artlist) +          → skill: realisateur-ia
   sons/musique (ElevenLabs)
     ↓
4. Montage, mixage, révélation logo (CapCut)   → skill: montage-capcut
```

L'étape 0 est optionnelle : si l'utilisateur fournit déjà des photos triées, on
passe directement à `shotlist-generator`. Les étapes 1-2 écrivent les prompts
(pas de coût), l'étape 3 les exécute réellement via Artlist et ElevenLabs — et
dépense de vrais crédits, toujours avec confirmation de budget au préalable.

### Alimentation Apify/Make déjà en place

Le scrape Instagram lui-même est géré côté Make, pas par ce dépôt : le scénario
`Apify → 30 dernieres photos → Google Drive (<slug>)` (actor Apify Instagram
Scraper `shu8hvrXbJbY3Eb9W`) prend l'URL du compte Instagram, récupère les 30
derniers posts et dépose les photos dans un sous-dossier Google Drive
`"<slug> - Photos Instagram - 30 dernieres"`. Le skill `selection-photos` sait
lire ce dossier Drive directement (voir sa section "Procédure spécifique —
source Google Drive"). À dupliquer dans Make pour chaque nouvel hôtel (changer
l'URL Instagram et le nom du dossier créé) tant que le scénario n'est pas
généralisé avec ces valeurs en paramètres d'entrée.

**Dossier parent commun** — tous ces sous-dossiers, un par établissement,
doivent être créés à l'intérieur du dossier Drive partagé du studio
**`Videos_immersives`**
(https://drive.google.com/drive/folders/1kDhEW9gV4UbEUG18eX8WVYeH7pJdtDqm),
jamais à la racine du Drive. Le module `google-drive:createAFolder` du
scénario Make cible déjà ce dossier comme `folderId` — en dupliquant le
scénario pour un nouvel hôtel, ne change que le nom du sous-dossier créé et
l'URL Instagram, laisse ce `folderId` tel quel.

En parallèle, la prospection est outillée par le skill `prospection-email`, et la
qualité du livrable final est validée par le skill `critique-artistique`.

## Structure du dépôt

```
.claude/skills/            Skills Claude Code (voir ci-dessous)
projects/
  _template/                Squelette vierge pour un nouvel hôtel
  <hotel-slug>/              Un dossier par hôtel prospecté/produit
    config.yaml               Identité de l'hôtel, positionnement, contacts
    photos-source/            Les 8 photos retenues (rempli par selection-photos)
    shots/                    Une fiche par plan (prompt vidéo + sound design)
    rushes/                   Vidéos générées par realisateur-ia (Artlist)
    audio/                    Sons + musique générés par realisateur-ia (ElevenLabs)
    exports/                  Livrables (shotlist.md, EDL montage, emails, generation-log.md)
templates/                  Gabarits réutilisables (email, config)
scripts/new_project.py      Scaffold un nouveau dossier hôtel depuis _template
```

## Démarrer un nouvel hôtel

```bash
python3 scripts/new_project.py "Castel Beau Site"
```

Crée `projects/castel-beau-site/` avec `config.yaml` à remplir et les sous-dossiers
`shots/` et `exports/`.

## Les 7 skills

| Skill | Rôle | Invoque |
|---|---|---|
| `/selection-photos` | Trie un dossier de photos brutes issues d'un scrape Instagram (ex: Apify) et sélectionne les 8 meilleures (résolution, diversité des plans, attractivité, adéquation image-to-video) | En amont, si les photos ne sont pas déjà triées |
| `/shotlist-generator` | À partir d'un brief hôtel + photos dispo (ou `photos-source/` déjà sélectionné), génère la shot-list complète (prompts caméra, durée, structure narrative façon Castel Beau Site) | En premier, une fois le projet scaffoldé |
| `/sound-design` | Génère les prompts ElevenLabs (ambiances + foley) par plan et la structure du thème musical 24s | Après la shot-list, avant génération vidéo ou en parallèle |
| `/realisateur-ia` | Réalisateur + directeur technique IA : exécute réellement les prompts caméra via Artlist (image-to-video) et les prompts sound design via ElevenLabs (sfx + musique), avec devis et confirmation de budget avant toute dépense | Une fois les prompts (shot-list + sound design) écrits, avant montage |
| `/montage-capcut` | Génère la feuille de montage (EDL) : ordre des plans, transitions, niveaux de mix dB, keyframes de révélation du logo | Une fois les rushes (vidéo + sons) générés par `realisateur-ia` |
| `/prospection-email` | Génère l'email de prospection personnalisé à partir du template validé, et tient le tracker de prospects | Indépendant, à tout moment du cycle commercial |
| `/critique-artistique` | Directeur artistique : analyse la vidéo finale et compare son identité visuelle (palette, lumière, cadrage, rythme) à celle du compte Instagram réel de l'hôtel, donne un verdict et des recommandations | En dernier, une fois la vidéo montée, avant envoi au client |

Chaque skill lit `projects/<hotel-slug>/config.yaml` quand il existe pour se
personnaliser automatiquement (nom de l'hôtel, étoiles, positionnement, ton).

## Cas de référence : Castel Beau Site

Le projet `projects/castel-beau-site/` sert de gabarit de qualité pour tous les
prochains hôtels : 5 plans (gastronomie macro, panorama côtier, chambre prestige,
espaces communs, paysage) + un outro logo. Voir `shots/` pour le détail de chaque
prompt.
