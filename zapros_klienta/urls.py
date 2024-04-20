from django.urls import path
from .views import get_location, chatbot_endpoint

urlpatterns = [
    path('get_location/', get_location, name='get_location'),
    path('api/', chatbot_endpoint, name='chatbot_endpoint'),
]
