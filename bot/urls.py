from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import WebhookListener


urlpatterns = [
    path("webhook/<str:token>/", csrf_exempt(WebhookListener.as_view()))
]
