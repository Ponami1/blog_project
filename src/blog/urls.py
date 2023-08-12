from django.urls import path
from .views import Home, DetailPost, CreatePost, UpdatePost, DeletePost, CategoryPost,CategoryPage, ShowProfilePage, CreateProfile, UpdateProfile

urlpatterns = [
  path('', Home, name='home'),
  path('article/<int:pk>/', DetailPost, name='blog_detail'),
  path('member/<int:pk>/profile_page', ShowProfilePage, name='show_profile'),
  path('member/profile_page/edit/<int:pk>', UpdateProfile, name='profile_edit'),
  path('member/profile_page/create_account', CreateProfile, name='profile_account'),
  path('article/create', CreatePost, name='create'),
  path('article/update/<int:pk>/', UpdatePost, name='update'),
  path('article/delete/<int:pk>/', DeletePost, name='delete'),
    path('category/<str:cats>/',CategoryPage, name='category_post'),
  path('article/create_category', CategoryPost, name='category'),
]