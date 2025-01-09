# urls.py

from django.urls import path
from .views import serve_media  # Import the media serving view.

urlpatterns = [
    ...
    path('static/<path:path>', serve_media, name='serve-media'),
]
