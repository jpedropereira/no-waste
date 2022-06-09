from django.contrib import admin
from recipes.models import Recipe, Ingredient

# Register your models here.

class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)

