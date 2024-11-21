from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from datetime import date
from decimal import Decimal

# Create your models here.
class menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    inventory = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    
    def __str__(self):
        return f"{self.title} : {self.price}"
    
class booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(
        validators=[MinValueValidator(1)],
        default=1
    )
    booking_date = models.DateField()
    
    def clean(self):
        # Validate booking date
        if self.booking_date:
            today = date.today()
            if self.booking_date < today:
                raise ValidationError('La fecha de reserva no puede estar en el pasado')
    
    def save(self, *args, **kwargs):
        self.full_clean()  # Ejecuta todas las validaciones
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} : {self.no_of_guests}"