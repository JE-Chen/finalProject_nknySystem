import sys
import time
import unittest

import JEWebSocket


class TestServer(unittest.TestCase):

    def tearDown(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    def testServer(self):
        websocket = JEWebSocket.WebsocketServer("localhost", 5555)
        time.sleep(3)
