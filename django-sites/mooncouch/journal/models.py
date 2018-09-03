import datetime
from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)

    def __str__(self):
        return "%s (%s)" % (self.name, self.email)


class Entry(models.Model):
    #pub_date = models.DateTimeField('published date')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    #entry_date = models.DateTimeField('entry date')
    instrument = models.CharField(max_length=10)
    setup = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    stop_loss = models.IntegerField(default=0)
    take_profit = models.IntegerField(default=0)
    #expiration_date = models.DateTimeField('expiration date')
    strike = models.IntegerField(default=0)
    premium = models.IntegerField(default=0)
    theta = models.IntegerField(default=0)
    delta = models.IntegerField(default=0)
    vega = models.IntegerField(default=0)
    #exit_date = models.DateTimeField('exit date')
    exit_price = models.IntegerField(default=0)
    pl = models.IntegerField(default=0)
    breakeven = models.CharField(max_length=3)
    fees= models.IntegerField(default=0)
    highest_price = models.IntegerField(default=0)
    lowest_price = models.IntegerField(default=0)
    notes = models.CharField(max_length=200)
    screenshots = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return "%s (%s)" % (self.title, self.author.name)


class Comments(models.Model):
    pass
