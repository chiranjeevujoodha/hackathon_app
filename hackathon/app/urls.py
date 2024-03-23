from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from app.views import *


urlpatterns = [
    
    path('', views.campaigns, name='home'),
    path('campaigns/', views.campaigns, name='campaigns'),
    path('campaignform/', views.campaignform, name='campaignform'),
    path('add/', views.add_campaign, name='add_campaign'),
    path('update/<id>', views.update_campaign, name='update_campaign'),
    path('delete/<id>', views.delete_campaign, name='delete_campaign'),
    path('contact/', views.contact, name='contact'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)