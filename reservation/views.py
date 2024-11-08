from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

from .models import menu, booking
from .serializers import menuSerializer, bookingSerializer
# Create your views here.

class bookingView(ListCreateAPIView):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer
    
class menuItemView(ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer
        
class singleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer
