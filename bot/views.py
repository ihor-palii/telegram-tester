from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MessageUpdate


class WebhookListener(APIView):
    def post(self, *args, **kwargs):
        body_data = self.request.data
        update = MessageUpdate.objects.create(token=kwargs.get("token", ""), data=body_data)
        return Response({"update_id": update.id})
