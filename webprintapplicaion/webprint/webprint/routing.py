from channels.routing import ProtocolTypeRouter,URLRouter,ChannelNameRouter
from channels.auth import AuthMiddlewareStack
import chat.routing
from webprint import consumer
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),    # (http->django views is added by default)
	"channel": ChannelNameRouter({
	        "htmlprint": consumer.HtmlPrintWorker,
	        "reply":chat.consumers.HtmlPrintConsumer,
	    }),
})