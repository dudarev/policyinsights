from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from policyinsights.models import ComparisonManager


class Program(models.Model):
    location = models.ForeignKey('locations.Location', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, null=False)
    content = models.TextField(max_length=2000, blank=True, default='')
    search_keywords = models.CharField(max_length=200, null=True, default=None)

    class Meta:
        unique_together = ['location', 'slug']

    def __str__(self):
        return '{} @ {}'.format(self.slug, self.location.slug)

    def get_absolute_url(self):
        return reverse('program-detail', args=[self.location.slug, self.slug])
    
    def save(self):
        for line in self.content.splitlines():
            if line.startswith('search_keywords:'):
                self.search_keywords = line.split(':', 1)[1].strip()[:200]
        super(Program, self).save()


# this is hack so that a separate object could be passed to django-start-ratings
class ProgramImportance(models.Model):
    program = AutoOneToOneField(Program, primary_key=True, on_delete=models.CASCADE, related_name='importance')


class UserProgram(models.Model):
    program = models.ForeignKey('programs.Program', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'program']


class ProgramsComparisonManager(ComparisonManager):
    compared_model = Program


class ProgramComparison(models.Model):
    object_1 = models.ForeignKey('programs.Program', on_delete=models.CASCADE, related_name='comparison_1')
    object_2 = models.ForeignKey('programs.Program', on_delete=models.CASCADE, related_name='comparison_2')
    objects = ProgramsComparisonManager()  # we use it so that order of programs is not relevant during comparison

    def __str__(self):
        return "{} - {}".format(self.object_1.slug, self.object_2.slug)

    def get_absolute_url(self):
        return reverse('program-comparison', args=[self.object_1.pk, self.object_2.pk ])
