import requests

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.conf import settings
from pygoogletranslation import Translator


from recipes.forms import GetRecipesForm
from recipes.models import Recipe, SearchQuery, MissingIngredient

API_ENDPOINT = settings.API_ENDPOINT
SPOONTACULAR_API_KEY = settings.SPOONTACULAR_API_KEY

#Create your views here.

class GetRecipesView(FormView):
    """This class renders the form generated to query recipes"""
    form_class = GetRecipesForm
    template_name = "recipes/get_recipes.html"
    success_url = "/recipes_list"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def get_spoontacular_data(include, exclude, number):
    """This function is used to collect recipe data from Spoontacular API"""
    
    recipe_config = {
        "apiKey": SPOONTACULAR_API_KEY,
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


def search_recipes_view(request):
    """This function renders a list with the recipes resulting from the user query"""

    #Gets and normalizes query data
    query_dict = request.GET
    ingredients_to_include = query_dict["ingredients_to_include"]
    ingredients_to_include = sorted(set(ingredients_to_include.split(",")))
    ingredients_to_include = ",".join(ingredients_to_include)
    
    
    ingredients_to_exclude = query_dict["ingredients_to_exclude"]
    ingredients_to_exclude = sorted(set(ingredients_to_exclude.split(",")))
    ingredients_to_exclude = ",".join(ingredients_to_exclude)

    recipes_number = query_dict["recipes_number"]

    search_query = f"incluide:{ingredients_to_include}|excluide:{ingredients_to_exclude}|count:{recipes_number}"

    #adds search query to db
    search = SearchQuery(search_query=search_query)
    search.save()

    
    
    #Retrieves recipes data matching user's query from Spoontacular API
    recipes_data = get_spoontacular_data(ingredients_to_include, ingredients_to_exclude, recipes_number)
    recipes_dict = recipes_data["results"]


    for recipe in recipes_dict:
        title = recipe["title"]
        picture = recipe["image"]
        ingredients = [ingredient["name"] for ingredient in recipe["nutrition"]["ingredients"]]
        missing_ingredients_count = recipe["missedIngredientCount"]
        carbs = recipe["nutrition"]["caloricBreakdown"]["percentCarbs"]
        proteins = recipe["nutrition"]["caloricBreakdown"]["percentProtein"]
        fats = recipe["nutrition"]["caloricBreakdown"]["percentFat"]
        calories = recipe["nutrition"]["nutrients"][0]["amount"]
        source_url = recipe["sourceUrl"]

        #adds recipe to database
        recipe_obj = Recipe(
            title=title,
            picture_url=picture,
            ingredients=ingredients,
            carbs=carbs,
            proteins=proteins,
            fats=fats,
            calories=calories,
            source_url=source_url
            )
        recipe_obj.save()

        search.recipes.add(recipe_obj)

        missing_count = MissingIngredient(count=missing_ingredients_count, recipe=recipe_obj, search_query=search)
        missing_count.save()
        




    # #Renders page    
    # context = {
    #     "recipes": recipes,
    # }
    return render(request, "recipes/recipes_list.html") #context=context)
