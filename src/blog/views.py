from django.shortcuts import render, redirect
from .models import Post, Category,Profile
from .forms import PostForm, EditPostForm, CategoryPostForm,ProfilePostForm, EditProfilePostForm, CreateCommentPostForm
from django.shortcuts import get_object_or_404
# Create your views here.

def Home(request):
  post = Post.objects.all()
  cats = Category.objects.all()
  
  context = {
    "post": post,
    "category_list":cats
    
  }
  return render(request, 'home.html', context=context)

def DetailPost(request, pk):
  post = get_object_or_404(Post, id=pk)
  comments = post.comments.filter(active=True)
  new_comment = None
  if request.method == "POST":
    comment_form = CreateCommentPostForm(request.POST)
    if comment_form.is_valid():
      new_comment = comment_form.save(commit=False)
      new_comment.name = request.user
      new_comment.post = post
      new_comment.save()
      print(new_comment)
  else:
    comment_form = CreateCommentPostForm()
  context = {
    "post": post,
    "new_comment":new_comment,
    "comments": comments,
    "comment_form":comment_form
  }
  
  return render(request, 'Detailview.html', context=context)

def CreatePost(request):
  if request.method ==  'POST': 
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('home')
  form = PostForm()
  context = {
    'form': form
  }
  return render(request, 'addblog.html', context=context)


def UpdatePost(request, pk):
  post = Post.objects.get(pk=pk)
  form = EditPostForm(instance=post)
  if request.method == 'POST':
    form = EditPostForm(request.POST or None, instance=post)
    if form.is_valid():
      form.save()
      return redirect('home')
  return render(request, 'update.html', {"form":form})

def DeletePost(request, pk):
  post = get_object_or_404(Post, id=pk)
  if request.method == 'GET':
      return render(request, 'DeletePost.html')
  elif request.method == 'POST':
    post.delete()
    return redirect('home')
  
  
def CategoryPost(request):
  if request.method ==  'POST': 
    form = CategoryPostForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  form = CategoryPostForm()
  context = {
    'form': form
  }
  return render(request, 'category.html', context=context)

def CategoryPage(request, cats):
  category_list = Post.objects.filter(category=cats)
  return render(request, 'categorypage.html', {'cat':cats, 'category':category_list})

def ShowProfilePage(request, pk):
  page_user =   get_object_or_404(Profile, id=pk)
  context = {
    "page_user": page_user,  
    }
  return render(request, 'registration/profile_page.html', context=context)


def UpdateProfile(request, pk):
  post = Profile.objects.get(pk=pk)
  form = EditProfilePostForm(instance=post)
  if request.method ==  'POST': 
    form = EditProfilePostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      form.save()
      return redirect('home')
  context = {
    'form': form
  }
  return render(request, 'registration/bio.html', context=context)


def CreateProfile(request):
  form = ProfilePostForm()
  if request.method ==  'POST': 
    form = ProfilePostForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('home')
  context = {
    'form': form
  }
  return render(request, 'registration/edit_bio.html', context=context)