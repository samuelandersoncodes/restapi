from django.shortcuts import render
from django.http import JsonResponse
from .serializers import EvSerializer


def evapi(request):
    # evapi view
    return render(request, 'evapi.html')
