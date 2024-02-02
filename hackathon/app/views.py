from django.shortcuts import render, HttpResponse, redirect
from .models import Campaign, Contact
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth, User


# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def campaigns(request):
    data = Campaign.objects.all()


    if request.method == 'POST':
        name = request.POST.get('name')
        organisor = request.POST.get('organisor')
        location = request.POST.get('location')
        date = request.POST.get('date')
        description = request.POST.get('description')
        
        Campaign.objects.create(name=name, organisor=organisor, location=location, date=date, description=description)
    return render(request, 'app/campaigns.html', {'data': data})

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(fname=fname, lname=lname, email=email, message=message)

    return render(request, 'app/contact.html')




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
                return redirect('home')
            
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
