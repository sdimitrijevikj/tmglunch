from django.db import models


class FoodItem(models.Model):

    date = models.DateField()
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    small_price = models.FloatField()
    large_price = models.FloatField()
    votes = models.IntegerField()

    def __unicode__(self):
        return self.name + '|' + str(self.date)


class Feedback(models.Model):

    food_item = models.ForeignKey(FoodItem)
    content = models.CharField(max_length=512)
    stars = models.IntegerField()
    date = models.DateField()

    def __unicode__(self):
        return self.date


class MenuDocs(models.Model):

    date_from = models.DateField()
    file = models.FileField(upload_to='menu')

    def __unicode__(self):
        return self.date_from