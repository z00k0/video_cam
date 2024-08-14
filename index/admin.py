from django.contrib import admin

from index.models import VideoModel


@admin.register(VideoModel)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ("ident", "file_name", "status")
