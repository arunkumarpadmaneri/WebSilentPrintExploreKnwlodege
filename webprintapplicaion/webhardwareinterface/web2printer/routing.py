
# web2printer/routing.py
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/web2printer/*',consumers.PrinterConsumer),
    url(r'^ws/notification/*',consumers.NotificationConsumer)
    # url(r'^ws/web2printer/printerconfiguration',consumers.ConfigurePrinterConsumer),
    # url(r'^ws/web2printer/print',consumers.PrintConsumer)

]
