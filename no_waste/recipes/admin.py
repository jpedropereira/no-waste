from django.contrib import admin


from recipes.models import Recipe, SearchQuery, MissingIngredient

# Register your models here.

admin.site.register(Recipe)
admin.site.register(SearchQuery)
admin.site.register(MissingIngredient)

