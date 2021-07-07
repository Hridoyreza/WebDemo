from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html", {'name' : 'jdhkjfs'})


def add(request):
    val1 = int(request.POST["number1"])
    val2 = int(request.POST["number2"])
    res = int(val1 + val2)
    return render(request, "result.html", {'result': res})
