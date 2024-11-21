from django.urls import path
from .views import menuItemView, singleMenuItemView, bookingView, singleBookingView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/', menuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', singleMenuItemView.as_view(), name='menu-detail'),
    path('bookings/', bookingView.as_view(), name='bookings'),
    path('bookings/<int:pk>', singleBookingView.as_view(), name='booking-detail'),
    path('api-token-auth/', obtain_auth_token),
    
]

