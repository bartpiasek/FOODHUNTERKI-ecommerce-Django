from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Categories
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
#CLASS BASED VIEW
class HomeView(ListView):
    model = Post
    #IF FHBLOG - BLOG.HTML, WITHOUT FHBLOG - POST_LIST.HTML
    template_name = 'fhblog/blog.html'
    cats = Categories.objects.all()
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Categories.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'fhblog/category.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})


def CategoryListView(request):
    cat_list = Categories.objects.all()
    return render(request, 'fhblog/category_list.html', {'cat_list':cat_list})


class PostDetailView(DetailView):
    model = Post
    template_name = 'fhblog/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categories.objects.all()
        
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'fhblog/newpost.html'


class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'fhblog/post_update.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'fhblog/post_delete.html'
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Categories
    template_name = 'fhblog/category_add.html'
    fields = '__all__'