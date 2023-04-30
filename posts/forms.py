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
    place = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'place-field',
                'class': 'form-control',
                'autocomplete': 'off',
                'list': 'address-list',
                'placeholder': '장소',
            }
        )
    )
    region = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'region-field',
                'class': 'form-control',
                'placeholder': '지역',
            }
        ),
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
                'class': 'form-control'
            }
        ),
        required=False
    )
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
            }
        )
    )
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
            }
        )
    )
    
    class Meta:
        model = Post
        fields = ('title', 'place', 'region', 'content', 'image', 'start_date', 'end_date',)


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