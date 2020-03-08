import math

from django.http import HttpResponse
from django.shortcuts import render

from maths.models import Math


# Create your views here.

def add(request, a, b):
    Math.objects.create(operation="add", a=a, b=b)
    result = a + b
    return render(
        request,
        'maths/result.html',
        {"result": result, 'operacja': "Dodawanie"}
    )


def sub(request, a, b):
    Math.objects.create(operation="sub", a=a, b=b)
    result = a - b
    return render(
        request,
        'maths/result.html',
        {"result": result}
    )


def div(request, a, b):
    if b == 0:
        result = "Nie można dzielić przez 0"
    else:
        Math.objects.create(operation="div", a=a, b=b)
        result = a / b
    return render(
        request,
        'maths/result.html',
        {"result": result}
    )


def mul(request, a, b):
    Math.objects.create(operation="mul", a=a, b=b)
    result = a * b
    return render(
        request,
        'maths/lista.html',
        {"result": result}
    )


def sqrt(request, a):
    Math.objects.create(operation="sqrt", a=a)
    result = math.sqrt(a)
    return render(
        request,
        'maths/result.html',
        {"result": result}
    )


def pow_view(request, a, b):
    Math.objects.create(operation="pow", a=a, b=b)
    result = a ** b
    return render(
        request,
        'maths/result.html',
        {"result": result}
    )


def lista_elementow(request):
    elementy = Math.objects.all()
    return render(
        request,
        'maths/lista.html',
        {"elements": elementy}
    )
