import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'common_group'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()



    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        notification = text_data_json['notification']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'notification_message',
                'notification': notification
            }
        )

    def notification_message(self, event):
        notification = event['notification']

        self.send(text_data=json.dumps({
            'type': 'notification',
            'notification': notification
        }))