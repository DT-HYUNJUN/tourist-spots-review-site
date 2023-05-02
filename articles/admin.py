from django.contrib import admin
from .models import Article, ArticleComment, ArticleImage,Tag

# Register your models here.

admin.site.register(Article)
admin.site.register(ArticleComment)
admin.site.register(ArticleImage)
# admin.site.register(Tag)

