from django import forms
from .models import Post, Categories


choices = Categories.objects.all().values_list('cat_name','cat_name')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'content', 'snippet', 'post_thumbnail_image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Tytuł posta'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Treść posta'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'snippet')
    
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Tytuł posta'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Treść posta'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
        }