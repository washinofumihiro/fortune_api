# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import BloodType, Result
from .serializer import BloodTypeSerializer, ResultSerializer


class BloodTypeViewSet(viewsets.ModelViewSet):
    queryset = BloodType.objects.all()
    serializer_class = BloodTypeSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

