from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    revenue = models.IntegerField()

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    number_plate = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.color} {self.model} by {str(self.manufacturer)}"
