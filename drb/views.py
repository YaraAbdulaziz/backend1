from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drb.serializer import DrbSZ
from .models import *

# Create your views here.

@api_view(['GET'])
def get_product(request):
    if request.method == 'GET':
        get_products = Drb.objects.all()
        serializer = DrbSZ(data=get_products, many=True)
        serializer.is_valid(raise_exception=False)
        return Response(serializer.data)


@api_view(['POST'])
def create_drb(request):
    if request.method == 'POST':
        cr_drb = DrbSZ(data=request.data)
        if cr_drb.is_valid(raise_exception=False):
            cr_drb.save()
            return Response(cr_drb.data)
    return Response(cr_drb.errors)