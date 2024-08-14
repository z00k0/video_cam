from django.urls import path, include
from .views import record, get_video, custom_admin, video_page, index, finish, set_status

urlpatterns = [
    path('', index),
    path('record', record, name='record'),
    path('get_video', get_video),
    path('finish', finish),
    path('all_videos', custom_admin),
    path('all_videos/<int:ident>', video_page),
    path('all_videos/<int:ident>/set_status', set_status)
]