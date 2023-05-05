from django import forms
from .models import Post, PostComment, PostImage


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
    # image = forms.ImageField(
    #     widget=forms.ClearableFileInput(
    #         attrs={
    #             'class': 'form-control mb-3',
    #         }
    #     ),
    #     required=False
    # )
    place_id = forms.CharField(
        widget=forms.TimeInput(
            attrs={
                'id': 'place-id',
                'class': 'hidden',
            }
        )
    )
    
    place_keyword = forms.CharField(
        widget=forms.TimeInput(
            attrs={
                'id': 'place-keyword',
                'class': 'hidden',
            }
        )
    )
    tags = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder' : '태그 사이에 쉼표를 넣어주세요.'
            }
        )
    )
    class Meta:
        model = Post
        fields = ('title', 'place', 'region', 'content', 'start_date', 'end_date', 'place_id', 'place_keyword', 'tags',)


class PostImageForm(forms.ModelForm):
    class Meta:
        model = Post
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


class DeletePostImageForm(forms.ModelForm):
    delete_images = forms.ModelMultipleChoiceField(
        queryset=PostImage.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = PostImage
        fields = []

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
        if instance:
            self.fields['delete_images'].queryset = instance.postimage_set.all()
    
    def save(self, commit=True):
        for image in self.cleaned_data['delete_images']:
            image.delete()

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
        fields = ('title', 'place', 'region', 'content', 'image', 'start_date', 'end_date', 'rating', )


comment_max = 100
class PostCommentForm(forms.ModelForm):
    content = forms.CharField(
        max_length=comment_max,
        widget=forms.Textarea(
            attrs={
                'id': 'comment-field',
                'class': 'border-0 w-100 comment-form' ,
                'placeholder': '댓글을 남겨보세요',
                'autocomplete': 'off',
                'data-max-length': comment_max,
                'onkeydown': 'resize(this)',
                'onkeyup': 'resize(this)',
                'rows': 1,
            }
        ),
    )
    class Meta:
        model = PostComment
        fields = ('content',)