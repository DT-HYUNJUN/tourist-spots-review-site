from django import forms
from .models import Article, ArticleComment, ArticleImage, Tag

# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = ('tag_content',)


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Article
        fields = ('title', 'content', )
    

class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='Image',
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
            'multiple': True,
            'class': 'form-control'
            }
        )
    )
    class Meta:
        model = ArticleImage
        fields = ('image',)


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ('content',)
    content = forms.CharField(
        widget = forms.TextInput(
            attrs= {
                'class' : 'form-control',
                'placeholder' : '댓글을 입력해주세요'
            }
        )
    )