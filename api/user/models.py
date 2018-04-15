from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
import uuid
from api.settings import ORG_USER_TYPES

# Create your models here.

# Custom user manager extending the BaseUserManager class
class UserManager(BaseUserManager):
    # Customizing the create_user() method
    def create_user(self, email, first_name, last_name, org_role, password=None, **kwargs):
    # Force email
        if not email:
            raise ValueError('email is required field')
    # Force organizational role
        if not org_role:
            raise ValueError('org_role is required field')
     # Force first_name
        if not first_name:
            raise ValueError('first_name is required field')
    # Force last_name
        if not last_name:
            raise ValueError('last_name is required field')
    
        user = self.model(
                email = self.normalize_email(email),
                org_role = self.org_role,
                first_name = self.first_name,
                last_name = self.last_name
                )
                
        user.set_password(password)
        user.save(using=self._db)
    
        return user
    
    # Skipping create_supeuser for now
    def create_superuser(self, first_name, last_name, email, org_role, password=None, **kwargs):
        pass



# Custom user model extending the AbstractBaseUser class
class User(AbstractBaseUser):
    user_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    email = models.EmailField(verbose_name = 'email address', max_length = 255, unique = True)
    first_name = models.CharField(verbose_name = 'first name', max_length = 255, blank = False)
    last_name = models.CharField(verbose_name = 'last name', max_length = 255, blank = False)
    org_role = models.CharField(max_length = 2, choices = ORG_USER_TYPES)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'org_role']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email