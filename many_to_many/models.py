from django.db import models
from django.utils.text import slugify


class Professor(models.Model):
    class Skill(models.TextChoices):
        BAD = "bad", "Bad"
        OK = "ok", "Ok"
        GOOD = "good", "Good"

    slug = models.SlugField(primary_key=True, blank=True)
    name = models.CharField(max_length=255)
    skill_level = models.CharField(
        max_length=4, choices=Skill.choices, default=Skill.OK
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Professor {self.name}"


class Class(models.Model):
    name = models.CharField(max_length=255)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    max_student_number = models.IntegerField()

    def __str__(self):
        return f"{self.professor}'s {self.name}"


class Student(models.Model):
    slug = models.SlugField(primary_key=True, blank=True)
    name = models.CharField(max_length=255)
    avg_grade = models.FloatField(max_length=4)
    classes = models.ManyToManyField(Class)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
