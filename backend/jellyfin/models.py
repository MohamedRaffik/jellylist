from django.db import models


class JellyfinServer(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    api_key = models.CharField(max_length=255)
