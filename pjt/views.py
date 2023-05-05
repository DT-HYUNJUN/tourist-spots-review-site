from django.shortcuts import render
from posts.models import Post
from articles.models import Article
from django.utils import timezone
# Create your views here.

def index(request):
    posts = Post.objects.order_by('-pk')[:4]
    new_posts(posts)
    articles = Article.objects.order_by('-pk')[:4]
    context = {
        'posts': posts,
        'articles': articles,
    }
    return render(request, 'pjt/index.html', context)


def new_posts(posts):
    now = timezone.now()
    for post in posts:
        time_diff = now - post.created_at
        if time_diff < timezone.timedelta(hours=1):
            post.is_new = True
        else:
            post.is_new = False