# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    usrname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
