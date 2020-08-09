from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Recipe
from .forms import RecipeForm

# Create your views here.
def apiRapid(request):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
    query = "burger"

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        form.save()

    form = RecipeForm()

    recipies = Recipe.objects.all()
    recipies_data = []

    for recipe in recipies:

        headers = {
            'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            'x-rapidapi-key': "e9501d69fbmsh5ec6484b5287032p13f36cjsn3eee13a92aa9"
            }
        querystring = {"query":query}

        response = requests.request("GET", url, headers=headers, params=querystring).json()
        recipies_data.append(querystring)
   
    # print(recipies_data)
    print(response)
    # print(response.text)

    #before: querystring:querystring
    context = {'recipies_data':querystring, 'form':form}
    return render(request, 'fhapipage/api.html', context)