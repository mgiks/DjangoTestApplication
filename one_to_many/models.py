from django.db import models


class Blog(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    author = models.CharField(max_length=100)
    status = models.CharField(
        max_length=9, choices=Status.choices, default=Status.ACTIVE
    )

    def __str__(self):
        return f"{self.author}'s blog"


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    from_blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
