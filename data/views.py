# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import cv2
import numpy as np
import math
import base64
# import json
import simplejson as json
from data.models import *
from API.views import *

def IndexView(request):
	template_name='index.html'
	img = np.ones((512,512,3), np.uint8)
	img[:,:,:]=255
	all_data=Sotdma.objects.all()
	
	my_data=MyData.objects.all()
	for _ in my_data:
		my_data=MyData.objects.get(uid=_)
		#print(my_data.lat)
		cv2.line(img,(256,256),(256,256-int(my_data.speed)),(255,0,0),3)
		cv2.circle(img,(256,256), 10, (0,255,0), -1)
	for indi in all_data:
		dta=Sotdma.objects.get(uid=indi)
		#print(			(int(256-(int(my_data.longi)-int(dta.longi))+round(math.cos(int(dta.direction)+90)*int(my_data.speed))),int(256-(int(my_data.lat)-int(dta.lat))+round(math.sin(int(dta.direction)+90)*int(my_data.speed)))),
#)
		cv2.line(img,
			(int(256-(int(my_data.longi)-int(dta.longi))),int(256-(int(my_data.lat)-int(dta.lat)))),
			(int(256-(int(my_data.longi)-int(dta.longi))+round(math.cos(int(dta.direction)+90-int(my_data.direction))*int(dta.speed))),int(256-(int(my_data.lat)-int(dta.lat))+round(math.sin(int(dta.direction)+90-int(my_data.direction))*int(dta.speed)))),
			(255,0,0),3)
		cv2.circle(img,(256-(int(my_data.longi)-int(dta.longi)),256-(int(my_data.lat)-int(dta.lat))), 6, (0,0,255), -1)

		#print(int(my_data.longi),int(dta.longi),int(my_data.lat),int(dta.lat))

	# cv2.imshow("img",img)

	# cv2.waitKey(0)
	ret, frame_buff = cv2.imencode('.jpg', img) #could be png, update html as well
	frame_b64 = base64.b64encode(frame_buff)

	context={

	'img':frame_b64
	}
	#print context

	return render(request, template_name, context)
    
