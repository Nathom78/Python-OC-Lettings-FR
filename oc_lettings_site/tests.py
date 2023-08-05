import pytest

from django.urls import reverse, resolve
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_profiles_index_url():
    path = reverse("index")

    assert path == "/"
    assert resolve(path).view_name == "index"


@pytest.mark.django_db
def test_index_view():
    client = Client()
    path = reverse("index")

    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")


def test_dummy():
    assert 1
