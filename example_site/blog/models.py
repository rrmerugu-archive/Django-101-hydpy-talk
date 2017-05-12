# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True)
    text = models.TextField()
    is_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, blank=False)
    
    def make_draft(self):
        self.is_draft = True
        self.save()

    def make_published(self):
        self.is_draft = False
        self.save()
        
    def generated_slug(self):
        self.slug = slugify(self.title)
        
    def save(self, *args, **kwargs):
        if not self.slug: # generate slug if not exist
            self.generated_slug()
        super(BlogPost, self).save(*args, **kwargs)

        