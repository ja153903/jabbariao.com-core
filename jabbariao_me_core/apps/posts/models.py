from django.db import models


class Post(models.Model):
    title = models.CharField(blank=True, default='', max_length=256)
    content = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)

