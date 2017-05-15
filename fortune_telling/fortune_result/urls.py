# coding: utf-8

from rest_framework import routers
from .views import ResultViewSet, BloodTypeViewSet


router = routers.DefaultRouter()
router.register(r'results', ResultViewSet)
router.register(r'blood_types', BloodTypeViewSet)
