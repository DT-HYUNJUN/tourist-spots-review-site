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
    place = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'place-field',
                'class': 'form-control',
                'autocomplete': 'off',
                'list': 'address-list',
            }
        )
    )
    region = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'region-field',
                'class': 'form-control',
            }
        ),
        
    )
    content = forms.CharField(
        widget=forms.Textarea(
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
        fields = ('title', 'place', 'region', 'content', 'image', 'start_date', 'end_date')


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