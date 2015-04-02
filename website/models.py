from django.db import models


class Day(models.Model):

    date = models.DateField()
    name = models.CharField(max_length=16)

    def __unicode__(self):
        return self.name


class FoodItem(models.Model):

    day = models.ForeignKey(Day)
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    small_price = models.IntegerField()
    large_price = models.IntegerField()
    votes = models.IntegerField()

    def __unicode__(self):
        return self.name


class Feedback(models.Model):

    food_item = models.ForeignKey(FoodItem)
    content = models.CharField(max_length=512)
    stars = models.IntegerField()
    date = models.DateField()

    def __unicode__(self):
        return self.date

