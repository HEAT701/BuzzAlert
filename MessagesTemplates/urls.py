from rest_framework.routers import DefaultRouter
from .views import MessageTemplateViewSet
from django.urls import path, include
router = DefaultRouter()
router.register(r'message-templates', MessageTemplateViewSet, basename='message-template')  
urlpatterns = [
    path('', include(router.urls)),
]