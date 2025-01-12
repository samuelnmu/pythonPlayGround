from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Airport, Passangers

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights":Flight.objects.all()
    })
    
def flight(request, flight_id):
    flight = Flight.objects.get(pk = flight_id) #pk meaning primary key or id
    return render(request, "flights/flight.html", {
        "flight":flight,
        "passangers":flight.passanger.all(),
        "non_passangers":passangers.objects.exclude(flights= flight. all())
    })
    
def book(request,flight_id ):
    if request.method == "POST":
        flight = Flight.objects.get(pk = flight_id)
        passanger = passanger.object.get(pk= int(request.POST["passanger"]))
        passanger.flight.add(flight)
        return HttpResponseRedirect(reverse("flight",args=(flight.id)))