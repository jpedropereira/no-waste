# NO WASTE!

No Waste is a Django application that collects users inputs regarding which ingredients they want to include or exclude and provides a list with a chosen number of recipes fitting the requirements.
Each recipe is displayed with its title, picture, list of ingredients already present, list of missing ingredients, carbs, proteins and calories. A suggestion on the what meal to prepare is generated based on which recipe has the minimum carbs and maximum proteins. 

## Requirements

In order to be able to use this application, you need to have an API key for Spoontacular's API (you can obtain it [here](https://spoonacular.com/food-api/) ). You should then assign the API key to an environment variable named "SPOONTACULAR_API_KEY".
A requirements.txt file is provided with this project.

## How to run the application

You can run the application by opening the command prompt cd to the directory where it is located and run `python manage.py runserver`. You can then access the application through your browser using the address [http://localhost:8000/get-recipes/](http://localhost:8000/get-recipes/)

## How to use

In order to query for recipes, you need to do the following:

- You need to insert the ingredients you want your recipes to contain separated by commas without spaces in between in the input box next to *What ingredients do you want to include?*. For example, if you want to obtain recipes containing bread, cheese and ham you should type: "*bread,cheese,ham*". This information is **mandatory**.

- If there are ingredients that you don't want your recipes to contain you can add them in the input box next to *What ingredients do you want to exclude?*. For example, if you want to obtain recipes that do not contain onion, garlic and bananas you should type: "*onion,garlic,bananas*". This information is **optional**.

- You need to define how many recipes you want to be shown in the input field next to *How many recipes do you want to see? (From 1 to 5)*. You must enter an integer number between 1 and 5. This information is **mandatory**

- Click the search bottom once all mandatory information is filled in.
