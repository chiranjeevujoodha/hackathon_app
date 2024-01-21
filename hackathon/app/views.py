from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def campaigns(request):
    return render(request, 'app/campaigns.html')

def contact(request):
    return render(request, 'app/contact.html')