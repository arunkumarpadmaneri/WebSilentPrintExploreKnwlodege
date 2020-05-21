DEBUG=True
#######################*******Printer Constants************##############
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
######################################################################
##########Info Function names ##################
WIN32_PRINTER ="win32_printer"
WIN32_PRINTER_CONFIG ="win32_printer_config"
WIN32_PRINTERJOB = "win32_printerjob"
WIN32PRINTER_STATUS="win32_printer_status"
DEFAULT_WIN32_PRINTER_PROPS = ["ServerName","SystemName","ShareName","RawOnly","PrinterState"]
DEFAULT_WIN32_PRINTER_CONF_PROPS =["Name"]
# WIN32CLASS_TO_FUNCTION_MAPPING = {
# 		"win32_printer_all":"get_all_win32print_props",
# 		"win32_printer_conf_all":"get_all_win32printconfigure_props",
# 		"win32_printer_spec":"get_win32printerobjbyname",
# 		"win32_printer_conf_spec":"get_win32printerconfigureobjbyname"
# }