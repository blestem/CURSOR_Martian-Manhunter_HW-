from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.core import serializers

from .models import Dealer


class DealersListView(ListView):
    model = Dealer.objects.all()
    context_object_name = 'dealers'
    template_name = 'dealers/list.html'

    def get_queryset(self):
        return Dealer.objects.all()


class DetailDealersView(DetailView):
    model = Dealer
    context_object_name = 'dealers'
    pk_url_kwarg = 'dealer_pk'
    template_name = 'dealers/detail.html'


def dealers_json(request):
    dealers = serializers.serialize('json', Dealer.odjects.all())
    return render(
        request,
        'dealers/json.html',
        {'dealers': dealers}
    )
