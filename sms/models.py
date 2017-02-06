from __future__ import unicode_literals

from django.db import models
from search.models import Topics
from django.contrib.auth.models import User


# Create your models here.
class Insms(models.Model):
    sender = models.CharField(max_length=255)
    to = models.CharField(max_length=255)
    date = models.DateTimeField()
    text = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    polarity = models.FloatField(max_length=255)

    class Meta:
        db_table = "Insms"
        verbose_name_plural = "Insms"

    def __str__(self):
        return self.sender, self.date, self.text



class Outsms(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    sent_date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)

    class Meta:
        db_table = "Outsms"
        verbose_name_plural = "Outsms"

    def __str__(self):
        return self.receiver, self.sent_date, self.text, self.sender

class Failedsms(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    sent_date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)

    class Meta:
        db_table = "Failedsms"
        verbose_name_plural = "Failedsms"

    def __str__(self):
        return self.receiver, self.sent_date, self.text, self.sender


class Blacklistsms(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    sent_date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)

    class Meta:
        db_table = "Blacklistsms"
        verbose_name_plural = "Blacklistsms"

    def __str__(self):
        return self.receiver, self.sent_date, self.text, self.sender


class Sms(models.Model):
    subscribed_topic = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Sms"
        verbose_name_plural = "Sms"

    def __str__(self):
        return self.subscribed_topic


















