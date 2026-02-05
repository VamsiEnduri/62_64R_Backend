from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .serializers import EmployeesSerializer
from .models import Employees
# Create your views here.
def home(req):
    return HttpResponse("home view")


@api_view(["PUT"])
def update_employee(req,id):
    e=Employees.objects.get(id=id)
    e1=EmployeesSerializer(e,data=req.data)
    if e1.is_valid():
        e1.save()
        return Response("updated")
    return Response(e1.errors)   



@api_view(["DELETE"])
def delete_employee(req,id):
    e=Employees.objects.get(id=id)
    e.delete()
    return Response("dltd")

@api_view(["GET"])
def get_employees(req):
    e=Employees.objects.all()   
    e1=EmployeesSerializer(e,many=True)
    return Response(e1.data)


@api_view(["POST"])    
def add_employee(req):
    e=EmployeesSerializer(data=req.data)
    if e.is_valid():
        e.save()
        return Response("emp added")
    return Response(e.errors)    