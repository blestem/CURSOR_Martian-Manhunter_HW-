from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=25)
    staff = models.ManyToManyField(
        'restaurant.RestaurantStaff'
    )
    country = models.OneToOneField(
        'restaurant.Country',
        on_delete=models.SET_NULL,
        null=True
    )
    city = models.OneToOneField(
        'restaurant.City',
        on_delete=models.SET_NULL,
        null=True
    )
    menu = models.ManyToManyField(
        'restaurant.Menu'
    )
    season_menu = models.ManyToManyField(
        'restaurant.SeasonMenu'
    )

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Ресторан'


class RestaurantStaff(models.Model):
    POST_ADMIN = 'administrator'
    POST_BARTENDER = 'bartender'
    POST_WAITER = 'waiter'
    POST_CHEF = 'chef'
    POST_CLEANER = 'cleaner'

    POSITION_CHOICES = (
        (POST_ADMIN, "Administrator"),
        (POST_BARTENDER, "Bartender"),
        (POST_WAITER, "Waiter"),
        (POST_CHEF, "Chef"),
        (POST_CLEANER, "Cleaner"),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    post = models.CharField(
        max_length=50,
        choices=POSITION_CHOICES,
        blank=True,
    )
    phone = models.IntegerField()

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'


class Country(models.Model):
    country = models.CharField(max_length=75)

    class Meta:
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'


class City(models.Model):
    city = models.CharField(max_length=75)

    class Meta:
        verbose_name = 'Місто'
        verbose_name_plural = 'Міста'


class Menu(models.Model):
    name = models.CharField(max_length=50)
    dishes = models.ManyToManyField(
        'restaurant.RestaurantDish'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class SeasonMenu(models.Model):
    name = models.CharField(max_length=50)
    dishes = models.ManyToManyField(
        'restaurant.RestaurantDish'
    )

    class Meta:
        verbose_name = 'Сезонне Меню'
        verbose_name_plural = 'Сезонне Меню'


class RestaurantDish(models.Model):
    dish = models.CharField(max_length=50)
    dish_composition = models.TextField
    price = models.FloatField

    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'

