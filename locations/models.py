from django.db import models
from django.urls import reverse


class Location(models.Model):
    slug = models.SlugField(max_length=200, null=False, unique=True)
    content = models.TextField(max_length=2000, blank=True, default='')

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('location-detail', args=[self.slug, ])
