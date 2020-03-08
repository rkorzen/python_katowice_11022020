import math

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def add(request, a, b):
    result = a + b
    return render(
        request,
        'maths/result.html',
        {"result": result, 'operacja': "Dodawanie"}
    )


def sub(request, a, b):
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
        result = a / b
    return render(
        request,
        'maths/result.html',
        {"result": result}
    )

def mul(request, a, b):
    result = a * b
    return render(
        request,
        'maths/result.html',
        {"result": result}
    )

def sqrt(request, a):
    result = math.sqrt(a)
    return render(
        request,
        'maths/result.html',
        {"result": result}
    )
def pow_view(request, a, b):
    result = a ** b
    return render(
        request,
        'maths/result.html',
        {"result": result}
    )