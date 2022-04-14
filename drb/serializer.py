from unittest.loader import VALID_MODULE_NAME
from rest_framework import serializers
from .models import *

class Location(serializers.ModelSerializer):
    class Meta:
        model = DrbLocation
        fields = ['drb_location_name']

class Detail(serializers.ModelSerializer):
    drb_location = Location(read_only=True, many=True)
    class Meta:
        model = DrbDetail
        fields = ['drb_type', 'drb_price', 'drb_date', 'drb_location']


class DrbSZ(serializers.ModelSerializer):
    drb_detail = Detail(read_only=True, many=True)
    class Meta:
        model = Drb
        fields = ['drb_name', 'drb_description', 'drb_img', 'drb_host', 'drb_detail',]


    def create_set(self, validated_data):
        drb_data = validated_data.pop('drb_detail')
        drb = Drb.objects.create(**drb_data)
        #for drb_data_ in drb_data:
        DrbDetail.objects.create(drb=Drb, **validated_data)
        return drb