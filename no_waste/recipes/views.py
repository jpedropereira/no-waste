from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView
from django.conf import settings

from recipes.forms import GetRecipesForm
from recipes.models import Recipe, SearchQuery
from recipes.spoonacular_gateway import SpoonacularGateway
from recipes.utils import get_translation

API_ENDPOINT = settings.API_ENDPOINT
SPOONACULAR_API_KEY = settings.SPOONACULAR_API_KEY


# Create your views here.

class GetRecipesView(FormView):
    """This class renders the form generated to query recipes"""
    form_class = GetRecipesForm
    template_name = "recipes/get_recipes.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SearchRecipesView(View):
    """This class view renders a list with the recipes resulting from the user query"""

    def get_recipes(self, include, exclude, count, query):
        """Builds Recipe objects based on a query and builds relationships with SearchQuery object"""

        # Retrieves recipes data matching user's query from Spoontacular API
        recipes_data = SpoonacularGateway.get_recipes(include, exclude, count)
        recipes_dict = recipes_data["results"]

        # Iterates through recipes dict to build Recipe objects
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

            # tries to find recipe in database and add it to query object. If not found in DB, it creates it and add it to query.

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
                source_url=source_url,
                missing_ingredients_count=missing_ingredients_count
            )
            recipe_obj.save()
            query.recipes.add(recipe_obj)

        return None

    def get_search_query(self, include, exclude, count):
        """This function searches the database for a search query.
        If the related SearchQuery object exists in the db, it returns it.
        If it doesn't, it creates the SearchQuery object, it fetches data from spoontacular API,
        builds the recipe objects and the relationships and then returns the SearchQuery object"""

        search_expression = f"include:{include}|exclude:{exclude}|count:{count}"

        try:
            # tries to get query object
            search = SearchQuery.objects.get(search_query=search_expression)

        except SearchQuery.DoesNotExist:
            # builds query object if it doesn't exist
            search = SearchQuery(search_query=search_expression)
            search.save()

            self.get_recipes(include, exclude, count, search)

        return search

    def get(self, request):
        # Gets and normalizes query data
        query_dict = request.GET
        ingredients_to_include = query_dict["ingredients_to_include"]
        ingredients_to_include = sorted(set(ingredients_to_include.split(",")))
        ingredients_to_include = ",".join(ingredients_to_include)

        ingredients_to_exclude = query_dict["ingredients_to_exclude"]
        ingredients_to_exclude = sorted(set(ingredients_to_exclude.split(",")))
        ingredients_to_exclude = ",".join(ingredients_to_exclude)

        recipes_number = query_dict["recipes_number"]

        query_object = self.get_search_query(include=ingredients_to_include, exclude=ingredients_to_exclude,
                                        count=recipes_number)

        recipes = query_object.recipes.all()

        # Renders page
        context = {
            "recipes": recipes,
        }

        return render(request, "recipes/recipes_list.html", context=context)
