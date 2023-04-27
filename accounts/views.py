from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomPasswordChangeForm, CustomAuthenticationForm, CustomUserChangeForm, CustomUserUserCreationForm

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



def signup(request):
    if request.method == 'POST':
      form = CustomUserUserCreationForm(request.POST)
      if form.is_valid():
          user = form.save()
          auth_login(request, user)
          return redirect('posts:index')
    else:
        form = CustomUserUserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

    