from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from keyboardhackerapp.models import RecordEvent


def mobile(req: HttpRequest) -> HttpResponse:
    return render(req, "keyboardhackerapp/mobile.html", {})


def activate(req: HttpRequest) -> HttpResponse:
    audio_start_time = int(req.POST['audio_start_time'])
    print(audio_start_time)
    RecordEvent.objects.create(audio_start_time=audio_start_time, active=True)
    return HttpResponse('ok')

def audio_upload(req: HttpRequest) -> HttpResponse:
    if RecordEvent.objects.count() == 0:
        return HttpResponse('No recording sessions', status=400)

    last = RecordEvent.objects.latest('audio_start_time')
    guid = last.guid
    last.active = False
    last.save()

    for file in req.FILES:
        file = req.FILES[file]
        with open("/tmp/%s.wav" % guid, "wb+") as f:
            for chunk in file.chunks():
                f.write(chunk)

    return HttpResponse("ok")
