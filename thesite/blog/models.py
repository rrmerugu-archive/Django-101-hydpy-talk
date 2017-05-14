# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, )
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __unicode__(self):
        return self.title