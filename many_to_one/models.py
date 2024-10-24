from django.db import models
from django.utils.text import slugify


class Manufacturer(models.Model):
    slug = models.SlugField(primary_key=True, blank=True)
    name = models.CharField(max_length=255)
    revenue = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Car(models.Model):
    number_plate = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.color} {self.model} by {str(self.manufacturer)}"
