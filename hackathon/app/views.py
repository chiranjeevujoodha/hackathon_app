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




# @api_view(['POST'])
# def add_campaign(request):
#     serializer = CampaignSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_campaigns(request):
#     campaigns = Campaign.objects.all()
#     serializer = CampaignSerializer(campaigns, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def add_contact(request):
#     serializer = ContactSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_contacts(request):
#     contacts = Contact.objects.all()
#     serializer = ContactSerializer(contacts, many=True)
#     return Response(serializer.data)


# Create your views here.

def home(request):
    return render(request, 'app/home.html')


def campaignform(request):
    form = CampaignForm()
    return render(request, 'app/campaignform.html', {'form':form})


def campaigns(request):
    data = Campaign.objects.all()
    # author = request.user

    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     organisor = request.POST.get('organisor')
    #     location = request.POST.get('location')
    #     date = request.POST.get('date')
    #     description = request.POST.get('description')
        
    #     Campaign.objects.create(name=name.capitalize(), author=author, organisor=organisor, location=location.capitalize(), date=date, description=description.capitalize())
    return render(request, 'app/campaigns.html', {'data': data})
    
def add_campaign(request):
    author = request.user

    if request.method == 'POST':
        name = request.POST.get('name')
        organisor = request.POST.get('organisor')
        location = request.POST.get('location')
        date = request.POST.get('date')
        description = request.POST.get('description')
        
        Campaign.objects.create(name=name.capitalize(), author=author, organisor=organisor, location=location.capitalize(), date=date, description=description.capitalize())
        return redirect('campaigns')

    return render(request, 'app/add_campaign.html')

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

        return redirect('profile')


    item = Campaign.objects.get(id = id)
    context = {'item':item}
    return render(request, 'app/update_campaign.html', context)

def delete_campaign(request,id):
    item = Campaign.objects.get(id = id)
    item.delete()
    return redirect('profile')



class UpdateCampaign(UpdateView):
    model = Campaign
    template_name = 'update_campaign.html'
    fields = ['name', 'organisor', 'location', 'date', 'description']

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(fname=fname, lname=lname, email=email, message=message)

    return render(request, 'app/contact.html')

@login_required
def profile(request):
    user_id = request.user.id
    data = Campaign.objects.filter(author_id = user_id)

    return render(request, 'app/profile.html', {'data': data})



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

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('signin')
    
    context = {'form':form}


    return render(request, 'app/signup.html', context=context)

# def signup(request):

#     if request.method == 'POST':
#         username = request.POST.get('username')
 
#         password = request.POST.get('password')

#         user = User.objects.create(username=username, password=password)

#         return redirect('signin')


#     return render(request, 'app/signup.html')

def signout(request):
    auth.logout(request)
    return redirect('signin')



# class ContactView(APIView):
#     def get(self, request):
#         output = [{
#             'fname': output.fname,
#             'lname': output.lname,
#             'email': output.email,
#             'message': output.message}
#             for output in Contact.objects.all()
#         ]
#         return Response(output)
#     def post(self, request):
#         print('ajaj')
#         serializer = ContactSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)


