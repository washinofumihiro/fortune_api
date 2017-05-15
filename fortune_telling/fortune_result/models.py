from django.db import models


class BloodType(models.Model):
    blood_type = models.CharField('血液型', max_length=255, default="")


    # def __str__(self):
    #     return self.blood_type
    #

    def __repr__(self):
        # 主キーとresultを表示させて見やすくする
        # ex) 1: Alice
        return "{}: {}".format(self.pk, self.blood_type)


    __str__ = __repr__  # __str__にも同じ関数を適用


class Result(models.Model):

    # name = models.CharField('占い結果')
    result = models.TextField('占い結果')
    date = models.CharField('日付', max_length=255, default="")

    # blood_type = models.ForeignKey(BloodType, related_name="entries")
    blood_type = models.ForeignKey(BloodType, related_name='entries')

    # def __str__(self):
    #     return self.result
    #
    # def __repr__(self):
    #     # 主キーとresultを表示させて見やすくする
    #     # ex) 1: Alice
    #     return "{}: {}".format(self.pk, self.result)
    #
    # __str__ = __repr__  # __str__にも同じ関数を適用

