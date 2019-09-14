from django.urls import path, include

from keyboardhackerapp import views

urlpatterns = [
    path('mobile', views.mobile),
    path('audio-upload', views.audio_upload),
    path('logger', views.logger),
    path('sync', views.sync),
]
