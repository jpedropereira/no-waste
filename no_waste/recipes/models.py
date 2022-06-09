from cgi import test
from operator import mod
from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    picture_url = models.URLField()
    ingredients = models.CharField()
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.FloatField()
    sourceurl = models.URLField()
