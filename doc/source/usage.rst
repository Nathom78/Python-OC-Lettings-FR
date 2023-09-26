Usage
=====

.. contents::
   :depth: 4
   :local:


*Chemins URL d'accès du site*
-----------------------------

- **Adresse du site Django admin :**

Pour accéder au site admin utiliser l'adresse *'/admin/'*

Avec les identifiants via ce lien : `<https://thomas-python-oc-lettings-fr.readthedocs.io/fr/master/README.html#panel-d-administration>`_

`Lien vers le site admin <https://orange-county-lettings.azurewebsites.net/admin/>`_

- **Adresse test sentry :**

Afin de tester grace à une erreur de division par zero, que la liaison avec Sentry est bien effective, il suffit d'aller à l'adresse suivante du site :
*'/sentry-debug/'*.

`Lien vers le site <https://orange-county-lettings.azurewebsites.net/sentry-debug/>`_


*Developpement - Amélioration*
------------------------------

* Ajout de nouvelle branche Git:


| Lors d'ajout de nouvelle branche au projet, une action de GitHub, génère les tests, lors des commits.
| Pour cela, il faut :
| - à la racine de la nouvelle branche, le fichier *requirements.txt*, avec pytest, coverage, flake8 ainsi que leur plug-ins.
| - ainsi que le fichier *setup.cfg* pour leur configuration.
| - pour chaque nouvelles applications, comme ici 'Lettings', 'Profile', il faut un fichier test.py,
| dans les nouveaux packages, afin de pouvoir réaliser les tests unitaires.








