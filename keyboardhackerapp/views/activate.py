def register(request):
    if request.method == "POST":
    context = {
        'form': form
    }
    return render(request, "template.html", context)
