from django.shortcuts import render
from django.http import HttpResponse
import requests
# from .forms import AnotherRecipeForm
from .models import RecipeForm


import json

# Create your views here.
# def apiRapid(request):
#     recipies_data = {}
    # url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
    #przerobic tam zeby tu byla zmienna i potem w dict tez zmienna jak na stackoverflow
    #query = "burger"

    # if 'food' in request.POST:
    #     form = RecipeForm(request.POST)
    #     if form.is_valid():
    #         recipies_data = form.search()
    # else:
    #     form = RecipeForm()
    
    # return render(request, 'fhapipage/api.html', {'form':form, 'recipe_data':recipies_data})


        # headers = {
        #     'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        #     'x-rapidapi-key': "e9501d69fbmsh5ec6484b5287032p13f36cjsn3eee13a92aa9"
        #     }
        # querystring = {"query":query}

        #response = requests.request("GET", url, headers=headers, params=querystring).json()
        # recipies_data.append(querystring)
        #TEST
        #recipies_data.append(response)
    # data =json.loads(response)
    # print(str(json.dumps(data, indent=2)))
    #WORKING WELL
    #print(response)
    
    #before: querystring:querystring
    # context = {'recipies_data':querystring, 'form':form}
    # return render(request, 'fhapipage/api.html', {'form':form, 'recipe_data':recipies_data})


#DRUGA WERSJA
# def recipeApi(request):
#     search_result = {}
#     if 'food' in request.POST:
#         form = AnotherRecipeForm(request.POST)

#         if form.is_valid():
#             search_result = form.search()
#     else:
#         form = AnotherRecipeForm()
    
#     return render(request, 'fhapipage/api.html', {'form':form, 'search_results':search_result})

def apiRapid(request):
    recipies_data = {}

    if 'food' in request.POST:
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipies_data = form.search()
    else:
        form = RecipeForm()
    return render(request, 'fhapipage/api.html', {'form':form, 'search_results':recipies_data})
