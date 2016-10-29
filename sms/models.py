from __future__ import unicode_literals

from django.db import models
from search.models import Topics

# Create your models here.
class Insms(models.Model):
    sender = models.CharField(max_length=255)
    reciever = models.CharField(max_length=255)
    date = models.DateTimeField()
    text = models.CharField(max_length=255)
    messageidnumber = models.CharField(max_length=255)

    class Meta:
        db_table = "Insms"
        verbose_name_plural = "Insms"

    def __str__(self):
        return self.sender, self.recieved_date, self.text



class Outsms(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    sent_date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)

    class Meta:
        db_table = "Outsms"
        verbose_name_plural = "Outsms"

    def __str__(self):
        return self.receiver, self.sent_date, self.text


class Sms(models.Model):
    subscribed_topic = models.ForeignKey(Topics, on_delete=models.CASCADE)

    class Meta:
        db_table = "Sms"
        verbose_name_plural = "Sms"

    def __str__(self):
        return self.subscribed_topic


















