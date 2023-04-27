from django.shortcuts import render
from posts.models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'pjt/index.html', context)