from datetime import timezone, datetime
from django.db.models import Count
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Post, PostComment
from .forms import PostForm, PostChangeForm ,PostCommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
# import requests

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-pk')
    new_posts(posts)
    select_sorting = request.GET.get('select_sorting')
    posts = sorting(posts, select_sorting)
    page = request.GET.get('page', '1')
    per_page = 4
    paginator = Paginator(posts, per_page)
    last_page = paginator.num_pages
    page_obj = paginator.get_page(page)
    context = {
        'last_page': last_page,
        'posts': page_obj,
        'region_name': '모든 지역',
        'app': posts,
        'select_sorting': select_sorting,
    }
    return render(request, 'posts/index.html', context)


def sorting(queryset, select_sorting):
    if select_sorting == '최신순':
        return queryset.order_by('-pk')
    elif select_sorting == '오래된순':
        return queryset.order_by('pk')
    elif select_sorting == '인기순':
        return queryset.order_by('-rating')
    elif select_sorting == '평점순':
        return Post.objects.annotate(num_likes=Count('like_users')).order_by('-num_likes')
    else:
        return queryset


def search(request):
    query = request.GET.get('q', '')
    if query:
        search = Post.objects.filter(
            Q(title__icontains=query)|
            Q(user__username__exact=query)
        ).order_by('-pk')
    else:
        search = Post.objects.all().order_by('-pk')
    return render(request, 'posts/index.html', {'posts':search, 'app':'posts'})


# 카테고리로 찾기
def region(request, region_name):
    posts = Post.objects.all().filter(region=region_name).order_by('-pk')
    select_sorting = request.GET.get('select_sorting')
    posts = sorting(posts, select_sorting)
    new_posts(posts)
    context = {
        'posts': posts,
        'region_name': region_name,
        'select_sorting': select_sorting,
    }
    return render(request, 'posts/index.html', context)




@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.rating = int(request.POST.get('rating', 0))
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
    prev_posts = Post.objects.filter(pk__lt=post_pk).order_by('-pk')[:2]
    next_posts = Post.objects.filter(pk__gt=post_pk).order_by('pk')[:2]
    posts = list(prev_posts) + [post] + list(next_posts)
    comment_form = PostCommentForm()
    comments = post.postcomment_set.all()
    user_age_range = age_range(post)
    context = {
        'user_age_range': user_age_range,
        'posts': posts,
        'comment_form': comment_form,
        'post': post,
        'comments': comments,
    }
    return render(request, 'posts/detail.html', context)


def age_range(post):
    result = ''
    if post.user.birthday:
        birthday = str(post.user.birthday)
        birthday = int(birthday.split('-')[0])
        year = datetime.now().year
        age = year - birthday
        print(age)
        result = f'{(age//10*10)}대'
    else:
        result = ''
    return result
        


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
                print('valid')
                form.save()
                print('save')
                return redirect('posts:detail', post_pk)
        else:
            form = PostForm(instance=post)
    else:
        return redirect('posts:detail', post.pk)
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
        is_liked = False
    else:
        post.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'like_count': post.like_users.count(),
    }
    return JsonResponse(context)


def new_posts(posts):
    now = timezone.now()
    for post in posts:
        time_diff = now - post.created_at
        if time_diff < timezone.timedelta(days=1):
            post.is_new = True
        else:
            post.is_new = False


@login_required
def comment_likes(request, post_pk, comment_pk):
    comment = PostComment.objects.get(pk=comment_pk)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    return redirect('posts:detail', post_pk)


def create_comment(post, text, user):
    comment = PostComment(post=post, text=text, user=user)
    comment.save()
    return comment


from django.http import JsonResponse

def create_comment_ajax(request):
    if request.method == 'GET':
        post_pk = request.GET.get('post_pk')
        text = request.GET.get('content')
        user = request.user
        post = get_object_or_404(Post, pk=post_pk)
        comment = create_comment(post, text, user)
        context = {
            'comment': {
                'id': comment.id,
                'content': comment.content,
                'user': comment.user.username,
                'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')
            }
        }
        return JsonResponse(context)
