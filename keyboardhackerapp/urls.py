from django.urls import path

from keyboardhackerapp import views

urlpatterns = [
    path('mobile', views.mobile),
]
