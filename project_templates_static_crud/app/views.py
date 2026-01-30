from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .models import Employees
# Create your views here.
def home(req):
    return render(req,"home.html")


@api_view(["GET"])
def get_employees(req):
    data=Employees.objects.all().values()
    # print(data,"data")
    dataAfterProcessing=[]
    for i in data:
        dataAfterProcessing.append(i)
        # print(,"emp")
    return Response({"msg":"fetched all data","data":dataAfterProcessing})

@api_view(["POST"])
def add_employee(req):
    n=req.data.get("name")
    a=req.data.get("age")
    e=req.data.get("email")
    d=req.data.get("dept")

    Employees.objects.create(name=n,age=a,email=e,dept=d)
    # data=Employees.objects.all()
    return    Response({"msg":"emp added successfully"})