from django.shortcuts import render
from django.http import JsonResponse
from .models import Ev
from .serializers import EvSerializer
from rest_framework.decorators import api_view


@api_view(["GET", "POST"])
def evapi(request):
    # evapi view
    if request.method == "GET":
        evs = Ev.objects.all()
        serializer = EvSerializer(evs, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = EvSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def ev_details(request, id):
    # ev detail view
    try:
        evs = Ev.objects.get(pk=id)
    except Ev.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = EvSerializer(evs)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = EvSerializer(evs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)