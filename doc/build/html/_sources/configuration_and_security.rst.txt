Configuration et sécurité
=========================

.. contents::
   :depth: 4
   :local:

.. _Django:

*Django*
--------


Django settings:
^^^^^^^^^^^^^^^^

.. code-block:: python

		# SECURITY WARNING: don't run with debug turned on in production!

		DEBUG = bool(os.environ.get('DEBUG', default=False))
		ALLOWED_HOSTS = ['orange-county-lettings.azurewebsites.net',
		                 '127.0.0.1',
		                 '.localhost',
		                 '0.0.0.0',
		                 'google.com',
		                 '[::1]'] if DEBUG is False else []

* Une variable d'environnement  DEBUG ($Env:DEBUG = True) peut être crée afin de lancer Django en mode developpement.
* ALLOWED_HOSTS sont les adresses que le serveur Django ou Gunicorn peuvent desservir. Ici sont les adresses du site de
  déploiement et les adresses afin de pouvoir utiliser le conteneur Docker en locale.


.. _whitenoise:

`Link WhiteNoise <https://whitenoise.readthedocs.io/en/latest/django.html>`_

WhiteNoise permet de servir les fichiers "static", de django et de l'application Python, en les compressant.
Il est conçu pour fonctionner sur un serveur WSGI, avec des fonctions intégré pour Django. Adapter pour être déployé,
même sur des CDN, avec sa compression Gzip et Brotli, gérant les en tête Accept-Encoding,
et Vary pour la réutilisation du cache.

Afin d'utiliser whitenoise :

.. code-block:: python

		MIDDLEWARE = [
		    'django.middleware.security.SecurityMiddleware',
		    'whitenoise.middleware.WhiteNoiseMiddleware',
		    ...

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


