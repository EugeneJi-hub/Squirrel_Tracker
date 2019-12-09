from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import SquirrelForm
from .models import squirrel


def map(request):
    alldata = squirrel.objects.all()
    assignment = {"s_t":alldata}
    return render(request, 'squirrel/map.html', assignment)
    
def sightings(request):
    alldata = squirrel.objects.all()
    assignment = {"s_t":alldata}
    return render(request, 'squirrel/sightings.html', assignment)


def update(request,unique_squirrel_id):
    s_t = squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    if request.method == 'POST':
        #check form data
        form = SquirrelForm(request.POST, instance=s_t)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{unique_squirrel_id}')
    else:
        form = SquirrelForm(instance=s_t)
    context = {
        'form':form,
    }
    return render(request, 'squirrel/update.html',context)

def add(request,unique_squirrel_id):
    if request.method == 'POST':
        #check form data
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SquirrelForm()
    context = {
        'form':form,
    }
    return render(request, 'squirrel/update.html',context)
