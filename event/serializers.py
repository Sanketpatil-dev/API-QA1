from rest_framework import serializers
from .models import *


class eventsserializer(serializers.ModelSerializer):
    class Meta:
        model=events
        fields = "__all__"