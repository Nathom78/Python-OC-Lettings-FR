from django.shortcuts import render


def index(request):
    """
    View for the home index.

    :param request: The request to this page.

    :return: Home’s HTML template.
    """
    return render(request, "index.html")
