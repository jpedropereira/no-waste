# NO WASTE!

No Waste is a Django application that seeks to minimize waste by providing users with recipes that they can cook with the ingredients they have available. 
The application collects users inputs regarding which ingredients should be included or excluded and provides a list with a chosen number of recipes fitting the requirements.
Each recipe is displayed with its title, picture, list of ingredients already present, list of missing ingredients, carbs, proteins and calories.

## How do does it work

Each time a user requests a meal, the application searches for it in the database. 
If this query exists in the database, the application displays the recipes associated with it. 
If the query doesn't exist, the application sends a call to Spoonacular's api in order to obtain the related data, adds the query and recipes to the database and displays the recipes to the user. This approach allows us to minimize the number of api calls.  

## Requirements

In order to be able to use this application, you need to have an API key for Spoontacular's API (you can obtain it [here](https://spoonacular.com/food-api/) ) 
and Docker installed in your machine. 

You need to create a .env file with the required environment variables. 
You can use for reference the .env.example file provided and add your django secret key and your Spoonacular API key.

## How to run the application

You should run the application through Docker. 
To perform the required migrations to be able to run the app, 
you should run in cmd `docker-compose run no_waste python manage.py migrate`. 
Once the migrations are made, you can run the application's container through `docker-compose up no_waste`.

You can then access the application through your browser using the address [http://localhost:8000/get-recipes/](http://localhost:8000/get-recipes/)

## How to use

In order to query for recipes, you need to do the following:

- You need to insert the ingredients you want your recipes to contain separated by commas without spaces in between in the input box next to *What ingredients do you want to include?*. For example, if you want to obtain recipes containing bread, cheese and ham you should type: "*bread,cheese,ham*". This information is **mandatory**.

- If there are ingredients that you don't want your recipes to contain you can add them in the input box next to *What ingredients do you want to exclude?*. For example, if you want to obtain recipes that do not contain onion, garlic and bananas you should type: "*onion,garlic,bananas*". This information is **optional**.

- You need to define how many recipes you want to be shown in the input field next to *How many recipes do you want to see? (From 1 to 5)*. You must enter an integer number between 1 and 5. This information is **mandatory**

- Click the search bottom once all mandatory information is filled in.
