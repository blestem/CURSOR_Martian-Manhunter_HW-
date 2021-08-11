from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.core import serializers

from .models import Order


class OrdersListView(ListView):
    model = Order.objects.all()
    context_object_name = 'orders'
    template_name = 'orders/list.html'

    def get_queryset(self):
        return Order.objects.all()


class DetailOrdersView(DetailView):
    model = Order
    context_object_name = 'orders'
    pk_url_kwarg = 'order_pk'
    template_name = 'orders/detail.html'


def orders_json(request):
    orders = serializers.serialize('json', Order.odjects.all())
    return render(
        request,
        'orders/json.html',
        {'orders': orders}
    )

