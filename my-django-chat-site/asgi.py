"""
ASGI config for my-django-chat-site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my-django-chat-site.settings')

application = ProtocolTypeRouter({
  # defines type of protocol
  "http": get_asgi_application(),
})
