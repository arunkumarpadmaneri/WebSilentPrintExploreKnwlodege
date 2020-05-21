#consumer for getting printer properties
from channels.generic.websocket import JsonWebsocketConsumer,WebsocketConsumer
from .printer.processor import Processor
from database import database_management
from asgiref.sync import async_to_sync
import json
class PrinterConsumer(JsonWebsocketConsumer):
    def connect(self):
        print("websocket connection accepted")
        self.accept()
    def receive_json(self,content):
        print("received data",content,self.channel_name)
        generic_processor = Processor(content)
        processor=generic_processor.get_processor()
        response= processor.process_request()
        print("response",response)
        self.send_json(response)
    def disconnect(self,code):
        print("connection closed")

class  NotificationConsumer(WebsocketConsumer):

    def connect(self):
        self.topic_name = self.scope['url_route']['kwargs']
        print("topic_name",self.topic_name)
        # self.topic_group_name = 'notify_%s' % self.topic_name
        print("channel name",self.channel_name)
        #subscripe topic wise notification
        async_to_sync(self.channel_layer.group_add)(
            "printerstate",
            self.channel_name
        )
        print("check send notification")
        self.accept()

    def notify(self,event):
        print("notify called")
        message = event["message"]
        self.send(text_data=json.dumps({
            'message': message
        }))

    def receive(self,text_data):
        print("received content")
        async_to_sync(self.channel_layer.group_send)(
            "printerstate",
            {
            "type":"notify",
            "message":"test"})
    def disconnect(self,close_code):
        #remove subscription
        async_to_sync(self.channel_layer.group_discard)(
            "printerstate",
            self.channel_name
        )