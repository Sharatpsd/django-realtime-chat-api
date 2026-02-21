from django.urls import path
from .views import chat_history

urlpatterns = [
    path("history/<str:room_name>/", chat_history),
]