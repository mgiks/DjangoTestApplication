from django.urls import path
from .views import (
    BlogListView,
    PostListView,
    BlogCreateView,
    PostCreateView,
    BlogReadUpdateDeleteView,
    PostReadUpdateDeleteView,
)

urlpatterns = [
    # Read
    path("blogs/", BlogListView.as_view(), name="blog_list"),
    path("posts/", PostListView.as_view(), name="post_list"),
    # Create
    path("blogs/create/", BlogCreateView.as_view(), name="blog_create"),
    path("posts/create/", PostCreateView.as_view(), name="post_create"),
    # Update/Delete
    path("blogs/<int:pk>/", BlogReadUpdateDeleteView.as_view(), name="blog_detail"),
    path("posts/<int:pk>/", PostReadUpdateDeleteView.as_view(), name="post_detail"),
]
