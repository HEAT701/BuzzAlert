from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializer import MessageTemplateSerializer
from .models import MessageTemplate


class MessageTemplateViewSet(viewsets.ModelViewSet):
    queryset = MessageTemplate.objects.all()
    serializer_class = MessageTemplateSerializer
