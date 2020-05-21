from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from celery import task
from web2printer.printer.printer_management import get_all_printer_status

@task
def push_printerstate():
	print("task called")
	channel_layer = get_channel_layer()
	message = get_all_printer_status() 
	async_to_sync(channel_layer.group_send)("printerstate", {"type": "notify","message":message},)

# from __future__ import absolute_import, unicode_literals
# from celery import shared_task
# @shared_task
# def add(x, y):
#     return x + y

