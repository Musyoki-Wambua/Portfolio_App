from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    decsription = models.TextField()
    technology = models.CharField(max_length=20)
