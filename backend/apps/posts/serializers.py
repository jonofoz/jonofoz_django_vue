from rest_framework.serializers import ModelSerializer

from .models import Post

class PostsSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'created_at', 'updated_at', 'user_id', 'title', 'body', 'slug']