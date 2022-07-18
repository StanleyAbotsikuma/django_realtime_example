"""
ASGI config for boom project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boom.settings')

# application = get_asgi_application()


# import os

# from channels.routing import ProtocolTypeRouter
# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# application = ProtocolTypeRouter({
#   'http': get_asgi_application(),
# })

# import os

# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application

# import test_app.routing

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# application = ProtocolTypeRouter({
#   'http': get_asgi_application(),
#   'websocket': URLRouter(
#       test_app.routing.websocket_urlpatterns
#     ),
# })

# core/asgi.py

import os

from channels.auth import AuthMiddlewareStack  # new import
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import test_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket': AuthMiddlewareStack(  # new
        URLRouter(
            test_app.routing.websocket_urlpatterns
        )
    ),  # new
})