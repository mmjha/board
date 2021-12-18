from .models import Post
from django_filters import rest_framework as filters


class PostFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    content = filters.CharFilter(field_name='content', lookup_expr='icontains')
    username = filters.CharFilter(field_name='user__username')

    class Meta:
        model = Post
        fields = ['title', 'content', 'username']