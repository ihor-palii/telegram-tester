from django.http import JsonResponse, HttpRequest
from django.views import View

from .models import MessageUpdate


class WebhookListener(View):
    def post(self, *args, **kwargs):
        body_data = self.request.POST.dict()
        print(self.request.headers, self.request.body)
        update = MessageUpdate.objects.create(token=kwargs.get("token", ""), data=body_data)
        return JsonResponse({"update_id": update.id})
