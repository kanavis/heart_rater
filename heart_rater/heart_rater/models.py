"""
Heart rate log: basic models
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class PressureRecord(models.Model):

    sys = models.IntegerField()
    dia = models.IntegerField()
    hr = models.IntegerField()
    comment = models.CharField(max_length=512, default="")
    time = models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    input_time = models.DateTimeField(auto_now_add=True)


class EventRecord(models.Model):

    event = models.CharField(max_length=512)
    time = models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    input_time = models.DateTimeField(auto_now_add=True)
