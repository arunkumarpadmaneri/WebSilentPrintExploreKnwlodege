import sys
from PyQt5 import QtCore, QtGui, QtWidgets,QtPrintSupport,QtNetwork
from PyQt5.QtNetwork import *
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.QtWebEngine import *
# from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
# from PyQt5.QtWebEngineCore import QWebEngineHttpRequest
import time
from multiprocessing import Process
from asgiref.sync import sync_to_async
import concurrent.futures
import asyncio
import multiprocessing
executor = concurrent.futures.ProcessPoolExecutor(max_workers=3)
#This function 
async def printhtml(reqdata):
	# print("request data",reqdata)
	# url =reqdata.get("url")
	# cookievalue=reqdata.get("cookieval")
	# if url and cookievalue:
	# 	# status=sync_to_async(printhtml_authcookie(url,cookievalue))
	# 	# status = await printhtml_authcookie(url,cookievalue)
	# 	# Create a limited process pool.
	# 	loop=asyncio.get_event_loop()
	# 	print(loop.is_running)
	# 	blocking_tasks =[loop.run_in_executor(executor,makeprint,url,cookievalue)]
	# 	completed, pending = await asyncio.wait(blocking_tasks)
	# 	# results = [t.result() for t in completed]
	# 	print("completed",completed)	
	# 	print("completion",loop.is_running)
	# 	return "success"
	# else:
	# 	print("Invalid Parameters")
	print("Not Yet Implemented")

def printhtml_authcookie(url,cookievalue):
	print("Not Yet Implemented")
	# time.sleep(20)
	# procs=Process(target=makeprint,args=(url,cookievalue))
	# procs.start()
	makeprint(url,cookievalue)

def printhtml_noauth(url):	
	print("Not Yet Implemented")


# def print(url,printername,pagesize):
# 	import sys
# 	from PyQt5 import QtCore, QtGui, QtWidgets,QtPrintSupport
# 	from PyQt5.QtPrintSupport import QPrinter
# 	from PyQt5.QtCore import *
# 	from PyQt5.QtGui import *
# 	from PyQt5.QtWidgets import *
# 	from PyQt5.QtWebEngine import *
# 	from PyQt5.QtWebEngineWidgets import *
# 	from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

# 	# def WebPrint(url,printername,pagesize):
# 	app = QApplication(sys.argv)
# 	web = QWebEngineView()
# 	web.load(QUrl(url))
# 	printer = QPrinter()
# 	printer.setPageSize(QPrinter.A4)
# 	printer.setPrinterName(printername)
# 	print(printer)
# 	def success(status):
# 		print("printed successuly",status)
# 		app.exit() 
# 	def print_web():
# 		web.page().print(printer,success)
# 	web.show()
	# web.loadFinished.connect(print_web)
	# sys.exit(app.exec())
	# if __name__=="__main__":
	# 	url2="http://localhost:8000/investigation/printresult/order/itooth/location4/itoothBH22067_2018110914:44:19?cat=Laboratory&order=itoothBH22067_2018110914:44:19_itoothlocation124-hours-urine-creatinine,&entitylocation=location2&regprint=false&startdate=20181107&enddate=20181110"
	# 	url1="http://localhost:8000/investigation/testprintbarcode/itooth/itoothBH22067/itoothBH22067_2018110310:13:58_itoothlocation124-hours-urine-creatinine?&order=itoothBH22067_2018110310:13:58_itoothlocation124-hours-urine-creatinine,&entitylocation=location1&regprint=false&startdate=20181028&enddate=20181109"
	# 	"""
	# 		1.url
	# 		2.printer name - Canon-LBP6030-6040-6018L
	# 		3.paper size

	# 	"""
	# 	arguments=sys.argv
	# 	print(arguments)
	# 	if arguments:
	# 		if arguments[0] and arguments[1] and arguments[2]:
	# 			WebPrint(arguments[1],arguments[2],None)


# def makeprint(url,cookiestring):
# 	app = QApplication(sys.argv)
# 	url1="http://localhost:8000/investigation/testprintbarcode/itooth/itoothBH22067/itoothBH22067_2018110310:13:58_itoothlocation124-hours-urine-creatinine?&order=itoothBH22067_2018110310:13:58_itoothlocation124-hours-urine-creatinine,&entitylocation=location1&regprint=false&startdate=20181028&enddate=20181109"
# 	url2="http://localhost:8000/user/login"
# 	web = QWebEngineView()
# 	printer = QPrinter()
# 	printer.setPageSize(QPrinter.A4)
# 	printer.setPrinterName("test")
# 	webenginehttpreq=make_webenginehttpreq(url,cookiestring)
# 	web.load(webenginehttpreq)
# 	# web.show()
# 	def print_status(status):
# 		print("successfully printed",status)
# 		app.exit() 
# 		print("app exits")
# 		print("successfully printed",status)
# 		return status
# 	def after_loaded():
# 		status=web.page().print(printer,print_status)
# 		return status
# 	web.loadFinished.connect(after_loaded)
# 	app.exec_()	
# 	print(multiprocessing.current_process())
# 	print("statussssssss")
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