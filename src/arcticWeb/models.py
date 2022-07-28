from django.db import models

# Create your models here.
class hotel(models.Model):
	city = models.CharField(max_length=100)
	checkIn = models.DateField()
	checkOut = models.DateField()
	choice = (
		("2 Adults 1 Room", "2 Adults 1 Room"),
		("2 Adults 2 Rooms", "2 Adults 2 Rooms"),
		("Children 1 Room", "Children 1 Room"),
		("Couple's Room", "Couple's Room"),
	)
	room = models.CharField(max_length=50,choices=choice)

	def __str__(self):
		return self.city


class hotelDb(models.Model):
	hotel_name = models.CharField(max_length=100)
	Location = models.CharField(max_length=100)
	hotel_image = models.ImageField(upload_to='media/images')
	price_night = models.CharField(max_length=30)

	def __str__(self):
		return self.hotel_name


class Car(models.Model):
	car_type = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	p_date = models.DateField()
	p_time = models.TimeField()
	d_date = models.DateField()
	d_time = models.TimeField() 

	def __str__(self):
		return self.car_type


class carDb(models.Model):
	car_name = models.CharField(max_length=100)
	car_model = models.CharField(max_length=100)
	description = models.TextField()
	price_day = models.CharField(max_length=30)
	car_image = models.ImageField()
	update_time = models.TimeField()

	def __str__(self):
		return self.car_name


	class Meta:
		ordering = ['-update_time']



class Flight(models.Model):
	Airport = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)
	seats = models.IntegerField()
	choose = (
		("First Class","First Class"),
		("Business Class","Business Class"),
		("Regular Economy Class","Regular Economy Class"),
		("Premium Economy Class","Premium Economy Class"),


	)
	Class = models.CharField(max_length=50,choices=choose)

	def __str__(self):
		return self.Airport


class flightDb(models.Model):
	flight_name = models.CharField(max_length=100)
	Destination = models.CharField(max_length=100)
	depart_airport = models.CharField(max_length=100)
	depart_date = models.DateField()
	depart_time = models.TimeField()
	price_seat = models.CharField(max_length=30)

	def __str__(self):
		return self.depart_airport


class Help(models.Model):
	name = models.CharField(max_length=100)
	mobile = models.CharField(max_length=100)
	email = models.EmailField()
	message = models.TextField()

	def __str__(self):
		return self.name


