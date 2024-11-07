from django.db import models

# Create your models here.
class menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return f"Booking for {self.name} on {self.booking_date}"