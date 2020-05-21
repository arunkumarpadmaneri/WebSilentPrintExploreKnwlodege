import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import pythoncom
import wmi
import win32print
import json
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

'''
This is a simple Websocket Echo server that uses the Tornado websocket handler.
Please run `pip install tornado` with python of version 2.7.9 or greater to install tornado.
This program will echo back the reverse of whatever it recieves.
Messages are output to the terminal for debuggin purposes. 
''' 
 
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('new connection')
      
    def on_message(self, message):
        print ('message received:',type(message))
        msg = json.loads(message)
        print("msg",msg)
        response=get_sys_info(msg['win32classname'],msg['props'])
        response_dict=json.dumps(response)
        # self.set_default_printer(message)
        # Reverse Message and send it back
        print ('sending back message',response_dict)
        self.write_message(response_dict)
 
    def on_close(self):
        print ('connection closed')
    def set_default_printer(self,Printername):
        win32print.SetDefaultPrinter(Printername)
        print("check")
    def check_origin(self, origin):
        return True
 
application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
 
if __name__ == "__main__":
# def main():
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()