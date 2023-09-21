from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Modèle représentant un profil utilisateur.

    Attributes:
        user (OneToOneField): La relation un-à-un avec le modèle User
            pour lier le profil à un utilisateur.
        favorite_city (CharField): La ville préférée de l'utilisateur
            (max 64 caractères, facultatif).

    Methods:
        __str__: Retourne une représentation sous forme
            de chaîne de caractères du profil.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
