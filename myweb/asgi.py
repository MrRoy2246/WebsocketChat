import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing  # Import routing from chat

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myweb.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),  # HTTP routing
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns  # Make sure this is correct
        )
    ),
})
