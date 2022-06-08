from operator import mod
from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    picture_url = models.URLField()
    ingredients = models.ManyToManyField(Ingredient)
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.FloatField()
    sourceurl = models.URLField()
