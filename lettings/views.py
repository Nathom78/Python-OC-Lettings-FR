from django.shortcuts import render
from .models import Letting


def index(request):
    """
    View for lettings" list
    :param request:
    :return:
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    View for a letting detail
    :param request:
    :param letting_id:
    :return:
    """
    letting_detail = Letting.objects.get(id=letting_id)
    context = {
        "title": letting_detail.title,
        "address": letting_detail.address,
    }
    return render(request, "lettings/letting.html", context)
