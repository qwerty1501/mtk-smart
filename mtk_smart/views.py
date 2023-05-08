from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import ServicesSerializers, FeedbackSerializers
from .models import Services, Feedback


# Создание услуг
class ServicesListAPIView(ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers


class ServicesRetrieveAPIView(RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers


# Создание формы обратной связи
class FeedbackCreateListView(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializers
    queryset = Feedback.objects.all()
    
    
class FeedbackDeleteView(generics.DestroyAPIView):
    serializer_class = FeedbackSerializers()
    queryset = Feedback.objects.all()