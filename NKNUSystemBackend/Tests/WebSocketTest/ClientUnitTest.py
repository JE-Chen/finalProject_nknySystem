import sys
import time
import unittest

import JEWebSocket


class TestClient(unittest.TestCase):

    def tearDown(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    def testClient(self):
        client = JEWebSocket.WebsocketClient('localhost:5555')
        time.sleep(3)
