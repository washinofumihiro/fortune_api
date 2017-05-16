# coding: utf-8

from rest_framework import routers
from .views import ResultViewSet, BloodTypeViewSet
# from .views import ATypeResultViewSet, BTypeResultViewSet, \
#     OTypeResultViewSet, ABTypeResultViewSet


router = routers.DefaultRouter()
router.register(r'results', ResultViewSet)
router.register(r'blood_types', BloodTypeViewSet)
# router.register(r'A', ATypeResultViewSet)
# router.register(r'B', BTypeResultViewSet)
# router.register(r'O', OTypeResultViewSet)
# router.register(r'AB', ABTypeResultViewSet)
#