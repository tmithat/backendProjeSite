# Generated by Django 4.1.7 on 2023-03-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='fiyat',
            field=models.CharField(default='Ucret belirtilmedi', max_length=6, verbose_name='Urunun Fiyati'),
        ),
    ]