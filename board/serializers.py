from rest_framework import serializers
from .models import Post, Comment, Like, CommentLike, Hit, Tag


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    like_count = serializers.IntegerField(
        source='commentlike_set.count', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        ordering = ['parent_comment_id']


class PostSerializer(serializers.ModelSerializer):
    """
            less_comments
            https://stackoverflow.com/questions/38289324/in-django-rest-framework-how-to-limit-number-foreign-key-objects-being-serializ
    """
    username = serializers.CharField(source='user.username', read_only=True)
    # comment_set = CommentSerializer(many=True, read_only=True, source="less_comments")
    like_count = serializers.IntegerField(
        source='like_set.count', read_only=True)
    comment_count = serializers.IntegerField(
        source='comment_set.count', read_only=True)
    tag = serializers.SerializerMethodField('get_tagname')

    class Meta:
        model = Post
        fields = '__all__'

    def get_tagname(self, obj):
        tags = Tag.objects.filter(post=obj.id).values_list('name', flat=True)
        return tags


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'
        ordering = ['-id', 'parent_comment_id']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
