from django.contrib import admin
from .models import Dealer, City, Country

# Register your models here.

admin.site.register(Dealer)
admin.site.register(City)
admin.site.register(Country)