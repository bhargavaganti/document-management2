from django.shortcuts import render, get_object_or_404
from .models import Customer, Document, Package
from .serializers import (CustomerSerializer, DocumentSerializer, PackageSerializer)
from rest_framework import viewsets


# Create your views here.
class CustomerViewset(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    
    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user,
                                modified_by = self.request.user)

class DocumentViewset(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    
    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user,
                                modified_by = self.request.user)

class PackageViewset(viewsets.ModelViewSet):
    serializer_class = PackageSerializer
    queryset = Package.objects.all()
    
    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user,
                                modified_by = self.request.user)