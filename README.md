Ce script Python vise à vérifier la disponibilité des URL spécifiées dans un fichier d'entrée et à les classer par pays en fonction de l'adresse IP extraite de chaque URL. Il utilise la bibliothèque `fake-useragent` pour générer des user agents aléatoires afin de tester la connectivité des URL sur différents ports.

## Description

Ce projet Python comprend un script permettant de vérifier la disponibilité des URL extraites d'un fichier et de les classer dans des dossiers par pays en utilisant les adresses IP correspondantes. L'outil utilise la base de données GeoIP `GeoLite2-Country.mmdb` pour obtenir les informations de pays à partir des adresses IP.

## Fonctionnement

1. **Dépendances**

   - Python 3.x
   - Fichier de sortie du script "[CamScan](https://gist.github.com/achillean/a45351496736ef389b9f)" de Achillean
   - Bibliothèques Python :
     - `geoip2`
     - `fake-useragent`

2. **Utilisation**

   - Téléchargez le script Python.
   - Assurez-vous de disposer du fichier `GeoLite2-Country.mmdb` pour la base de données GeoIP.
   - Exécutez le script en spécifiant les chemins des fichiers d'entrée et de sortie, ainsi que les options de tri.

3. **Paramètres**

   - `input_file_path`: Chemin vers le fichier contenant les URLs à vérifier.
   - `output_folder_path`: Chemin du dossier de sortie pour la classification par pays.
   - `sort_unique_addresses`: Si `True`, les URLs uniques seront triées.
   - `sort_by_country`: Si `True`, les URLs seront classées dans des dossiers selon leur pays. Si `False`, toutes les URLs seront stockées dans un seul dossier.

4. **Notes**

   - Si `sort_by_country` est défini sur `False`, toutes les URLs seront stockées dans le dossier de sortie spécifié par `output_folder_path` sans être classées dans des sous-dossiers par pays.
   - Le script continuera à vérifier la disponibilité des URLs sur les ports 80 (HTTP) et 443 (HTTPS) en utilisant des agents utilisateurs aléatoires.
   - Ce projet est uniquement destiné à des fins éducatives.

## Optimisations

- Implémentation du Tor : Pour améliorer la confidentialité et l'anonymat lors des requêtes, une option d'implémentation du réseau Tor serait à mettre en place.

## Avertissement Éthique

- Assurez-vous d'utiliser cet outil de manière responsable et éthique.
