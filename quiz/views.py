from django.shortcuts import render
from rest_framework import viewsets
from quiz.serializers import QuestionsSerializer
from quiz.models import Questions


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

