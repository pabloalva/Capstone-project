# Generated by Django 4.2.11 on 2024-04-27 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0003_alter_booking_no_of_guests"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Booking",
            new_name="Bookings",
        ),
        migrations.RenameModel(
            old_name="Menu",
            new_name="Menus",
        ),
    ]
