import asyncio

import websockets


class WebsocketClient:

    def __init__(self, uri):
        asyncio.get_event_loop().run_until_complete(self.connect_to_server_receive_forever('ws://' + str(uri)))

    @staticmethod
    async def connect_to_server_receive_forever(uri):
        async with websockets.connect(uri) as websocket:
            await websocket.send("exit")
            print(await websocket.recv())
