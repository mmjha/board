from django.urls import path, include
from .views import PostViewSet, CommentViewSet, LikeViewSet, TagViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'like', LikeViewSet)
router.register(r'tag', TagViewSet)

urlpatterns = [
	path('', include(router.urls)),
]
