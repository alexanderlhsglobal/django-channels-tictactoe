from django.urls import path
from .consumers import TicTacToeConsumer

websocket_urlpatterns = [
    path('ws/play/<slug:room_code>/', TicTacToeConsumer.as_asgi()),
]