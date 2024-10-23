from django.db import models


class Professor(models.Model):
    class Skill(models.TextChoices):
        BAD = "bad", "Bad"
        OK = "ok", "Ok"
        GOOD = "good", "Good"

    name = models.CharField(max_length=255, primary_key=True)
    skill_level = models.CharField(max_length=4, choices=Skill.choices, default=Skill.OK)

    def __str__(self):
        return f"Professor {self.name}"


class Class(models.Model):
    name = models.CharField(max_length=255)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    max_student_number = models.IntegerField()

    def __str__(self):
        return f"{self.professor}'s {self.name}"


class Student(models.Model):
    name = models.CharField(max_length=255)
    avg_grade = models.FloatField(max_length=4)
    classes = models.ManyToManyField(Class)

    def __str__(self):
        return self.name
