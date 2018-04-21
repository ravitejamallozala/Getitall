# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Card(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    modified_time=models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.title

class Tag(models.Model):
    tagname=models.CharField(max_length=25)
    card=models.ForeignKey(Card,on_delete=models.CASCADE,related_name='tags')

    def __unicode__(self):        return self.tagname
