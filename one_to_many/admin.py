from django.contrib import admin
from .models import Blog, Post

models = [Blog, Post]
admin.site.register(models)
