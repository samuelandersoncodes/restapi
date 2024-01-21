from django.urls import path
from . import views

urlpatterns = [
    path('', views.evapi, name='evapi'),
    path('latestevs/<int:pk>/', views.ev_details, name='ev_details'),
]
