from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    title_pt = models.CharField(max_length=200)
    picture_url = models.URLField()
    ingredients = models.CharField(max_length=500)
    ingredients_pt = models.CharField(max_length=500)
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.FloatField()
    source_url = models.URLField()
    missing_ingredients_count = models.IntegerField()

class SearchQuery(models.Model):
    search_query = models.CharField(max_length=500, unique=True)
    recipes = models.ManyToManyField(Recipe, related_name="recipes")

    class Meta:
        verbose_name_plural = "Search queries"



    