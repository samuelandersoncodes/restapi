from django.db import models


class Ev(models.Model):
    make = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    average_price = models.CharField(max_length=20)
    seats = models.IntegerField(
        default=(5, "five"),
        choices=[
            (2, "Two"),
            (5, "Five"),
            (6, "Six"),
            (7, "Seven"),
            (8, "Eight"),
            (9, "Nine"),
        ],
    )
    efficiency = models.CharField(max_length=30)
    top_speed = models.CharField(max_length=30)
    battery_range = models.CharField(max_length=30)
    fast_charge = models.CharField(max_length=20)
    released_date = models.DateField()

    def __str__(self):
        return self.make + " " + self.type
