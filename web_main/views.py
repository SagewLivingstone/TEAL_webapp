from django.shortcuts import render
from django.http import HttpResponse

from .models import LandDetails

def index(request):
    # Give the home page the 10 first land objects from vLandDetails
    first_10_lands = LandDetails.objects.all()[:10]
    context = {
        'first_10_lands': first_10_lands,
    }
    return render(request, 'web_main/index.html', context)

def land_detail(request, land_id):
    context = {}
    return render(request, 'web_main/index.html', context)
