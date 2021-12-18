from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet 

router = DefaultRouter()
router.register(r'', UserViewSet)

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
