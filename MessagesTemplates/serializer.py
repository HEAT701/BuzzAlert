from .models import MessageTemplate
from rest_framework import serializers


class MessageTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageTemplate
        fields = ['id', 'user', 'name', 'content', 'created_at']
        