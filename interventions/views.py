from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Location


class LocationsSearchView(ListView):

    model = Location

    def get_queryset(self):
        queryset = Location.objects.all()
        if self.request.GET.get('q'):
            queryset = queryset.filter(name__contains=self.request.GET.get('q'))
        return queryset


class LocationDetail(DetailView):

    model = Location
