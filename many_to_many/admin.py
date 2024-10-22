from .models import Class, Professor, Student
from django.contrib import admin

models = [Class, Professor, Student]

admin.site.register(models)
