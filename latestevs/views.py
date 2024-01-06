from django.shortcuts import render
from django.http import JsonResponse
from .models import Ev
from .serializers import EvSerializer
from rest_framework.decorators import api_view


@api_view("GET", "POST")
def evapi(request):
    # evapi view
    if request.method == "GET":
        evs = Ev.objects.all()
        serializer = EvSerializer(evs, many=True)
        return JsonResponse({"evs": serializer.data}, safe=False)
