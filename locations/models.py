from django.db import models


class Location(models.Model):
    slug = models.SlugField(max_length=200, null=False, unique=True)
    content = models.TextField(max_length=2000, blank=True, default='')

    def __str__(self):
        return self.slug