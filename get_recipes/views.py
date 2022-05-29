import os
import requests
from django.shortcuts import render
from django.views.generic.edit import FormView
from dotenv import load_dotenv

from .forms import GetRecipesForm

load_dotenv()

API_KEY = os.getenv("SPOONTACULAR_API_KEY")
API_ENDPOINT = "https://api.spoonacular.com/recipes/complexSearch"


#Create your views here.
class GetRecipesView(FormView):
    form_class = GetRecipesForm
    template_name = "get_recipes/get_recipes.html"
    success_url = "/recipes_list"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def get_spoontacular_data(include, exclude, number):
    recipe_config = {
        "apiKey": API_KEY,
        "includeIngredients": include,
        "excludeIngredients": exclude,
        "instructionsRequired": True,
        "addRecipeNutrition": True,
        "sort": "min-missing-ingredients",
        "number": number,
        }

    response = requests.get(url=API_ENDPOINT, params=recipe_config)
    response.raise_for_status()
    recipes = response.json()

    print(recipes)

    return recipes


def search_recipes(request):
    query_dict = request.GET
    ingredients_to_include = query_dict["ingredients_to_include"]
    ingredients_to_exclude = query_dict["ingredients_to_exclude"]
    recipes_number = query_dict["recipes_number"]

    recipes_data = get_spoontacular_data(ingredients_to_include, ingredients_to_exclude, recipes_number)
    recipes_dict = recipes_data["results"]

    context = {
        "recipes": recipes_dict
    }
    return render(request, "get_recipes/recipes_list.html", context=context)

