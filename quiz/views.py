from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Quiz
from .serializers import QuizSerializer
import random


class QuizViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticatedOrReadOnly,)
	queryset = Quiz.objects.all()
	serializer_class = QuizSerializer
