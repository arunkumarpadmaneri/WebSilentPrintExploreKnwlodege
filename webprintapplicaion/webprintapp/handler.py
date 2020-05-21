
import asyncio
import datetime
import random
import websockets
import json
from workers import infoconsumer,printconsumer,htmlprintproducer 
async def mainhandler(websocket,path):
	consumer_task = asyncio.ensure_future(consumer_handler(websocket, path))
	producer_task = asyncio.ensure_future(producer_handler(websocket, path))
	done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED,
    )
	print("created task")
	for task in pending:
		task.cancel()


async def consumer_handler(websocket,path):
	async for message in websocket:
		reqdict=json.loads(message)
		action = reqdict["action"]
		msg    =  reqdict["msg"]
		print("test",action)
		if action!=1:
			response = await printconsumer(msg)
		else:
			response = await infoconsumer(msg)
			print(response)
		await websocket.send(json.dumps(response))
async def producer_handler(websocket, path):
    while True:
        message = await htmlprintproducer()
        await websocket.send(message)