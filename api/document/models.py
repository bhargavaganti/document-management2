from django.db import models
import uuid
from datetime import datetime
from api.settings import (ORG_USER_TYPES, DOC_STATUS, DOC_TYPES, PACKAGE_TYPES, PACKAGE_STATUS, TITLE)
from api.settings import AUTH_USER_MODEL as User

# Create your models here.


# Need to set up a custom manager model here to ensure that package, user and document
# are all created at the same time

# Table of customers
class Customer(models.Model):
    customer_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    first_name = models.CharField(max_length = 128, blank = False)
    last_name = models.CharField(max_length = 128, blank = False)
    title = models.CharField(max_length = 2, choices = TITLE)
    email = models.EmailField(max_length = 96, blank = False, unique = True)
    # phone = models.CharField()
    # cnp = models.CharField()
    created_by = models.ForeignKey(User, editable = False, on_delete = models.CASCADE, related_name = 'customers_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, editable = False, blank = True, on_delete = models.CASCADE, related_name = 'customers_updated_by')
    # modified_at = 
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

# Document package model to have a 1-to-1 relationship with customer and 1-to-many relationship with document
class Package(models.Model):
    pack_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    pack_type = models.CharField(max_length = 2, choices = PACKAGE_TYPES)
    created_by = models.ForeignKey(User, editable = False, on_delete = models.CASCADE, related_name = 'packages_created_by')
    created_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, editable = False, blank = True, on_delete = models.CASCADE, related_name = 'packages_updated_by')
    # modified_at = 
    pack_status = models.CharField(max_length = 2, choices = PACKAGE_STATUS, default = PACKAGE_STATUS[0])
    owner = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'customer_packages')
    comments = models.TextField()
    
    def __str__(self):
        return '%s %s' % (self.owner, self.owner)

# Document model
class Document(models.Model):
    doc_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    doc_type = models.CharField(max_length = 2, choices = DOC_TYPES)
    created_by = models.ForeignKey(User, editable = False, on_delete = models.CASCADE, related_name = 'documents_created_by')
    created_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, editable = False, blank = True, on_delete = models.CASCADE, related_name = 'documents_updated_by')
    # modified_at =
    doc_status = models.CharField(max_length = 2, choices = DOC_STATUS, default = DOC_STATUS[0])
    owner = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'customer_documents')
    package = models.ForeignKey(Package, on_delete = models.CASCADE, related_name = 'package_documents')
    comments = models.TextField()
    
    def __str__(self):
        return '%s %s' % (self.owner, self.doc_type)