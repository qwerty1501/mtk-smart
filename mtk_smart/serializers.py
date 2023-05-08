from rest_framework import serializers as s

from .models import Services, Feedback


class ServicesSerializers(s.ModelSerializer):
    
    class Meta:
        model = Services
        fields = ['loga', 'title_one', 'description_one', 'title_two', 'description_two', 'id']
        

class FeedbackSerializers(s.ModelSerializer):
    
    class Meta:
        model = Feedback
        fields = ['name', 'number', 'id']