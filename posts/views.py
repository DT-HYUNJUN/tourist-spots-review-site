from django.shortcuts import render, redirect
from .models import Post, PostComment
from .forms import PostForm, PostCommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-pk')
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect('posts:index')
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