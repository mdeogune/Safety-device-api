
from rest_framework import serializers
from data.models import *

class SotdmaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sotdma
		fields=('uid','longi','lat','speed','direction')
