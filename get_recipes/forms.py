from django import forms

class GetRecipesForm(forms.Form):
    ingredients_to_include = forms.CharField(
        max_length=200,
        label="What ingredients do you want to incluide? Separate them with a comma and without spaces in between",
        required=True
        )
    ingredients_to_exclude = forms.CharField(
        max_length=200, 
        required=False
        )
    recipes_number = forms.IntegerField(
        min_value=0, 
        max_value=5,
        required=True
        )