from django.contrib import admin
from .models import Manufacturer, Car

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Car)
