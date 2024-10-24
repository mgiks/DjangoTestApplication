from django.urls import path
from .views import render_form

urlpatterns = [path("", render_form, name="render_form")]
