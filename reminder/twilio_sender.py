from twilio.rest import Client
from django.conf import settings
from .models import Reminder

def messages_sender(reminder_id):
    reminder = Reminder.objects.get(id=reminder_id)
    
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    
    message = client.messages.create(
        body=reminder.messages,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=reminder.phone
    )
    
    # Update reminder status
    reminder.status = 'sent'
    reminder.save()
    
    return message.sid