from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def home(req):
    return HttpResponse("home view")

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard(req):
    return Response({"msg":'dashboard'})

@api_view(["POST"])
def login(req):
    username=req.data.get("username")    
    password=req.data.get("password")

    if  not username or not password:
        return Response({"msg":"all fields are required"}) 

    user=authenticate(username=username,password=password)

    if user:
        at=AccessToken.for_user(user)
        print(at)
        return Response({"token":str(at)})
    else:
        return Response("user not found")
    # return Response({"user":list(user)})   


@api_view(["POST"])
def register(req):
    username=req.data.get("username") # ""    
    password=req.data.get("password") # ""

    if  not username or not password:
        return Response({"msg":"all fields are required"})


    if User.objects.filter(username=username).exists():
        return Response({"res":"user already exists"})


    User.objects.create_user(
        username=username,
        password=password
    )    

    return Response({"msg":"user registered successfully..."})    

