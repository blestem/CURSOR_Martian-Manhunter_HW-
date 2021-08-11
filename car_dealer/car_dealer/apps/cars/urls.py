from django.urls import path

from .views import CarsListView, DetailCarsView, cars_json

app_name = 'cars'

urlpatterns = [
    path(
        '',
        CarsListView.as_view(),
        name='car_list'
    ),
    path(
        '<str:car_slug>/',
        DetailCarsView.as_view(),
        name='car_detail'
    ),
    path(
        'json',
        cars_json,
    ),
]
