import json
import django
django.setup()

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def get_room(self, room_id):
        return Room.objects.get(pk=room_id)
    
    @database_sync_to_async
    def create_message(self, message, room, sender):
        return Message.objects.create(
            content=message,
            room=room,
            sender=sender
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        room = await self.get_room(self.room_id)

        message_instance = await self.create_message(message, room, self.scope['user'])

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_instance.content,
                'user': message_instance.sender.email,
                'created_at': message_instance.created_at.isoformat(),
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        created_at = event['created_at']

        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
            'created_at': created_at,
        }))
