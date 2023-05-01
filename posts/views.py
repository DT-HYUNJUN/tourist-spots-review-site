from datetime import timezone
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, PostComment
from .forms import PostForm, PostCommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# import requests

# Create your views here.
"""
def search_keyword(keyword):
    searching = keyword
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(searching)
    headers = {
        "Authorization": "KakaoAK 2caddc4f25bdd55869865a211f7d13bb"
    }
    places = requests.get(url, headers = headers).json()['documents']
    lst = []
    for place in places:
        lst.append(
            {
                'place_name': place['place_name'],
                'address_name': place['address_name'],
            }
        )
"""

def index(request):
    posts = Post.objects.all().order_by('-pk')
    context = {
        'posts': posts,
        'app': posts,
    }
    return render(request, 'posts/index.html', context)


def search(request):
    query = request.GET.get('q', '')
    if query:
        search = Post.objects.filter(
            Q(title__icontains=query)|
            Q(user__username__exact=query)
        )
    else:
        search = Post.objects.all()[::-1] 
    return render(request, 'posts/index.html', {'posts':search, 'app':'posts'})


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = PostCommentForm()
    comments = post.postcomment_set.all()
    context = {
        'comment_form': comment_form,
        'post': post,
        'comments': comments,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        post.delete()
    return redirect('posts:index')


@login_required
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('posts:detail', post_pk)
        else:
            form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'posts/update.html', context)


@login_required
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = PostCommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment_form.save()
        return redirect('posts:detail', post_pk)
    detail(request, post_pk)


@login_required
def comment_delete(request, post_pk, comment_pk):
    comment = PostComment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('posts:detail', post_pk)


@login_required
def post_likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if post.like_users.filter(pk=request.user.pk).exists():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:detail', post_pk)


def new_posts(posts):
    now = timezone.now()
    for post in posts:
        time_diff = now - post.created_at
        if time_diff < timezone.timedelta(secondes=1):
            post.is_new = True
        else:
            post.is_new = False


def comment_likes(request, post_pk, comment_pk):
    comment = PostComment.objects.get(pk=comment_pk)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    return redirect('posts:detail', post_pk)