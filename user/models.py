from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.urls import reverse

# Create your models here.


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class UserQuerySet(models.QuerySet):
    def users(self):
        return self.filter(is_staff=False)

    def admins(self):
        return self.filter(is_staff=True)


class CustomUserManager(UserManager):
    _queryset_class = UserQuerySet
    """
        https://docs.djangoproject.com/en/3.2/topics/db/managers
    """

    def get_queryset(self):
        return super().get_queryset().filter()

    def admins(self):
        return self.get_queryset().admins()


class User(AbstractUser):
    objects = CustomUserManager()
    is_active = models.BooleanField(
        default=False, help_text='회원가입 후 관리자 승인 전까지 미사용')

    class Meta:
        db_table = 'user'
        ordering = ['-id']
