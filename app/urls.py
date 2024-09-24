from django.urls import path
from .views import index_view,proxy_request
from . import consumers

websocket_urlpatterns = [
    path('ws/speech/', consumers.SpeechToTextConsumer.as_asgi()),
]

# urlpatterns = [
#     path('', index_view, name='index'),  # Home page
# ]


urlpatterns = [
    path('', index_view, name='index'),  # Main page
    path('api/proxy/', proxy_request, name='proxy_request'),  # API for proxy requests
]