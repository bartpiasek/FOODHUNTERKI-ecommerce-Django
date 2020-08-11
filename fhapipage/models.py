from django.db import models
import requests
import json

# Create your models here.
class RecipeForm(models.Model):
    food = models.CharField(max_length=500)

    def search(self):
        food = self.cleaned_data['food']

    headers = {
            'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            'x-rapidapi-key': "e9501d69fbmsh5ec6484b5287032p13f36cjsn3eee13a92aa9"
    }

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

    querystring = {
        "diet":"vegetarian",
        "excludeIngredients":"coconut",
        "intolerances":"egg%2C gluten",
        "number":"10",
        "offset":"0",
        "type":"main course",
        "query":food
        }
    # jak params to printuje jedno, jak data=quersytring to duzo
    # chyba jest dobrze, ale to wtedy nie dopisuje do results
    response = requests.request("GET", url, headers=headers, data=querystring)

    if (response.status_code != requests.codes.ok):
        print ('error')
    else:
    #data = json.dumps(response, indent=4, sort_keys=True)
        data = response.json() # przy tym sposobie mam results zapelnione []!!!
    #tata = json.loads(data)
        print(data)
        
        #DUMPS
        #data = json.dumps(response.json(), indent=4)
        #print(data)
        #zrobic return jakis i na html?


