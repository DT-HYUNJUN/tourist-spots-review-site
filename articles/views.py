from django.shortcuts import render, redirect
from .models import Article, ArticleComment
from .forms import ArticleForm, ArticleCommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    articles = Article.objects.all().order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


@login_required
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')


@login_required
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid(): 
                form.save()
                return redirect('articles:detail', article_pk)
        else:
            form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


@login_required
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = ArticleCommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commite=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article_pk)
    context = {
        'article' : article,
        'comment_form' : comment_form
    }
    return render(request, 'articles/detail.html', context)


@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:detail', article_pk)
