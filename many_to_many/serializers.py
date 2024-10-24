from .models import Class, Professor, Student
from rest_framework import serializers


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ["name", "skill_level"]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "avg_grade", "classes"]
