from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

def mobile(req: HttpRequest) -> HttpResponse:
    return render(req, "keyboardhackerapp/mobile.html", {})