# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        # Dołączenie do grupy WebSocket
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Usunięcie z grupy po zakończeniu połączenia
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Otrzymanie wiadomości od klienta
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Wysłanie wiadomości do grupy
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # Otrzymanie wiadomości z grupy
        message = event['message']

        # Wysłanie wiadomości do WebSocket klienta
        await self.send(text_data=json.dumps({
            'message': message
        }))
