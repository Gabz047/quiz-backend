from django.shortcuts import render
from quiz.models import Answer, Quiz
from rest_framework.viewsets import ModelViewSet
from quiz.serializers import AnswerDetailSerializer, AnswerWriteSerializer, QuizDetailSerializer, QuizWriteSerializer

# Create your views here.

class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()

    def get_serializer_class(self):
        if self.action in ["list"]:
            return QuizDetailSerializer
        elif self.action in ["retrieve"]:
            return QuizDetailSerializer
        return QuizWriteSerializer
    http_method_names=["get", "put", "delete", "post"]
    
class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()

    def get_serializer_class(self):
        if self.action in ["list"]:
            return AnswerDetailSerializer
        elif self.action in ["retrieve"]:
            return AnswerDetailSerializer
        return AnswerWriteSerializer
    
