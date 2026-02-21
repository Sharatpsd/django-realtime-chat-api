from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Message

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def chat_history(request, room_name):
    messages = Message.objects.filter(room=room_name).order_by("timestamp")
    data = [
        {
            "username": msg.sender.username,
            "message": msg.content,
            "timestamp": msg.timestamp,
        }
        for msg in messages
    ]
    return Response(data)