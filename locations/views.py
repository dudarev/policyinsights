from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, CreateView, ListView
from django.urls import reverse

from policyinsights.views import CompareView
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
        recent_locations = self.request.session.get('recent_locations', [])
        if not self.object.pk in recent_locations:
            recent_locations = [self.object.pk, ] + recent_locations
            recent_locations = recent_locations[:settings.NUMBER_OF_RECENT]
        self.request.session['recent_locations'] = recent_locations
        context = super(LocationDetail, self).get_context_data()
        programs = self.object.program_set.all()
        context.update({'programs': programs})
        return context


class LocationUpdate(LocationCreateUpdateMixin, UpdateView):
    pass


class LocationsList(ListView):
    model = Location


def compare_select(request, pk):
    try:
        l = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        raise Http404("Location does not exist")
    recent_locations_ids = request.session.get('recent_locations', []),
    recent_locations = Location.objects.filter(pk__in=recent_locations_ids[0])
    return render(
        request,
        'locations/compare_select.html',
        {
            'l': l,
            'recent_locations': recent_locations,
        }
    )


class LocationsCompare(CompareView):
    model = Location
    template = 'locations/compare.html'
