from django.db import models


class Post(models.Model):
    title = models.CharField(blank=True, default="", max_length=256)
    content = models.TextField(blank=True, default="")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(blank=True, default="", max_length=256, primary_key=True)
    posts = models.ManyToManyField(Post, related_name="tags")


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    # Note here that for replies, we have to make sure that we can still render old replies
    parent = models.ForeignKey("self", null=True, related_name="replies", on_delete=models.DO_NOTHING)
    content = models.CharField(blank=True, default="", max_length=140)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
