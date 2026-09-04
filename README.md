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
1. Image-to-Video (Runway Gen-3 / Kling)      → skill: shotlist-generator
     ↓
2. Sound Design (ElevenLabs Text-to-Sound)     → skill: sound-design
     ↓
3. Thème musical (24s, IA musicale)            → skill: sound-design
     ↓
4. Montage, mixage, révélation logo (CapCut)   → skill: montage-capcut
```

L'étape 0 est optionnelle : si l'utilisateur fournit déjà des photos triées, on
passe directement à `shotlist-generator`.

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
    exports/                  Livrables (shotlist.md, EDL montage, emails)
templates/                  Gabarits réutilisables (email, config)
scripts/new_project.py      Scaffold un nouveau dossier hôtel depuis _template
```

## Démarrer un nouvel hôtel

```bash
python3 scripts/new_project.py "Castel Beau Site"
```

Crée `projects/castel-beau-site/` avec `config.yaml` à remplir et les sous-dossiers
`shots/` et `exports/`.

## Les 4 skills

| Skill | Rôle | Invoque |
|---|---|---|
| `/selection-photos` | Trie un dossier de photos brutes issues d'un scrape Instagram (ex: Apify) et sélectionne les 8 meilleures (résolution, diversité des plans, attractivité, adéquation image-to-video) | En amont, si les photos ne sont pas déjà triées |
| `/shotlist-generator` | À partir d'un brief hôtel + photos dispo (ou `photos-source/` déjà sélectionné), génère la shot-list complète (prompts caméra, durée, structure narrative façon Castel Beau Site) | En premier, une fois le projet scaffoldé |
| `/sound-design` | Génère les prompts ElevenLabs (ambiances + foley) par plan et la structure du thème musical 24s | Après la shot-list, avant génération vidéo ou en parallèle |
| `/montage-capcut` | Génère la feuille de montage (EDL) : ordre des plans, transitions, niveaux de mix dB, keyframes de révélation du logo | Une fois les rushes (vidéo + sons) disponibles |
| `/prospection-email` | Génère l'email de prospection personnalisé à partir du template validé, et tient le tracker de prospects | Indépendant, à tout moment du cycle commercial |
| `/critique-artistique` | Directeur artistique : analyse la vidéo finale et compare son identité visuelle (palette, lumière, cadrage, rythme) à celle du compte Instagram réel de l'hôtel, donne un verdict et des recommandations | En dernier, une fois la vidéo montée, avant envoi au client |

Chaque skill lit `projects/<hotel-slug>/config.yaml` quand il existe pour se
personnaliser automatiquement (nom de l'hôtel, étoiles, positionnement, ton).

## Cas de référence : Castel Beau Site

Le projet `projects/castel-beau-site/` sert de gabarit de qualité pour tous les
prochains hôtels : 5 plans (gastronomie macro, panorama côtier, chambre prestige,
espaces communs, paysage) + un outro logo. Voir `shots/` pour le détail de chaque
prompt.
