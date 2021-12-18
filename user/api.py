from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.db.models import Prefetch
from user.serializers import UserSerializer
from user.models import User
from board.models import Post

class UserViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

	#urls='my-post'
	@action(detail=False, methods=['get'])
	def my_post(self, requeust):
		queryset = self.get_queryset().prefetch_related(
			Prefetch('post_set', queryset=Post.objects.all())
		)

		return Response(self.get_serializer(queryset, many=True).data)
	