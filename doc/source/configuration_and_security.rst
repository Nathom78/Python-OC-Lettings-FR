Configuration et sécurité
=========================

.. contents::
   :depth: 4
   :local:

.. _Django:

*Django*
########


Django settings:
****************
`Documentation Django <https://docs.djangoproject.com/fr/4.2/ref/settings/>`_


.. important::

	Django refuse de démarrer si SECRET_KEY n’est pas défini.

`Secret Key documentation <https://docs.djangoproject.com/fr/4.2/ref/settings/#std-setting-SECRET_KEY>`_

.. envvar:: SECRET_KEY

	SECRET_KEY = os.environ.get('SECRET_KEY')
.. code-block:: python

	# SECURITY WARNING: keep the secret key used in production secret!
	SECRET_KEY = os.environ.get('SECRET_KEY')

Ici la clé secret à été stocké entant que variable d'environnement.
voir `démarrage rapide - variable d'environnement <https://thomas-python-oc-lettings-fr.readthedocs.io/en/latest/README.html#variables-d-environnements>`_

.. note::
	Par défaut elle est composé d'un minimum de 50 caractère avec les caractères spéciaux autorisés. Afin quelle reste introuvable.

Une solution pour la générer:

.. code-block:: console

	python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

.. envvar:: DEBUG

.. code-block:: python

		# SECURITY WARNING: don't run with debug turned on in production!

		DEBUG = bool(os.environ.get('DEBUG', default=False))
		ALLOWED_HOSTS = ['orange-county-lettings.azurewebsites.net',
		                 '127.0.0.1',
		                 '.localhost',
		                 '0.0.0.0',
		                 'google.com',
		                 '[::1]'] if DEBUG is False else []


* Une variable d'environnement DEBUG ($Env:DEBUG = True) peut être crée afin de lancer Django en mode developpement.
* ALLOWED_HOSTS sont les adresses que le serveur Django ou Gunicorn peuvent desservir. Ici sont les adresses du site de
  déploiement et les adresses afin de pouvoir utiliser le conteneur Docker en locale.


WhiteNoise:
^^^^^^^^^^^

`WhiteNoise <https://whitenoise.readthedocs.io/en/latest/django.html>`_

WhiteNoise permet de servir tous les fichiers "static", de django et de l'application Python, en les compressant.
Il est conçu pour fonctionner sur un serveur WSGI, avec des fonctions intégré pour Django. Adapter pour être déployé,
même sur des CDN, avec sa compression Gzip et Brotli, gérant les en tête Accept-Encoding,
et Vary pour la réutilisation du cache.

Afin d'utiliser whitenoise : (à insérer dans settings.py)

.. code-block:: python

		MIDDLEWARE = [
		    'django.middleware.security.SecurityMiddleware',
		    'whitenoise.middleware.WhiteNoiseMiddleware',
		    ...
		]

.. code-block:: python

		# Static files (CSS, JavaScript, Images)
		# https://docs.djangoproject.com/en/3.0/howto/static-files/

		STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

		STATIC_URL = 'staticfiles/'
		STATICFILES_DIRS = [BASE_DIR / "static", ]

		STORAGES = {
		    "default": {
		        "BACKEND": "django.core.files.storage.FileSystemStorage",
		    },
		    "staticfiles": {
		        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
		    },
		}




Sentry:
^^^^^^^

""Agissez sur les lignes de code brisées, les plantages et les appels d’API interrompus avec la seule
plate-forme de surveillance des applications axée sur les développeurs, conçue pour vous donner des réponses, et non des indices.""

Nous avons choisi Sentry comme outil de surveillance afin de garder notre application competitive dans le temps.
(à insérer dans settings.py)

.. code-block:: python


		def profiles_sampler(sampling_context):
		    # ...
		    # return a number between 0 and 1 or a boolean
		    return True

		sentry_sdk.init(
		    dsn=os.environ.get('DSN'),
		    # Set traces_sample_rate to 1.0 to capture 100%
		    # of transactions for performance monitoring.
		    # We recommend adjusting this value in production.
		    traces_sample_rate=1.0,
		    # Set profiles_sample_rate to 1.0 to profile 100%
		    # of sampled transactions.
		    # We recommend adjusting this value in production.
		    profiles_sample_rate=1.0,

		    # Alternatively, to control sampling dynamically
		    profiles_sampler=profiles_sampler,
		    integrations=[
		        DjangoIntegration(
		            transaction_style='url',
		            middleware_spans=True,
		            signals_spans=True,
		            cache_spans=True,
		        ),
		    ],
		    send_default_pii=True
		)

Pour l'instant 100% des erreurs sont échantillonnés.
Voir la documentation ci dessous afin d'obtenir le DSN, et autres configuration possible pour Django.
`Sentry Platform Django <https://docs.sentry.io/platforms/python/guides/django>`_

Gunicorn
^^^^^^^^

Déploiement de Django avec Gunicorn :

`Gunicorn <https://gunicorn.org/>`_ (« Green Unicorn ») est un serveur WSGI en pur Python pour UNIX. Il n’a aucune dépendance et peut être installé avec pip.
Microsoft Azure conseil pour une meilleure compatibilité avec les applications en Python de le mettre en place, ainsi que Django

La configuration se trouve dans le fichier *dockerfile*, situé à la racine du projet, comme ceci :

.. code-block:: python

		CMD gunicorn --bind=0.0.0.0:8080 --timeout 200 oc_lettings_site.wsgi


`Exemple de commandes de démarrage, pour Python, avec Azure. <https://learn.microsoft.com/fr-fr/azure/app-service/configure-language-python#example-startup-commands>`_

----



*Microsoft Azure*
#################

