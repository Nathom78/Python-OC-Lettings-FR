import pytest

from django.urls import reverse, resolve


# from lettings.models import Letting, Address


def test_lettings_index_url():
    path = reverse("lettings_index")

    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings_index"

# @pytest.mark.django_db
# def test_lettings_index_url():
#     Address.objects.create(number=1601,
#                            street="California street",
#                            city="Palo Alto",
#                            state="USA",
#                            zip_code=94304,
#                            country_iso_code="CA")
#
#     path = reverse("lettings_index", kwargs={'pk': 1})
#
#     assert path == "/1"
#     assert resolve(path).view_name == "infos"
