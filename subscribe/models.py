from __future__ import unicode_literals

from django.db import models
from search.models import Topics

# Create your models here.

TOPIC_CHOICES = Topics.objects.all()

class Subscribers(models.Model):
    mobile_number = models.CharField(max_length=255)
    subscribed_topic = models.ForeignKey(Topics, on_delete=models.CASCADE)

    class Meta:
        db_table = "Subscribers"
        verbose_name_plural = "Subscribers"

    def __str__(self):
        return self.mobile_number, self.subscribed_topic

