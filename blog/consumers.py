import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Notification
from .serializers import NotificationSerializer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(
            "notifications",
            self.channel_name
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "notifications",
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def notification_message(self, event):
        notification = event["text"]
        # Send notification to WebSocket
        await self.send(text_data=json.dumps({
            'notification': notification
        }))





