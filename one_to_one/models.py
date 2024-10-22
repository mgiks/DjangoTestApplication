from django.db import models


class Family(models.Model):
    lastname = models.CharField(max_length=255)
    number_of_members = models.IntegerField()

    def __str__(self):
        return self.lastname

    class Meta:
        # Django не знает правильную множественную форму :)
        verbose_name_plural = "Families"


class House(models.Model):
    house_address = models.CharField(max_length=255)
    family = models.OneToOneField(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.house_address
