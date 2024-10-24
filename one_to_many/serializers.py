from .models import Blog, Post
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["author", "status"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "body", "from_blog"]
