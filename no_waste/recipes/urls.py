from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetRecipesView.as_view()),
    path("search/", views.search_recipes_view)
    ]