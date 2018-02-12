from django.contrib import admin

from interventions.models import InterventionCategory, Intervention, Location


class InterventionCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)


class InterventionAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)


admin.site.register(Intervention, InterventionAdmin)
admin.site.register(InterventionCategory, InterventionCategoryAdmin)
admin.site.register(Location)
