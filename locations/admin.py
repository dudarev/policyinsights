from django.contrib import admin

from .models import Location


class LocationAdmin(admin.ModelAdmin):
    search_fields = ['slug', 'fips_code',]


admin.site.register(Location, LocationAdmin)
