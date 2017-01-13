from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class StreamTweets(models.Model):
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date = models.DateField()
    polarity = models.FloatField(max_length=255)

    class Meta:
        db_table = "StreamTweets"
        verbose_name_plural = "StreamTweets"

    def __str__(self):
        return self.text, self.author
