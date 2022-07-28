# Generated by Django 3.2.6 on 2021-08-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('checkIn', models.DateField()),
                ('checkOut', models.DateField()),
                ('room', models.CharField(choices=[('2 Adults 1 Room', '2 Adults 1 Room'), ('2 Adults 2 Rooms', '2 Adults 2 Rooms'), ('Children 1 Room', 'Children 1 Room'), ("Couple's Room", "Couple's Room")], max_length=50)),
            ],
        ),
    ]
