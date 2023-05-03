from django.contrib import admin
from .models import Article, ArticleComment, ArticleImage

# Register your models here.

admin.site.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'tag_list',)
    list_filter = ('tag_list',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    
    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())



admin.site.register(ArticleComment)
admin.site.register(ArticleImage)