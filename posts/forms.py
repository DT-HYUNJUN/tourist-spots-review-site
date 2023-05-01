from django import forms
from .models import Post, PostComment


class PostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목',
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용',
            }
        )
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False
    )
    class Meta:
        model = Post
        fields = ('title', 'place', 'content', 'image', 'start_date', )


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