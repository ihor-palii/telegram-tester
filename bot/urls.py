from django.urls import path
from .views import WebhookListener


urlpatterns = [
    path("webhook/<str:token>/", WebhookListener.as_view())
]
