from django.db import models


class Post(models.Model):
    title = models.CharField(blank=True, default="", max_length=256)
    content = models.TextField(blank=True, default="")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(blank=True, default="", max_length=256)
    posts = models.ManyToManyField(Post, related_name="tags")
