from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

def logger(req: HttpRequest) -> HttpResponse:
    return render(req, "keyboardhackerapp/logger.html", {})