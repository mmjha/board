from django.urls import path, include
from .views import QuizViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', QuizViewSet)

urlpatterns = [
	path('', include(router.urls))
]

