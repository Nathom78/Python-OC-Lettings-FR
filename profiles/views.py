from django.shortcuts import render

from .models import Profile


def index(request):
    """
    View for the list of profiles.

    :param request: The request for this page.

    :return: profiles_list HTML template.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    View for the detail of one profile.

    :param request: The request for this page.
    :param username: The reference to the profile's name.

    :return: profile_detail HTML template.
    """
    profile_detail = Profile.objects.get(user__username=username)
    context = {"profile": profile_detail}
    return render(request, "profiles/profile.html", context)
