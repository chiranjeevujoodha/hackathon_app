from django.shortcuts import render, HttpResponse
from .models import Campaign


# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def campaigns(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        organisor = request.POST.get('organisor')
        location = request.POST.get('location')
        date = request.POST.get('date')
        description = request.POST.get('description')
        
        Campaign.objects.create(name=name, organisor=organisor, location=location, date=date, description=description)
    return render(request, 'app/campaigns.html')

def contact(request):
    return render(request, 'app/contact.html')