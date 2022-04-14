from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from event.serializer import EventSZ
from .models import *

# Create your views here.

@api_view(['GET'])
def get_product(request):
    if request.method == 'GET':
        get_products = Event.objects.all()
        serializer = EventSZ(data=get_products, many=True)
        serializer.is_valid(raise_exception=False)
        return Response(serializer.data)



@api_view(['POST'])
def create_event(request):
    if request.method == 'POST':
        cr_event = EventSZ(data=request.data)
        if cr_event.is_valid(raise_exception=False):
            cr_event.save()
            return Response(cr_event.data)
    return Response(cr_event.errors)