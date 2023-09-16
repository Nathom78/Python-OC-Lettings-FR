from django.shortcuts import render
from .models import Letting


def index(request):
    """
    View for lettings list.

    :param request: the request for this page.

    :return: lettings_list in html.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    View for a letting detail.

    :param request: the request for this page.

    :param letting_id: the reference to the letting.

    :return: letting_detail in html.
    """
    letting_detail = Letting.objects.get(id=letting_id)
    context = {
        "title": letting_detail.title,
        "address": letting_detail.address,
    }
    return render(request, "lettings/letting.html", context)
