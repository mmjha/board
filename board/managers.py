from django.db import models
from .queryset import (
    PostQuerySet,
    CommentQuerySet
)

class PostManager(models.Manager):
    _queryset_class = PostQuerySet

    """
        https://docs.djangoproject.com/en/3.2/topics/db/managers
    """

class CommentManager(models.Manager):
    _queryset_class = CommentQuerySet

    """
        https://docs.djangoproject.com/en/3.2/topics/db/managers
    """
    
    def less_comments(self, id=None):
        return self.get_queryset().less_comments(id)