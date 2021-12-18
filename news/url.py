from django.urls import path, include
from .views import NewsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', NewsViewSet)

urlpatterns = [
	path('', include(router.urls)),
]

#user_list = UserViewSet.as_view({
#	'get' : 'list'
#})
#user_detail = UserViewSet.as_view({
#	'get' : 'retrieve'
#})
#
#urlpatterns = format_suffix_patterns([
#	path('users/', user_list, name='user-list'),
#	path('users/<int:pk>/', user_detail, name='user-detail')
#])
