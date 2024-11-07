from django.urls import path
from .views import menuItemView, singleMenuItemView, bookingView

urlpatterns = [
    path('menu/', menuItemView.as_view()),
    path('menu/<int:pk>', singleMenuItemView.as_view()),
    path('booking/', bookingView.as_view()),
    
]

