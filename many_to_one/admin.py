from django.contrib import admin
from .models import Manufacturer, Car

models = [Manufacturer, Car]
admin.site.register(models)
