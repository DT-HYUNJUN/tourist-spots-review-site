from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone
import os
import re

# Create your models here.

class Tag(models.Model):
    tag_content = models.TextField(max_length=20, unique=True)
    def __str__(self):
        return self.tag_content


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    bookmark_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmark_articles')
    views = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='view_articles')
    tagging = models.ManyToManyField(Tag, blank=True, related_name='tagged')
    
    def post_image_path(instance, filename):
        return f'posts/{instance.pk}/{filename}'
    image = models.ImageField(blank=True, upload_to=post_image_path)

    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        super(Article, self).delete(*args, **kargs)

    def save(self, *args, **kwargs):
        if self.id:
            old_review = Article.objects.get(id=self.id)
            if self.image != old_review.image:
                if old_review.image:
                    os.remove(os.path.join(settings.MEDIA_ROOT, old_review.image.name))
        super(Article, self).save(*args, **kwargs)


    def save(self, *args, **kwargs):
    # content 필드에서 해시태그 추출
        tags = re.findall(r'#(\w+)\b', self.content)
        if tags:
            # 추출한 해시태그를 이용하여 Tag 모델에 저장
            for tag in tags:
                tag_obj, created = Tag.objects.get_or_create(tag_content=tag.lower())
                self.tagging.add(tag_obj)
        super().save(*args, **kwargs)
    

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return self.strftime('%Y-%m-%d')


class ArticleComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comment')
    dislike_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_comments')

    
    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return self.strftime('%Y-%m-%d')

