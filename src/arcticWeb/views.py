from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import hotel,Car,Flight,Help,hotelDb,carDb,flightDb
from .forms import hotelForm,carForm,flightForm,helpForm,detailsForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.

def home(request):
	return render(request,'arcticWeb/index.html',{})


def hotel(request):
	form = hotelForm()
	if request.method == 'POST':
		form = hotelForm(request.POST)
		if form.is_valid():
			form.save()
			search = form.cleaned_data['city'].capitalize()
			results = hotelDb.objects.filter(Location__contains=search)
		return render(request,'arcticWeb/hotel.html',{'search':search,'results':results,})	
	else:
		return render(request,'arcticWeb/hotel.html',{'form':form})
		

def car(request):
	form = carForm()
	if request.method == 'POST':
		form = carForm(request.POST)
		if form.is_valid():
			form.save()
			search = form.cleaned_data['car_type'].capitalize()
			results = carDb.objects.filter(car_name__contains=search)
		return render(request,'arcticWeb/car.html',{'search':search,'results':results})
	else:
		return render(request,'arcticWeb/car.html',{'form':form})


def flight(request):
	form = flightForm()
	if request.method == 'POST':
		form = flightForm(request.POST)
		if form.is_valid():
			form.save()
			search = form.cleaned_data['Airport'].capitalize()
			results = flightDb.objects.filter(depart_airport__contains=search)
			if results is not None:
				return render(request,'arcticWeb/flight.html',{'search':search,'results':results,})
			else:
				messages.success(request, ("Sorry, Airport matching that name was not Found,Please enter a known Airport"))
				return redirect('flight')			
		
	else:
		return render(request,'arcticWeb/flight.html',{'form':form})


def contact(request):
	form = helpForm()
	if request.method == 'POST':
		form = helpForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data['name']
			mobile = form.cleaned_data['mobile']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']

			data = {
				'Name':name,
				'Mobile':mobile,
				'Email':email,
				'Message':message,
			}

			info = '''
			Name: {}
			Phone Number: {}
			Email: {}
			Message: {}
			'''.format(data['Name'],data['Mobile'],data['Email'],data['Message'])

			send_mail(data['Name'],info,'',['kinyuacaleb554@gmail.com'])
			return render(request,'arcticWeb/help.html',{'name':name})
	else:
		return render(request,'arcticWeb/help.html',{'form':form})

@login_required
def book(request):
	form = detailsForm()
	if request.method == 'POST':
		form = detailsForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data['name']
			mobile = form.cleaned_data['mobile']
			email = form.cleaned_data['email']
			return redirect('payment')
	else:
		return render(request,'arcticWeb/book.html',{'form':form})	
				

def payment(request):
	details = hotelDb.objects.all()
	return render(request,'arcticWeb/payment.html',{'details':details})


def HotelData(request):
	dt = list(hotelDb.objects.values())
	return JsonResponse({'data':dt})




