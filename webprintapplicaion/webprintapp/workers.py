import asyncio
import concurrent.futures
from printer_management import get_printer_names,img_print
import json
# from PyQt5 import QtCore, QtGui, QtWidgets,QtPrintSupport,QtNetwork
# from PyQt5.QtNetwork import *
# from PyQt5.QtPrintSupport import QPrinter
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtWebEngine import *
# from PyQt5.QtWebEngineWidgets import *
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
# from PyQt5.QtWebEngineCore import QWebEngineHttpRequest
import sys
# Queue to store a tasks 
queue = asyncio.Queue()
outputqueue = asyncio.Queue()

# executor = concurrent.futures.ProcessPoolExecutor(
#         max_workers=2,
#     )

############ message format#################
# action - print, info 
# type - img,html,raw(text or printer supported commands) 
# format(img) - base64,bytes,file
# format(html) - file,htmltring
# format(text) - text,supported commands   
async def printconsumer(message):
	await queue.put(message)
	json.loads([])
	return "successfully added"
# info type - get printers name - 1
#TODO:Dynamically get info function names
async def infoconsumer(message):
	info_type=message["info_type"]
	if info_type == 1:
		result = get_printer_names()
	else:
		result = []
	return result
# async def htmlprintconsumer(message):
# 	await queue.put(message)
# 	return "successfully added"


async def htmlprintproducer():
	msg=await outputqueue.get()
	return msg

async def worker():
	print(queue.qsize)
	msg =  await queue.get()
	queue.taskdone()
	print(queue.qsize)
	asyncio.sleep(3)
	# loop = asyncio.get_event_loop()
	# blocking_tasks = [
 #        loop.run_in_executor(executor, makeprint, None,None)
 #    ]
	# completed, pending = await asyncio.wait(blocking_tasks)
	# try:
	# 	results = [t.result() for t in completed]
	# except:
	# 	print(sys.exc_info())
	# print(results)
	await outputqueue.put(msg)

# def makeprint(url,cookiestring):
# 	app = QApplication(sys.argv)
# 	url1="http://localhost:8000/investigation/testprintbarcode/itooth/itoothBH22067/itoothBH22067_2018110310:13:58_itoothlocation124-hours-urine-creatinine?&order=itoothBH22067_2018110310:13:58_itoothlocation124-hours-urine-creatinine,&entitylocation=location1&regprint=false&startdate=20181028&enddate=20181109"
# 	url2="http://localhost:8000/user/login"
# 	web = QWebEngineView()
# 	printer = QPrinter()
# 	printer.setPageSize(QPrinter.A4)
# 	printer.setPrinterName("test")
# 	# webenginehttpreq=make_webenginehttpreq(url,cookiestring)
# 	# web.load(webenginehttpreq)
# 	web.load(QUrl(url2))
# 	# web.show()
# 	def print_status(status):
# 		print("successfully printed",status)
# 		app.exit() 
# 		print("app exits")
# 		print("successfully printed",status)
# 	def after_loaded():
# 		status=web.page().print(printer,print_status)
# 	web.loadFinished.connect(after_loaded)
# 	app.exec_()	
# 	return "success"


# def make_webenginehttpreq(url,cookval):
# 	# cookval="vid=f0Ba62WymXTkbaTjJZ3n; __hstc=181257784.75459c14da4fdf28b495241c6b77b631.1539161902496.1542282819929.1542303664377.55; hubspotutk=75459c14da4fdf28b495241c6b77b631; _ga=GA1.1.34458617.1540793115; _gid=GA1.1.283817371.1542127926; __hssrc=1; __hssc=181257784.1.1542303664377; _fbp=fb.0.1542303667604.1945466683"
# 	webenginehttpreq=QWebEngineHttpRequest(QUrl(url),1) 
# 	# webenginehttpreq.setMethod(0)
# 	# postData = QUrlQuery()
# 	# postData.addQueryItem("email", "nathankps@yahoo.com");
# 	# postData.addQueryItem("pwd", "test")
# 	# print(type(postData),postData.toString(QUrl.FullyEncoded))
# 	webenginehttpreq.setHeader(bytearray("Accept","utf-8"),bytearray("text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","utf-8"))
# 	webenginehttpreq.setHeader(bytearray("Cookie","utf-8"),bytearray(cookval,"utf-8"))
# 	# webenginehttpreq.setHeader(bytearray("Accept","utf-8"),bytearray("text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","utf-8"))
# 	webenginehttpreq.setHeader(bytearray("Host","utf-8"),bytearray("localhost:8000","utf-8"))
# 	webenginehttpreq.setHeader(bytearray("Content-Type","utf-8"),bytearray("application/x-www-form-urlencoded","utf-8"))
# 	# webenginehttpreq.setPostData(bytearray(postData.toString(QUrl.FullyEncoded),"utf-8"))
# 	return webenginehttpreq