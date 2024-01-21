from django.urls import path
from . import views

urlpatterns = [
    path('', views.evapi, name='evapi'),
    path('latestevs/<int:id>/', views.ev_details, name='ev_details'),
]
