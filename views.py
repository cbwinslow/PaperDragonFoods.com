# views.py

from django.views.static import serve
from django.conf import settings

def serve_media(request, path):
    return serve(request, os.path.join(settings.MEDIA_ROOT, path))
