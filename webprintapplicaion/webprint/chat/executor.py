import sys
from PyQt5 import QtCore, QtGui, QtWidgets,QtPrintSupport,QtNetwork
from PyQt5.QtNetwork import *
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngine import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWebEngineCore import QWebEngineHttpRequest
import concurrent.futures
import asyncio
import time
# executor = concurrent.futures.ProcessPoolExecutor(max_workers=3)

def makeprint():
	app = QApplication(sys.argv)
	url1="http://localhost:8000/investigation/testprintbarcode/itooth/itoothBH22067/itoothBH22067_2018110310:13:58_itoothlocation124-hours-urine-creatinine?&order=itoothBH22067_2018110310:13:58_itoothlocation124-hours-urine-creatinine,&entitylocation=location1&regprint=false&startdate=20181028&enddate=20181109"
	url2="https://stackoverflow.com/questions/46074841/why-coroutines-cannot-be-used-with-run-in-executor"
	web = QWebEngineView()
	printer = QPrinter()
	printer.setPageSize(QPrinter.A4)
	printer.setPrinterName("test")
	# webenginehttpreq=make_webenginehttpreq(url,cookiestring)
	web.load(QUrl(url2))
	# web.show()
	def print_status(status):
		print("successfully printed",status)
		app.exit() 
		print("app exits")
		print("successfully printed",status)
		return status
	def after_loaded():
		status=web.page().print(printer,print_status)
		return status
	web.loadFinished.connect(after_loaded)
	app.exec_()	
	print("statussssssss")
	return "success"

# async def functiontest():
# 	loop=asyncio.get_event_loop()
# 	blocking_tasks = [
#     loop.run_in_executor(executor,makeprint)
# 	]
# 	# completed, pending = await asyncio.wait(blocking_tasks)
# 	# results = [t.result() for t in completed]
# 	# print(results)
# def functionsleep():
# 	print("entered1")
# 	time.sleep(5)
# 	print("completed1")
# 	return "suceess"
# def functionsleep2():
# 	print("entered")
# 	time.sleep(1)
# 	print("completed2")
# 	return "success2"
# async def main():	
# 	with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
# 		future = executor.submit(functionsleep)
# 		future1 = executor.submit(functionsleep2)
# 		print(future.result())
# 		print(future1.result())
# if __name__=="__main__":
# 	# await functiontest()

import asyncio
import concurrent.futures
import logging
import sys
import time


def blocks(n):
    log = logging.getLogger('blocks({})'.format(n))
    log.info('running')
    time.sleep(0.1)
    log.info('done')
    return n ** 2


async def run_blocking_tasks(executor):
    log = logging.getLogger('run_blocking_tasks')
    log.info('starting')

    log.info('creating executor tasks')
    loop = asyncio.get_event_loop()
    blocking_tasks = [
        loop.run_in_executor(executor,makeprint)
    ]
    log.info('waiting for executor tasks')
    completed, pending = await asyncio.wait(blocking_tasks)
    results = [t.result() for t in completed]
    log.info('results: {!r}'.format(results))

    log.info('exiting')


if __name__ == '__main__':
    # Configure logging to show the name of the thread
    # where the log message originates.
    logging.basicConfig(
        level=logging.INFO,
        format='%(threadName)10s %(name)18s: %(message)s',
        stream=sys.stderr,
    )

    # Create a limited thread pool.
    executor = concurrent.futures.ProcessPoolExecutor(
        max_workers=3,
    )

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(
            run_blocking_tasks(executor)
        )
    finally:
        event_loop.close()
