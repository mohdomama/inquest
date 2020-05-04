from django.db import models
from django.utils.text import slugify
from django.conf import settings
import time
# Create your models here.

# Best way to access user model
User = settings.AUTH_USER_MODEL

class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True, max_length=512)
    published = models.DateTimeField(auto_now_add=True, blank=True)

    # Not the best approach
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + '-' + str(time.time())[:10])
        return super().save(*args, **kwargs)
