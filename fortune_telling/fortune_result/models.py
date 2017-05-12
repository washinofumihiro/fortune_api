from django.db import models


class result(models.Model):

    name = models.CharField('占い結果')

    def __str__(self):
        return self.name


# Create your models here.
