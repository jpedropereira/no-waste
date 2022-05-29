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
    print(request)
    context = {}
    return render(request, "get_recipes/recipes_list.html", context=context)
