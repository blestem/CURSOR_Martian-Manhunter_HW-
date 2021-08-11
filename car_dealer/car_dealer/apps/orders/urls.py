from django.urls import path

from .views import OrdersListView, DetailOrdersView, orders_json


app_name = 'orders'


urlpatterns = [
    path(
        '',
        OrdersListView.as_view(),
        name='order_list',
    ),

    path(
        '<int:order_pk>/',
        DetailOrdersView.as_view(),
        name='order_detail',
    ),

    path(
        'json',
        orders_json,
    ),
]
