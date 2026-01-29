from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .models import Employees
# Create your views here.
def home(request):
    return HttpResponse("home view")


@api_view(["POST"])
def add_employee(request):
    n=request.data.get("name")
    a=request.data.get("age")
    e=request.data.get("email")
    d=request.data.get("dept")
    s=request.data.get("salary")
    Employees.objects.create(name=n,age=a,email=e,dept=d,sal=s)
    return HttpResponse("added emp successfully....")

@api_view(["GET"])
def get_employees(request):
    allEmpData=Employees.objects.all().values()
    return Response({"employees":allEmpData})

@api_view(["GET"])
def get_employee(req):
    singleEmpData=Employees.objects.get(id=1)
    return Response({"employees":model_to_dict(singleEmpData)})

@api_view(["PUT"])
def update_employee(request,__id):
    n=request.data.get("name")
    a=request.data.get("age")
    e=request.data.get("email")
    d=request.data.get("dept")
    s=request.data.get("salary")

    emp=Employees.objects.get(id=__id)
    emp.name=n
    emp.age=a 
    emp.email=e
    emp.dept =d 
    emp.sal =s 
    emp.save()
    return Response(f"emp who is having id number {__id} got updated ")   
#  pip install djnagorestframework

@api_view(["DELETE"])
def delete_employee(request,__id):
    e=Employees.objects.get(id=__id)
    e.delete()
    return Response(f"emp who is having id number {__id} got deleted ")  

