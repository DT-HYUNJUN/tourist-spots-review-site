from django.shortcuts import render
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-pk')
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

