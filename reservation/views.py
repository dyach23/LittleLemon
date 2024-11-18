from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateAPIView, 
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from .models import menu, booking
from .serializers import menuSerializer, bookingSerializer
# Create your views here.

class bookingView(ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [IsAuthenticated]
    
class menuItemView(ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [IsAuthenticated]
        
class singleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [IsAuthenticated]   