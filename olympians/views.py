from rest_framework import generics, permissions
from .models import Company
from .serializers import CompanySerializer


class CompanyListView(generics.ListCreateAPIView):
    queryset            = Company.objects.all()
    serializer_class    =  CompanySerializer
    permission_classes =  (permissions.AllowAny, )
    
class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset            = Company.objects.all()
    serializer_class    = CompanySerializer
    lookup_field        = 'pk'
    permission_classes = (permissions.AllowAny, )







