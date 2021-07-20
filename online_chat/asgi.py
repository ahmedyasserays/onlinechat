"""
ASGI config for online_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from main.routing import websocket_urlpatterns
from django import setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_chat.settings')

django_asgi_app = get_asgi_application()
setup()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    )
})
