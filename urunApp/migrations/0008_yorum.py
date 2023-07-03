# Generated by Django 4.1.7 on 2023-04-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunApp', '0007_alter_urun_stokadet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yorum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yazar', models.CharField(max_length=50, verbose_name='Yazar')),
                ('mesaj', models.TextField(max_length=350, verbose_name='Mesaj')),
                ('olusturuldu', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
