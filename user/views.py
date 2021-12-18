from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Prefetch
from django.contrib.auth import get_user_model
from board.models import Post
from .serializers import (
    UserSerializer,
    MyPostSerializer,
    SignUpSerializer
)
from notice.util import NoticeUtil


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.dict()  # querydict to dict
        serializer = SignUpSerializer(data=data)  # paramtype : json
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        NoticeUtil().send_email()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True,
            url_path='post',
            methods=['get'],
            serializer_class=MyPostSerializer)
    def my_post(self, requeust, pk=None):
        """
                https://www.django-rest-framework.org/api-guide/viewsets/
        """
        queryset = self.get_queryset().filter(id=pk).prefetch_related(
            Prefetch('post_set', queryset=Post.objects.all())
        )
        return Response(self.get_serializer(queryset, many=True).data)

    @action(detail=False, url_path='admin', methods=['get'])
    def admin(self, request):
        queryset = get_user_model().objects.admins()
        return Response(self.get_serializer(queryset, many=True).data)
