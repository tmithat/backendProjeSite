# Generated by Django 4.1.7 on 2023-07-02 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunApp', '0022_alter_makeappointment_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makeappointment',
            name='tel',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefon No'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='tel',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefon No'),
        ),
    ]
