from django.db import models


class Portfolio(models.Model):
    def __str__(self):
        item = self.item_name + '' + self.item_description + ''
        return item
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)


class Hobby(models.Model):
    def __str__(self):
        hobby = self.hobby_name + '' + self.hobby_description + ''
        return hobby
    hobby_name = models.CharField(max_length=200)
    hobby_description = models.CharField(max_length=200)