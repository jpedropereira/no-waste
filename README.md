# NO WASTE!

No Waste is a Django application that collects users inputs regardint which ingrediants they want to incluide or exclude and provides a list with a chosen number of recipes fitting the requirements.
Each recipe is displayed with its title, picture, list of ingredients already present, list of missing ingredients, carbs, proteins and calories. A suggestion on the what meal to prepare is generated based on which recipe has the minimum carbs and maximum proteins. 

## Requirements

In order to be able to use this application, you need to have an API key for Spoontacular's API (you can obtain it [here](https://spoonacular.com/food-api/) ). You should then assign the API key to an environment variable named "SPOONTACULAR_API_KEY".
A requirements.txt file is provided with this project.

## Licencing

MIT License

Copyright (c) 2022 Joao Pereira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

