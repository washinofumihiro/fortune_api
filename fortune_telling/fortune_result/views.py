# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import Result
from .serializer import ResultSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

