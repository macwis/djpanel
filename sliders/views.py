from django.shortcuts import render

# Create your views here.
from bokeh.embed import server_document
from django.http import HttpRequest, HttpResponse


def sliders(request: HttpRequest) -> HttpResponse:
    script = server_document(request.build_absolute_uri())
    return render(request, "base.html", dict(script=script))
