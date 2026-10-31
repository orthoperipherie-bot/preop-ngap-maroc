# Pharmacie de garde Maroc

Application web mobile installable (PWA), publiée dans un sous-dossier du site GitHub Pages du dépôt.

## Utilisation
- Rechercher une ville ou un quartier au Maroc.
- Utiliser le GPS après autorisation.
- Afficher les pharmacies OpenStreetMap autour du point choisi.
- Consulter les pages de garde Garde24 disponibles pour Salé, Rabat et Témara.
- Ouvrir l'appel téléphonique ou l'itinéraire lorsque les données sont disponibles.

## Distinction essentielle
La carte localise les pharmacies répertoriées dans OpenStreetMap. Elle ne confirme **pas** leur statut de garde. Pour consulter les pharmacies de garde, l'application ouvre le planning externe de Garde24 lorsqu'une page ville connue est disponible. Pour les autres villes, elle ouvre la page d'accueil du service. Toujours téléphoner avant de se déplacer.

## Déploiement
Le workflow principal copie ce dossier vers le répertoire publié de GitHub Pages. Adresse attendue :
https://orthoperipherie-bot.github.io/preop-ngap-maroc/pharmacie-garde-maroc/

## Confidentialité
La localisation GPS n'est demandée qu'après action de l'utilisateur. Les coordonnées servent à interroger OpenStreetMap/Overpass et ne sont pas enregistrées par cette application.
