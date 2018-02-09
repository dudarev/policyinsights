from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Intervention(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
