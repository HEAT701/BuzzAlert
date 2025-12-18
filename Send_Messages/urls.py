from django.urls import path
from .views import CreateScheduledCampaignAPI
urlpatterns = [
    path('create_scheduled_campaign/', CreateScheduledCampaignAPI.as_view(), name='create_scheduled_campaign'),
]