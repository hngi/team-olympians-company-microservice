from django.utils import timezone
from rest_framework import serializers
from .models import Company



class CompanySerializer(serializers.ModelSerializer):
    url             = serializers.HyperlinkedIdentityField(
                            view_name='detail',
                            lookup_field='pk'
                            )
    
    class Meta:
        model = Company
        fields = [
                'url',
                'pk',
                'company_name',
                'company_email',
                'company_address',
                'company_description',
                'company_logo',                     
        ]
