from django.db import models


class Result(models.Model):

    # name = models.CharField('占い結果')
    name = models.TextField('占い結果')

    def __str__(self):
        return self.name


# Create your models here.
