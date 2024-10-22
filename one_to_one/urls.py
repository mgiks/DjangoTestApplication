from django.urls import path
from .views import (
    HouseListView,
    FamilyListView,
    HouseCreateView,
    FamilyCreateView,
    FamilyReadUpdateDeleteView,
    HouseReadUpdateDeleteView,
)


urlpatterns = [
    # Read
    path("houses/", HouseListView.as_view(), name="house_list"),
    path("families/", FamilyListView.as_view(), name="family_list"),

    # Create
    path("houses/create/", HouseCreateView.as_view(), name="house_create"),
    path("families/create/", FamilyCreateView.as_view(), name="house_create"),

    # Update/Delete
    path("houses/<int:pk>/", HouseReadUpdateDeleteView.as_view(), name="house_details"),
    path(
        "families/<int:pk>/",
        FamilyReadUpdateDeleteView.as_view(),
        name="family_details",
    ),
]
