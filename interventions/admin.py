from django.contrib import admin

from interventions.models import Intervention, Location


class InterventionAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)

admin.site.register(Intervention, InterventionAdmin)
admin.site.register(Location)
