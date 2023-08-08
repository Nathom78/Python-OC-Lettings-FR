import pytest

from django.urls import reverse, resolve
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

from profiles.models import Profile
from django.contrib.auth.models import User

C = Client()


@pytest.mark.django_db
def test_profiles_index_url():
    user = User.objects.create_user(username="TestUser")
    Profile.objects.create(user=user, favorite_city="FavoriteCost")
    path = reverse("profiles_index")

    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles_index"


@pytest.mark.django_db
def test_profiles_letting_url():
    user = User.objects.create_user(username="TestUser")
    Profile.objects.create(user=user, favorite_city="FavoriteCost")
    path = reverse("profile", kwargs={'username': "TestUser"})

    assert path == "/profiles/" + "TestUser/"
    assert resolve(path).view_name == "profile"


@pytest.mark.django_db
def test_profiles_index_view():
    client = C
    user = User.objects.create_user(username="TestUser")
    Profile.objects.create(user=user, favorite_city="FavoriteCost")
    path = reverse("profiles_index")
    response = client.get(path)
    content = response.content.decode()

    expected_content = '<a href="/profiles/TestUser/">TestUser</a>'

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profiles_profile_view():
    client = C
    user = User.objects.create_user(username="TestUser")
    Profile.objects.create(user=user, favorite_city="FavoriteCost")
    path = reverse("profile", kwargs={'username': 'TestUser'})
    response = client.get(path)
    content = response.content.decode()

    expected_content = ['<p><strong>First name :</strong> </p>',
                        '<p><strong>Last name :</strong> </p>',
                        '<p><strong>Email :</strong> </p>',
                        '<p><strong>Favorite city :</strong> FavoriteCost</p>'
                        ]

    for elem in expected_content:
        assert elem in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")


@pytest.mark.django_db
def test_profile_model():
    Client()
    user = User.objects.create_user(username="TestUser")
    profile = Profile.objects.create(user=user,
                                     favorite_city="FavoriteCost")

    expected_content = "TestUser"

    assert str(profile) == expected_content
