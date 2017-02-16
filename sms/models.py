from __future__ import unicode_literals

from django.db import models
from twittersearch.models import Topics
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator



# Create your models here.
class Insms(models.Model):
    sender = models.CharField(max_length=255)
    to = models.CharField(max_length=255)
    date = models.DateTimeField()
    text = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    polarity = models.FloatField(max_length=255)
    msg_number = models.PositiveIntegerField(validators=[MaxValueValidator(999999999999)])
    msg_type_status = models.BooleanField()
    msg_read_status = models.BooleanField()


    class Meta:
        db_table = "Insms"
        verbose_name_plural = "Insms"
        get_latest_by = 'date'

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
        get_latest_by = 'sent_date'

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
        get_latest_by = 'sent_date'

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
        get_latest_by = 'sent_date'

    def __str__(self):
        return self.receiver, self.sent_date, self.text, self.sender


class Sms(models.Model):
    subscribed_topic = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Sms"
        verbose_name_plural = "Sms"

    def __str__(self):
        return self.subscribed_topic


















