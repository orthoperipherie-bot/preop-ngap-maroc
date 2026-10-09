# Fiche préopératoire NGAP Maroc

Application web interactive pour iPhone : recherche d'actes NGAP, estimation des honoraires, implants, hospitalisation, frais de clinique, répartition et historique local.

## Déploiement GitHub Pages

Le workflow GitHub Actions `.github/workflows/deploy.yml` reconstruit le catalogue depuis le PDF NGAP publié par la CNOPS et publie l'application dans GitHub Pages. Le fichier généré `acts.json` est également versionné à la racine pour que la recherche reste disponible si GitHub Pages utilise le mode de publication depuis la branche.

Le moteur de recherche associe notamment « canal carpien » au code présent dans le catalogue (`C609`) et « PTH » aux références de prothèse de hanche.

Les libellés et coefficients sont extraits automatiquement du PDF source et doivent être vérifiés dans la nomenclature applicable avant toute facturation. Les calculs sont des simulations, pas une validation réglementaire.

## Tarification et automatisations

La sélection d’un acte propose les champs déductibles de la nomenclature, une durée indicative modifiable et une ligne d’implant/consommable à préciser. En mode clinique privée, les coûts locaux peuvent être mémorisés comme modèle sur l’appareil. En mode hôpital public/ESH, l’app utilise une grille indicative de forfaits selon le coefficient, lorsqu’une valeur est disponible, et ne recompte pas le séjour, l’anesthésie, le bloc et la pharmacie séparément. Les forfaits publics sont des estimations à confirmer auprès de l’établissement et du payeur ; pour les actes hors grille, saisir le montant confirmé. Références : [CNOPS](https://www.cnops.org.ma/fr/Reglementation_page) et [Ministère de la Santé](https://www.sante.gov.ma/Reglementation/Pages/TARIFICATION.aspx).

## Utilisation sur iPhone

Ouvre le site publié dans Safari, puis **Partager → Sur l’écran d’accueil**. Après le premier chargement, l'application peut fonctionner hors connexion grâce au service worker. Les fiches restent dans le stockage local du navigateur ; exporte régulièrement une sauvegarde.

Source NGAP : https://cnops.org.ma/sites/default/files/2022-10/Nomeclature_0.pdf
