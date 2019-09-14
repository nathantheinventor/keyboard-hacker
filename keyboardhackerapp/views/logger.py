import json

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from keyboardhackerapp.models import RecordEvent

def logger(req: HttpRequest) -> HttpResponse:
    return render(req, "keyboardhackerapp/logger.html", {})


def is_active(req: HttpRequest) -> HttpResponse:
    if RecordEvent.objects.count() == 0:
        return HttpResponse('0')
    else:
        last = RecordEvent.objects.latest('audio_start_time')
        active = '1' if last.active else '0'
        return HttpResponse(active)


def upload_keys(req: HttpRequest) -> HttpResponse:
    for attr in req.POST:
        print(attr, req.POST[attr])

    # Do we have an active event?
    if RecordEvent.objects.count() == 0:
        return HttpResponse('No logging sessions', status=400)

    # Where to save?
    guid = RecordEvent.objects.latest('audio_start_time').guid
    json.dump(json.loads(req.POST['data']), "/tmp/%s.wav" % guid)
