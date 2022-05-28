from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetRecipesView.as_view()),
    path("recipes_list", views.recipes_list)
]
