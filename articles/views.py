from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, ArticleComment, ArticleImage,Tag
from .forms import ArticleForm, ArticleCommentForm , ArticleImageForm
from django.contrib.auth.decorators import login_required
from datetime import date, datetime, timedelta
from django.db.models import Q
from django.contrib import messages



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
        form = ArticleForm(request.POST)
        images = request.FILES.getlist('image')
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            for i in images:
                ArticleImage.objects.create(article=article, image=i)
            return redirect('articles:index')       
        else:
            print(form.errors)
    else:
        form = ArticleForm()
        imageform = ArticleImageForm()
    context = {
        'form': form,
        'imageform' : imageform

    }
    return render(request, 'articles/create.html', context)



def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # view
    if request.user not in article.views.all():
        article.views.add(request.user)

    comment_form = ArticleCommentForm()
    comments = article.articlecomment_set.all()
    # tag_form = TagForm

    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments,
        # 'tag_form' : tag_form,
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
        comment = comment_form.save(commit=False)
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


@login_required
def bookmark(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.bookmark_user.filter(pk=request.user.pk).exists():
        article.bookmark_user.remove(request.user)
    else:
        article.bookmark_user.add(request.user)
    return redirect('articles:detail', article_pk)


@login_required
def comment_likes(request, article_pk, comment_pk):
    comment = ArticleComment.objects.get(pk=comment_pk)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    return redirect('articles:detail', article_pk)


@login_required
def comment_dislikes(request, article_pk, comment_pk):
    comment = ArticleComment.objects.get(pk=comment_pk)
    if comment.dislike_user.filter(pk=request.user.pk).exists():
        comment.dislike_user.remove(request.user)
    else:
        comment.dislike_user.add(request.user)
    return redirect('articles:detail', article_pk)



@login_required
def comment_delete(request, article_pk, comment_pk):
    comment = ArticleComment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)


def search(request):
    query = request.GET.get('q', '')
    if query:
        search = Article.objects.filter(
            Q(title__icontains=query)|
            Q(user__username__exact=query)
        )
    else:
        search = Article.objects.all()[::-1] 
    return render(request, 'articles/index.html', {'articles':search, 'app':'articles'})



# @login_required
# def tag_add(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     tag_form = TagForm(request.POST)
#     if tag_form.is_valid():
#         tag = tag_form.save(commit=False)
#         # tag, created = Tag.objects.get_or_create(name=tag.tag_content)
#         tag, created = Tag.objects.get_or_create(tag_content=tag.tag_content)
#         article.tagging.add(tag)
#         return redirect('articles:detail', article_pk)
#     else:
#         tag_form = TagForm()
#     context = {
#         'article' : article, 
#         'tag_form' : tag_form
#     }
#     return render(request, 'articles/tag_add.html', context)

# @login_required
# def hashtag(request, tag_pk):
#     hashtag = get_object_or_404(Tag, pk=tag_pk)
#     articles = hashtag.article_set.order_by('-pk')
#     context = {
#         'hashtag' : hashtag,
#         'articles' : articles
#     }
#     return render(request, 'articles/hashtag.html', context)