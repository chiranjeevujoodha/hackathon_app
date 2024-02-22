from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from app.views import *


urlpatterns = [
    
    # path('', views.home, name='home'),
    # path('api/', ContactView.as_view(), name='api'),
    # path('campaigns/', views.campaigns, name='campaigns'),
    # path('contact/', views.contact, name='contact'),
    # path('signin/', views.signin, name='signin'),
    # path('signup/', views.signup, name='signup'),
    # path('signout/', views.signout, name='signout'),
    path('api/campaigns/', views.add_campaign, name='add_campaign'),
    path('api/campaigns/all', views.get_campaigns, name='get_campaigns'),
    path('api/contacts/', views.add_contact, name='add_contact'),
    path('api/contacts/all', views.get_contacts, name='get_contacts'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)