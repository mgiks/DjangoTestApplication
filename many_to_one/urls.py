from django.urls import path
from .views import (
    ManufacturerListView,
    CarListView,
    ManufacturerCreateView,
    CarCreateView,
    ManufacturerReadUpdateDeleteView,
    CarReadUpdateDeleteView,
)

urlpatterns = [
    # Read
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer_list"),
    path("cars/", CarListView.as_view(), name="car_list"),
    # Create
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer_create",
    ),
    path("cars/create/", CarCreateView.as_view(), name="car_create"),
    # Update/Delete
    path(
        "manufacturers/<str:pk>/",
        ManufacturerReadUpdateDeleteView.as_view(),
        name="manufacturer_detail",
    ),
    path("cars/<int:pk>/", CarReadUpdateDeleteView.as_view(), name="car_detail"),
]
