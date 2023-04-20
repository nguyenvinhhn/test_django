from django.db import models

# Create your models here.

# một chapter có nhiều level
class Level(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    img = models.CharField(max_length=255)

class Chapter(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    img = models.CharField(max_length=255)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True, default=None)
