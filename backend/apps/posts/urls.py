from rest_framework import routers

from .views import PostsViewSet

router = routers.DefaultRouter()
router.trailing_slash = '/?'

router.register(r'posts', PostsViewSet)
