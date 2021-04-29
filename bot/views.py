from django.http import JsonResponse, HttpRequest
from django.views import View

from .models import MessageUpdate


class WebhookListener(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        body_data = request.POST.dict()
        print(body_data)
        update = MessageUpdate.objects.create(token=kwargs.get("token", ""), data=body_data)
        return JsonResponse({"update_id": update.id})
