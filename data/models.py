# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Sotdma(models.Model):
	uid=models.CharField(max_length=250,null=True,blank=True)
	longi=models.CharField(max_length=250,null=True,blank=True)
	lat=models.CharField(max_length=250,null=True,blank=True)
	speed=models.CharField(max_length=250,null=True,blank=True)
	direction=models.CharField(max_length=250,null=True,blank=True)
	def __str__(self):
		return '%s'%self.uid

class MyData(models.Model):
	uid=models.CharField(max_length=250,null=True,blank=True)
	longi=models.CharField(max_length=250,null=True,blank=True)
	lat=models.CharField(max_length=250,null=True,blank=True)
	speed=models.CharField(max_length=250,null=True,blank=True)
	direction=models.CharField(max_length=250,null=True,blank=True)
	def __str__(self):
		return "%s"%self.uid