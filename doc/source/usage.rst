Usage
=====

.. contents::
   :depth: 4
   :local:


*Developpement - Amélioration*
------------------------------

* Ajout de nouvelle branche Git:


| Lors d'ajout de nouvelle branche au projet, une action de GitHub, génère les tests, lors des commits.
| Pour cela, il faut :
| - à la racine de la nouvelle branche, le fichier *requirements.txt*, avec pytest, coverage, flake8 ainsi que leur plug-ins.
| - ainsi que le fichier *setup.cfg* pour leur configuration.
| - pour chaque nouvelles applications, comme ici 'Lettings', 'Profile', il faut un fichier test.py,
| dans les nouveaux packages, afin de pouvoir réaliser les tests unitaires.








