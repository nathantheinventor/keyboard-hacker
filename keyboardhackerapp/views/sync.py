from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from time import time

def sync(req: HttpRequest) -> HttpResponse:
    return HttpResponse(time())