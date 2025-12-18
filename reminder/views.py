from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated ,AllowAny
from rest_framework.response import Response
from .models import Reminder
from .serializer import ReminderSerializer
from .twilio_sender import messages_sender
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
# Create your views here.


@api_view(['POST'])
def Login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return Response({'message': 'Login successful'})
    else:
        return Response({'message': 'Invalid credentials'}, status=401)


@api_view(['POST'])
def ragister_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({'message': 'Username and password are required'}, status=400)
    if User.objects.filter(username=username).exists():
        return Response({'message': 'Username already exists'}, status=400)
    User.objects.create_user(username=username, password=password)
    return Response({'message': 'User registered successfully'})

@api_view(['POST'])
@permission_classes([AllowAny])
def create_reminder(request):

    data = request.data.copy()
    data['messages'] = data.get('messages') or data.get('message')

    if not data['messages']:
        return Response({'error': 'messages field is required'}, status=400)

    serializer = ReminderSerializer(data=data)

    if serializer.is_valid():
        if request.user.is_authenticated:
            reminder = serializer.save(user=request.user)
        else:
            reminder = serializer.save(user=None)

        message_sid = messages_sender(reminder.id)

        return Response({
            'message': 'Reminder created and message sent',
            'sid': message_sid
        }, status=201)

    return Response(serializer.errors, status=400)


# get the all reminders of the user
@ api_view(['GET'])
@ permission_classes([AllowAny])
def list_reminders(request):
    reminders = Reminder.objects.filter(user=request.user) if request.user.is_authenticated else Reminder.objects.all()
    serializer = ReminderSerializer(reminders, many=True)
    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([AllowAny])
def summary_remenders(request):

    # Total reminders count
    total_reminders = Reminder.objects.count()
    total_pending = Reminder.objects.filter(status='pending').count()
    # Count based on status
    total_messages = Reminder.objects.filter(status='sent').count()
    total_delivered = Reminder.objects.filter(status='delivered').count()
    total_failed = Reminder.objects.filter(status='failed').count()

    return Response({
        'total_reminders': total_reminders,
        'total_sent': total_messages,
        'total_delivered': total_delivered,
        'total_failed': total_failed,
        'total_pending': total_pending
    })



