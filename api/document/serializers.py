from document.models import (Customer, Package, Document)
from rest_framework import serializers


# Customer serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')
        read_only_fields = ('created_by', 'created_at', 'modified_by', 'modified_at')
        lokup_value = 'customer_id'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('__all__')
        read_only_fields = ('created_by', 'created_at', 'modified_by', 'modified_at')
        lokup_value = 'document_id'


class PackageSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    document = DocumentSerializer()
    class Meta:
        model = Package
        fields = ('__all__')
        read_only_fields = ('created_by', 'created_at', 'modified_by', 'modified_at')
        lokup_value = 'package_id'