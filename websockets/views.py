from django.shortcuts import render
from .forms import (
    HouseForm,
    FamilyForm,
    BlogForm,
    PostForm,
    ManufacturerForm,
    CarForm,
    ClassForm,
    ProfessorForm,
    StudentForm,
)


def render_form(request):
    house_form = HouseForm()
    family_form = FamilyForm()
    blog_form = BlogForm()
    post_form = PostForm()
    manufacturer_form = ManufacturerForm()
    car_form = CarForm()
    class_form = ClassForm()
    professor_form = ProfessorForm()
    student_form = StudentForm()

    return render(
        request,
        "websockets/index.html",
        context={
            "house_form": house_form,
            "family_form": family_form,
            "blog_form": blog_form,
            "post_form": post_form,
            "manufacturer_form": manufacturer_form,
            "car_form": car_form,
            "class_form": class_form,
            "professor_form": professor_form,
            "student_form": student_form,
        },
    )
