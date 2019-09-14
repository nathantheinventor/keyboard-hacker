from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from keyboardhackerapp.models import RecordEvent


def mobile(req: HttpRequest) -> HttpResponse:
    return render(req, "keyboardhackerapp/mobile.html", {})

def audio_upload(req: HttpRequest) -> HttpResponse:

    if RecordEvent.objects.count() == 0:
        return HttpResponse('No recording sessions', status=300)

    guid = RecordEvent.objects.latest(order='audio_start_time').guid
    for file in req.FILES:
        file = req.FILES[file]
        with open("/tmp/%s.wav" % guid, "wb+") as f:
            for chunk in file.chunks():
                f.write(chunk)

    return HttpResponse("ok")
