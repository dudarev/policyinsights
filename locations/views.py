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
