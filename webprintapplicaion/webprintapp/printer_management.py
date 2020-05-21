from escpos import *
from constants import *
import sys

import wmi
class WPrinter(object):
	def __init__(self,ip):
		sel.printer = printer.Network(ip)

	def img_print(imgpath):
		if self.printer:
			try:
				self.printer.image(imgpath)
			except:
				print("print an image failed",sys.exc_info())
		else:
			print("printer is not valid")
	def barcode_print():
		self.printer.barcode('1324354657687', 'EAN13', 64, 2, '', '')
		self.printer.cut()
	def text_print():
		self.printer.text("hello world")

def get_wmi():
	return wmi.WMI()
def get_default_printername():
	return win32print.GetDefaultPrinter ()
# return printer objs
def get_printers():
	printerobjs = [];
	for printer in get_wmi().Win32_Printer ():
		if printer.DeviceId:
			printerobjs.append(printer)
	return printerobjs
#return printer device id
def get_printer_names():
	printernames = [];
	for printer in get_wmi().Win32_Printer ():
		if printer.DeviceId:
			printernames.append(printer.DeviceId)
	return printernames
#return specified printer jobs
def get_jobs(printer):
	printerjobobjs=[]
	for job in c.Win32_PrintJob (DriverName=printer.DriverName):
		printerjobobjs.append(job)
	return printerjobobjs
def img_print(printer_name,data,scaling=False,isfile=False):
	import win32print
	import win32ui
	from PIL import Image, ImageWin
	from io import BytesIO
	import base64
	#
	# Constants for GetDeviceCaps
	#
	#
	# HORZRES / VERTRES = printable area
	#
	HORZRES = 8
	VERTRES = 10
	#
	# LOGPIXELS = dots per inch
	#
	LOGPIXELSX = 88
	LOGPIXELSY = 90
	#
	# PHYSICALWIDTH/HEIGHT = total area
	#
	PHYSICALWIDTH = 110
	PHYSICALHEIGHT = 111
	#
	# PHYSICALOFFSETX/Y = left / top margin
	#
	PHYSICALOFFSETX = 112
	PHYSICALOFFSETY = 113

	# printer_name = win32print.GetDefaultPrinter ()

	#
	# You can only write a Device-independent bitmap
	#  directly to a Windows device context; therefore
	#  we need (for ease) to use the Python Imaging
	#  Library to manipulate the image.
	#
	# Create a device context from a named printer
	#  and assess the printable size of the paper.
	#
	hDC = win32ui.CreateDC ()
	hDC.CreatePrinterDC (printer_name)
	printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES)
	printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)
	printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY)

	#
	# Open the image, rotate it if it's wider than
	#  it is high, and work out how much to multiply
	#  each pixel by to get it as big as possible on
	#  the page without distorting.
	#
	if isdata:
		img = Image.open(BytesIO(base64.b64decode(file_name))) 
	else:
		img = Image.open (file_name)
	bmp = img.convert("RGB") 
	print("image mode",bmp.mode)
	if bmp.size[0] > bmp.size[1]:
	  bmp = bmp.rotate (90)

	if scaling:
		ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
		scale = min (ratios)
		scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
		x1 = int ((printer_size[0] - scaled_width) / 2)
		y1 = int ((printer_size[1] - scaled_height) / 2)
		x2 = x1 + scaled_width
		y2 = y1 + scaled_height
	else:		
		x1 = int ((printer_size[0]) / 2)
		y1 = int ((printer_size[1]) / 2)
		x2 = x1 + bmp.size[0]
		y2 = y1 + bmp.size[1]

	#
	# Start the print job, and draw the bitmap to
	#  the printer device at the scaled size.
	#
	hDC.StartDoc (file_name)
	hDC.StartPage ()

	dib = ImageWin.Dib (bmp)
	dib.draw (hDC.GetHandleOutput (), (x1, y1, x2, y2))

	hDC.EndPage ()
	hDC.EndDoc ()
	hDC.DeleteDC ()


# raw_data could equally be raw PCL/PS read from
#  some print-to-file operation

# if sys.version_info >= (3,):
#   raw_data = bytes ("This is a test", "utf-8")
# else:
#   raw_data = "This is a test"

def raw_printing(printer_name,raw_data,printdocname="rawprint"):
	import os, sys
	import win32print
	hPrinter = win32print.OpenPrinter (printer_name)
	try:
	  hJob = win32print.StartDocPrinter (hPrinter, 1, (printdocname, None, "RAW"))
	  try:
	    win32print.StartPagePrinter (hPrinter)
	    win32print.WritePrinter (hPrinter,bytes(raw_data,"utf-8"))
	    win32print.EndPagePrinter (hPrinter)
	  finally:
	    win32print.EndDocPrinter (hPrinter)
	finally:
	  win32print.ClosePrinter (hPrinter)



####################unittesting###########################
def test_img_print():
	data2='''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'''
	#second parameter for scaling 
	img_print(get_default_printername(),data2,False)
	img_print(get_default_printername(),data2,True)
def test_raw_printing():
	data="\nN\n"+"q609\n"+"Q203,26\n"+"B5,26,0,1A,3,7,152,B,'1234'\n"+"A310,26,0,3,1,1,N,'SKU 00000 MFG 0000'\n"+"A310,56,0,3,1,1,N,'QZ PRINT APPLET'\n"
	raw_printing(get_default_printername(),data)
###########################################################