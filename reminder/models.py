from django.db import models
from django.contrib.auth.models import User

class Reminder(models.Model):
    user = models.ForeignKey(User, null= True, blank=True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=15)
    title = models.CharField(max_length=100)
    messages = models.TextField()
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
