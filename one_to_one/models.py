from django.db import models
from django.utils.text import slugify


class Family(models.Model):
    slug = models.SlugField(primary_key=True, blank=True)
    lastname = models.CharField(max_length=255)
    number_of_members = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.lastname)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.lastname

    class Meta:
        # Django не знает правильную множественную форму :)
        verbose_name_plural = "Families"


class House(models.Model):
    slug = models.SlugField(primary_key=True, blank=True)
    house_address = models.CharField(max_length=255)
    family = models.OneToOneField(Family, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.house_address)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.house_address
