from django.urls import path

from .views import ServicesListAPIView, ServicesRetrieveAPIView, FeedbackCreateListView, FeedbackDeleteView

urlpatterns = [
    path('services/', ServicesListAPIView.as_view()),
    path('services/<int:pk>', ServicesRetrieveAPIView.as_view()),
    
    path('feedback/', FeedbackCreateListView.as_view()),
    path('feedback/delete/<int:pk>/', FeedbackDeleteView.as_view()),
]