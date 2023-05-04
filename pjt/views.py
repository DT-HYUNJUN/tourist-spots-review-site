from django.shortcuts import render
from posts.models import Post
from articles.models import Article
# Create your views here.

def index(request):
    posts = Post.objects.order_by('-pk')[:4]
    articles = Article.objects.order_by('-pk')[:4]
    context = {
        'posts': posts,
        'articles': articles,
    }
    return render(request, 'pjt/index.html', context)