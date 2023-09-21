from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse.

    Attributes:
        number (PositiveIntegerField): Le numéro de l'adresse (entre 1 et 9999).

        street (CharField): Le nom de la rue (max 64 caractères).

        city (CharField): Le nom de la ville (max 64 caractères).

        state (CharField): Le code d'État ou de province (2 caractères min).

        zip_code (PositiveIntegerField): Le code postal (entre 1 et 99999).

        country_iso_code (CharField): Le code ISO du pays (3 caractères min).

    Methods:
        __str__: Retourne une représentation sous forme
            de chaîne de caractères de l'adresse.

    Meta:
        verbose_name_plural: Nom au pluriel utilisé dans l'administration.

    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Modèle représentant une location.

    Attributes:
        title (CharField): Le titre de la location (max 256 caractères).

        address (OneToOneField): L'adresse de la location (relation un-à-un avec le modèle Address).

    Methods:
        __str__: Retourne une représentation sous forme de chaîne de caractères de la location.

    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
