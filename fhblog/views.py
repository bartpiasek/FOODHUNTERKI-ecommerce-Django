from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Categories
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
# from .models import *


# Create your views here.
# def home(request):
#     return render(request, 'fhblog/blog.html')

#CLASS BASED VIEW
class HomeView(ListView):
    model = Post
    #IF FHBLOG - BLOG.HTML, WITHOUT FHBLOG - POST_LIST.HTML
    template_name = 'fhblog/blog.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'fhblog/post_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'fhblog/newpost.html'
    # fields = '__all__'

class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'fhblog/post_update.html'
    # fields = {'title', 'content'}

class DeletePostView(DeleteView):
    model = Post
    template_name = 'fhblog/post_delete.html'
    success_url = reverse_lazy('home')

