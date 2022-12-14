from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Services
from .serializers import ServicesSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def service_list(request):
    if request.method == 'GET':
        Service = Services.objects.all()
        serializer = ServicesSerializer(Service, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ServicesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)