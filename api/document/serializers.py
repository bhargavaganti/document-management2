from document.models import (Customer, Package, Document)
from rest_framework import serializers


# Customer serializer - general purpose - will be removed/rewritten
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')
        read_only_fields = ('created_by', 'created_at', 'modified_by', 'modified_at')
        lokup_value = 'customer_id'

class CustomerReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('title', 'first_name', 'last_name', 'email')
        read_only_fields = ( 'title', 'first_name', 'last_name','email')
        lookup_value = 'customer_id'



class DocumentSerializer(serializers.ModelSerializer):
    package = serializers.PrimaryKeyRelatedField(many = False, read_only = True)
    class Meta:
        model = Document
        fields = ('__all__')
        read_only_fields = ('created_by', 'created_at', 'modified_by', 'modified_at')
        lokup_value = 'document_id'


class PackageSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(many = False, read_only = False, queryset = Customer.objects.all())
    documents = DocumentSerializer()
    class Meta:
        model = Package
        fields = ('package_documents', 'owner', 'documents', )
        read_only_fields = ('created_by', 'created_at', 'modified_by', 'modified_at')
        lokup_value = 'package_id'
