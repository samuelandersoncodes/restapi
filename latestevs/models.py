from django.db import models


class Ev(models.Model):
    make = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    effieciency = models.CharField(max_length=30)
    top_speed = models.CharField(max_length=30)
    battery_range = models.CharField(max_length=30)
    fast_charge = models.CharField(max_length=20)
    released_date = models.DateField()
