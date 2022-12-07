from django.contrib import admin
from .models import Post
from .models import Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body']
    list_display = ['title', 'created_at']
    list_filter = ['created_at']

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email','body']
    list_display = ['name', 'email','created_at']
    list_filter = ['name','email','created_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)