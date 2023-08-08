import pytest

from django.urls import reverse, resolve
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

from lettings.models import Letting, Address

C = Client()


def test_lettings_index_url():
    path = reverse("lettings_index")

    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings_index"


def test_lettings_letting_url():
    path = reverse("letting", kwargs={'letting_id': 1})

    assert path == "/lettings/1/"
    assert resolve(path).view_name == "letting"


@pytest.mark.django_db
def test_lettings_index_view():
    client = C
    address_1 = Address.objects.create(number=1601,
                                       street="California street",
                                       city="Palo Alto",
                                       state="USA",
                                       zip_code=94304,
                                       country_iso_code="CA")
    Letting.objects.create(title="FaceBook",
                           address=address_1)
    path = reverse("lettings_index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = '<a href="/lettings/1/">FaceBook</a>'

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_lettings_letting_view():
    client = C
    address_1 = Address.objects.create(number=1601,
                                       street="California street",
                                       city="Palo Alto",
                                       state="USA",
                                       zip_code=94304,
                                       country_iso_code="CA")
    Letting.objects.create(title="FaceBook",
                           address=address_1)
    path = reverse("letting", kwargs={'letting_id': 1})
    response = client.get(path)
    content = response.content.decode()
    expected_content = ['<p>1601 California street</p>',
                        '<p>Palo Alto, USA 94304</p>',
                        '<p>CA</p>'
                        ]
    for elem in expected_content:
        assert elem in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")


class TestModels:
    pytestmark = pytest.mark.django_db

    def test_address_model(self):
        Client()

        address_1 = Address.objects.create(number=1601,
                                           street="California street",
                                           city="Palo Alto",
                                           state="USA",
                                           zip_code=94304,
                                           country_iso_code="CA")

        expected_content = "1601 California street"

        assert str(address_1) == expected_content

    def test_letting_model(self):
        Client()
        address_1 = Address.objects.create(number=1601,
                                           street="California street",
                                           city="Palo Alto",
                                           state="USA",
                                           zip_code=94304,
                                           country_iso_code="CA")
        letting = Letting.objects.create(title="FaceBook",
                                         address=address_1)
        expected_content = "FaceBook"

        assert str(letting) == expected_content
