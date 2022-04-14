
from rest_framework import serializers
from .models import *

class Location(serializers.ModelSerializer):
    class Meta:
        model = EventLocation
        fields = ['ev_location_name']


class Detail(serializers.ModelSerializer):
    event_location = Location(read_only=True, many=True)
    class Meta:
        model = EventDetail
        fields = ['ev_type', 'ev_price', 'ev_date', 'event_location']


class EventSZ(serializers.ModelSerializer):
    ev_detail = Detail(read_only=True, many=True)
    class Meta:
        model = Event
        fields = ['ev_name', 'ev_description', 'ev_img', 'ev_host', 'ev_detail',]

    def create_set(self, validated_data):
        event = Event.objects.create(**validated_data)
        detail = validated_data.pop('ev_detail')
        detail = EventDetail.objects.get_or_create(
            event_id = event, **event
        )
        location = validated_data.pop('event_location')
        location = EventLocation.objects.create(
           event_location_id = detail, **detail
        )
        return event

