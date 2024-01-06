from django.shortcuts import render
from django.http import JsonResponse
from .models import Ev
from .serializers import EvSerializer
from rest_framework.decorators import api_view


def evapi(request):
    # evapi view
    evs = Ev.objects.all()
    serializer = EvSerializer(evs, many=True)
    return JsonResponse({"evs": serializer.data}, safe=False)
