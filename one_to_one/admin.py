from django.contrib import admin
from .models import House, Family

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("house_address",)}


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("lastname",)}
