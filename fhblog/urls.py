from django.urls import path

#CLASS BASED VIEW URLS
from .views import HomeView, PostDetailView, AddPostView, \
    EditPostView, DeletePostView, AddCategoryView, CategoryView, \
    CategoryListView

#CLASS BASED VIEW URLS - as_view()
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('add_post/', AddPostView.as_view(), name="post-new"),
    path('post/edit_post/<int:pk>', EditPostView.as_view(), name="post-edit"),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name="post-delete"),
    path('add_category/', AddCategoryView.as_view(), name="category-new"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category-list"),
    ]

