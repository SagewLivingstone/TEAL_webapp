from django.shortcuts import render
from django.http import HttpResponse

from .models import Land

def index(request):
    first_10_lands = Land.objects.all()[:10]
    context = {
        'first_10_lands': first_10_lands,
    }
    return render(request, 'web_main/index.html', context)

def land_detail(request, land_id):
    context = {}
    return render(request, 'web_main/index.html', context)

def search(request):
	context = {}
	return render(request, 'web_main/search.html', context)

def add(request):
    context = {}
    return render(request, 'web_main/add.html', context)
