# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from data.models import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from API.serializers import *

@api_view(['GET'])
def getData(request, format=None):
	all_data=Sotdma.objects.all()
	my_data=MyData.objects.all()
	my_serializer=SotdmaSerializer(my_data, many=True)
	serializer=SotdmaSerializer(all_data, many=True)
	print("oye",serializer)
	data={
	"my":my_serializer.data,
	"all":serializer.data
	}
	return Response(data)