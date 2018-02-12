from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class InterventionCategory(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Intervention categories"

    def __str__(self):
        return '{}, {}'.format(self.name, self.location.name)


class Intervention(models.Model):
    category = models.ForeignKey(InterventionCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
