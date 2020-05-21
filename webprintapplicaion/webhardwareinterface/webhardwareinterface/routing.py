from channels.routing import ProtocolTypeRouter,URLRouter,ChannelNameRouter
from channels.auth import AuthMiddlewareStack
from web2printer  import routing as printerrouter
# from webprint import consumer
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            printerrouter.websocket_urlpatterns
        )
    ),    # (http->django views is added by default)
	# "channel": ChannelNameRouter({
	#         "htmlprint": consumer.HtmlPrintWorker,
	#         "reply":chat.consumers.HtmlPrintConsumer,
	#     }),
})