from django.contrib import admin
from .models import House, Family

models = [House, Family]
admin.site.register(models)
