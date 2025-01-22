from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer


class ChatTemplateView(TemplateView):
    template_name = 'chats/chat.html'


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
