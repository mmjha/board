from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from news.serializers import NewsSerializer
from news.models import News

# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticatedOrReadOnly,)
	queryset = News.objects.all()
	serializer_class = NewsSerializer

