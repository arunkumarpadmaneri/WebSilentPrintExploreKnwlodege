import asyncio
import datetime
import random
import websockets
from handler import mainhandler
start_server = websockets.serve(mainhandler, 'localhost', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()