from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import *



#Register User

class CreateUserForm(UserCreationForm):
    ngo_name = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'ngo_name', 'email']



# login User
        
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = ['name', 'organisor', 'location', 'date', 'description']