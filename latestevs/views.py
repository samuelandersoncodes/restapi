from django.shortcuts import render
from . import views


def evapi(request):
    #evapi view
    def get(self, request):
        return render(request, 'evapi.html')
