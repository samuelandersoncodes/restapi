from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.evapi, name='evapi'),
    path('latestevs/<int:id>/', views.ev_details, name='ev_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)