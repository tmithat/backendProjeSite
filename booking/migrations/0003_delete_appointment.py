# Generated by Django 4.1.7 on 2023-07-02 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_remove_appointment_day_alter_appointment_time_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]