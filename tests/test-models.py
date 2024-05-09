from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import datetime

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="Pasta", Price = 12.00, Inventory = 10)
        self.assertEqual(item, "Pasta : 12.00")

class BookingTest(TestCase):

    def test_create_booking(self):
        booking = Booking.objects.create(
            name="Juan Perez",
            number_of_guests=2,
            booking_date=datetime(2024, 5, 31, 19, 0)
        )
        expected_str = "Juan Perez for 2 guests on 2024-05-31 19:00:00"
        self.assertEqual(str(booking), expected_str)

