from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import os

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    def profile(instance, filename):
        return f'profiles/{instance.username}/{filename}'
    profile_image = ProcessedImageField(blank=True,
                                upload_to = profile,
                                processors= [ResizeToFill(90, 90)],
                                format='JPEG',
                                options={'quality' : 60},
                                )
    def delete(self, *args, **kargs):
        if self.profile_image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.profile_image.path))      
        super(User, self).delete(*args, **kargs)

    def save(self, *args, **kwargs):
        if self.id:
            old_user = User.objects.get(id=self.id)
            if self.profile_image != old_user.profile_image:
                if old_user.profile_image:
                    os.remove(os.path.join(settings.MEDIA_ROOT, old_user.profile_image.path))
        super(User, self).save(*args, **kwargs)

    birthday = models.DateField(null=True, blank=True)
    mbti = models.TextField(null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)