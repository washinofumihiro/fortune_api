# coding: utf-8

from rest_framework import serializers

from .models import Result, BloodType


class BloodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodType
        fields = ('b_type',)


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('result', 'date')



