# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
# Create your models here.


class ContactEntry(models.Model):
    subject = models.CharField(max_length=300)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)