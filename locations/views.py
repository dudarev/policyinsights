from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, CreateView, ListView
from django.urls import reverse

from .models import Location
from .forms import LocationForm


class LocationCreateUpdateMixin():
    model = Location
    form_class = LocationForm

    def get_success_url(self):
        return reverse('location-detail', args=[self.object.slug])


class LocationCreate(LocationCreateUpdateMixin, CreateView):
    pass


class LocationDetail(DetailView):
    model = Location

    def get_context_data(self, **kwargs):
        context = super(LocationDetail, self).get_context_data()
        programs = self.object.program_set.all()
        context.update({'programs': programs})
        return context


class LocationUpdate(LocationCreateUpdateMixin, UpdateView):
    pass


class LocationsList(ListView):
    model = Location


def compare(request, pk1, pk2):
    try:
        l1 = Location.objects.get(pk=pk1)
        l2 = Location.objects.get(pk=pk2)
    except Location.DoesNotExist:
        raise Http404("Location does not exist")
    return render(request, 'locations/compare.html', {'l1': l1, 'l2': l2})
