from channels.consumer import AsyncConsumer
from chat.printer_management import printhtml
class HtmlPrintWorker(AsyncConsumer):
	async def print_worker(self,event):
		print("event",event)
		response=await printhtml(event['reqdata'])
		print("worker",response)
		await self.channel_layer.send(
		"reply",
        {
            "type": "getw",
            "reqdata": "mssss"
            },
        )

	async def printtest(self,reqdata):
		print(reqdata)