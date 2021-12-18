from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.fields import AutoSlugField
from .managers import (
    PostManager,
    CommentManager
)

# Create your models here.


class Tag(models.Model):
    """
        https://stackoverflow.com/questions/17346636/manytomany-tags-in-html-template
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tag'


class Post(models.Model):
    objects = PostManager()
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    photo = models.CharField(max_length=200, null=True)
    hits = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'


class Comment(models.Model):
    objects = CommentManager()
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        db_table = 'like'


class CommentLike(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE)  # TODO set null
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        db_table = 'comment_like'


class Hit(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=15, default=None, null=True)
    post = models.ForeignKey(
        Post,
        default=None,
        null=True,
        on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'hit'
        unique_together = ('ip', 'post', 'date',)
