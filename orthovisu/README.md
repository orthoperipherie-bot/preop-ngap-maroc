# OrthoVisu — Atlas visuel orthopédique

Application web mobile conçue comme un **visualiseur d'images** pendant la consultation : sélection par région/pathologie, affichage plein écran, navigation entre vues, vignettes, zoom, balayage tactile et accès discret aux crédits.

## Contenu actuel

12 entrées : gonarthrose, rupture du LCA, lésion méniscale, rupture de la coiffe des rotateurs, coxarthrose, hernie discale lombaire, fracture du radius distal, hallux valgus, scoliose, canal carpien, entorse latérale de cheville et fracture bi-/trimalléolaire.

Les médias sont un ensemble de planches anatomiques, illustrations médicales, photographies et radiographies provenant de Wikimedia Commons. Le contenu disponible varie selon la pathologie : certaines fiches n'ont pour l'instant qu'une seule image. Les visuels sont affichés sans modification et leur page de source, l'auteur et la licence sont accessibles depuis le bouton « Sources & licences » dans l'application.

## Crédits iconographiques et licences

Pour chaque fichier, la page Commons liée depuis l'application constitue la notice d'attribution de référence. Les médias sont affichés sans modification.

| Fichier | Auteur / ayant droit crédité | Licence indiquée |
|---|---|---|
| [Healthy knee joint.svg](https://commons.wikimedia.org/wiki/File:Healthy_knee_joint.svg) | InjuryMap | CC BY-SA 4.0 |
| [Knee anatomy.svg](https://commons.wikimedia.org/wiki/File:Knee_anatomy.svg) | InjuryMap | CC BY-SA 4.0 |
| [Knee Osteoarthritis.svg](https://commons.wikimedia.org/wiki/File:Knee_Osteoarthritis.svg) | InjuryMap | CC BY-SA 4.0 |
| [Knee injuries.svg](https://commons.wikimedia.org/wiki/File:Knee_injuries.svg) | InjuryMap | CC BY-SA 4.0 |
| [Anterior Cruciate Ligament Tear.jpg](https://commons.wikimedia.org/wiki/File:Anterior_Cruciate_Ligament_Tear.jpg) | BruceBlaus | CC BY-SA 4.0 |
| [Rotator cuff injury.svg](https://commons.wikimedia.org/wiki/File:Rotator_cuff_injury.svg) | InjuryMap | CC BY-SA 4.0 |
| [Hip anatomy.svg](https://commons.wikimedia.org/wiki/File:Hip_anatomy.svg) | InjuryMap | CC BY-SA 4.0 |
| [Hip osteoarthritis.svg](https://commons.wikimedia.org/wiki/File:Hip_osteoarthritis.svg) | InjuryMap | CC BY-SA 4.0 |
| [Healthy spine.svg](https://commons.wikimedia.org/wiki/File:Healthy_spine.svg) | InjuryMap | CC BY-SA 4.0 |
| [Herniated disk.svg](https://commons.wikimedia.org/wiki/File:Herniated_disk.svg) | InjuryMap | CC BY-SA 4.0 |
| [Degenerated disk.svg](https://commons.wikimedia.org/wiki/File:Degenerated_disk.svg) | InjuryMap | CC BY-SA 4.0 |
| [Distalradiusfracture.jpg](https://commons.wikimedia.org/wiki/File:Distalradiusfracture.jpg) | Curtishand (photographie : Dr Keith Segalman, Curtis National Hand Center) | Domaine public (voir la notice Commons) |
| [Pins across a distal radius fracture.jpg](https://commons.wikimedia.org/wiki/File:Pins_across_a_distal_radius_fracture.jpg) | Curtishand | Domaine public (voir la notice Commons) |
| [Halluxvalgus.jpg](https://commons.wikimedia.org/wiki/File:Halluxvalgus.jpg) | 2braqu | CC BY-SA 4.0 |
| [Blausen 0785 Scoliosis 01.png](https://commons.wikimedia.org/wiki/File:Blausen_0785_Scoliosis_01.png) | BruceBlaus / Blausen Medical | CC BY 3.0 |
| [Carpal Tunnel Syndrome.jpg](https://commons.wikimedia.org/wiki/File:Carpal_Tunnel_Syndrome.jpg) | Manu5 / Top Medical Animation Studio | CC BY-SA 4.0 |
| [Ankle pain.svg](https://commons.wikimedia.org/wiki/File:Ankle_pain.svg) | InjuryMap | CC BY-SA 4.0 |
| [X-ray of bimalleolar fracture.jpg](https://commons.wikimedia.org/wiki/File:X-ray_of_bimalleolar_fracture.jpg) | Nazzar Tellisi, I. S. Abdulkareem, P. G. Giannoudis | CC BY 4.0 |
| [Trimalleolar Ankle Fracture.jpg](https://commons.wikimedia.org/wiki/File:Trimalleolar_Ankle_Fracture.jpg) | Chaim Mintz | CC BY-SA 4.0 |

### Règles de réutilisation

- Les licences Creative Commons BY imposent notamment de créditer l'auteur, de référencer la source et de fournir un lien vers la licence.
- Les licences BY-SA ajoutent une obligation de partage dans les mêmes conditions lorsqu'une adaptation de l'œuvre est diffusée.
- Les deux images signalées « Domaine public » sont accompagnées de leur notice Commons ; aucune licence CC0 distincte n'est revendiquée ici.
- Vérifier la notice Commons de chaque fichier avant toute redistribution séparée, modification, impression commerciale ou nouvelle publication. En cas de mise à jour de la licence ou du fichier source, actualiser les crédits de l'application.

## Fonctionnement et limites

- Les fichiers images sont chargés directement depuis Wikimedia Commons : une connexion internet est nécessaire pour afficher les images.
- Le service worker met en cache l'interface de l'application, pas les images distantes.
- Les images sont des illustrations et exemples iconographiques généraux ; elles ne représentent pas le patient présent et ne remplacent pas ses radiographies ou examens.
- Le contenu actuel est une première sélection visuelle et ne prétend pas couvrir toutes les pathologies ni offrir des modèles 3D manipulables.
- Aucune donnée de patient n'est demandée ni enregistrée. L'application n'est ni un dispositif médical ni une aide au diagnostic.

## Installation sur iPhone

Ouvrir l'adresse de l'application dans Safari, toucher **Partager**, puis **Sur l'écran d'accueil**.
