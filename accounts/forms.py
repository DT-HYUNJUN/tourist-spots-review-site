from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model


class CustomUserUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',)
    username = forms.CharField(
        required=True,
        label='ID',
        widget= forms.TextInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : '영문 소문자 또는 영문 대문자, 숫자 조합 6~12 자리',
          }
        )
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget= forms.EmailInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : 'Email 입력',
          }
        )
    )
    password1 = forms.CharField(
        required=True,
        label='Password1',
        widget= forms.PasswordInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : '영문, 숫자, 특수문자(~!@#$%^&*) 조합 8~15 자리',
          }
        )
    )
    password2 = forms.CharField(
        required=True,
        label='Password2',
        widget= forms.PasswordInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : '영문, 숫자, 특수문자(~!@#$%^&*) 조합 8~15 자리',
          }
        )
    )


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        label='ID',
        widget= forms.TextInput(
          attrs = {
              'class' : 'form-control',
              'placeholder' : 'ID 입력',
          }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
          attrs={
            'class' : 'form-control',
            'placeholder' : 'Password 입력',
          }
        )
    )


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        fields = ('email', 'profile_image', 'mbti', 'birthday',)
    email = forms.EmailField(
        required=True,
        label='Email',
        widget= forms.EmailInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : 'Email 입력',
          }
        )
    )
    profile_image = forms.ImageField(
        required=False,
        label='Profile_image',
        widget= forms.ClearableFileInput(
          attrs = {
            'class' : 'form-control',
          }
        )
    )
    mbti = forms.CharField(
        required=False,
        label='mbti',
        widget= forms.TextInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : 'mbti',
          }
        )
    )
    birthday = forms.DateField(
        required=False,
        label='Profile_image',
        widget= forms.DateInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : '생년월일',
          }
        )
    )




class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="기존 비밀번호",
        widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '기존 비밀번호 입력'
        })
    )
    new_password1 = forms.CharField(
        required=True,
        label='Password1',
        widget= forms.PasswordInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : '새 비밀번호(영문, 숫자, 특수문자(~!@#$%^&*) 조합 8~15 자리)',
          }
        )
    )
    new_password2 = forms.CharField(
        required=True,
        label='Password2',
        widget= forms.PasswordInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : '새 비밀번호 다시 입력',
          }
        )
    )