from django.contrib import admin


from no_waste.recipes.models import Recipe, SearchQuery

# Register your models here.

admin.site.register(Recipe)
admin.site.register(SearchQuery)


