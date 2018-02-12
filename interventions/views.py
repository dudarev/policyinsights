from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Location, InterventionCategory


class LocationsSearchView(ListView):

    model = Location

    def get_queryset(self):
        queryset = Location.objects.all()
        if self.request.GET.get('q'):
            queryset = queryset.filter(name__icontains=self.request.GET.get('q'))
        return queryset


class LocationDetail(DetailView):

    model = Location


class InterventionCategoriesSearchView(ListView):

    model = InterventionCategory

    def get_queryset(self):
        queryset = InterventionCategory.objects.all().filter(location=self.kwargs.get('location_pk'))
        if self.request.GET.get('q'):
            queryset = queryset.filter(name__icontains=self.request.GET.get('q'))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = Location.objects.get(pk=self.kwargs.get('location_pk'))
        return context
