# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import BloodType, Result
from .serializer import BloodTypeSerializer, ResultSerializer


class BloodTypeViewSet(viewsets.ModelViewSet):
    queryset = BloodType.objects.all()
    # queryset = BloodType.objects.all().prefetch_related("entries").get(id=1).entries.all()
    serializer_class = BloodTypeSerializer
    # for blood_type in BloodType.objects.all().prefetch_related("entries"):
    #     print(blood_type.get(id=1).entries.all())
    # print(BloodType.objects.all().prefetch_related("entries").get(id=2))
    # print(Result.objects.all().result)
    report = Result.objects.all()
    print(report.get(date=20170520).date)

    print("test")


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    # print(Result.objects.all()[0])

