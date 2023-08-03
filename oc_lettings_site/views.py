from django.shortcuts import render


def index(request):
    """
    View for the home index
    :param request:
    :return: Home’s template
    """
    return render(request, "index.html")
