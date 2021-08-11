import factory


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Car'

    dealer_id = 1
    picture_id = 1
    color_id = 1
    model_id = 1
    number = 'BC 1234 CP'
    slug = 'MINI_Cooper_2013'
    price = 11500
    engine_power = 136
    fuel_type = 'petrol'
    capacity = 1.5
    sitting_place = 4
    doors = 3


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Color'

    name = 'dark green'


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Brand'

    name = 'MINI'


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Property'

    name = 'Coupe'


class ModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Model'

    brand_id = 1
    name = 'Cooper'


