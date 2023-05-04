from django import forms
from .models import Article, ArticleComment, ArticleImage


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
    tags = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder' : '태그 사이에 쉼표를 넣어주세요.'
            }
        )
    )
    class Meta:
        model = Article
        fields = ('title', 'content', 'tags')
    

class ArticleImageForm(forms.ModelForm):
    class Meta:
        model = ArticleImage
        fields = ('image',)
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


class DeleteArticleImageForm(forms.ModelForm):
    delete_images = forms.ModelMultipleChoiceField(
        queryset=ArticleImage.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = ArticleImage
        fields = []

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
        if instance:
            self.fields['delete_images'].queryset = instance.articleimage_set.all()
    
    def save(self, commit=True):
        for image in self.cleaned_data['delete_images']:
            image.delete()



class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ('content',)
    content = forms.CharField(
        widget = forms.TextInput(
            attrs= {
                'class' : 'comment--create',
                'style' : 
                    'width: 100%; outline: 1px solid #cccccc; border:1px solid #ffffff; border-radius:5px; padding:1rem;', 
                'placeholder' : '댓글을 입력해주세요!'
            }
        )
    )