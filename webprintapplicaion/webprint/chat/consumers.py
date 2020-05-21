from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
import json
from chat.printer_management import printhtml
from webprint.printerinfo.printer_management import get_printers
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name

#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )

#         self.accept()

#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )

#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )

#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']

#         # Send message to WebSocket
#         self.send(text_data=json.dumps({
#             'message': message
#         }))

# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))



#Consumer  for  html content print
# parameters:
#         1.html content or url 
#         2.Authentication Mode
#             1.cookies - 1
#             2.hmac   - 2 - (in future)
#             3.No Authentictaion -3
class HtmlPrintConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("websocket connection accepted")
        await self.accept()
    async def disconnect(self,code):
        print("connection closed")
    async def receive(self,text_data):
        # print("received data",type(text_data),text_data)
        reqdata = json.loads(text_data)
        printers =  get_printers()
        print("printers",printers)
        # await self.send("received successfuly")
        # print(reqdata) 
        # call print
        # response=await self.channel_layer.send(
        # "htmlprint",
        # {
        #     "type": "print.worker",
        #     "reqdata": reqdata,
        #     },
        # )
        print("reqdata",reqdata)
        await self.send(text_data="successfuly added")
            # await printhtml(reqdata)
    async def getw(self,data):
        print("data",data)
        await self.send(data)

#consumer for getting printer properties

class PrinterProperityConsumer(WebsocketConsumer):
    def connect(self):
        print("websocket connection accepted")
        self.accept()
    def receive(self,text_data):
        print("received data",text_data)
        reqdata = json.loads(text_data)
        printers =  get_printers()
        print("printers",printers)
        self.send(text_data=json.dumps(printers))
    def disconnect(self,code):
        print("connection closed")
