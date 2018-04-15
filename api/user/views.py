from django.shortcuts import render
from user.models import User
from rest_framework import viewsets
from user.serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('user_id')
    serializer_class = UserSerializer
