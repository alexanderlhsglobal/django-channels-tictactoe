from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import Game, Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('play/<slug:room_code>/<slug:choice>/', Game.as_view(), name='game'),
]

# Serving media files in development
if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)