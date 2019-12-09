from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import squirrel
from .forms import SquirrelForm


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
    
def stats(request):
    total_counts = squirrel.objects.count()
    AM_counts = squirrel.objects.filter(shift = 'AM').count()
    PM_counts = squirrel.objects.filter(shift = 'PM').count()
    adult_counts = squirrel.objects.filter(age = 'Adult').count()
    juvenile_counts = squirrel.objects.filter(age = 'Juvenile').count()
    gray_counts = squirrel.objects.filter(primary_fur_color = 'Gray').count()
    cinnamon_counts = squirrel.objects.filter(primary_fur_color = 'Cinnamon').count()
    black_counts = squirrel.objects.filter(primary_fur_color = 'Black').count()
    running_counts = squirrel.objects.filter(running = True).count()
    chasing_counts = squirrel.objects.filter(chasing = True).count()
    climbing_counts = squirrel.objects.filter(climbing = True).count()
    eating_counts = squirrel.objects.filter(eating = True).count()
    
    context = {
        'total_counts': total_counts,
	'AM_counts': AM_counts,
	'PM_counts': PM_counts,
	'adult_counts': adult_counts,
	'juvenile_counts': juvenile_counts,
	'gray_counts': gray_counts,
	'cinnamon_counts': cinnamon_counts,
	'black_counts': black_counts,
	'running_counts': running_counts,
	'chasing_counts': chasing_counts,
	'climbing_counts': climbing_counts,
	'eating_counts': eating_counts,
    }
    
    return render(request, 'squirrel/stats.html', context)
