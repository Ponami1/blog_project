from django.contrib import admin
from .models import Post, Category, Comment, Profile
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ["id", "Author",]
  list_filter = ['Author']
  search_fields = ["Author", "title"]
  #prepopulated_fields = {'slug': ('title',)}
  #date_hierarchy = 'published'
  #raw_id_fields = ['Author']
  
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ["name"]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ["user"]
  
@admin.register(Comment)
class ComentProfile(admin.ModelAdmin):
  list_display = ["post", "name", "date_added", "active"]
  actions = ["approve_comments"]
  
  def approve_comments(self, request, queryset):
    queryset.update(active=True)
