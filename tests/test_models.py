from django.test import TestCase
from reservation.models import menu, booking as Booking
from datetime import date, timedelta
from django.core.exceptions import ValidationError

class MenuTest(TestCase):
    def test_get_item(self):
        item = menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
        
    def test_get_items(self):
        menu.objects.create(title="IceCream", price=80, inventory=100)
        menu.objects.create(title="Pizza", price=100, inventory=100)
        items = menu.objects.all()
        self.assertEqual(len(items), 2)     
        
class BookingTest(TestCase):
    def test_get_booking(self):
        future_date = date.today() + timedelta(days=30)
        item = Booking.objects.create(
            name="John Doe", 
            no_of_guests=2, 
            booking_date=future_date
        )
        self.assertEqual(str(item), "John Doe : 2")
        
    def test_get_bookings(self):
        future_date1 = date.today() + timedelta(days=30)
        future_date2 = date.today() + timedelta(days=31)
        Booking.objects.create(name="John Doe", no_of_guests=2, booking_date=future_date1)
        Booking.objects.create(name="Jane Doe", no_of_guests=3, booking_date=future_date2)
        bookings = Booking.objects.all()
        self.assertEqual(len(bookings), 2)

    def test_booking_date_in_future(self):
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=2,
            booking_date="2025-10-10"
        )
        booking.full_clean()
    
    def test_no_of_guests_less_than_1(self):
        with self.assertRaises(ValidationError):
            booking = Booking.objects.create(
                name="John Doe",
                no_of_guests=0,
                booking_date=date.today()
            )
            booking.full_clean()
    
    def test_booking_date_in_past(self):
        with self.assertRaises(ValidationError):
            booking = Booking.objects.create(
                name="John Doe",
                no_of_guests=2,
                booking_date="2022-10-10"
            )
            booking.full_clean()
    
    def test_booking_date_is_today(self):
        booking = Booking.objects.create(name="John Doe", no_of_guests=2, booking_date=date.today())
        self.assertEqual(booking.booking_date, date.today())
        
    def test_booking_date_is_not_today(self):
        future_date = date.today() + timedelta(days=30)
        booking = Booking.objects.create(
            name="John Doe", 
            no_of_guests=2, 
            booking_date=future_date
        )
        self.assertNotEqual(booking.booking_date, date.today())
        
    def test_booking_date_is_tomorrow(self):
        booking = Booking.objects.create(name="John Doe", no_of_guests=2, booking_date=date.today() + timedelta(days=1))
        self.assertEqual(booking.booking_date, date.today() + timedelta(days=1))
        
    def test_booking_date_is_not_tomorrow(self):
        future_date = date.today() + timedelta(days=30)
        booking = Booking.objects.create(
            name="John Doe", 
            no_of_guests=2, 
            booking_date=future_date
        )
        self.assertNotEqual(booking.booking_date, date.today() + timedelta(days=1))