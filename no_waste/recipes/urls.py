from django.urls import path
from recipes import views

urlpatterns = [
    path("", views.GetRecipesView.as_view()),
    path("search/", views.SearchRecipesView.as_view())
    ]
