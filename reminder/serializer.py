from rest_framework import serializers
from .models import Reminder
class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'phone', 'title', 'messages', 'status', 'created_at']
        read_only_fields = ['id', 'created_at']
