from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.core import serializers

from .models import Car


class CarsListView(ListView):
    model = Car.objects.all()
    context_object_name = 'cars'
    template_name = 'cars/list.html'

    def get_queryset(self):
        return Car.objects.all()


class DetailCarsView(DetailView):
    model = Car
    context_object_name = 'cars'
    slug_url_kwarg = 'car_slug'
    template_name = 'cars/detail.html'


def cars_json(request):
    cars = serializers.serialize('json', Car.odjects.all())
    return render(
        request,
        'cars/json.html',
        {'cars': cars}
    )




