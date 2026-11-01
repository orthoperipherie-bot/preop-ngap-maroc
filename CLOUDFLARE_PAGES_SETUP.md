# Migration Cloudflare Pages et protection Access

## Déploiement du dépôt

Le dépôt contient plusieurs applications statiques. Le script `scripts/build-cloudflare-pages.sh` les rassemble dans `dist/`.

Dans Cloudflare :

1. Ouvrir **Workers & Pages** puis **Create application > Pages > Connect to Git**.
2. Connecter GitHub et sélectionner `orthoperipherie-bot/preop-ngap-maroc`.
3. Branche de production : `main`.
4. Framework preset : **None**.
5. Build command : `bash scripts/build-cloudflare-pages.sh`.
6. Build output directory : `dist`.
7. Lancer **Save and Deploy**.

Cloudflare Pages prendra ensuite en charge les déploiements du dépôt à chaque mise à jour Git.

## Protection obligatoire avec Cloudflare Access

Le simple fait de déployer sur Cloudflare Pages ne rend pas les applications privées.

Après le premier déploiement :

1. Dans le projet Pages, ouvrir **Settings > General** et activer **Enable access policy** pour les déploiements de prévisualisation.
2. Dans **Zero Trust > Access > Applications**, ouvrir l'application Access créée pour le projet Pages, puis **Configure**.
3. Pour protéger également le domaine de production `<nom-du-projet>.pages.dev`, suivre la procédure Cloudflare « Enable Access on your *.pages.dev domain » : dans **Public hostname**, remplacer le sous-domaine générique `*` par le nom du projet, puis enregistrer. Revenir dans le projet Pages et réactiver l'option de protection des déploiements de prévisualisation si nécessaire.
4. Vérifier que la politique comporte uniquement une règle **Allow** pour l'adresse e-mail du propriétaire (par exemple avec le fournisseur **One-time PIN**). Ne pas ajouter de règle générale autorisant tout le monde.
5. Si un domaine personnalisé est ajouté, créer aussi une application Access distincte pour ce nom d'hôte.

## Éviter le contournement par l'ancien hébergement

Le site actuel est aussi publié sur GitHub Pages. Tant que cette adresse fonctionne, elle peut contourner la protection Cloudflare. Après vérification que Cloudflare Access protège bien le site de production, désactiver GitHub Pages dans **GitHub > Settings > Pages**. Tester ensuite les anciennes URL `github.io` : elles ne doivent plus servir les applications.

## Limite importante : confidentialité du code source

Le dépôt GitHub est actuellement **public**. Cloudflare Access peut protéger l'accès aux applications hébergées, mais ne rend pas le code source GitHub privé. Pour rendre aussi le code source inaccessible au public, il faut changer la visibilité du dépôt en privé et vérifier que le plan GitHub utilisé autorise le mode de déploiement souhaité.

## Applications incluses

- `/` : catalogue NGAP
- `/simulateur-honoraires/`
- `/orthoos-ebot/`
- `/orthoscores/`
- `/suivi-patients/`
- `/ortho-clair/`
- `/orthovisu/`
- `/pharmacie-garde-maroc/`
- `/ortho-suite/` : portail réunissant les applications

Référence officielle : [Cloudflare Pages — Git integration](https://developers.cloudflare.com/pages/configuration/git-integration/) · [Cloudflare Pages — Known issues / Access sur pages.dev](https://developers.cloudflare.com/pages/platform/known-issues/) · [Cloudflare Access — Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/).