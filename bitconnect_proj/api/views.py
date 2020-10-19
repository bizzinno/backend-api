from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from social_django.utils import psa
from rest_framework import serializers,status
 
from google.oauth2 import id_token
from google.auth.transport import requests

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS



@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def index(request):
    print("This will be accesible to a authenticated user")