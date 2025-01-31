import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

from ideas.chat.routing import websocket_urlpatterns  # Używamy routing z chat

# Ustawienie zmiennej środowiskowej dla Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')
django.setup()

# Aplikacja ASGI
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),  # Obsługuje HTTP
        "websocket": AuthMiddlewareStack(  # Middleware dla WebSocket
            URLRouter(websocket_urlpatterns)  # Ładowanie URL z pliku routing.py
        ),
    }
)
