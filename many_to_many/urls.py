from django.urls import path
from .views import (
    ClassListView,
    StudentListView,
    ProfessorListView,
    ClassCreateView,
    StudentCreateView,
    ProfessorCreateView,
    ClassReadUpdateDeleteView,
    StudentReadUpdateDeleteView,
    ProfessorReadUpdateDeleteView,
)

urlpatterns = [
    # Read
    path("classes/", ClassListView.as_view(), name="class_list"),
    path("students/", StudentListView.as_view(), name="student_list"),
    path("professors/", ProfessorListView.as_view(), name="professor_list"),
    # Create
    path("classes/create/", ClassCreateView.as_view(), name="class_create"),
    path("students/create/", StudentCreateView.as_view(), name="student_create"),
    path("professors/create/", ProfessorCreateView.as_view(), name="professor_create"),
    # Update/Delete
    path("classes/<int:pk>/", ClassReadUpdateDeleteView.as_view(), name="class_detail"),
    path(
        "students/<int:pk>/",
        StudentReadUpdateDeleteView.as_view(),
        name="student_detail",
    ),
    path(
        "professors/<int:pk>/",
        ProfessorReadUpdateDeleteView.as_view(),
        name="professor_detail",
    ),
]
