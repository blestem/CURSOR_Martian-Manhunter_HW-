from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
USER_MODEL = get_user_model()


class Dealer(models.Model):
    title = models.CharField(max_length=250)
    email = models.EmailField(
        max_length=50,
        unique=True,
    )
    city = models.ForeignKey(
        'dealers.City',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name='dealer',
    )

    class Meta:
        verbose_name = 'Дилер'
        verbose_name_plural = 'Дилери'

    def __str__(self):
        return self.title


class City(models.Model):
    name = models.CharField(
        max_length=75,
        unique=True,
    )
    country = models.ForeignKey(
        'dealers.Country',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Місто'
        verbose_name_plural = 'Міста'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(
        max_length=75,
        unique=True,
    )

    code = models.CharField(
        max_length=5,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'

    def __str__(self):
        return self.name
