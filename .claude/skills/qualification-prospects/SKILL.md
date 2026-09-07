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
  - Modèle Claude : `claude-sonnet-4-20250514` (connexion Anthropic déjà
    configurée dans ce workspace Make, réutilisée depuis le scénario
    "Radar IA").
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

## État connu au 2026-09-07 — à vérifier avant un premier run en masse

Le scénario a été testé une fois de bout en bout sur un enregistrement réel
(Manoir de Lan Kerellec). Un bug bloquant a été trouvé et corrigé : les
modules `datastore:SearchRecord` et `datastore:UpdateRecord` exposent/
attendent les champs sous une clé `data` imbriquée (`{{1.data.champ}}` en
lecture, `data: {...}` en écriture), pas à plat — ce n'est documenté nulle
part dans l'aide des modules, seule la RPC `iface2`/`expect` le révèle.
Cette correction est en place dans le scénario actuel.

Le dernier run de test a consommé seulement 6 opérations (au lieu d'environ
11 attendues pour un passage complet jusqu'à `UpdateRecord`) sans erreur
reportée, et le champ `raison` n'a pas été rempli — signe que l'exécution
s'arrête quelque part entre la récupération des posts Apify et l'appel
Claude, sans lever d'erreur exploitable via l'API Make. **Avant de lancer un
run sur un vrai lot de prospects, ouvrir le scénario une fois dans
l'éditeur visuel Make (scenario 9766362) et faire un "Run once" — l'éditeur
montre le contenu réel de chaque bundle à chaque étape, ce qui permettra de
voir immédiatement où ça s'arrête (probablement le nombre d'items retournés
par `fetchDatasetItems`, ou une des 3 récupérations d'image).** C'est un
diagnostic visuel de 2 minutes, pas refaisable à l'aveugle depuis cette
interface.
