from django.db import models


class MessageUpdate(models.Model):
    data = models.JSONField()
    token = models.CharField(max_length=256, blank=True, default="")
    created_on = models.DateTimeField(auto_now_add=True)
