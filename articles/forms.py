from django import forms
from .models import Article, ArticleComment, Tag

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
    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control'
            }
        ),
        required=False
    )


    class Meta:
        model = Article
        fields = ('title', 'content', 'image',)
    
    

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