from django.urls import path

from .views import DealersListView, DetailDealersView, dealers_json


app_name = 'dealers'

urlpatterns = [
    path(
        '',
        DealersListView.as_view(),
        name='dealer_list'
    ),
    path(
        '<int:dealer_pk>/',
        DetailDealersView.as_view(),
        name='dealer_detail',
    ),
    path(
        'json',
        dealers_json,
    ),
]
