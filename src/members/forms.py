from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
  checkbox = forms.BooleanField()
  class Meta:
    model = User
    fields = ["username", "email", "first_name", "last_name", "password1", "password2", "checkbox"]
    

    
class ProfileChangeForm(UserChangeForm):
  class Meta:
    model = User
    fields = ["username", "email","first_name", "last_name",]