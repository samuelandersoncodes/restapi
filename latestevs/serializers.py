from rest_framework import serializers
from .models import Ev


class EvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ev
        fields = [
            "id",
            "make",
            "average_price",
            "seats",
            "type",
            "efficiency",
            "top_speed",
            "battery_range",
            "fast_charge",
            "released_date",
        ]
