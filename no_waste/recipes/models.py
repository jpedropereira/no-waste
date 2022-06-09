from cgi import test
from operator import mod
from django.db import models

# Create your models here.




class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture_url = models.URLField()
    ingredients = models.CharField(max_length=500)
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.FloatField()
    sourceurl = models.URLField(unique=True)

class SearchQuery(models.Model):
    search_query = models.CharField(max_length=500)
    recipes = models.ManyToManyField(Recipe)

    