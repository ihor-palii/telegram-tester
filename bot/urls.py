from django.urls import path
from .views import WebhookListener


urlpatterns = [
    path("<str:token>/", WebhookListener.as_view())
]
