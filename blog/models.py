from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    content = models.TextField()
    preview = models.ImageField(upload_to='blog_previews/')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.slug)])
