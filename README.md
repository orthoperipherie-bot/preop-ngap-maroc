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


## Nouveau simulateur d’honoraires NGAP

Application mobile distincte : **https://orthoperipherie-bot.github.io/preop-ngap-maroc/simulateur-honoraires/**

- Recherche d’une intervention par libellé ou code ; coefficient principal prérempli depuis le catalogue NGAP.
- Ajout de plusieurs gestes associés avec code et coefficient importés automatiquement.
- Calcul live des honoraires chirurgicaux et anesthésiques au moyen des coefficients NGAP et de la valeur K/KC.
- Estimation d’un tarif global à partir des tranches de la grille forfaitaire de chirurgie publiée dans l’arrêté n°1961-06, puis ventilation du résiduel entre bloc et établissement.
- Simulation Payant / CNSS / CNOPS / FAR / assurance privée et Direct / PEC / Remboursement.

### Hypothèses du simulateur

La grille forfaitaire de chirurgie consultée provient de l’arrêté n°1961-06 publié en 2006 ; elle constitue une référence publiée à vérifier au regard des conventions et TNR effectivement appliquées en pratique. Pour les coefficients inférieurs à K30, qui ne figurent pas dans cette grille, le total est une estimation technique et non un forfait réglementaire.

Le coefficient d’anesthésie lorsqu’il est indiqué dans la ligne NGAP est utilisé tel quel, multiplié par la même pondération appliquée à l’acte associé. En l’absence de coefficient anesthésique, le simulateur estime ce coefficient à 50 % du coefficient chirurgical correspondant ; cette approximation est signalée. Le partage du reliquat entre bloc opératoire (20 % par défaut, modifiable) et part clinique (solde) est une hypothèse de ventilation, car la grille consultée indique les éléments inclus dans le forfait mais ne publie pas une décomposition chiffrée bloc/clinique.

Taux de couverture initialement suggérés pour faciliter le calcul : Payant 0 %, CNOPS 90 %, CNSS 70 %, FAR 90 %, assurance privée 80 %. Seul le repère CNOPS de 90 % en chirurgie privée s’appuie sur les indications publiées par la CNOPS ; les autres taux sont des hypothèses de simulation, modifiables. Pour une PEC ou un remboursement réels, il faut remplacer ces hypothèses par les droits, la TNR et la décision du payeur.

Sources : NGAP marocaine, arrêté n°177-06 : https://cnops.org.ma/sites/default/files/2022-10/Nomeclature_0.pdf ; grille forfaitaire, arrêté n°1961-06 : https://www.sante.gov.ma/Reglementation/ASSURANCEMALADIE/1961-06.pdf ; CNOPS — hospitalisation et chirurgie : https://www.cnops.org.ma/fr/hospitalisation-et-chirurgie.

### Module « Implants & TNR » ajouté en octobre 2026

Le simulateur inclut un sous-module de 44 lignes TNR historiques d’implants et dispositifs orthopédiques extraites du barème officiel n°2314-08 (2008) : composants de prothèses de hanche/genou/épaule, fixateurs, plaques, vis, clous et broches. Pour chaque ligne, l’outil distingue le TNR historique, le prix d’achat fournisseur (facultatif), la base de remboursement estimée plafonnée au TNR et le statut « facturé en sus du forfait opératoire ». Le coût d’implant n’est ajouté au total de l’intervention que si la case « En sus » est cochée, afin d’éviter le double comptage.

**Avertissement de mise à jour :** l’arrêté n°3207-15 a remplacé certains tarifs de la classe III. Les valeurs orthopédiques importées sont donc affichées avec leur source et leur date, et doivent être confirmées à partir du barème applicable / accord du payeur avant de les considérer comme les TNR actuels. La CNOPS indique qu’un accord préalable peut être nécessaire et que la base de remboursement d’un dispositif est plafonnée au forfait réglementaire ou au prix d’achat s’il est inférieur. Les taux d’implants CNOPS (100 %) et CNSS/AMO (70 %) sont préproposés comme simulation à confirmer selon l’éligibilité du dispositif et le dossier. 


## Catalogue spécialisé NGAP (octobre 2026)

Le simulateur mobile charge désormais `orthopedie-actes.json`, un catalogue spécialisé de **338 entrées** construit à partir du PDF NGAP transmis dans la conversation : codes traumatologiques A, actes reconstructeurs et de parties molles utiles au membre C113–C139, muscles/tendons C200–C218, os C300–C314, articulations/prothèses C400–C442, gestes vasculaires des principaux vaisseaux des membres (C534/C537/C539/C542), nerfs périphériques sélectionnés (C605–C610/C614/C615), gestes rachidiens orthopédiques sélectionnés (F100/F101/F110–F112/F114/F115/F118–F141/F143), membre supérieur G, membre inférieur N et assimilations dédiées. Les actes sans rapport avec la pratique orthopédique (ex. varices, infiltrations de nerfs crâniens, certaines interventions intramédullaires neurochirurgicales) sont écartés. Le simulateur ne charge plus la nomenclature complète toutes spécialités pour les recherches.

### Secteur et calcul automatique

- **Privé :** K/KC prérempli à 22,50 DH d’après l’arrêté n°1961-06. Les forfaits publiés par tranche de coefficient sont utilisés à partir de K30. Pour K inférieur à K30, l’application affiche une interpolation et la signale comme indicative.
- **Public :** K/KC prérempli à 7,50 DH selon l’arrêté conjoint n°10-04 (2004). Le forfait public global n’étant pas directement déductible du seul code NGAP, le total public est une estimation comparative calculée au prorata 7,50/22,50 du forfait de référence privé. Il est explicitement étiqueté non officiel et doit être remplacé par le tarif de l’établissement lorsqu’il est connu.
- **Cumul :** le défaut suit l’article 9 B de la NGAP : coefficient le plus élevé à 100 %, deuxième acte à 50 %, suivants non cotés ; des options permettent d’utiliser les exceptions de 75 % et du troisième acte à 50 % dans les situations décrites par le texte.
- **Anesthésie :** le coefficient secondaire du catalogue est utilisé lorsqu’il figure dans l’acte ; à défaut, K15 est retenu sans dépasser le coefficient opératoire, conformément à l’article 22.
- **Bloc opératoire :** 50 % du coefficient opératoire pondéré, conformément à l’article 23.
- **Ventilation :** la part clinique/établissement est un solde estimé du total global après honoraires et bloc ; elle ne constitue pas un honoraire autonome garanti.

Sources officielles utilisées : NGAP fournie (arrêté n°177-06), forfaits et valeur K/KC du privé dans l’arrêté n°1961-06, et valeur K/KC du public dans l’arrêté conjoint n°10-04. Le mode public reste une estimation comparative, pas une grille de forfait public complète.


### Contrôle des actes de regroupement

Les codes A129 et A150 sont conservés comme rubriques informatives non cotables en tant qu’actes autonomes : A129 renvoie vers A130/A131 selon le caractère unifragmentaire ou multifragmentaire ; A150 renvoie vers A151/A152 selon le nombre de piliers cotyloïdiens et les voies d’abord. Le moteur ne leur affecte donc pas de coefficient indépendant.
