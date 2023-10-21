from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket connect........',event)
        self.send({
            'type':'websocket.accept',
        })

    
    def websocket_receive(self,event):
        print('websocket received from Clint',event)
        print(event['text'])
        self.send({
            'type':'websocket.send',
            'text':'Message Send to Client '
        })


    def websocket_disconnect(self,event):
        print('websocket disconnect........',event)
        raise StopConsumer()