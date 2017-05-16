# coding: utf-8

from rest_framework import serializers

from .models import Result, BloodType


class BloodTypeSerializer(serializers.ModelSerializer):
    # blood_result = ResultSerializer()

    class Meta:
        model = BloodType

        # fields = 'blood_type'では無理らしい
        # fields = ('blood_type', 'blood_result')
        fields = ('blood_type', )


class ResultSerializer(serializers.ModelSerializer):
    # blood_type = BloodTypeSerializer()

    class Meta:
        model = Result
        fields = ('result', 'date', 'blood_type')


