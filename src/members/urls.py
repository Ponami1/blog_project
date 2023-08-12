from django.urls import path
from .views import Register, Profile,PasswordChange,activate



urlpatterns = [
  path('register', Register, name='register'),
  path('edit_profile', Profile, name='edit_user'),
  path('password/',PasswordChange, name='change_password'),
  path('activate/<uidb64>/<token>', activate, name='activate') 

]