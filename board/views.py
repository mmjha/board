import datetime
from ipware import get_client_ip
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .filters import PostFilter
from .models import Post, Comment, Like, Hit, Tag
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, TagSerializer
from django.core import serializers

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter
    # renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )

    # def list(self, request, *args, **kwargs):
    # 	"""
    # 		https://www.django-rest-framework.org/api-guide/renderers/#templatehtmlrenderer
    # 		https://stackoverflow.com/questions/18925358/how-do-you-access-data-in-the-template-when-using-drf-modelviewset-and-templateh
    # 		https://stackoverflow.com/questions/55720486/django-rest-framework-rendering-form-elements-in-list-response
    # 	"""
    # 	response = super(PostViewSet, self).list(request, *args, **kwargs)
    # 	if request.accepted_renderer.format == 'html':
    # 		return Response({'data': sorted(response.data.items())}, template_name='board.html')
    # 	return response

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def retrieve(self, request, pk=None):
        ip, is_routable = get_client_ip(request)
        instance = self.get_object()
        hit, created = Hit.objects.get_or_create(
            ip=ip, post=instance, date=datetime.datetime.now())
        if created:
            Post.objects.filter(id=pk).update(hits=instance.hits + 1)
        return super().retrieve(self, request, pk)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        queryset = Comment.objects.less_comments(pk)
        page = self.paginate_queryset(queryset)
        if page is None:
            return Response(CommentSerializer(queryset, many=True).data)
        return self.get_paginated_response(
            CommentSerializer(page, many=True).data)


class CommentViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.all().order_by('parent_comment_id')
    serializer_class = CommentSerializer


class LikeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
