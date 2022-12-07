from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)

def show(request, slug):
    post = get_object_or_404(Post, slug = slug)

    return render(request, 'show.html', {"post": post})