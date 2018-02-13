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

    STATUS_CHOICES = (
        ('n', 'None'),
        ('pl', 'Planning'),
        ('pr', 'In Progress'),
        ('co', 'Complete'),
    )
    TYPE_CHOICES = (
        ('n', 'None'),
        ('rb', 'Rebate'),
        ('te', 'Tax Expenditure'),
        ('co', 'Communication'),
        ('pa', 'Predictive Analysis'),
    )
    METHODOLOGY_CHOICES = (
        ('n', 'None'),
        ('rct', 'RCT'),
        ('iv', 'Instrumental Variables'),
        ('rd', 'Regression Discontinuity'),
    )

    cost = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=5
    )
    type = models.CharField(
        choices=TYPE_CHOICES,
        max_length=5
    )
    methodology = models.CharField(
        choices=METHODOLOGY_CHOICES,
        max_length=5
    )

    def __str__(self):
        return self.name
