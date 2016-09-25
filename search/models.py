from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Topics(models.Model):
    topic_id = models.AutoField(primary_key=True)
    topic_title = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "Topics"
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.topic_title

class KeyWords(models.Model):
    key_word_id = models.AutoField(primary_key=True)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    key_word = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "Keywords"
        verbose_name_plural = "Keywords"

    def __str__(self):
        return self.key_word