from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import GetRecipesForm

# Create your views here.
class GetRecipesView(FormView):
    form_class = GetRecipesForm
    template_name = "get_recipes/get_recipes.html"
    success_url = "/recipes_list"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def search_recipes(request):
    query_dict = request.GET
    ingredients_to_include = query_dict["ingredients_to_include"]
    ingredients_to_exclude = query_dict["ingredients_to_exclude"]
    recipes_number = query_dict["recipes_number"]
    print(ingredients_to_include)
    context = {
        "ingredients_to_include": ingredients_to_include,
        "ingredients_to_exclude": ingredients_to_exclude,
        "recipes_number": recipes_number,
    }
    return render(request, "get_recipes/recipes_list.html", context=context)
