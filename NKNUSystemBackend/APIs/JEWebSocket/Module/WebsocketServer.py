import asyncio
import sys

import websockets

Users = set()


class WebsocketServer:

    def __init__(self, address, port):
        self.Server = websockets.serve(self.message, address, port)
        asyncio.get_event_loop().run_until_complete(self.Server)
        asyncio.get_event_loop().run_forever()

    @staticmethod
    async def notify_state():
        if USERS:
            message = state_event()
            await asyncio.wait([user.send(message) for user in USERS])

    @staticmethod
    async def notify_users():
        if USERS:
            message = users_event()
            await asyncio.wait([user.send(message) for user in USERS])

    @staticmethod
    async def register(websocket):
        USERS.add(websocket)
        await notify_users()

    @staticmethod
    async def unregister(websocket):
        USERS.remove(websocket)
        await notify_users()

    @staticmethod
    async def message(websocket, path):
        async for message in websocket:
            print("Command : " + message)
            if message == 'Hello':
                await websocket.send("Hello Client")
            elif message == 'exit':
                await websocket.send("Server close connection")
                await websocket.close()

