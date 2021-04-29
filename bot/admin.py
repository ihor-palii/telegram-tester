from django.contrib import admin
from .models import MessageUpdate


@admin.register(MessageUpdate)
class MessageUpdateAdmin(admin.ModelAdmin):
    list_display = ["id"]
