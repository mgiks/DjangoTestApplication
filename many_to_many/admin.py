from .models import Class, Professor, Student
from django.contrib import admin


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Class)