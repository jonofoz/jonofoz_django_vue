from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostsSerializer
# Create your views here.
class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

    def get_queryset(self):
        # Get all posts if a user's id isn't provided, else return only posts by user id.
        user = self.request.GET.get('user', '')
        if user:
            return Post.objects.filter(user=user)
            pass
        else:
            return Post.objects.all()