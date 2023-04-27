from django.shortcuts import render
from .models import Article, ArticleComment

# Create your views here.


def index(request):
    articles = Article.objects.all().order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)