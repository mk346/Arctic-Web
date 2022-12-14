# Generated by Django 3.2.6 on 2021-08-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arcticWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('p_date', models.DateField()),
                ('p_time', models.TimeField()),
                ('d_date', models.DateField()),
                ('d_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='carDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price_day', models.CharField(max_length=30)),
                ('car_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('seats', models.IntegerField()),
                ('Class', models.CharField(choices=[('First Class', 'First Class'), ('Business Class', 'Business Class'), ('Regular Economy Class', 'Regular Economy Class'), ('Premium Economy Class', 'Premium Economy Class')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='flightDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_name', models.CharField(max_length=100)),
                ('Destination', models.CharField(max_length=100)),
                ('depart_date', models.DateField()),
                ('depart_time', models.TimeField()),
                ('price_seat', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='hotelDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('hotel_image', models.ImageField(upload_to='')),
                ('price_night', models.CharField(max_length=30)),
            ],
        ),
    ]
