from django import forms

class GetRecipesForm(forms.Form):
    ingredients_to_include = forms.CharField(
        max_length=200,
        label="What ingredients do you want to include?",
        required=True
        )
    ingredients_to_exclude = forms.CharField(
        max_length=200,
        label="What ingredients do you want to exclude?",
        required=False
        )
    recipes_number = forms.IntegerField(
        min_value=0, 
        max_value=5,
        label="How many recipes do you want to see? (From 1 to 5)",
        required=True
        )
        