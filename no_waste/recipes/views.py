from xml.etree.ElementInclude import include
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

def get_translation(text):
    """This method translates English to Portuguese"""
    translator = Translator()
    translation = translator.translate(text=text, src="en", dest="pt")

    return translation


def get_recipes(include, exclude, count, query):
    """Builds Recipe and MissingIngredient objects based on a query and builds relationships with SearchQuery object"""

    #Retrieves recipes data matching user's query from Spoontacular API
    recipes_data = get_spoontacular_data(include, exclude, count)
    recipes_dict = recipes_data["results"]

    #Iterates through recipes dict to build Recipe and MissingIngredient objects
    for recipe in recipes_dict:
        title = recipe["title"]
        title_pt = get_translation(title)
        picture = recipe["image"]
        ingredients = [ingredient["name"] for ingredient in recipe["nutrition"]["ingredients"]]
        ingredients_pt = [get_translation(ingredient["name"]) for ingredient in recipe["nutrition"]["ingredients"]]
        missing_ingredients_count = recipe["missedIngredientCount"]
        carbs = recipe["nutrition"]["caloricBreakdown"]["percentCarbs"]
        proteins = recipe["nutrition"]["caloricBreakdown"]["percentProtein"]
        fats = recipe["nutrition"]["caloricBreakdown"]["percentFat"]
        calories = recipe["nutrition"]["nutrients"][0]["amount"]
        source_url = recipe["sourceUrl"]

        #adds recipe to database
        recipe_obj = Recipe(
            title=title,
            title_pt=title_pt,
            picture_url=picture,
            ingredients=ingredients,
            ingredients_pt=ingredients_pt,
            carbs=carbs,
            proteins=proteins,
            fats=fats,
            calories=calories,
            source_url=source_url
            )
        recipe_obj.save()

        query.recipes.add(recipe_obj)

        #builds MissingIngredient object
        missing_count = MissingIngredient(count=missing_ingredients_count, recipe=recipe_obj, search_query=query)
        missing_count.save()

        return None

def get_query(include, exclude, count):
    """This function searches the database for a search query. 
    If the related SearchQuery object exists in the db, it returns it. 
    If it doesn't, it creates the SearchQuery object, it fetches data from spoontacular API, builds the recipe objects 
    and missing count objects and builds the relationships
    and then returns the SearchQuery object"""

    search_expression = f"include:{include}|exclude:{exclude}|count:{count}"

    try:
        #tries to get query object
        search = SearchQuery.objects.get(search_query=search_expression)

    except:
        #builds query object
        search = SearchQuery(search_query=search_expression)
        search.save()

        get_recipes(include, exclude, count, search)


    return search


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

    query = get_query(include=ingredients_to_include, exclude=ingredients_to_exclude, count=recipes_number)

    

    
    # #Renders page    
    # context = {
    #     "recipes": recipes,
    
    return render(request, "recipes/recipes_list.html") #context=context)


