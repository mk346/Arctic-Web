from django import forms
from django.forms import ModelForm
from .models import hotel,Car,Flight,Help


class hotelForm(ModelForm):
	class Meta:
		model = hotel
		fields = ('city','checkIn','checkOut','room')
		labels = {
		    'city': 'Where To',  'class':'form-label',
			'checkIn': 'Check In',  'class':'form-label',
			'checkOut': 'Check Out',  'class':'form-label',
			'room': 'Please Choose Your Room',  'class':'form-label',
		}

		widgets = {
			'city':forms.TextInput(attrs={'class':'form-control', 'Placeholder':'city/town',}),
			'checkIn':forms.DateInput(attrs={'class':'form-control','type':'date',}),
			'checkOut':forms.DateInput(attrs={'class':'form-control','type':'date',}),
		}

class carForm(ModelForm):
	class Meta:
		model = Car
		fields = '__all__'
		labels = {
		    'car_type': 'Type of Car eg. Convertible',  'class':'form-label',
		    'address': 'Pick up Location',  'class':'form-label',
		    'p_date': 'Pick up Date',  'class':'form-label',
		    'p_time': 'Pick up Time',  'class':'form-label',
		    'd_date': 'Drop off Date',  'class':'form-label',
		    'd_time': 'Drop off Time',  'class':'form-label',

		}

		widgets = {
		    'car_type':forms.TextInput(attrs={'class':'form-control','Placeholder':'Enter car type',}),
		    'address':forms.TextInput(attrs={'class':'form-control','Placeholder':'Pick up Location',}),
		    'p_date':forms.TextInput(attrs={'class':'form-control','type':'date'}),
		    'p_time':forms.TextInput(attrs={'class':'form-control','type':'time'}),
		    'd_date':forms.TextInput(attrs={'class':'form-control','type':'date'}),
		    'd_time':forms.TextInput(attrs={'class':'form-control','type':'time'}),


		}


class flightForm(ModelForm):
	class Meta:
		model = Flight
		fields = ('Airport','destination','seats','Class')
		labels = {
		    'Airport': 'Airport',  'class':'form-label',
		    'destination': 'Going To',  'class':'form-label',
		    'seats': 'Number of Seats To Book',  'class':'form-label',
		    'Class': 'Choose Flight Class',  'class':'form-label',
		}
		widgets = {
		    'Airport':forms.TextInput(attrs={'class':'form-control','Placeholder':'Departing From',}),
		    'destination':forms.TextInput(attrs={'class':'form-control','Placeholder':'Destination',}),
		    'seats':forms.TextInput(attrs={'class':'form-control','Placeholder':'Number of Seats',}),
		}


class helpForm(ModelForm):
	class Meta:
		model = Help
		fields = '__all__'
		labels = {
		    'name': 'Your Name',  'class':'form-label',
		    'mobile': 'Your Phone Number',  'class':'form-label',
		    'email': 'Your Email',  'class':'form-label',
		    'message': 'Problem You are Experiencing',  'class':'form-label',

		}
		widgets = {
		    'name':forms.TextInput(attrs={'class':'form-control','Placeholder':'enter your name',}),
		    'mobile':forms.TextInput(attrs={'class':'form-control','Placeholder':'enter your phone number',}),
		    'email':forms.EmailInput(attrs={'class':'form-control','Placeholder':'enter your email','type':'email'}),
		    'message':forms.Textarea(attrs={'class':'form-control',}),
		}



class detailsForm(ModelForm):
	class Meta:
		model = Help
		fields = ('name','mobile','email')
		labels = {
		    'name': 'Your Name',  'class':'form-label',
		    'mobile': 'Your Phone Number',  'class':'form-label',
		    'email': 'Your Email',  'class':'form-label',
		    

		}
		widgets = {
		    'name':forms.TextInput(attrs={'class':'form-control','Placeholder':'enter your name',}),
		    'mobile':forms.TextInput(attrs={'class':'form-control','Placeholder':'enter your phone number',}),
		    'email':forms.EmailInput(attrs={'class':'form-control','Placeholder':'enter your email','type':'email'}),
		}



