[![Tests Status](https://github.com/Nathom78/Python-OC-Lettings-FR/blob/badges/master/reports/tests-badge.svg?raw=true)](http://htmlpreview.github.io/?https://github.com/Nathom78/Python-OC-Lettings-FR/blob/badges/master/reports/junit/index.html)
[![Coverage Status](https://github.com/Nathom78/Python-OC-Lettings-FR/blob/badges/master/reports/coverage-badge.svg?raw=true)](http://htmlpreview.github.io/?https://github.com/Nathom78/Python-OC-Lettings-FR/blob/badges/master/reports/coverage/index.html)
[![Flake8 Status](https://github.com/Nathom78/Python-OC-Lettings-FR/blob/badges/master/reports/flake8-badge.svg?raw=true)](http://htmlpreview.github.io/?https://github.com/Nathom78/Python-OC-Lettings-FR/blob/badges/master/reports/flake8/index.html)
[![Build and deploy container app to Azure Web App - Orange-County-Lettings](https://github.com/Nathom78/Python-OC-Lettings-FR/actions/workflows/master_ORANGE_COUNTY_LETTINGS.yml/badge.svg)](https://github.com/Nathom78/Python-OC-Lettings-FR/actions/workflows/master_ORANGE_COUNTY_LETTINGS.yml)

Documentation avec readthedocs:

[![Documentation Status](https://readthedocs.org/projects/thomas-python-oc-lettings-fr/badge/?version=latest)](https://thomas-python-oc-lettings-fr.readthedocs.io/fr/latest/?badge=latest)

[**Projet 13** du parcours OpenClassrooms Développeur d'application - Python](https://openclassrooms.com/fr/paths/518/projects/841/assignment)

# *Résumé*

Orange County Lettings est une start-up dans le secteur de la location de biens immobiliers.
La start-up est en pleine phase d’expansion aux États-Unis. 

L'objectif de ce projet est :
- de mettre à l'échelle une application Django en utilisant une architecture modulaire.
- La réduction de divers problèmes technique. Et du coup une mise en place de test, voir de les automatiser est organisé.
- Surveillance de l'application et suivi des erreurs via Sentry.
- Mettre en place un pipeline CI/CD et le déploiement du site web vers un hébergeur.(Azure de choisi).
- Ainsi qu'une documentation publiée en ligne sur le site readthedocs.io.

Plusieurs domaines du site *OC Lettings* ont été améliorés à partir du projet d'OpenClassrooms forker et cloner depuis l'adresse suivante :
[Python-OC-Lettings-FR](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR).

Avec le
[Cahier des charges site 2.0](https://s3.eu-west-1.amazonaws.com/course.oc-static.com/projects/Python+FR/841+Mettez+%C3%A0+l'%C3%A9chelle+une+application+Django+en+utilisant+une+architecture+modulaire/Site+web+2.0+-+caracte%CC%81ristiques+et+ame%CC%81liorations.pdf).

# *Développement local*

## - Prérequis

- Compte GitHub avec accès en lecture à ce repository
- [Git CLI](https://git-scm.com/downloads)
- [SQLite3 CLI](https://sqlite.org/download.html) *incorporé à Django ou avec son IDE
- [Interpréteur Python](https://www.python.org/downloads/), version 3.11 minimum
- [Docker](https://www.docker.com/products/docker-desktop/) 
- [Compte Sentry](https://sentry.io/signup/)
- [Azure](https://azure.microsoft.com/fr-fr/free/)

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

## - macOS / Linux

### Cloner le repository


- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

## - Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

***

# *Variables d'environnements*
Afin que le déploiement se réalise, et que le site puisse via Django être sécurisé, il y a plusieurs variables 
d'environnements misent en place.
Ici se trouve juste la liste exhaustive, pour de plus ample explication, voir dans la documentation.

## - En locale

Utilisé par Django pour le setup dans settings.py :

Il y a la clé secréte de Django pour la sécurité.
Et la clé DSN afin d'avoir toute la journalisation centralisé sur Sentry.

Ps : la variable d'environnement DEBUG, n'est utile qu'en local, et s'il faut activer le mode débogage de Django.
* sous windows :

  `$Env:SECRET_KEY = "yourKeyKeepInSafe"`

  `$Env:DSN = "https://number.ingest.sentry.io/number`

  `**$Env:DEBUG = "True"**`
* sous Linux :

  `export SECRET_KEY="yourKeyKeepInSafe"`

  de même avec DSN, et voir DEBUG.
* sous Apple :

  `% SECRET_KEY="yourKeyKeepInSafe"`

  de même avec DSN, et voir DEBUG.

[Lien configuration et sécurité](https://thomas-python-oc-lettings-fr.readthedocs.io/fr/latest/configuration_and_security.html)

## - En production 

Via GitHub, d'autre variables sont utilisé pour le déploiement vers Azure, aussi bien pour se connecter à Docker
et le passage à l'environnement final, avec le maximum de sécurité pour ces variables.
Sur GitHub, il existe des variables "secrets" afin de garantir la confidentialité dans les fichiers log. 

![Liste des variables sur GitHub](https://github.com/Nathom78/Python-OC-Lettings-FR/blob/master/doc/source/_static/GitHub_secrets.jpeg?raw=true)

* variable lié à Azure :
  - APP_NAME : nom de l'application
  - RESOURCE_GROUP : nom du groupe de ressource utilisé pour la facturation
  - AZUREAPPSERVICE_PUBLISHPROFILE_ORANGE : contenu du profil de publication
  - AZURE_CREDENTIALS : voir [GitHub Action for Azure Login](https://github.com/azure/login#github-action-for-azure-login)
* variable lié à Docker :
  - DOCKER_PASSWORD : Access token avec des droits d'écriture et lecture 
  - DOCKER_REPOSITORY : nom du repository
  - DOCKER_USERNAME : nom du namespace
* et on retrouve SECRET_KEY et DSN afin de les passer au build final.

***

# *Technologies*
<p>
<img src="https://skillicons.dev/icons?i=git,github,githubactions,python,django,sqlite,docker,linux,azure,sentry,powershell,css,html,bootstrap&theme=dark">
</p>

***

# *Conventions de nommage et de codes :*
<p>PEP 8 – Style Guide for Python Code
<a href="https://peps.python.org/pep-0008/">ici</a>.
</p>

Un rapport **flake8** au format HTML est disponible dans le repertoire `\reports\flake8`, dans la branche badges.

PS : De cliquer sur les badges ou le nom du projet vous dirige vers les rapports des tests, ou le site concerné pour la documentation