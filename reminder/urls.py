
from django.urls import path
from .views import Login_view,create_reminder,list_reminders,summary_remenders
urlpatterns = [
    path('login/', Login_view, name='login'),
    path('create_reminder/', create_reminder, name='create_reminder'),
    path('list_reminders/', list_reminders, name='list_reminders'),
    path('summary_remenders/', summary_remenders, name='summary_remenders'),
]