from django.contrib import admin

from .models import Result, BloodType


# Register your models here.
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass


@admin.register(BloodType)
class BloodTypeAdmin(admin.ModelAdmin):
    pass


