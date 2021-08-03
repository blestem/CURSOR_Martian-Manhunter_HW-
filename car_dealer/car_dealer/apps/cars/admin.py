from django.contrib import admin
from .models import Car, Color, Model, Brand, Property, Picture, FuelType

# Register your models here.

admin.site.register(Car)
admin.site.register(Color)
admin.site.register(Model)
admin.site.register(Brand)
admin.site.register(Property)
admin.site.register(Picture)
admin.site.register(FuelType)