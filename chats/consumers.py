import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('===================')
        self.room_name = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_name}'

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        print('===================')
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print('===================')
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        room = Room.objects.get(name=self.room_name)

        # Create a new message
        message_instance = Message.objects.create(
            content=message,
            room=room,
            created_by=self.scope['user']
        )

        # Send the message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_instance.content,
                'user': message_instance.created_by.username,
                'created_at': message_instance.created_at.isoformat(),
            }
        )

    async def chat_message(self, event):
        print('===================')
        message = event['message']
        user = event['user']
        created_at = event['created_at']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
            'created_at': created_at,
        }))
