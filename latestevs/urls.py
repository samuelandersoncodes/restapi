from django.urls import path

urlpatterns = [
    path("", views.EvApi.as_view(), name="evapi"),
]
