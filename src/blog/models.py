from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import readtime

class Category(models.Model):
  name = models.CharField(max_length=300)

class Profile(models.Model):
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  bio = RichTextField()
  profile_image = models.ImageField(null=True, blank=True, upload_to="Images/profile/")
  
  def __str__(self):
    return str(self.user)

class Post(models.Model):
  title = models.CharField(max_length=500)
  image = models.ImageField(null=True, blank=True, upload_to="Images/")
  title_tag = models.CharField(max_length=300, default='default blog post')
  Author = models.ForeignKey(User, on_delete=models.CASCADE)
  body = RichTextField()
  category = models.CharField(max_length=300, default='coding')
  
  def __str__(self):
    return self.title
  
  def get_readtime(self):
     result = readtime.of_text(self.body)
     return result
   
class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
  name = models.ForeignKey(User, on_delete=models.CASCADE)
  #name = models.CharField(max_length=300)
  body = RichTextField()
  date_added = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=False)
  
  def __str__(self) :
    return '%s - %s' %(self.post.title, self.name)
  