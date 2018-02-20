from django.views.generic import DetailView, UpdateView, CreateView
from django.urls import reverse_lazy, reverse

from .models import Location


class LocationCreate(CreateView):

    model = Location
    fields = ['content', 'slug', ]
    success_url = '/'

    def get_success_url(self):
        return reverse('location-detail', args=[self.object.slug])


class LocationDetail(DetailView):

    model = Location


class LocationUpdate(UpdateView):

    model = Location
    fields = ['content', 'slug', ]

    def get_success_url(self):
        return reverse('location-detail', args=[self.object.slug])
