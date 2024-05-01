from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import UpdateView
from .models import Campaign, Contact
from .forms import CreateUserForm, LoginForm, CampaignForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth, User
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import *
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.decorators import login_required
from datetime import date

# Create your views here.

def home(request):
    return render(request, 'app/home.html')


def campaignform(request):
    form = CampaignForm()
    return render(request, 'app/campaignform.html', {'form':form})


def campaigns(request):
    today_date = date.today()
    
    # print(today_date)
    if 'q' in request.GET:
        q = request.GET['q']
        data = Campaign.objects.filter(name__icontains=q,date__gt=today_date )
    else:
        data = Campaign.objects.filter(date__gt=today_date).order_by('date')

    today_data = Campaign.objects.filter(date=today_date)

    context = {
            'today_data': today_data,
            'data': data
    }

    return render(request, 'app/campaigns.html', context)
    
@login_required
def add_campaign(request):
    author = request.user
    
    ngo_name = NGO.objects.get(user_id = author)

    if request.method == 'POST':
        name = request.POST.get('name')
        organisor = request.POST.get('organisor')
        location = request.POST.get('location')
        date = request.POST.get('date')
        description = request.POST.get('description')
        
        Campaign.objects.create(name=name.capitalize(), author=author, organisor=organisor, location=location.capitalize(), date=date, description=description.capitalize())
        return redirect('campaigns')
    

    return render(request, 'app/add_campaign.html', {'ngo_name': ngo_name})

@login_required
def update_campaign(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        organisor = request.POST.get('organisor')
        location = request.POST.get('location')
        date = request.POST.get('date')
        description = request.POST.get('description')

        query = Campaign.objects.get(id = id)
        query.name = name
        query.organisor = organisor
        query.location = location
        query.date = date
        query.description = description
        query.save()

        return redirect('dashboard')


    item = Campaign.objects.get(id = id)
    context = {'item':item}
    return render(request, 'app/update_campaign.html', context)

@login_required
def delete_campaign(request,id):
    item = Campaign.objects.get(id = id)
    item.delete()
    return redirect('dashboard')


def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(fname=fname, lname=lname, email=email, message=message)

    return render(request, 'app/contact.html')


def profile(request, id):
    # user_id = request.user.id
    data = NGO.objects.get(user_id=id)
    
    # data = Campaign.objects.filter(author_id = user_id)

    return render(request, 'app/profile.html', {'data': data})

@login_required
def dashboard(request):
    user_id = request.user.id
    data = Campaign.objects.filter(author_id = user_id).order_by('date')

    return render(request, 'app/dashboard.html', {'data': data})


def signin(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('campaigns')
            
    context = {'form':form}

    return render(request, 'app/signin.html', context=context)




def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username').lower()
            user.save()

            ngo_name = form.cleaned_data.get('ngo_name')
            email = form.cleaned_data.get('email')
            if ngo_name:
                NGO.objects.create(user=user, name=ngo_name, email=email)
            return redirect('signin')
    
    else:
        form = CreateUserForm()

    return render(request, 'app/signup.html', {'form':form})


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
    
#     else:
#         form = SignUpForm()
    
#     return render(request, 'app/signup.html', {'form':form})



def signout(request):
    auth.logout(request)
    return redirect('signin')




