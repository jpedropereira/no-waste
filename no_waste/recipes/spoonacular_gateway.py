import requests
from django.conf import settings


class SpoonacularGateway:

    @classmethod
    def get_recipes(cls, include, exclude, number):
        """This function is used to collect recipe data from Spoontacular API"""
        recipes_endpoint = "/recipes/complexSearch"

        recipe_config = {
            "apiKey": settings.SPOONACULAR_API_KEY,
            "includeIngredients": include,
            "excludeIngredients": exclude,
            "instructionsRequired": True,
            "addRecipeNutrition": True,
            "sort": "min-missing-ingredients",
            "number": number,
        }

        response = requests.get(url=settings.API_ENDPOINT + recipes_endpoint, params=recipe_config)
        response.raise_for_status()
        recipes = response.json()

        return recipes
