from django.contrib import admin
from .models import hotel,hotelDb,Car,carDb,Flight,flightDb,Help

# Register your models here.
admin.site.register(hotel)
admin.site.register(hotelDb)
admin.site.register(Car)
admin.site.register(carDb)
admin.site.register(Flight)
admin.site.register(flightDb)
admin.site.register(Help)

