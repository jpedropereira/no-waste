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
    source_url = models.URLField(unique=True)

class SearchQuery(models.Model):
    search_query = models.CharField(max_length=500, unique=True)
    recipes = models.ManyToManyField(Recipe, related_name="recipes")

    class Meta:
        verbose_name_plural = "Search queries"

class MissingIngredient(models.Model):
    missing_ingredient_count = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe")
    search_query = models.ForeignKey(SearchQuery, on_delete=models.CASCADE, related_name="query")


    