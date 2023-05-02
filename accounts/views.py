from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomPasswordChangeForm, CustomAuthenticationForm, CustomUserChangeForm, CustomUserUserCreationForm
from django.contrib.auth import get_user_model
from posts.models import Post
from articles.models import Article


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form' : form})


@login_required
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('posts:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    if request.method == 'POST':
      form = CustomUserUserCreationForm(request.POST)
      if form.is_valid():
          user = form.save()
          auth_login(request, user)
          return redirect('posts:index')
    else:
        form = CustomUserUserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('posts:index')



@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
        else:
            print(form.errors)
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/update.html', {'form' : form})



@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('posts:index')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form':form})


def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    post = Post.objects.order_by('-pk') 
    article = Article.objects.order_by('-pk') 
    context = {
        'person' : person,
        'post' : post,
        'article' : article
    }
    return render(request, 'accounts/profile.html', context)


def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)

    if person != request.user:
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
 