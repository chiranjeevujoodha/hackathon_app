from rest_framework import serializers
from .models import *

class CampaignSerializer( serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['id', 'name','organisor','location','date','description']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id','fname', 'lname', 'email', 'message']