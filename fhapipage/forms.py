from django.forms import ModelForm, TextInput
from .models import Recipe
import requests

# class RecipeForm(ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ['recipe']
#         widgets = {'recipe': TextInput(attrs={'class':'input', 'placeholder':'Meal'})}


#INNA WERSJA
# class AnotherRecipeForm(ModelForm):
#     food = forms.CharField(max_length=2000)

# def search(self):
#     food = self.c_data['food']

#     url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

#     body = {"query":food,
#             "diet":"vegetarian",
#             "excludeIngredients":"coconut",
#             "intolerances":"egg%2C gluten",
#             "number":"10",
#             "offset":"0",
#             "type":"main course"
#         }

#     headers = {
#         'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
#         'x-rapidapi-key': "e9501d69fbmsh5ec6484b5287032p13f36cjsn3eee13a92aa9"
#         }

#     response = requests.request("POST", url, headers=headers, params=body)
#     #PARAMS TO DATA
#     params = response.json()

#     #tutaj jeszcze nie zmienione
#     return params['foods'][0]
#     print(response.text)

# class NutritionForm(forms.Form):
#     food = forms.CharField(max_length=100000)

# def search(self):
#     # result = {}
#     food = self.cleaned_data['food']

#     headers = {
#         'x-app-id': "ff0ccea8",
#         'x-app-key': "605660a17994344157a78f518a111eda",
#         'x-remote-user-id': "7a43c5ba-50e7-44fb-b2b4-bbd1b7d22632",
#         'Content-Type': "application/x-www-form-urlencoded",

#     }

#     url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
#     body = {
#         'query': food,
#         'timezone': 'US/Eastern',
#     }
#     response = requests.request("POST", url, data=body, headers=headers)
#     data = response.json()

#     print ('food name: ', data['foods'][0]['food_name'])
#     print ('food calories: ', data['foods'][0]['nf_calories'])
#     print ('food protein: ', data['foods'][0]['nf_protein'])
#     print ('food fats: ', data['foods'][0]['nf_total_fat'])