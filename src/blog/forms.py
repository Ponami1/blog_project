from django import forms
from .models import Post, Category, Profile, Comment


choices = Category.objects.all().values_list('name','name')
choice_list =[]
for choice in choices:
  choice_list.append(choice)
class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('image', 'title', 'title_tag', 'Author', 'category', 'body')
    
    widgets = {
      'title':forms.TextInput(),
      'title_tag':forms.TextInput(),
      'Author':forms.TextInput(attrs={'id':'author'}),
      #'Author':forms.Select(),
      'category':forms.Select(choices=choice_list),
      'body':forms.Textarea(attrs={'rows':3}),
  
    }
    
class EditPostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'title_tag', 'body')
    
    widgets = {
      'title':forms.TextInput(),
      'title_tag':forms.TextInput(),
      'body':forms.Textarea(attrs={'rows':3}),
    }
    
class CategoryPostForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = '__all__'

class ProfilePostForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = '__all__'

class EditProfilePostForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['bio', 'profile_image']
    
class CreateCommentPostForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['name', "body"]
    
        
    widgets = {
      'name':forms.TextInput(attrs={'readonly':'readonly'}),
      'body':forms.Textarea(attrs={'rows':3}),
    }