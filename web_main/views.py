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

def search(request):
	counties=County.objects.all()
	form = request.POST
	if request.method == 'POST':
			selected_item = get_object_or_404(County, pk=request.POST.get('county_id'))
			user.item = selected_item
			user.save()
	context = {'counties': counties,}
	return render_to_response('web_main/search.html', {'counties':county}, context,)

def add(request):
    context = {}
    return render(request, 'web_main/add.html', context)
