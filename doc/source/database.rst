Base de donnée
==============

.. contents::
   :depth: 4
   :local:


*SQLite3*
---------

La base de données que nous utilisons pour cette application est SQLite (ici SQLite3).

SQLite est un moteur de base de données SQL léger, orienté fichier autonome.
Souvent utilisé pour des applications de petite et moyenne taille, en raison de sa facilité d’installation et d’utilisation.

Pourquoi utiliser SQLite3 ? :

1/ Configuration facile : Django est configuré pour utiliser SQLite par défaut lors de la création d’un nouveau projet.
Dans votre fichier de paramètres Django *'settings.py'*, vous trouverez la configuration de la base de données en tant que base de données.

2/ Aucun serveur requis: Contrairement à d’autres systèmes de gestion de base de données comme PostgreSQL ou MySQL,
SQLite ne nécessite pas de processus serveur distinct. Toutes les données sont stockées dans un seul fichier, qui est géré directement par le moteur SQLite.

3/ Portabilité : Puisque la base de données SQLite est simplement un fichier,
il est facile de copier et de déplacer vers un autre emplacement ou système


Présentation des objets et de l'ERD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Trois objets sont représenté dans la base de donnée : Profile, Letting, Address.

* Profile : représente un client.  Il est liée au modèle 'User' de Django (django.contrib.auth.models).
  Permet l’identification d’un utilisateur.

* Letting : représente une annonce de location. Lié à une adresse 'Address' afin d'identifier l'objet.

* Address : représente une propriété à loué. L'adresse de la propriété est fournis.



Présentation des modèles
^^^^^^^^^^^^^^^^^^^^^^^^

**Profile : Représentant un client.**
"""""""""""""""""""""""""""""""""""""

                    .. autoclass:: profiles.models.Profile
                       :members:
                       :no-index:

**Letting : Représentant une location.**
""""""""""""""""""""""""""""""""""""""""

                    .. autoclass:: lettings.models.Letting
                       :members:
                       :no-index:


**Address : Représentant une propriété a loué.**
""""""""""""""""""""""""""""""""""""""""""""""""

                    .. autoclass:: lettings.models.Address
                       :members:
                       :no-index:
