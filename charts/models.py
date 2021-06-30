from django.db import models


# Create your models here.
# 数据均为中国
class ProvinceHistoryEpidemicData(models.Model):
    year = models.SmallIntegerField()
    date = models.CharField(max_length=5)
    province = models.CharField(max_length=4)
    confirm = models.IntegerField()
    dead = models.IntegerField()
    heal = models.IntegerField()  # 治愈
    confirm_add = models.IntegerField()
    newConfirm = models.IntegerField()
    newHeal = models.IntegerField()
    newDead = models.IntegerField()

    def __str__(self):
        return str(self.year) + self.date + self.province + str(self.confirm) + str(self.dead) + str(self.heal)


class HuBeiProvinceHistoryEpidemicData(models.Model):
    y = models.SmallIntegerField()
    date = models.CharField(max_length=5)
    city = models.CharField(max_length=4)
    confirm = models.IntegerField()
    dead = models.IntegerField()
    heal = models.IntegerField()  # 治愈
    suspect = models.IntegerField()
    confirm_add = models.IntegerField()

    def __str__(self):
        return str(self.y) + self.date + self.city + str(self.confirm) + str(self.dead) + str(self.heal)


class WuhanPopulationMigrationOut(models.Model):
    city_code = models.IntegerField()
    city_name = models.CharField(max_length=20)
    city_rate_out = models.FloatField()
    city_rate_in = models.FloatField()


class WeiBoCommentWordRate(models.Model):
    word = models.CharField(max_length=5)
    num = models.IntegerField()


class EmotionData(models.Model):
    positive_sum = models.IntegerField()
    middle_sum = models.IntegerField()
    negative_sum = models.IntegerField()


class EmotionWordData(models.Model):
    word = models.CharField(max_length=5)
    num = models.IntegerField()
    kind = models.IntegerField()  # 积极 1, 中性 0, 消极 -1
