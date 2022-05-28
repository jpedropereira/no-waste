from django.shortcuts import render

# Create your views here.
def get_recipe(request):
    return render(request, "get_recipes/get_recipes.html")