from django.shortcuts import render
from .models import squirrel
from django.http import HttpResponse


def map(request):
    alldata = squirrel.objects.all()
    assignment = {"s_t":alldata}
    return render(request, 'squirrel/map.html', assignment)
    
def sightings(request):
    alldata = squirrel.objects.all()
    assignment = {"s_t":alldata}
    return render(request, 'squirrel/sightings.html', assignment)
