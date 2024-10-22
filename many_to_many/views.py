from .models import Class, Professor, Student
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import ClassSerializer, ProfessorSerializer, StudentSerializer


# Read
class ClassListView(ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ProfessorListView(ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


# Create
class ClassCreateView(CreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class StudentCreateView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ProfessorCreateView(CreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


# Update/Delete
class ClassReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class StudentReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ProfessorReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
