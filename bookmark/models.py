from django.db import models

class Bookmark(models.Model):
    mane = models.CharField(max_length=10)
    models = models.URLField()
