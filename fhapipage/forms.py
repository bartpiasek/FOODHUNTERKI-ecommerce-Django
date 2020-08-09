from django.forms import ModelForm, TextInput
from .models import Recipe

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe']
        widgets = {'recipe': TextInput(attrs={'class':'input', 'placeholder':'Meal'})}