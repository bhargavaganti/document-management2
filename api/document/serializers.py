from document.models import (Customer, Package, Document)
from rest_framework import serializers

# Document serializer 
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('__all__')
        read_only_fields = ('created_by', 'created_at', 'modified_by', 'modified_at')
        lokup_value = 'document_id'


class PackageSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField(many = False, read_only = False, queryset = Customer.objects.all())
    package_documents = DocumentSerializer(many = True)
    class Meta:
        model = Package
        fields = ('__all__')
        read_only_fields = ('created_by', 'created_at', 'modified_by', 'modified_at')
        lokup_value = 'package_id'

# Customer serializer - general purpose - will be removed/rewritten
class CustomerSerializer(serializers.ModelSerializer):
    customer_packages = PackageSerializer(many = True)
    class Meta:
        model = Customer
        fields = ('customer_id', 'first_name', 'last_name', 'title', 'email', 
        'created_by', 'created_at', 'modified_by','customer_packages')
        read_only_fields = ('created_by', 'created_at', 'modified_by', 'modified_at')
        lokup_value = 'customer_id'


