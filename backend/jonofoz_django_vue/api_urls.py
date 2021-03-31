
from django.urls import include, path
from rest_framework import routers

from apps.users.urls import router as user_router
from apps.posts.urls import router as posts_router


router = routers.DefaultRouter()
router.registry.extend(user_router.registry)
router.registry.extend(posts_router.registry)

urlpatterns = [
    path('', include(router.urls)),
]
