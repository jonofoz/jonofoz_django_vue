from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=300)
    body = models.TextField()
    slug = models.SlugField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['id', 'created_at', 'updated_at', 'user_id', 'title', 'body', 'slug']