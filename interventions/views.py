from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Intervention, InterventionCategory, Location


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
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['location'] = Location.objects.get(pk=self.kwargs.get('location_pk'))
        return context


class InteventionsSearchView(ListView):

    model = Intervention

    def get_queryset(self):
        intervention_category_pk = self.kwargs.get('intervention_category_pk')
        queryset = Intervention.objects.filter(category=intervention_category_pk)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        intervention_category = InterventionCategory.objects.get(
            pk=self.kwargs.get('intervention_category_pk'))
        context['intervention_category'] = intervention_category
        context['location'] = intervention_category.location
        return context
