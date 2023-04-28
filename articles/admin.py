from django.contrib import admin
from .models import Article, ArticleComment, Tag

# Register your models here.

admin.site.register(Article)
admin.site.register(ArticleComment)
# admin.site.register(Tag)

