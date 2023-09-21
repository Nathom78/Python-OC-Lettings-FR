import pytest

from django.urls import reverse, resolve
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_profiles_index_url():
    """
    Test that the URL for the 'index' view resolves
    to the correct view function.
    """
    path = reverse("index")

    assert path == "/"
    assert resolve(path).view_name == "index"


@pytest.mark.django_db
def test_trigger_error_url_resolves():
    """
    Test that the URL for the 'sentrytest' view resolves
    to the correct view function.
    """
    path = reverse("sentrytest")

    assert path == "/sentry-debug/"
    assert resolve(path).view_name == "sentrytest"


@pytest.mark.django_db
def test_index_view():
    """
    Test that the 'index' view returns a status code of 200
    and uses the correct template.

    """
    client = Client()
    path = reverse("index")

    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "oc_lettings_site/index.html")


@pytest.mark.django_db
def test_trigger_error_view():
    """
    Test that the 'sentrytest' view returns a status code of 500
    and uses the 'error.html' template.
    """
    client = Client()
    path = reverse("sentrytest")

    response = client.get(path)

    assert response.status_code == 500
    assertTemplateUsed(response, 'error.html')


def test_dummy():
    assert 1
