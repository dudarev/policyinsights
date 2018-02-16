from django.contrib import admin

from interventions.models import InterventionCategory, Intervention, Location, CaseStudy


class InterventionCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)


class InterventionAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)


class CaseStudyAdmin(admin.ModelAdmin):
    readonly_fields = ('added_at',)


admin.site.register(Intervention, InterventionAdmin)
admin.site.register(InterventionCategory, InterventionCategoryAdmin)
admin.site.register(Location)
admin.site.register(CaseStudy, CaseStudyAdmin)
