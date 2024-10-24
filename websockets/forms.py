from django import forms
from one_to_one.models import House, Family
from one_to_many.models import Blog, Post
from many_to_one.models import Manufacturer, Car
from many_to_many.models import Class, Professor, Student


# One to One
class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        exclude = ["slug"]


class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        exclude = ["slug"]


# One to Many
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ["slug"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["slug"]


# Many to One
class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        exclude = ["slug"]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


# Many to Many
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = "__all__"


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        exclude = ["slug"]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ["slug"]
