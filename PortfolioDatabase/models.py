from django.db import models


class Portfolio(models.Model):
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)


class Hobby(models.Model):
    hobby_name = models.CharField(max_length=200)
    hobby_description = models.CharField(max_length=200)