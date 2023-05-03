from django import forms
from .models import Post, PostComment


class PostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': '제목',
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': '여행지를 소개해주세요~',
            }
        )
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control mb-3',
            }
        ),
        required=False
    )
    class Meta:
        model = Post
        fields = ('title', 'place', 'region', 'content', 'image', 'start_date', 'end_date',)

class PostChangeForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': '제목',
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': '여행지를 소개해주세요~',
            }
        )
    )
    # image = forms.ImageField(
    #     widget=forms.ClearableFileInput(
    #         attrs={
    #             'class': 'form-control mb-3',
    #         }
    #     ),
    #     required=False
    # )
    class Meta:
        model = Post
        fields = ('title', 'place', 'region', 'content', 'image', 'start_date', 'end_date', 'rating', )


class PostCommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'border-0 w-100 comment-form' ,
                'placeholder': '댓글을 남겨보세요',
                'autocomplete': 'off',
            }
        )
    )
    class Meta:
        model = PostComment
        fields = ('content',)