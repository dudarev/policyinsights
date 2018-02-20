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


class LocationUpdate(LocationCreateUpdateMixin, UpdateView):

    pass


class LocationsList(ListView):

    model = Location
