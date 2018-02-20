from django.db import models


class Program(models.Model):
    location = models.ForeignKey('locations.Location', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, null=False)
    content = models.TextField(max_length=2000, blank=True, default='')

    class Meta:
        unique_together = ['location', 'slug']

    def __str__(self):
        return '{} @ {}'.format(self.slug, self.location.slug)
