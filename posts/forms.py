from django import forms
from .models import Post, PostComment


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
        ),
        required=False
    )
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')


class PostCommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    class Meta:
        model = PostComment
        fields = ('content',)