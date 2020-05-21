import pythoncom
import wmi
import win32print

# ################# window class and WMI ##################################
def get_wmi():
	pythoncom.CoInitialize()
	return wmi.WMI()
def get_win32_objs(win32classname):
	return get_wmi().instances(win32classname)
############################################################
#********************Printer Properties#########################

def get_default_printername():
	import win32print
	return win32print.GetDefaultPrinter ()

def get_obj_attr(obj,attributename):
	if hasattr(obj,attributename):
		return getattr(obj,attributename)
	else:
		return None

def  get_printer_attr(obj,attributename):
		return get_obj_attr(obj,attributename)

def get_sys_info(win32classname,props):
	objcount = 0
	sysinfo = {}
	for obj in get_win32_objs(win32classname):
		sysinfo[objcount]=get_win32objs_props(obj,props)
		objcount=objcount+1
	return sysinfo

def get_win32objs_props(printerobj,arrprop):
	props = {}
	for prop in arrprop:
		val=get_printer_attr(printerobj,prop)
		props[prop]=val
	print(props)
	return props



