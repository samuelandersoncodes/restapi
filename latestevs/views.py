from django.shortcuts import render
from . import views


def evapi(request):
    # evapi view
    return render(request, 'evapi.html')
