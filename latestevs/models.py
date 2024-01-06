from django.db import models


class Ev(models.Model):
    make = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    average_price = models.CharField(max_length=20)
    seats = models.IntegerField(
        default=5,
        choices=[
            (2, "Two"),
            (4, "Four"),
            (5, "five"),
            (6, "six"),
            (7, "seven"),
            (8, "eight"),
            (9, "nine"),
        ],
    )
    efficiency = models.CharField(max_length=30)
    top_speed = models.CharField(max_length=30)
    battery_range = models.CharField(max_length=30)
    fast_charge = models.CharField(max_length=20)
    released_date = models.DateField()

    def __str__(self):
        return self.make + " " + self.type
