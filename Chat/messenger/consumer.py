import json
from channels.generic.websocket import WebsocketConsumer

# синхронный потребитель WebSocket, который принимает все соединения,
# получает сообщения от своего клиента и отправляет эти сообщения обратно тому же клиенту.
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))