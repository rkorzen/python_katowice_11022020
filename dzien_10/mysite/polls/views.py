from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def hello_view(request, name="World"):
    return HttpResponse(f"Hello {name}")


