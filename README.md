# Fiche préopératoire NGAP Maroc

Application interactive mobile pour estimer le budget d’une intervention orthopédique ou traumatologique et distinguer les postes de dépense par acteur.

## Dans l’application

- Recherche NGAP avec autocomplétion dès la première lettre ; filtre par défaut « Orthopédie / traumatologie » et accès possible à toutes les rubriques du catalogue extrait du PDF.
- Trois types d’établissement : hôpital public/ESH, clinique privée à but lucratif, clinique à but non lucratif/œuvre sociale.
- Trois modes de soins : hospitalisation avec nuitées, ambulatoire sans nuitée, hôpital de jour.
- Deux modes de tarification : détail par poste ou forfait global confirmé.
- Estimation automatique poste par poste : honoraires chirurgien, anesthésiste, bloc, pharmacie/consommables, nuitées, implants/dispositifs et frais d’établissement sont préremplis à partir de la catégorie d’intervention. Une fourchette basse/haute et un scénario central sont affichés. Les montants restent modifiables si un devis local est disponible.
- Payeur : CNOPS, CNSS, FAR/régime militaire, assurance privée, patient direct ou autre organisme ; mode de règlement en tiers payant, avance puis remboursement, ou paiement intégral.
- Calcul indicatif de la part payeur, du reste patient et de la somme à régler le jour des soins ; historique local, sauvegarde JSON, export TXT et impression/PDF.
- Modèle local de tarifs d’établissement, pour éviter de ressaisir les mêmes frais.

## Règles de calcul et limites

Les honoraires et frais sont estimés automatiquement à partir d'un profil d'intervention et ventilés entre les postes du devis. Le coefficient NGAP et la valeur K/KC restent affichés comme référence, mais ne sont pas assimilés à un devis réel de clinique. La ventilation par poste est un modèle de budget, pas un barème réglementaire.

Les prix réels de bloc, de pharmacie, de nuitée, d’implants et d’établissement ne sont pas fournis par une grille nationale publique exhaustive comparable pour chaque acte et chaque établissement. L’application utilise donc des fourchettes de marché publiées pour certaines interventions (PTH, PTG, ligamentoplastie, arthroscopie) et des modèles indicatifs par catégorie pour les autres. Les parts par poste sont une décomposition estimative, pas des honoraires contractuels. En mode forfait global, les postes réputés inclus ne sont pas ajoutés une seconde fois ; ce mode ne doit être utilisé que si un forfait confirmé est disponible.

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


## Modèle d’estimation automatique — version octobre 2026

Le moteur classe l’acte NGAP sélectionné par code et libellé, puis applique un profil de prix et une ventilation poste par poste pour les catégories suivantes : prothèse totale de hanche, prothèse totale de genou, ligamentoplastie du LCA/LCP, suture méniscale, arthroscopie/gestes méniscaux, coiffe des rotateurs, canal carpien/chirurgie mineure de la main, ablation de matériel, chirurgie du rachis, fracture du fémur proximal, autres ostéosynthèses, chirurgie du pied/de la main et catégorie orthopédique générique.

Repères de marché intégrés :
- PTH : 30 000 à 110 000 DH (publication marocaine datée de septembre 2026).
- PTG : 45 000 à 80 000 DH (publication marocaine datée de septembre 2026).
- Ligamentoplastie du croisé : 15 000 à 30 000 DH.
- Arthroscopie/ménisque : 6 000 à 14 000 DH.
- La suture méniscale dispose aussi d’un repère publié en euros par un centre spécialisé, destiné à sa propre offre, pas à l’ensemble du marché.

Sources publiques consultées :
- CNOPS, règles de couverture et dispositifs médicaux : https://www.cnops.org.ma/fr/Reglementation_page
- Guide de prix PTH (septembre 2026) : https://journalsantemaroc.com/prix-soins/chirurgie/prix-prothese-hanche-maroc-2026.html
- Guide de prix chirurgie du genou (septembre 2026) : https://journalsantemaroc.com/prix-soins/chirurgie/prix-operation-genou-maroc-2026.html
- Centre orthopédique — tarifs indicatifs et prestations incluses : https://www.moroccoorthopaediccenter.com/tarifs

### Limites importantes

Les coefficients de comparaison de secteur (clinique privée = 100 %, non lucratif = 80 %, public = 45 %) sont des hypothèses internes de simulation pour comparer des scénarios, **pas des tarifs officiels ni des moyennes nationales vérifiées**. Dans le secteur public, le budget économique calculé n’est pas forcément la facture réglée par le patient. La fourchette est plus fiable pour les catégories disposant de prix publiés ; les autres profils restent à forte incertitude.

La base de remboursement/TNR est calculée par défaut comme **75 % du budget modélisé** uniquement pour permettre une simulation d’assurance sans saisie initiale. Ce n’est pas la TNR officielle propre à l’acte. Les taux CNOPS sont préproposés à titre de référence générale ; les valeurs CNSS sont des hypothèses à confirmer et les taux FAR/assurance/mutuelle sont illustratifs. Pour engager un patient ou facturer, comparer le résultat avec le devis détaillé, le tarif conventionnel de l’établissement et l’accord officiel du payeur.


Source de taux AMO : [ACAPS — indemnisation en AMO](https://www.acaps.ma/fr/grand-public/droits/indemnisation-en-amo). La CNSS indique un taux général de 70 % de la TNR, pouvant monter à 90 % pour certaines maladies graves/invalidantes prises en charge dans le public ; la CNOPS applique 90 % en privé et 100 % dans le public pour l’hospitalisation/chirurgie.

## Nouveau simulateur d’honoraires NGAP

Application mobile distincte : **https://orthoperipherie-bot.github.io/preop-ngap-maroc/simulateur-honoraires/**

- Recherche d’une intervention par libellé ou code ; coefficient principal prérempli depuis le catalogue NGAP.
- Ajout de plusieurs gestes associés avec code et coefficient importés automatiquement.
- Calcul live des honoraires chirurgicaux et anesthésiques au moyen des coefficients NGAP et de la valeur K/KC.
- Estimation d’un tarif global à partir des tranches de la grille forfaitaire de chirurgie publiée dans l’arrêté n°1961-06, puis ventilation du résiduel entre bloc et établissement.
- Simulation Payant / CNSS / CNOPS / FAR / assurance privée et Direct / PEC / Remboursement.

### Hypothèses du simulateur

- **Médecin libéral / secteur privé :** K/KC prérempli à **22,50 DH** selon la référence conventionnelle privée publiée en 2006. Le forfait chirurgical AMO privé est appliqué par tranches à partir de K30. Pour un coefficient inférieur à K30, le calcul est explicitement partiel : honoraires NGAP + frais de salle estimés ; l’application n’invente pas les frais d’hospitalisation, de clinique ou de pharmacie absents de cette grille.
- **Médecin du secteur public :** K/KC prérempli à **13 DH**, référence AMO pour les établissements publics (convention de 2007). En hospitalisation, le calcul du reste patient utilise le forfait AMO public par tranche de coefficient. **Ce barème d’établissement ne correspond pas à une facture d’honoraires individuelle ni au salaire d’un médecin fonctionnaire.** Les valeurs sont historiques et doivent être confirmées par l’hôpital et l’organisme gestionnaire.
- **Cumul des gestes :** conformément à l’article 9 B du NGAP fourni, l’acte de coefficient le plus élevé est coté à 100 %, le deuxième à 50 % et les suivants ne sont normalement pas cotés. Une option active l’exception à 75 % pour le deuxième acte dans les situations décrites dans le texte ; une autre permet le troisième acte à 50 % en cas de traumatismes multiples récents.
- **Honoraires chirurgien :** coefficient NGAP pondéré × valeur K/KC du secteur.
- **Anesthésie :** le coefficient secondaire est utilisé lorsqu’il est indiqué dans la NGAP. À défaut, l’article 22 prévoit K15 sans dépasser le coefficient de l’acte opératoire ; cette règle est utilisée et signalée.
- **Bloc opératoire :** 50 % de la cotation opératoire, selon l’article 23 du NGAP.
- **Part clinique/établissement :** solde du forfait global après honoraires et bloc. C’est une ventilation de travail, pas un tarif contractuel autonome. Si les postes détaillés dépassent le forfait, l’application signale que la ventilation de la clinique ne peut pas être déterminée par soustraction.
- **Couverture :** les valeurs de départ CNOPS/CNSS sont des hypothèses pour hospitalisation/chirurgie, modifiables. FAR et assurance privée n’ont pas de taux universel prérempli. Direct, PEC et remboursement changent le montant estimé à avancer, mais ne remplacent jamais l’accord du payeur.

Sources de référence : [NGAP marocaine, arrêté n°177-06](https://cnops.org.ma/sites/default/files/2022-10/Nomeclature_0.pdf) ; [grille privée de chirurgie, arrêté n°1961-06](https://www.sante.gov.ma/Reglementation/ASSURANCEMALADIE/1961-06.pdf) ; [grille n°1 AMO publique, convention de mai 2007 — K = 13 DH](https://anam.ma/anam/wp-content/uploads/2021/09/Grille1_2007.pdf) ; [grille forfaitaire publique de chirurgie — convention AMO de mai 2007](https://anam.ma/anam/wp-content/uploads/2021/09/Grille2_2007.pdf).

### Module « Implants & TNR » — révision du 10 octobre 2026

Le catalogue du simulateur comprend **252 références d’implants et dispositifs** : **71 lignes KE** portant une valeur historique issue du barème n°2314-08 (2008), et **181 références** pour lesquelles aucun TNR actuel n’est vérifié dans cette base. Les lignes KE sont explicitement marquées comme historiques ; la valeur doit être confirmée dans le service TNR actuel de l’organisme payeur avant d’en déduire un remboursement. Les codes KE ajoutés et la correction de catégories améliorent la couverture des plaques, du coude, des ciments et de certains dispositifs rachidiens.

Les prix d’achat sont désormais séparés du TNR :
- Les deux seuls repères de prix automatiquement préremplis sont les fourchettes publiques marocaines publiées pour **un set complet de PTH (15 000–25 000 DH)** et **un set complet de PTG (12 000–22 000 DH)**. La valeur centrale affichée est une hypothèse de travail, pas un devis ni un prix officiel.
- Pour chaque autre composant, plaque, vis, clou, ancre, kit sportif, implant rachidien ou prothèse de reprise, le prix d’achat reste vide tant qu’aucun prix fiable spécifique n’a été vérifié. Saisir le montant TTC sur un devis récent du distributeur.
- Un taux de couverture propre aux implants est séparé du taux des actes. Pour la CNOPS, il est prérempli à **100 % de la base remboursable du dispositif** : prix d’achat si inférieur au TNR, sinon TNR réglementaire. Pour CNSS, FAR et assurance privée, le taux reste vide à renseigner selon le régime, la convention et le contrat. Un TNR absent ou un taux non renseigné rend le reste patient « à confirmer » au lieu d’inventer la couverture.
- Le total principal demeure le reste à charge estimé du patient pour l’acte. Le total combiné additionne le reste de l’acte et le reste estimé des implants sélectionnés ; lorsque le prix ou la prise en charge d’un dispositif est inconnu, le résultat combiné est signalé « à confirmer ».

**Limites réglementaires :** la page CNOPS renvoie aux arrêtés n°2314-08, n°2315-08 et à la modification n°3207-15. Certains dispositifs nécessitent un accord préalable. Le TNR historique de 2008 n’est pas présenté comme automatiquement en vigueur en 2026. Les prix de kits complets PTH/PTG viennent d’un guide public de prix marocain daté du 8 mai 2026 ; il ne fournit pas des prix unitaires par référence fournisseur. Voir les liens sources dans le simulateur et confirmer le devis, l’éligibilité, le TNR et l’accord auprès du payeur.


## Catalogue spécialisé NGAP (octobre 2026)

Le simulateur mobile charge `orthopedie-actes.json`, un catalogue spécialisé de **354 entrées** construit à partir du PDF NGAP transmis : 335 références codées NGAP (A100–A158, A200–A216, A300–A308, A400 ; C113–C139, C200–C218, C300–C314, C400–C442, C605–C610 et C614–C615 ; rachis orthopédique F100–F101, F110–F112 et F118–F143 ; G100–G118 et G120–G152 ; N100–N117, N126–N128 et N200–N232) et 6 entrées d’assimilation/appareillage. Les codes A129 et A150 sont conservés comme rubriques sans coefficient autonome, avec renvoi aux sous-codes. Les règles spécifiques A153/A154/A155/A211/A215/A216 et les suppléments rachidiens sont identifiés comme tels. Les codes non pertinents pour la pratique orthopédique courante (p. ex. ganglions du trijumeau, varices et soins cutanés veineux) sont exclus. Les actes intraduraux/intramédullaires, malformations crânio-cervicales et myéloméningocèles relevant principalement de la neurochirurgie ont été écartés du sélecteur orthopédique.

### Secteur et calcul automatique

- **Privé :** K/KC prérempli à 22,50 DH d’après l’arrêté n°1961-06 (2006). Les forfaits privés publiés par tranche de coefficient sont utilisés à partir de K30. Pour K inférieur à K30, le total est partiel (honoraires NGAP + bloc estimé) et les frais d’établissement non chiffrés ne sont pas inclus.
- **Public :** K prérempli à 13 DH selon la grille n°1 de la convention nationale AMO des établissements publics (mai 2007). Le total utilise les forfaits publics de cette convention par tranche de coefficient, mais leur application actuelle doit être confirmée auprès de l’établissement.
- **Cumul :** le défaut suit l’article 9 B de la NGAP : coefficient le plus élevé à 100 %, deuxième acte à 50 %, suivants non cotés ; des options permettent d’utiliser les exceptions de 75 % et du troisième acte à 50 % dans les situations décrites par le texte.
- **Anesthésie :** le coefficient secondaire du catalogue est utilisé lorsqu’il figure dans l’acte ; à défaut, K15 est retenu sans dépasser le coefficient opératoire, conformément à l’article 22.
- **Bloc opératoire :** 50 % du coefficient opératoire pondéré, conformément à l’article 23.
- **Ventilation :** la part clinique/établissement est un solde estimé du total global après honoraires et bloc ; elle ne constitue pas un honoraire autonome garanti.

Sources utilisées : NGAP marocaine fournie (arrêté n°177-06) ; grille forfaitaire privée de l’arrêté n°1961-06 (2006) ; convention nationale AMO des établissements publics (mai 2007). Ces références sont datées et ne garantissent pas qu’un établissement ou un payeur les applique encore sans avenant. Le forfait AMO est un forfait de référence, pas nécessairement le montant final réclamé au patient.


### Contrôle des actes de regroupement

Les codes A129 et A150 sont conservés comme rubriques informatives non cotables en tant qu’actes autonomes : A129 renvoie vers A130/A131 selon le caractère unifragmentaire ou multifragmentaire ; A150 renvoie vers A151/A152 selon le nombre de piliers cotyloïdiens et les voies d’abord. Le moteur ne leur affecte donc pas de coefficient indépendant.

Le catalogue spécialisé a été contrôlé par code et catégorie sur la base du PDF fourni : les rubriques A129/A150 sans coefficient autonome sont signalées comme règles, et le coefficient A306 est K40 selon le document. Les catégories des actes sont normalisées afin de faciliter la recherche quotidienne.
