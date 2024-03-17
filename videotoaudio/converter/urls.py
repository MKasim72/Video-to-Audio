from django.contrib import admin
from django.urls import path
# from .views import video_to_audio,index
from converter import views
urlpatterns = [
    path("",views.index,name="home"),
    path('convert-video-to-audio/', views.video_to_audio, name='convert_video_to_audio'),
]
