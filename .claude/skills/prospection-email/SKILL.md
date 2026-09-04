---
name: prospection-email
description: Génère l'email de prospection personnalisé pour un hôtel 4/5 étoiles à partir du template validé (accroche sur la qualité de leurs photos, chiffres conversion vidéo, lien vers l'espace de visionnage, appel à un échange téléphonique — jamais de prix mentionné à froid), et tient à jour le tracker CSV des prospects contactés. Utilise ce skill dès que l'utilisateur veut écrire, personnaliser ou envoyer un email de prospection hôtelière, préparer une relance, ou faire le point sur les prospects en cours ("où j'en suis avec mes prospects", "email pour [hôtel]", "relance [contact]").
---

# Prospection & emails — studio vidéo immersive hôtelière

## Objectif

Produire un email de prospection personnalisé par hôtel en quelques minutes, en
respectant strictement le positionnement validé : posture haut de gamme, aucune
mention de prix au premier contact, un seul objectif — obtenir le visionnage de
la démo et déclencher un appel de 10 minutes.

## Étape 0 — Récupérer le contexte de l'hôtel

Si `projects/<slug>/config.yaml` existe, lis-y le nom de l'hôtel, la catégorie
(4 ou 5 étoiles), le contact commercial et son rôle. Sinon, demande au moins le
nom de l'hôtel et, si possible, le nom/rôle du contact — un email "Bonjour," sans
destinataire identifié perd presque toute sa force face à un Directeur Général.

## Étape 1 — Personnaliser le template

Le template de base est dans `assets/email-template.md` — c'est le texte validé,
ne le réécris pas depuis zéro. Personnalise uniquement les éléments variables :

- Nom de l'hôtel et prénom/civilité du contact.
- Le lien vers l'espace de visionnage (page Notion privée ou vidéo non
  répertoriée, téléchargement désactivé, zéro filigrane) — si aucun lien n'est
  encore prêt, dis-le clairement à l'utilisateur plutôt que de laisser un
  placeholder vague dans l'email final.
- Le jour proposé pour l'appel — choisis un jour ouvré proche et cohérent avec
  la date du jour si l'utilisateur n'en précise pas.
- Le nombre de clichés animés dans la démo, s'il diffère de 4.

Ne touche pas au reste : la structure (accroche → chiffres → proposition de
valeur → preuve concrète → appel à l'action) et le ton sobre sont ce qui fait
marcher cet email — ne pas ajouter d'enthousiasme, de superlatifs ou
d'émojis, ce serait en décalage avec la posture "créateur de contenus immersifs"
pour une clientèle de luxe.

## Étape 2 — Ne jamais introduire de prix

Si l'utilisateur demande d'ajouter un tarif dans l'email, rappelle-lui la
politique validée (aucun prix au premier contact, l'objectif est uniquement le
visionnage + l'appel) avant de le faire à sa demande explicite — ce n'est pas un
refus, juste s'assurer que c'est un choix conscient et pas un oubli de la
stratégie.

## Étape 3 — Tenir le tracker de prospects

Le tracker vit dans `projects/prospects.csv` (à la racine de `projects/`, partagé
entre tous les hôtels). Utilise `scripts/update_tracker.py` pour ajouter ou mettre
à jour une ligne plutôt que d'éditer le CSV à la main — ça évite les erreurs de
colonnes. Colonnes : `hotel, contact, role, email, statut, date_premier_contact,
date_derniere_relance, notes`. Statuts possibles : `a_contacter`, `contacte`,
`relance`, `rdv_obtenu`, `signe`, `perdu`.

Quand l'utilisateur demande "où j'en suis" ou équivalent, lis le CSV et résume par
statut plutôt que de recracher toutes les lignes — ce qui compte c'est de voir vite
qui a besoin d'une relance.

## Étape 4 — Relances

Une relance reprend le même ton, jamais insistant. Base-toi sur
`assets/relance-template.md`. Une relance sans nouvelle depuis l'email initial se
fait généralement 5-7 jours ouvrés après — si `date_derniere_relance` ou
`date_premier_contact` montre un délai plus court, signale-le à l'utilisateur au
lieu d'envoyer une relance trop rapprochée qui sonnerait pressant.
