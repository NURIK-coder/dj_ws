import json

import jwt
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings

from chat.models import Chat
from users.models import User


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        token = self.scope['query_string'].decode('utf-8').split('=')[1]



        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = payload['user_id']
        self.user_id = user_id
        self.room_group_name= f'chat_{self.room_name}'
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

        await self.close()


    def get_user(self):
       return {'user': User.objects.get(id=self.user_id)}

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)

        res = await database_sync_to_async(self.get_user)()
        print(res['user'].username)
        data['user_id'] = self.user_id
        # await self.send(text_data=json.dumps(data))
        await self.channel_layer.group_send(
            self.room_group_name, {'type': 'chat.message', 'data': data}
        )
    async def chat_message(self, event):
        data = event['data']
        await self.send(json.dumps(data))
