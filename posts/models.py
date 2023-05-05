import math
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager
from django.urls import reverse
from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
import os
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    is_new = models.BooleanField(default=False)
    place = models.CharField(max_length=100, default='Unknown')
    region = models.CharField(max_length=50, default='Unknown')
    place_id = models.CharField(max_length=100, default='18577297')
    place_keyword = models.CharField(max_length=100, default='카카오 스페이스닷원')
    start_date = models.DateField(default='2023-05-01')
    end_date = models.DateField(default='2023-05-07')
    rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    tags = TaggableManager(blank=True)
    
    def get_absolute_url(self):
        return reverse('posts:detail', args=[int(self.id)])
    
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


class PostImage(models.Model):
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    
    def post_image_path(instance, filename):
        return f'posts/{instance.post.pk}/{filename}'
           
    image = ProcessedImageField(blank=True,
                                upload_to = post_image_path,
                                # processors= [ResizeToFill(200, 200)],
                                format='JPEG',
                                options={'quality' : 90},
                                null = True,
                                )
    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
            dir_path = os.path.dirname(os.path.join(settings.MEDIA_ROOT, self.image.name))
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
        super(PostImage, self).delete(*args, **kargs)


class PostComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')


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