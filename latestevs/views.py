from django.shortcuts import render
from django.http import JsonResponse
from .models import Ev
from .serializers import EvSerializer


def evapi(request):
    # evapi view
    evs = Ev.objects.all()
    serializer = EvSerializer(evs, many=True)
    return JsonResponse(serializer.data, safe=False)
