from django.db import models
# from .queryset import (
#     UserQuerySet
# )

class UserQuerySet(models.QuerySet):
    def admins(self):
        return self.filter(is_staff=True)


class CustomUserManager(models.Manager):
    # _queryset_class = UserQuerySet
    """
        https://docs.djangoproject.com/en/3.2/topics/db/managers
    """
    def get_queryset(self):
        return super().get_queryset().filter()

    def admins(self):
        return self.get_queryset().admins()