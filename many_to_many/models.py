from django.db import models

class Family(models.Model):
    lastname = models.CharField(max_length=255)
    number_of_members = models.IntegerField()

class House(models.Model):
    house_address = models.CharField(max_length=255, primary_key=True)
    family = models.ForeignKey(Family)
