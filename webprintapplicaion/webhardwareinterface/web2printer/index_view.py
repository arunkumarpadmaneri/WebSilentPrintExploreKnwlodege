
from django.shortcuts import render
from web2printer.printer.printer_management import get_printer_props_homepage
from django.contrib.auth.decorators import login_required
 # Create your views here.
@login_required
def home(request):
	# print("request obj type",request.__dict__)
	printer_props,printer_conf_props=get_printer_props_homepage()
	print("printer basic properties",printer_props)
	return render(request, 'web2printer/index.html', {"printers":printer_props})
	
