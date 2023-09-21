Usage
=====


.. _running:

*Running*
---------

.. code-block:: console

	(.env) py manage runserver

*Developpement - Amélioration*
------------------------------

* Ajout de nouvelle branche Git:
	Lors d'ajout de nouvelle branche au projet, une action de GitHub, génère les tests, lors des commits.
	Pour cela, il faut :
	- à la racine du projet, le fichier *requirements.txt*, avec pytest, coverage, flake8 avec leurs plug-ins.
	- ainsi que le fichier *setup.cfg* pour leur configuration
	- pour chaque modules, ici 'Lettings', 'Profile', et voir d'autres à venir, il faut un fichier test.py,
	dans chaque modules, afin de pouvoir réaliser les tests unitaires.







