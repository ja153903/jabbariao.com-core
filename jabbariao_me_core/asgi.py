import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jabbariao_me_core.settings")

application = get_asgi_application()
