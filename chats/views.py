from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer


class RoomDetailView(LoginRequiredMixin, DetailView):
    model = Room
    template_name = 'chats/room.html'
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.object
        context['messages'] = room.messages.all()
        context['users'] = room.users.all()
        return context


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        room = self.get_object()
        room.users.add(request.user)
        return Response({'status': 'Joined room'})


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
