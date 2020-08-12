from django.urls import path
# from . import views

#CLASS BASED VIEW URLS
from .views import HomeView, PostDetailView, AddPostView, EditPostView, DeletePostView


urlpatterns = [
    # path('', views.home, name='home'),
    # path('about/', views.about, name='about'),

    #CLASS BASED VIEW URLS - as_view()
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('add_post/', AddPostView.as_view(), name="post-new"),
    path('post/edit_post/<int:pk>', EditPostView.as_view(), name="post-edit"),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name="post-delete"),
]

