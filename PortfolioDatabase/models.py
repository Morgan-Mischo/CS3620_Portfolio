from django.db import models


class Portfolio(models.Model):
    def __str__(self):
        item = self.item_name + '' + self.item_description + ''
        return item
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_image = models.CharField(max_length=500, default="https://www.hostinger.com/tutorials/wp-content/uploads/sites/2/2021/08/how-to-make-an-online-portfolio.png")


class Hobby(models.Model):
    def __str__(self):
        hobby = self.hobby_name + '' + self.hobby_description + ''
        return hobby
    hobby_name = models.CharField(max_length=200)
    hobby_description = models.CharField(max_length=200)
    hobby_image = models.CharField(max_length=500, default="https://fjwp.s3.amazonaws.com/blog/wp-content/uploads/2020/02/29113959/hobby-money.png")

class Contact(models.Model):
    def __str__(self):
        contact = self.name + '' + self.email + '' + self.message + ''
        return contact
    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    contact_message = models.CharField(max_length=500)