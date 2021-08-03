from django.db import models


# Create your models here.


class Car(models.Model):
    color = models.ForeignKey(
        'cars.Color',
        on_delete=models.CASCADE,
    )
    dealer = models.ForeignKey(
        'dealers.Dealer',
        on_delete=models.CASCADE,
    )
    model = models.ForeignKey(
        'cars.Model',
        on_delete=models.CASCADE,
    )
    ENGINE_INJECTOR = 'Injector engine'
    ENGINE_CARBURETOR = 'Carburetor engine'
    ENGINE_ELECTRIC = 'Electric motors'

    ENGINE_CHOICE = (
        (ENGINE_INJECTOR, 'Injector engine'),
        (ENGINE_CARBURETOR, 'Carburetor engine'),
        (ENGINE_ELECTRIC, 'Electric motors'),
    )

    engine_type = models.CharField(
        max_length=50,
        choices=ENGINE_CHOICE,
        default=ENGINE_CARBURETOR,
    )
    POLLUTANT_CLASS_A = 'class A'
    POLLUTANT_CLASS_B = 'class B'
    POLLUTANT_CLASS_C = 'class C'
    POLLUTANT_CLASS_D = 'class D'
    POLLUTANT_CLASS_E = 'class E'
    POLLUTANT_CLASS_F = 'class F'
    POLLUTANT_CLASS_G = 'class G'

    POLLUTANT_CLASS_CHOICE = (
        (POLLUTANT_CLASS_A, 'class A'),
        (POLLUTANT_CLASS_B, 'class B'),
        (POLLUTANT_CLASS_C, 'class C'),
        (POLLUTANT_CLASS_D, 'class D'),
        (POLLUTANT_CLASS_E, 'class E'),
        (POLLUTANT_CLASS_F, 'class F'),
        (POLLUTANT_CLASS_G, 'class G'),
    )
    pollutant_class = models.CharField(
        max_length=50,
        choices=POLLUTANT_CLASS_CHOICE,
        default=POLLUTANT_CLASS_B,
    )

    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )
    fuel_type = models.ForeignKey(
        'cars.FuelType',
        on_delete=models.CASCADE,
    )

    STATUS_PENDING = 'Pending'
    STATUS_PUBLISH = 'Publish'
    STATUS_SOLD = 'Sold'
    STATUS_ARCHIVED = 'Archived'

    STATUS_CHOICE = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_PUBLISH, 'Publish'),
        (STATUS_SOLD, 'Sold'),
        (STATUS_ARCHIVED, 'Archived'),
    )
    status = models.CharField(
        max_length=25,
        choices=STATUS_CHOICE,
        default=STATUS_PENDING,
    )
    doors = models.SmallIntegerField()

    capacity = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )
    GEAR_CASE_MECHANICAL = 'Mechanical'
    GEAR_CASE_AUTOMATIC = 'Automatic'
    GEAR_CASE_ROBOTIC = 'Robotic'
    GEAR_CASE_VARIABLE = 'Variable'

    GEAR_CHOICE = (
        (GEAR_CASE_MECHANICAL, 'Mechanical'),
        (GEAR_CASE_AUTOMATIC, 'Automatic'),
        (GEAR_CASE_ROBOTIC, 'Robotic'),
        (GEAR_CASE_VARIABLE, 'Variable'),
    )

    gear_case = models.CharField(
        max_length=30,
        choices=GEAR_CHOICE,
        default=GEAR_CASE_AUTOMATIC
    )
    number = models.CharField(max_length=10)

    slug = models.SlugField(max_length=75)

    sitting_place = models.SmallIntegerField()

    first_registration_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )

    engine_power = models.SmallIntegerField()

    body_type = models.ManyToManyField(
        'cars.Property',
        blank=True,
    )
    CAR_SEGMENT_A = 'segment A'
    CAR_SEGMENT_B = 'segment B'
    CAR_SEGMENT_C = 'segment C'
    CAR_SEGMENT_D = 'segment D'
    CAR_SEGMENT_E = 'segment E'
    CAR_SEGMENT_F = 'segment F'

    CAR_SEGMENTS_CHOICE = (
        (CAR_SEGMENT_A, 'segment A'),
        (CAR_SEGMENT_B, 'segment B'),
        (CAR_SEGMENT_C, 'segment C'),
        (CAR_SEGMENT_D, 'segment D'),
        (CAR_SEGMENT_E, 'segment E'),
        (CAR_SEGMENT_F, 'segment F'),
    )

    car_segments = models.CharField(
        max_length=50,
        choices=CAR_SEGMENTS_CHOICE,
        default=CAR_SEGMENT_B,
    )

    description = models.TextField(
        blank=True,
    )

    picture = models.ForeignKey(
        'cars.Picture',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Автомобіль'
        verbose_name_plural = 'Автомобілі'

    def __str__(self):
        return self.slug


class Color(models.Model):
    name = models.CharField(max_length=75)

    class Meta:
        verbose_name = 'Колір'
        verbose_name_plural = 'Кольори'

    def __str__(self):
        return self.name


class Model(models.Model):
    brand = models.ForeignKey(
        'cars.Brand',
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=75)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Моделі'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=75)

    brand_mark = models.ImageField(
        upload_to='picture_brand_mark',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренди'

    def __str__(self):
        return self.name


class Property(models.Model):
    BODY_TYPE_SEDAN = 'Sedan'
    BODE_TYPE_SUV = 'SUVs'
    BODE_TYPE_WAGON = 'Wagon'
    BODE_TYPE_COUPE = 'Coupe'
    BODE_TYPE_CROSSOVER = 'Crossover'
    BODE_TYPE_CABRIO = 'Cabrio'
    BODE_TYPE_SPORTS = 'Sports'
    BODE_TYPE_MICRO = 'Micro'
    BODE_TYPE_HATCHBACK = 'Hatchback'
    BODE_TYPE_PICKUP = 'Pickup'
    BODE_TYPE_VAN = 'VAN'
    BODE_TYPE_COUPE_SUV = 'Coupe SUV'
    BODE_TYPE_OFF_ROADER = 'Off-roader'

    BODY_TYPE_CHOICE = (
        (BODY_TYPE_SEDAN, 'Sedan'),
        (BODE_TYPE_SUV, 'SUVs'),
        (BODE_TYPE_WAGON, 'Wagon'),
        (BODE_TYPE_COUPE, 'Coupe'),
        (BODE_TYPE_CROSSOVER, 'Crossover'),
        (BODE_TYPE_CABRIO, 'Cabrio'),
        (BODE_TYPE_SPORTS, 'Sports'),
        (BODE_TYPE_MICRO, 'Micro'),
        (BODE_TYPE_HATCHBACK, 'Hatchback'),
        (BODE_TYPE_PICKUP, 'Pickup'),
        (BODE_TYPE_VAN, 'VAN'),
        (BODE_TYPE_COUPE_SUV, 'Coupe SUV'),
        (BODE_TYPE_OFF_ROADER, 'Off-roader'),
    )
    body_type = models.CharField(
        max_length=50,
        choices=BODY_TYPE_CHOICE,
        default=BODY_TYPE_SEDAN,
    )
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Тип кузова'
        verbose_name_plural = 'Типи кузовів'

    def __str__(self):
        return self.name


class Picture(models.Model):
    url = models.ImageField(
        upload_to='pictures_car',
        null=True,
        blank=True,
    )
    position = models.SmallIntegerField(
        blank=True,
    )

    metadata = models.CharField(
        max_length=150,
        blank=True,
    )

    class Meta:
        verbose_name = 'Зображення'
        verbose_name_plural = 'Зображення'

    def __str__(self):
        return self.metadata


class FuelType(models.Model):
    FUEL_GAS = 'gas'
    FUEL_PETROL = 'petrol'
    FUEL_DIESEL = 'diesel'
    FUEL_ELECTRICITY = 'electricity'

    FUEL_CHOICE = (
        (FUEL_GAS, 'Gas'),
        (FUEL_PETROL, 'Petrol'),
        (FUEL_DIESEL, 'Diesel'),
        (FUEL_ELECTRICITY, 'Electricity'),
    )

    fuel_type = models.CharField(
        max_length=50,
        choices=FUEL_CHOICE,
        default=FUEL_PETROL,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тип пального'
        verbose_name_plural = 'Пальне'

    def __str__(self):
        return self.fuel_type
