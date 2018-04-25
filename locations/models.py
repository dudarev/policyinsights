from django.db import models
from django.urls import reverse

from policyinsights.models import ComparisonManager


class Location(models.Model):
    slug = models.SlugField(max_length=200, null=False, unique=True)
    content = models.TextField(max_length=2000, blank=True, default='')

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('location-detail', args=[self.slug, ])


class LocationsComparisonManager(ComparisonManager):
    compared_model = Location


class LocationComparison(models.Model):
    object_1 = models.ForeignKey('locations.Location', on_delete=models.CASCADE, related_name='comparison_1')
    object_2 = models.ForeignKey('locations.Location', on_delete=models.CASCADE, related_name='comparison_2')
    objects = LocationsComparisonManager()  # we use it so that order of locations is not relevant during comparison

    def __str__(self):
        return "{} - {}".format(self.object_1.slug, self.object_2.slug)

    def get_absolute_url(self):
        return reverse('location-comparison', args=[self.object_1.pk, self.object_2.pk ])
