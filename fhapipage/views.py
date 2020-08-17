from django.shortcuts import render
from django.http import HttpResponse
import requests
# from .forms import AnotherRecipeForm
# from .models import RecipeForm
import json

# Create your views here.
def apiRapid(request):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

    querystring = {
        "diet":"vegetarian",
        "excludeIngredients":"coconut",
        "intolerances":"egg%2C gluten",
        "number":"9",
        "offset":"0",
        "type":"main course",
        "query":"burger"}

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "e9501d69fbmsh5ec6484b5287032p13f36cjsn3eee13a92aa9",
        'Content-Type': "application/json"
        }

    recipe_ids = []
    response = requests.request("GET", url, headers=headers, data=querystring)
    
    #     data = response.json() # przy tym sposobie mam results zapelnione []!!!
    
    results = response.json()['results']

    for result in results:
        recipe_ids.append(result['title'])
    
    recipe_params = {
        'id': ', '.join(recipe_ids) 
    }

    r = requests.get(url, params=recipe_params, headers=headers)

    resultstwo = print(r.json()['results'])

    recipes = []
    for result in results:
        # print(result['title'])
        # print(result['id'])
        # print(result['sourceUrl'])
        # print(result['image'])
        recipe_data = {
            'title': result['title'],
            'id': result['id'],
            'url': result['sourceUrl'],
            'img': result['image'],
            'min': result['readyInMinutes']
        }
        recipes.append(recipe_data)

    #PRINTUJE TO - DZIAŁA
    # print(recipes)

   
    context = {
        # 'title': result['title'],
        # 'id': result['id'],
        # 'url': result['sourceUrl'],
        # 'img': result['image']
        'recipes': recipes
    }

    return render(request, 'fhapipage/api.html', context)




#DODATKOWY WARUNEK PRZED POBRANIEM API
# def apiRapid(request):
#     recipies_data = {}

#     if 'food' in request.POST:
#         form = RecipeForm(request.POST)
#         if form.is_valid():
#             recipies_data = form.search()
#     else:
#         form = RecipeForm()
#     return render(request, 'fhapipage/api.html', {'form':form, 'search_results':recipies_data})