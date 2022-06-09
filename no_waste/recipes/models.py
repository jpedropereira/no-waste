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

class MissingIngredients(models.Model):
    count = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    search_query = models.ForeignKey(SearchQuery, on_delete=models.CASCADE)


    