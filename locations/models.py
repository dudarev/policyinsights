from django.db import models


class Location(models.Model):
    slug = models.SlugField(max_length=200, null=False, unique=True, allow_unicode=True)
    content = models.TextField(max_length=2000, blank=True, default='')
    fips_code = models.CharField(max_length=7, blank=True, null=True, default=None,
                                 help_text='FIPS Code (2 digits for state, 5 digits for county, 7 digits for a place)',
                                 db_index=True)

    def __str__(self):
        return self.slug