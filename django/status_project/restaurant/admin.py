from django.contrib import admin

# Register your models here.
from .models import Restaurant, RestaurantStaff, Country, City, Menu, SeasonMenu, RestaurantDish

admin.site.register(Restaurant)
admin.site.register(RestaurantStaff)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Menu)
admin.site.register(SeasonMenu)
admin.site.register(RestaurantDish)
