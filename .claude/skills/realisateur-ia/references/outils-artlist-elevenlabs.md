# Cheat-sheet technique — Artlist (vidéo) & ElevenLabs (son)

Les noms d'outils MCP et de modèles évoluent — si un appel échoue avec une
erreur de type "outil introuvable" ou "modèle inconnu", relance `ToolSearch`
sur `mcp__artlist__` ou `mcp__ElevenLabs__` pour vérifier le nom exact avant
de conclure que la fonctionnalité a disparu.

## Artlist — génération vidéo depuis une photo

### 1. Uploader la photo

La photo est un fichier local (`projects/<slug>/photos-source/`), pas une URL
publique — utilise le mode upload en 3 appels :

1. `mcp__artlist__upload_image` avec `mimeType: "image/jpeg"` et `fileName`
   (le nom du fichier, ex: `01-gastronomie-dessert.jpg`) → renvoie
   `uploadUrl` + `uploadId`.
2. `PUT` les octets du fichier vers `uploadUrl` (Bash `curl -X PUT --data-binary @<chemin> -H "Content-Type: image/jpeg" "<uploadUrl>"`).
3. `mcp__artlist__confirm_upload` avec le même `uploadId` et `mimeType` →
   renvoie `assetId`. Un `urlPending: true` sans `url` n'est pas un échec, la
   génération fonctionne déjà avec cet `assetId`.

### 2. Choisir le modèle

`mcp__artlist__list_models` avec `kind: "video"` et
`feature: "image-to-video"` pour lister les modèles compatibles. Puis
`get_model_config` sur le modèle retenu pour connaître ses réglages
disponibles (durée, force du mouvement, etc.) avant de generer — ne devine
jamais un nom de réglage.

Réglages à viser, cohérents avec les invariants du studio
(`shotlist-generator`) : durée 4-5s, mouvement de caméra faible/lent quand le
modèle expose ce réglage. Si le modèle a une option de "camera motion
strength" ou équivalent, préfère toujours la valeur la plus basse disponible
au-dessus de zéro — c'est ce qui évite le warping architectural.

### 3. Générer

`generate_video` avec :
- `input: { assetId }` (l'asset uploadé — jamais une image générée dans ce
  contexte, on anime toujours la photo source réelle).
- `prompt` : le prompt caméra du plan, tel qu'écrit par `shotlist-generator`
  (déjà en anglais descriptif naturel, compatible avec la plupart des
  modèles image-to-video).
- `modelGroupId` ou `modelId` du modèle retenu à l'étape précédente.
- `settings` : les réglages validés via `get_model_config`.

Coût : toujours `get_generation_cost` avec les mêmes paramètres avant le
premier appel réel de la session pour ce plan (voir SKILL.md Étape 1).

### 4. Récupérer le résultat

`get_generation_status(generationId)` — rappeler immédiatement si `pending`
(l'outil bloque déjà côté serveur jusqu'à 50s, pas de `sleep` à ajouter).
Pour plusieurs plans lancés d'affilée, passer un tableau de `generationId` à
un seul appel plutôt que d'en faire un par plan.

Le résultat terminé contient une URL de fichier vidéo — télécharge-la avec
Bash (`curl -o projects/<slug>/rushes/<NN>-<categorie>.mp4 "<url>"`).

## ElevenLabs — sound effects & musique

Il n'existe pas d'outil dédié "générer un son" ou "générer une musique" —
les deux passent par `creative_generate_in_flow`, avec `node_type` différent :

- **Effets sonores (ambiance, foley)** : `node_type: "sfx"`,
  `model_id: "eleven_text_to_sound_v2"`.
- **Musique** : `node_type: "music"`, `model_id: "eleven_music_v2"` (ou
  `eleven_music_v1` si `v2` n'est pas disponible dans l'espace de travail —
  vérifier avec `creative_get_model_guide` sur le modèle avant de générer, la
  syntaxe de prompt musical diffère parfois d'une version à l'autre).

Toujours passer `context` (pourquoi cette génération — une phrase suffit,
c'est un paramètre requis par l'outil) et `prompt`. Pour l'ambiance et la
musique, c'est le texte déjà écrit par `sound-design`, repris tel quel. Pour
le foley, c'est le prompt que tu viens d'écrire toi-même en observant le rush
(SKILL.md Étape 3) — jamais un prompt anticipé depuis la photo.

Toujours passer aussi `generations_count: 1` explicitement. Le défaut de
l'outil est 4 (pour laisser choisir parmi plusieurs variations), ce qui
quadruple le coût sans qu'on en ait besoin ici — une seule variation par
plan suffit pour ce studio.

### Devis avant génération

Appeler une première fois avec `estimate_only: true` — l'outil renvoie le
coût en crédits sans rien générer. C'est ce résultat qui sert à construire le
total présenté à l'utilisateur avant de lancer quoi que ce soit (SKILL.md
Étape 1). Le coût réel facturé après génération est souvent nettement
inférieur au devis (observé : devis 55 crédits, coût réel ~16,7) — le devis
majore par prudence, ce n'est pas une erreur, juste ne pas s'y fier à la
décimale près pour le budget final.

### Exemples de prompts foley (écrits depuis un rush observé, pas une photo)

Le point commun de ces exemples : ils décrivent un geste vu dans les frames
extraites, pas un geste supposé. Même structure que les ambiances — matière →
action → distance au micro — mais un seul événement net, jamais deux cumulés :

- Liquide versé (frames montrant un filet continu) : *"Thin stream of sauce
  being poured from a small ceramic jug onto a plate, light continuous
  trickle, close mic, no reverb."*
- Lame qui tranche (frames montrant une coupe progressive) : *"Single knife
  slicing through a firm aged cheese wheel, clean crisp cut, subtle
  blade-on-wood contact at the end, close mic, no reverb."*
- Tissu qui bouge (frames montrant un rideau/nappe qui ondule) : *"Light
  fabric rustle, soft continuous movement, close and dry, no wind."*

Si les frames ne montrent aucun de ces cas — juste un push-in de caméra sur
une scène par ailleurs immobile — c'est le signal qu'aucun foley n'est
justifié, pas qu'il faut en inventer un pour ne pas repartir bredouille.

### Suivi et récupération

`creative_generate_in_flow` renvoie `flow_id` et `session_id(s)`. Suivre avec
`creative_get_flow_run_status(flow_id, session_ids)` en attendant
`poll_after_seconds` entre deux appels, jusqu'à `all_completed` (ou
`has_failures`, auquel cas relire l'erreur avant de relancer — jamais
relancer en boucle sans comprendre pourquoi ça a échoué). Une fois terminé,
`creative_show_flow_results` (ou l'URL déjà présente dans le statut) donne le
fichier audio à télécharger (Bash `curl`) vers
`projects/<slug>/audio/<nom>.mp3`.

### Un flow par génération suffit

Pas besoin de `creative_create_flow` en amont pour ce studio : chaque son ou
musique est un one-off indépendant, pas une chaîne de générations qui se
nourrissent l'une l'autre (contrairement à un lipsync par exemple). Laisser
`flow_id` vide à chaque appel crée un flow séparé à chaque fois, ce qui est
très bien ici.
