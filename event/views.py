from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets
import json

# Create your views here.
class eventsviewset(viewsets.ModelViewSet):
    queryset=events.objects.all()
    serializer_class=eventsserializer
