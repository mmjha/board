"""myapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers, permissions
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('admin/', admin.site.urls),
    # https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
    # path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/', include('allauth.urls')),
	path('api/user/', include('user.url')),
	path('api/quiz/', include('quiz.url')),
	path('api/news/', include('news.url')),
	path('api/board/', include('board.url')),
]