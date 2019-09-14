from django.urls import path

from keyboardhackerapp import views

urlpatterns = [
    path('mobile', views.mobile),
    path('audio-upload', views.audio_upload),
    path('sync', views.sync),
]
