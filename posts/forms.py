from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    content = forms.CharField(
        widget=forms.TimeInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)