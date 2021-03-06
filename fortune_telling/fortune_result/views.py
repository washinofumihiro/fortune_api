# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import BloodType, Result
from .models import ATypeResult, BTypeResult, OTypeResult, ABTypeResult
from .serializer import BloodTypeSerializer, ResultSerializer
from .serializer import ATypeResultSerializer, BTypeResultSerializer, \
    OTypeResultSerializer, ABTypeResultSerializer


class BloodTypeViewSet(viewsets.ModelViewSet):
    queryset = BloodType.objects.all()

    # queryset = BloodType.objects.filter(id=1).prefetch_related("entries")

    # queryset = list(BloodType.objects.all()) + list(Result.objects.all())

    # print(queryset)
    # queryset = BloodType.objects.all()
    # queryset = BloodType.objects.all().prefetch_related("entries")[0].entries.all()[0]
    # queryset = BloodType.objects.all().prefetch_related("entries").get(id=2).entries.all()
    # print(queryset)
    serializer_class = BloodTypeSerializer

    # for blood_type in BloodType.objects.all().prefetch_related("entries"):
    #     print(blood_type.entries.all())
    #     print(blood_type.entries.all()[0].date)

    # print(BloodType.objects.all().prefetch_related("entries").get(id=2))
    # print(Result.objects.all().result)
    # report = Result.objects.all()
    # report = BloodType.objects.all().prefetch_related("entries").entries.all()
    # print(report.get(blood_type=1).date)

    # print("test")


class ResultViewSet(viewsets.ModelViewSet):
    # queryset = Result.objects.all()
    queryset = Result.objects.filter(blood_type=1)
    serializer_class = ResultSerializer
    # print(Result.objects.all()[0])


class ATypeResultViewSet(viewsets.ModelViewSet):
    queryset = ATypeResult.objects.all().order_by('date')
    # queryset = Result.objects.filter(blood_type=1)
    serializer_class = ATypeResultSerializer
    lookup_field = 'date'


class BTypeResultViewSet(viewsets.ModelViewSet):
    queryset = BTypeResult.objects.all().order_by('date')
    # queryset = Result.objects.filter(blood_type=1)
    serializer_class = BTypeResultSerializer
    lookup_field = 'date'


class OTypeResultViewSet(viewsets.ModelViewSet):
    queryset = OTypeResult.objects.all().order_by('date')
    # queryset = Result.objects.filter(blood_type=1)
    serializer_class = OTypeResultSerializer
    lookup_field = 'date'


class ABTypeResultViewSet(viewsets.ModelViewSet):
    queryset = ABTypeResult.objects.all().order_by('date')
    # queryset = Result.objects.filter(blood_type=1)
    serializer_class = ABTypeResultSerializer
    lookup_field = 'date'


