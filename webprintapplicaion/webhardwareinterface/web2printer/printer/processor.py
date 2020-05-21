import json
import wmi
from .printer_management import get_all_win32print_props, get_all_win32printconfigure_props, get_all_win32printconfigure_props,get_all_printers_jobs 
from .printer_management import get_all_printer_status,get_win32printerobjbyname, get_win32printerconfigureobjbyname, get_win32objs_props,conf_printer
from .constants import WIN32_PRINTER,WIN32_PRINTER_CONFIG,WIN32_PRINTERJOB,WIN32PRINTER_STATUS
class Processor(object):
    def __init__(self,req):
        self.request=req
    def get_processor(self):
        print(type(self.request))
        processor=None
        if self.request['proctype']==1:
            processor = PrinterProperityProcessor(self.request)
        elif self.request['proctype']==2:
            processor = PrinterConfigureProcessor(self.request)
        elif self.request['proctype']==3:
            processor = PrintPDFProcessor(self.request)
        return processor

class PrinterProperityProcessor(Processor):
    def __init__(self,reqobj):
        self.request=reqobj 
        self.printername=None
    def process_request(self):        
        response_prop_dict={}
        props_dict = self.request['props']
        self.printername = self.request['printername']
        print("props",props_dict)
        for win32_class_code,props in props_dict.items(): 
            props_value=self.get_props(win32_class_code,props)
            response_prop_dict[win32_class_code]=props_value
        return response_prop_dict
    def format_response(self,win32props,win32confprops):
        print("formatted")
    # get props from win32 win32config
    def get_props(self,win32ClassCode,props):
        win32props =None
        if  self.printername == "all" :
            if win32ClassCode==WIN32_PRINTER:
                win32props = get_all_win32print_props(props)
                print("win32props",win32props)
            elif win32ClassCode == WIN32_PRINTER_CONFIG:
                win32props = get_all_win32printconfigure_props(props)
                print("win32confprops",win32props)
            elif win32ClassCode ==  WIN32_PRINTERJOB:
                win32props =  get_all_printer_status()
            elif win32ClassCode == WIN32PRINTER_STATUS:
                win32props =  get_all_printer_status()
        else:
            win32obj = None
            if win32ClassCode == WIN32_PRINTER:
                win32obj = get_win32printerobjbyname(self.printer_name)
                win32props = get_win32objs_props(win32obj,props)
            elif win32ClassCode == WIN32_PRINTER_CONFIG: 
                win32obj = get_win32printerconfigureobjbyname(self.printername)
                win32props = get_win32objs_props(win32obj,props)                
            print("win32props",win32props)
        return win32props


class PrinterConfigureProcessor(Processor):
    def __init__(self,reqobj):
        self.request =  reqobj
        self.printername = None
    def process_request(self):
        self.props = self.request['props']    
        self.printername = self.request['printername']
        self.conf_type =  self.request["conf_type"]
        return self.configure()
        # if self.request['action'] =="configure":
        #     self.configure()
        # else:
        #     self.get_printers_current_props()
    def configure(self):
        conf_printer(self.conf_type,self.printername,self.props)
        return "successfully configured"
    # def get_printers_props():
    #     if self.printername == "all":
    #         props=get_all_printersconfigure_props(printer_objs,self.props)
    #     else:
    #         printerobj = get_printerconfigureobjbyname(self.printername)
    #         props = get_printer_props(printerobj,self.props)
    #     return props

class PrinterPDFProcessor(Processor):
    def __init__(self,reqobj):
        self.printername = None
    def process_request():
        self.props = self.request['props']    