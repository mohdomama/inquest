from django.db import models
from django.utils.text import slugify
import time
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True, max_length=512)

    # Not the best approach
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + '-' + str(time.time())[:10])
        return super().save(*args, **kwargs)
