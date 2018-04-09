from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Program(models.Model):
    location = models.ForeignKey('locations.Location', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, null=False)
    content = models.TextField(max_length=2000, blank=True, default='')

    class Meta:
        unique_together = ['location', 'slug']

    def __str__(self):
        return '{} @ {}'.format(self.slug, self.location.slug)

    def get_absolute_url(self):
        return reverse('program-detail', args=[self.location.slug, self.slug])


# this is hack so that a separate object could be passed to django-start-ratings
class ProgramImportance(models.Model):
    program = AutoOneToOneField(Program, primary_key=True, on_delete=models.CASCADE, related_name='importance')


class UserProgram(models.Model):
    program = models.ForeignKey('programs.Program', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'program']
