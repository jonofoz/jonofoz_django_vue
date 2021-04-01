from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300)
    body = models.TextField()
    slug = models.SlugField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['created_at', 'updated_at', 'user', 'title', 'body', 'slug']