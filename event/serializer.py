from asyncio import events
from rest_framework import serializers
from .models import *

class Location(serializers.ModelSerializer):
    class Meta:
        model = EventLocation
        fields = ['ev_location_name']


class Detail(serializers.ModelSerializer):
    event_location = Location(many=True)
    class Meta:
        model = EventDetail
        fields = ['ev_type', 'ev_price', 'ev_date', 'event_location']

class EventSZ(serializers.ModelSerializer):
    ev_detail = Detail(many=True)
    class Meta:
        model = Event
        fields = ['ev_name', 'ev_description', 'ev_img', 'ev_host', 'ev_detail'] 

    def create(self, validated_data):
        locations_data = validated_data.pop('event_location')
        details_data = validated_data.pop('ev_detail')
        event = Event.objects.create(**validated_data)
        for location_data in locations_data:
            EventLocation.objects.create(**location_data, event_location=location_data)
        for detail_data in details_data:
            EventDetail.objects.create(**detail_data, event=event)
        return event

