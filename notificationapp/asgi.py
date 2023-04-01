import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from blog.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notificationapp.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    "websocket": URLRouter(websocket_urlpatterns),
    "http": application,
})