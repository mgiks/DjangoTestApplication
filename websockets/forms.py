from django import forms
from one_to_one.models import House, Family
from one_to_many.models import Blog, Post
from many_to_one.models import Manufacturer, Car
from many_to_many.models import Class, Professor, Student


# One to One
class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = "__all__"


class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = "__all__"


# One to Many
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


# Many to One
class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"


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
        fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
