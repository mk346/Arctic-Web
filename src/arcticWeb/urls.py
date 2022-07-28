from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('hotel',views.hotel,name='hotel'),
    path('car',views.car,name='car'),
    path('flight',views.flight,name='flight'),
    path('help',views.contact,name='help'),
    path('book',views.book,name='book'),
    path('payment',views.payment,name='payment'),
    path('Hotel-Json',views.HotelData,name='Hotel-Json'),




]