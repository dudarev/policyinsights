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

    cost = models.DecimalField(null=True, max_digits=12, decimal_places=2, default=None, blank=True)
    anual_cost = models.DecimalField(null=True, max_digits=12, decimal_places=2, default=None, blank=True)
    cost_per_household = models.DecimalField(null=True, max_digits=12, decimal_places=2, default=None, blank=True)
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=5,
        default='n'
    )
    type = models.CharField(
        choices=TYPE_CHOICES,
        max_length=5,
        default='n'
    )
    methodology = models.CharField(
        choices=METHODOLOGY_CHOICES,
        max_length=5,
        default='n'
    )
    description = models.TextField(null=True, max_length=1000, default=None, blank=True)
    years_active = models.TextField(null=True, max_length=200, default=None, blank=True)
    number_participants = models.IntegerField(null=True, default=None, blank=True)
    number_replicated = models.IntegerField(null=True, default=None, blank=True)
    number_iterations = models.IntegerField(null=True, default=None, blank=True)
    number_incidents = models.IntegerField(null=True, default=None, blank=True, verbose_name="Number of crime incidents")
    funding_source = models.CharField(max_length=200, null=True, default=None, blank=True)
    contact = models.TextField(null=True, max_length=1000, default=None, blank=True)

    def __str__(self):
        return self.name


class CaseStudy(models.Model):
    user_name = models.CharField(max_length=300, verbose_name='Name')
    email = models.EmailField(max_length=300)
    program_name = models.CharField(max_length=300)
    more_information = models.TextField(max_length=2000, blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} by {}'.format(self.program_name, self.user_name)
