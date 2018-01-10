from django.contrib import admin
from django_geonames.browser.models import City


class CityAdmin(admin.ModelAdmin):
    fields = ('name', 'latitude', 'longitude', 'country_code')
    actions = None
    list_display = fields
    search_fields = fields


admin.site.register(City, CityAdmin)
