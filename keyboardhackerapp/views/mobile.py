from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

def mobile(req: HttpRequest) -> HttpResponse:
    return render(req, "keyboardhackerapp/mobile.html", {})

def audio_upload(req: HttpRequest) -> HttpResponse:
    for file in req.FILES:
        file = req.FILES[file]
        with open("/tmp/file.wav", "wb+") as f:
            for chunk in file.chunks():
                f.write(chunk)

    return HttpResponse("ok")

def example(req):
    data = json.loads(req.POST["data"])
    