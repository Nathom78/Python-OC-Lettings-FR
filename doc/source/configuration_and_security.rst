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

WhiteNoise:
^^^^^^^^^^^

`WhiteNoise <https://whitenoise.readthedocs.io/en/latest/django.html>`_

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



.. _sentry:

Sentry:
^^^^^^^

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

`Sentry <https://docs.sentry.io/platforms/python/guides/django/?original_referrer=https%3A%2F%2Fdocs.sentry.io%2Fplatforms%2Fpython%2Fconfiguration%2Fintegrations%2F%3Foriginal_referrer%3Dhttps%253A%252F%252Fwww.google.fr%252F>`_