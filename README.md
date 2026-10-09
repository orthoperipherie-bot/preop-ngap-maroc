# Fiche préopératoire NGAP Maroc

Application interactive mobile pour estimer le budget d’une intervention orthopédique ou traumatologique et distinguer les postes de dépense par acteur.

## Dans l’application

- Recherche NGAP avec autocomplétion dès la première lettre ; filtre par défaut « Orthopédie / traumatologie » et accès possible à toutes les rubriques du catalogue extrait du PDF.
- Trois types d’établissement : hôpital public/ESH, clinique privée à but lucratif, clinique à but non lucratif/œuvre sociale.
- Trois modes de soins : hospitalisation avec nuitées, ambulatoire sans nuitée, hôpital de jour.
- Deux modes de tarification : détail par poste ou forfait global confirmé.
- Devis détaillé : honoraires chirurgien, estimation des honoraires d’anesthésie à partir du coefficient associé lorsqu’il est disponible et à vérifier, bloc, pharmacie/consommables, nuitées, implants/dispositifs, frais d’établissement et autres frais.
- Payeur : CNOPS, CNSS, FAR/régime militaire, assurance privée, patient direct ou autre organisme ; mode de règlement en tiers payant, avance puis remboursement, ou paiement intégral.
- Calcul indicatif de la part payeur, du reste patient et de la somme à régler le jour des soins ; historique local, sauvegarde JSON, export TXT et impression/PDF.
- Modèle local de tarifs d’établissement, pour éviter de ressaisir les mêmes frais.

## Règles de calcul et limites

Le montant indicatif des honoraires chirurgicaux est calculé par **coefficient NGAP × valeur K/KC saisie** (valeur initiale 22,50 DH, modifiable). Si le libellé extrait du PDF est signalé « à vérifier », le calcul automatique des honoraires est désactivé pour cet acte. Le second coefficient n’est considéré que comme une estimation possible d’anesthésie et doit être vérifié acte par acte.

La NGAP ne suffit pas à déterminer le prix de la nuitée, les tarifs de bloc, les prix d’implants, les frais de pharmacie, la convention propre à une clinique ou le forfait global d’un établissement : ces montants doivent être saisis depuis un devis ou un barème confirmé. Aucun forfait hospitalier n’est inféré automatiquement à partir du seul coefficient. En mode forfait global, les postes inclus ne sont pas ajoutés une seconde fois ; seuls les implants et autres frais explicitement hors forfait sont ajoutés.

Taux préproposés, **à vérifier avant toute décision** :
- **CNOPS** : valeurs indicatives publiées de 80 % de la TNR pour certains actes ambulatoires, 90 % pour l’hospitalisation/chirurgie dans le secteur privé et 100 % dans le secteur public/militaire. Les forfaits de dispositifs médicaux/implants, exclusions, plafonds et conditions d’accord peuvent modifier le calcul.
- **CNSS** : 70 % est utilisé comme hypothèse initiale de référence ; le cas d’une ALD reconnue en établissement public peut déclencher une suggestion à 90 % dans cette application. Vérifie le taux applicable et les dispositions en vigueur dans le dossier concerné.
- **FAR, assurance privée, mutuelle ou autre organisme** : aucun taux n’est présumé ; il faut saisir le taux et la base éligible confirmés.
- **Établissement à but non lucratif** : le statut non lucratif ne signifie pas automatiquement secteur public. Vérifie sa classification, sa convention et la réponse de l’organisme payeur.

La base remboursable globale/TNR et le taux restent modifiables. Le montant « part payeur » est une simulation mathématique, non une promesse de remboursement ni une décision de prise en charge. Les données saisies restent dans le stockage local du navigateur ; ne stocke pas de données identifiantes inutilement et exporte une sauvegarde si nécessaire.

## Références

- [PDF NGAP — nomenclature générale des actes professionnels](https://data.gov.ma/data/fr/dataset/b8425cb6-828f-4fa9-9f02-cdd372d18f65/resource/f66d23ac-012f-4439-ac99-4beb129ce640/download/ngap-cnops-2014.pdf)
- [CNOPS — taux et prestations](https://www.cnops.org.ma/fr/infopratiqueps)
- [ANAM — rapport annuel AMO 2019, hypothèses réglementaires CNSS/CNOPS](https://anam.ma/anam/wp-content/uploads/2023/03/02072021-RAG_2019-DEEA.pdf)

Le catalogue texte contient des extractions automatiques du PDF ; certains libellés ou coefficients nécessitent une vérification dans la page source. Cette application est un outil de préparation de devis, pas un logiciel de facturation certifié.

## Utilisation sur iPhone

Ouvre le site publié dans Safari, puis **Partager → Sur l’écran d’accueil**. Le service worker tente de mettre en cache les fichiers de l’application après le premier chargement ; conserve une connexion disponible pour la première ouverture et exporte périodiquement les fiches que tu souhaites garder.
