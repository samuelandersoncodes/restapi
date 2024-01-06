from django.shortcuts import render
from django.http import JsonResponse
from . import views


def evapi(request):
    # evapi view
    return render(request, 'evapi.html')
