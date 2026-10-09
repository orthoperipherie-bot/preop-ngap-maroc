# Fiche préopératoire NGAP Maroc

Application web interactive pour iPhone : recherche d'actes NGAP, estimation des honoraires, implants, hospitalisation, frais de clinique, répartition et historique local.

## Déploiement GitHub Pages

Le workflow GitHub Actions `.github/workflows/deploy.yml` reconstruit le catalogue depuis le PDF NGAP publié par la CNOPS et publie l'application dans GitHub Pages. Le fichier généré `acts.json` est également versionné à la racine pour que la recherche reste disponible si GitHub Pages utilise le mode de publication depuis la branche.

Les libellés et coefficients sont extraits automatiquement du PDF source et doivent être vérifiés dans la nomenclature applicable avant toute facturation. Les calculs sont des simulations, pas une validation réglementaire.

## Utilisation sur iPhone

Ouvre le site publié dans Safari, puis **Partager → Sur l’écran d’accueil**. Après le premier chargement, l'application peut fonctionner hors connexion grâce au service worker. Les fiches restent dans le stockage local du navigateur ; exporte régulièrement une sauvegarde.

Source NGAP : https://cnops.org.ma/sites/default/files/2022-10/Nomeclature_0.pdf
