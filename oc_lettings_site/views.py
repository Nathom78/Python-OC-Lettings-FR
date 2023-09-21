from django.shortcuts import render
import sentry_sdk


def index(request):
    """
    View for the home index.

    :param request: The request to this page.

    :return: Home’s HTML template.
    """
    return render(request, "oc_lettings_site/index.html")


def trigger_error(request):
    """
    Déclenche une erreur de division par zéro pour tester
    la capture d'exception par Sentry.

    Args:
        request (HttpRequest): L'objet HttpRequest
        qui représente la requête HTTP.

    Returns:
        HttpResponse: L'objet HttpResponse qui représente
        la réponse HTTP contenant la page d'erreur.

    """
    try:
        return 1 / 0
    except ZeroDivisionError as e:
        sentry_sdk.capture_exception(e)
        return render(
            request, 'error.html', {'error_message': str(e)}, status=500)
