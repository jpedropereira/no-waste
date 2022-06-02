import os
import requests
from django.shortcuts import render
from django.views.generic.edit import FormView
from dotenv import load_dotenv
from pygoogletranslation import Translator

from .forms import GetRecipesForm

load_dotenv()

API_KEY = os.getenv("SPOONTACULAR_API_KEY")
API_ENDPOINT = "https://api.spoonacular.com/recipes/complexSearch"


#Create your views here.

class GetRecipesView(FormView):
    """This class renders the form generated to query recipes"""
    form_class = GetRecipesForm
    template_name = "get_recipes/get_recipes.html"
    success_url = "/recipes_list"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def get_spoontacular_data(include, exclude, number):
    """This function is used to collect recipe data from Spoontacular API"""
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

    return recipes

def translate_recipes(recipe):
    """This function translates text in English to Portuguese"""
    translator = Translator()
    translation = translator.translate(text=recipe, src="en", dest="pt")
    return translation


class Recipe:
    """This class represents recipes"""
    def __init__(self, title, picture, ingredients, requested_ingredients, carbs, proteins, fats, calories, sourceurl):
        self.title_en = title
        self.picture = picture
        self.ingredients = ingredients
        self.requested_ingredients = requested_ingredients.split(",")
        self.missing_ingredients = [ingredient for ingredient in self.requested_ingredients if ingredient not in self.ingredients]
        self.carbs = carbs
        self.proteins = proteins
        self.fats = fats
        self.calories = calories
        self.sourceurl = sourceurl



def search_recipes_view(request):
    """This function renders a list with the recipes resulting from the user query"""
    query_dict = request.GET
    ingredients_to_include = query_dict["ingredients_to_include"]
    ingredients_to_exclude = query_dict["ingredients_to_exclude"]
    recipes_number = query_dict["recipes_number"]

    recipes_data = get_spoontacular_data(ingredients_to_include, ingredients_to_exclude, recipes_number)
    recipes_dict = recipes_data["results"]

    recipes = [] 

    for recipe in recipes_dict:
        title = recipe["title"]
        image = recipe["image"]
        ingredients = [ingredient["name"] for ingredient in recipe["nutrition"]["ingredients"]]
        requested_ingredients = ingredients_to_include
        carbs = recipe["nutrition"]["caloricBreakdown"]["percentCarbs"]
        proteins = recipe["nutrition"]["caloricBreakdown"]["percentProtein"]
        fats = recipe["nutrition"]["caloricBreakdown"]["percentProtein"]
        calories = recipe["nutrition"]["nutrients"][0]["amount"]
        source_url = recipe["sourceUrl"]


        recipe_obj = Recipe(title, image, ingredients, requested_ingredients, carbs, proteins, fats, calories, source_url)
        recipes.append(recipe_obj)
        
    context = {
        "recipes": recipes,
    }
    return render(request, "get_recipes/recipes_list.html", context=context)

