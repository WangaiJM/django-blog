from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)

def show(request, slug):
    post = get_object_or_404(Post, slug = slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            form.save()
            
            return redirect('show', slug = slug)
    else:
        form = CommentForm()

    return render(request, 'show.html', {"post": post, "form": form})