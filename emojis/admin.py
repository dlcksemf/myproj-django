from django.contrib import admin
from emojis.models import Emojis


@admin.register(Emojis)
class EmojisAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
