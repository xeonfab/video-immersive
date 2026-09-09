# Qualification IA des prospects Instagram

## Objectif

Avant de lancer le scraping complet (60 dernières photos) sur un nouvel
établissement, ce skill fait un tri léger et rapide sur une liste de
prospects (potentiellement 100+) : est-ce que le compte Instagram de cet
établissement a des visuels assez qualitatifs, n'a pas déjà une forte
présence vidéo, et correspond au concept du studio (hôtel indépendant haut
de gamme) ? Ça évite de lancer un scraping complet (et de solliciter le
commercial) sur un prospect qui ne convertira jamais.

Ce skill ne fait pas l'analyse lui-même dans la conversation — à l'échelle
de 100+ comptes, ce serait beaucoup trop lent et coûteux en tokens. Il
pilote un **scénario Make** dédié qui fait tourner le jugement IA en masse,
côté Make, sur un **Data Store** partagé.

## Architecture (déjà en place)

- **Data Store Make** `Prospects Instagram — qualification` (id `183729`,
  team 1687066) — un enregistrement par établissement :
  `nom`, `slug`, `instagram_url`, `site_web`, `statut`
  (`a_qualifier` / `viable` / `ecarte` / `erreur`), `score` (0-100),
  `raison`, `ratio_video_pct`, `qualite_visuelle`, `date_qualification`.
- **Scénario Make** `Qualification prospects Instagram — score IA`
  (id `9766362`) : pour chaque enregistrement `statut = a_qualifier`,
  scrape léger Apify (12 derniers posts, pas de téléchargement Drive),
  envoie 3 images + le résumé JSON des posts à Claude (vision), récupère
  un verdict structuré (`viable`, `score`, `raison`, `ratio_video_pct`,
  `qualite_visuelle`), et met à jour l'enregistrement.
  - Modèle Claude : `claude-sonnet-5` (connexion Anthropic déjà configurée
    dans ce workspace Make, id `13999972`).
  - Coût : 1 run Apify (léger, resultsLimit 12) + 1 appel Claude vision par
    prospect. Pas de stockage Drive à cette étape — uniquement au moment du
    scraping complet, une fois le prospect validé viable.

## Étape 1 — Alimenter le Data Store

Pour chaque établissement de la liste fournie par l'utilisateur (nom,
Instagram, site web), créer un enregistrement dans le data store `183729`
avec `statut: "a_qualifier"` (`mcp__Make__data-store-records_create`, ou
`data-store-records_create` en boucle pour un lot). Ne jamais réutiliser
une clé existante pour un établissement déjà qualifié — vérifier d'abord
avec `data-store-records_list` si l'établissement n'y est pas déjà.

## Étape 2 — Lancer la qualification

Le scénario Make est `on-demand`. Il traite TOUS les enregistrements
`a_qualifier` en un seul run (`mcp__Make__scenarios_run` avec
`scenarioId: 9766362`, `responsive: true`) — pas besoin de le relancer par
établissement. Le scénario doit être **actif** avant de le lancer
(`scenarios_activate`) — attention au plafond du compte Make (2 scénarios
actifs simultanément observé sur ce compte au 2026-09-07) : vérifier avec
`scenarios_list` s'il faut désactiver temporairement un autre scénario
avant, et **toujours demander confirmation à l'utilisateur** avant de
désactiver un scénario qui n'est pas à toi (ex: le radar RSS ou un scraper
photo en cours d'usage).

À l'échelle de 100+ prospects, un seul run peut consommer beaucoup
d'opérations Make (chaque prospect ≈ 9-11 opérations) — prévenir
l'utilisateur du volume avant de lancer un run sur un gros lot, et proposer
de le découper (ex: 20 par 20) si le solde d'opérations Make est serré.

## Étape 3 — Lire les résultats

Une fois le run terminé, relire le data store
(`data-store-records_list`, `dataStoreId: 183729`) et présenter un
récapitulatif à l'utilisateur :
- Nombre de prospects traités, viables, écartés, en erreur.
- Table triée par score décroissant pour les viables (nom, score, raison).
- Table des écartés avec la raison (ratio vidéo trop élevé, qualité
  visuelle insuffisante, hors-concept...).

## Étape 4 — Enchaîner sur le scraping complet

Pour chaque prospect `statut = viable` que l'utilisateur valide, la suite
du pipeline est **inchangée** : créer le scénario Make dédié "Apify → 60
dernières photos → Google Drive (<slug>)" sur le modèle des scénarios
existants (voir `references/outils-artlist-elevenlabs.md` du skill
`realisateur-ia` pour le pattern équivalent côté vidéo — ici le pattern de
référence est le scénario "Apify → 50 photos → Google Drive (domainedebiar)",
id `9766274`, à cloner/adapter avec le bon `directUrls` et `resultsLimit:
60`), puis enchaîner sur `selection-photos`.

## État validé au 2026-09-09 — pipeline fonctionnel de bout en bout

Le scénario a été testé complet sur un enregistrement réel (Manoir de Lan
Kerellec, `test-manoirdelankerellec`) : `statut` passe correctement à
`viable`/`ecarte` avec `score`, `raison`, `ratio_video_pct` et
`qualite_visuelle` tous remplis par le jugement Claude. Plusieurs bugs
Make non documentés ont été trouvés et corrigés au passage :

1. **Placement du paramètre `datastore`** : doit être dans `parameters`
   (statique), pas dans `mapper` — sinon `TypeError: Cannot read properties
   of undefined (reading 'datastore')`.
2. **Forme du filtre `SearchRecord`** : `filter` doit être un tableau
   imbriqué (`[[{...}]]`, groupes OR de conditions AND), pas un tableau
   plat.
3. **Nesting `data`** : `datastore:SearchRecord` expose les champs sous
   `{{N.data.champ}}` (pas `{{N.champ}}`), et `datastore:UpdateRecord`
   attend `mapper: {key, upsert, overwriteArrays, data: {...champs}}` (pas
   les champs à plat dans `mapper`). Non documenté dans l'aide du module —
   seule la RPC `iface2`/`expect?action=update` le révèle.
4. **Indexation de tableau** : `{{get(array; N).champ}}` ne chaîne pas
   l'accesseur — il retourne tout l'objet JSON de l'item au lieu du champ.
   Utiliser la notation crochets `{{array[N].champ}}`, qui fonctionne
   correctement.
5. **Types numériques** : `max_tokens` et `temperature` du module Claude
   doivent être des nombres JSON (`700`, `0`), pas des chaînes (`"700"`,
   `"0"`) — sinon `[400] max_tokens: Input should be a valid integer`.
6. **Modèle Claude** : `claude-sonnet-4-20250514` n'est plus disponible sur
   cette connexion Anthropic (404) — utiliser `claude-sonnet-5`. Vérifier
   la liste à jour avec la RPC `listModels` si un modèle est de nouveau
   invalide un jour.
7. **Le plus gros piège — sortie du module `anthropic-claude:createAMessage`** :
   il n'existe **aucun champ `textResponse`** en sortie de ce module,
   contrairement à ce que suggère un scénario de référence ("Radar IA")
   copié initialement. La sortie réelle est `content: [...]`, un tableau de
   blocs (`{type, text, ...}`) — le texte de la réponse Claude est dans
   `{{9.content[1].text}}` (premier bloc de type texte), pas
   `{{9.textResponse}}`. Utiliser une référence inexistante ne lève pas
   d'erreur dans Make : elle s'évalue silencieusement en chaîne vide, ce
   qui a fait planter `json:ParseJSON` en aval (`BundleValidationError`)
   sans qu'aucun log ne pointe vers la vraie cause. Vérifié avec
   `mcp__Make__app-module_get` (schéma de sortie du module) — pas visible
   dans l'éditeur visuel sans l'ouvrir soi-même.

Toutes ces corrections sont en place dans le scénario actuel (id
`9766362`). Le blueprint de référence à jour est : `SearchRecord` (data
imbriquée) → `apify:runActorNew`/`apifyApiCall`/`fetchDatasetItems` →
`BasicAggregator` → 3× `http:ActionGetFile` (URLs en notation crochets) →
`anthropic-claude:createAMessage` (modèle `claude-sonnet-5`, max_tokens/
temperature en nombres) → `json:ParseJSON` sur `{{9.content[1].text}}` →
`datastore:UpdateRecord` (data imbriquée).

Méthode de diagnostic qui a permis de trouver ces bugs (utile pour la
prochaine fois) : bisection par troncature du blueprint (retirer les
modules après le point suspect) + branches diagnostiques dédiées qui
écrivent une valeur brute (ex: `{{9.content[1].text}}`, une longueur de
tableau, un item indexé) directement dans un champ du data store via un
`UpdateRecord` de test — `executions_get-detail` ne donne pas
d'introspection utile par module dans cet environnement, contrairement à
ce que sa description laisse penser.
