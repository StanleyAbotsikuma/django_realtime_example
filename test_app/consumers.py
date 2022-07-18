import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

# from .models import Room


class messageConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.set_name = None
        self.name = None
        
    def connect(self):
        
        self.name = self.scope['url_route']['kwargs']['name']
        self.set_name = f'chat_{self.name}'
       
        
        self.accept()

        # join the room group

        async_to_sync(self.channel_layer.group_add)(
            self.set_name,
            self.channel_name,
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.set_name,
            self.channel_name,
        )
        

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # send chat message event to the room
        async_to_sync(self.channel_layer.group_send)(
            self.set_name,
            {
                'type': 'payload',
                'message': message,
                'sender_channel_name': self.channel_name
            }
        )
        

    def payload(self, event):
        #sending to every except sender
        if self.channel_name != event.get('sender_channel_name'):

            #send every thing
            # self.send(text_data=json.dumps(event))

            print(event)
            self.send(json.dumps({'type': 'websocket.send','message': "hello"}))



    # async def websocket_receive(self, event):
    #     encoded_frame = event.get('text', None)
    #     if encoded_frame is not None:
    #         await self.channel_layer.group_send(
    #             self.flight_room,
    #             {
    #                 'type': 'video_frame',
    #                 'frame': encoded_frame,
    #                 'sender_channel_name': self.channel_name
    #             }
    #         )

    # async def video_frame(self, event):
    #     if self.channel_name != event.get('sender_channel_name'):
    #         await self.send({
    #             'type': 'websocket.send',
    #             'text': event.get('frame')
    #         })