# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from data.models import *
class SotdmaAdmin(admin.ModelAdmin):

	def uid(obj):
		return obj.Sotdam.uid

	def lat(obj):
		return obj.Sotdam.lat

	def long(obj):
		return obj.Sotdam.long

	def speed(obj):
		return obj.Sotdam.speed

	def direction(obj):
		return obj.Sotdam.direction
class MySotdmaAdmin(admin.ModelAdmin):

	def uid(obj):
		return obj.Sotdam.uid

	def lat(obj):
		return obj.Sotdam.lat

	def long(obj):
		return obj.Sotdam.long

	def speed(obj):
		return obj.Sotdam.speed

	def direction(obj):
		return obj.Sotdam.direction


admin.site.register(Sotdma,SotdmaAdmin)
admin.site.register(MyData,MySotdmaAdmin)