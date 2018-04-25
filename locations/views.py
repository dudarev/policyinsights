from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, CreateView, ListView
from django.urls import reverse

from policyinsights.views import CompareView, CompareSelectView
from .models import Location, LocationComparison
from .forms import LocationForm


class LocationCreateUpdateMixin():
    model = Location
    form_class = LocationForm

    def get_success_url(self):
        return reverse('location-detail', args=[self.object.slug])


class LocationCreate(LoginRequiredMixin, LocationCreateUpdateMixin, CreateView):
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


class LocationUpdate(LoginRequiredMixin, LocationCreateUpdateMixin, UpdateView):
    pass


class LocationsList(ListView):
    model = Location


class LocationCompareSelect(CompareSelectView):
    model = Location
    template = 'locations/compare_select.html',
    recent_objects_str = 'recent_locations'


class LocationsCompare(CompareView):
    model = Location
    comparison_model = LocationComparison
    template = 'locations/compare.html'
