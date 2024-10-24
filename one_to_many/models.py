from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    slug = models.SlugField(primary_key=True, blank=True)
    author = models.CharField(max_length=100)
    status = models.CharField(
        max_length=9, choices=Status.choices, default=Status.ACTIVE
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.author)
        super().save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.slug = slugify(self.author)
        super().update(*args, **kwargs)

    def __str__(self):
        return f"{self.author}'s blog"


class Post(models.Model):
    slug = models.SlugField(primary_key=True, blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    from_blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
