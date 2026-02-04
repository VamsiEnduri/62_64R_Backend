# with searlizers  
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import EmpSerializers
from .models import Employees


@api_view(["GET"])
def get_employees(req):
    e=Employees.objects.all() #modal 
    e1=EmpSerializers(e,many=True) #model --> json#entire json data (emps model)
    return Response(e1.data) #response

@api_view(["POST"])
def add_employee(req):
    e=EmpSerializers(data=req.data)
    if e.is_valid():    #auto validation
        e.save() # auto  creation of modal object
        return Response(e.data)
    return Response(e.errors) # auto validation fails, then error    

















# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.forms.models import model_to_dict
# from .models import Employees
# # Create your views here.
# def home(req):
#     return render(req,"home.html")

# @api_view(["PUT"])
# def update_emp(req,__id):
#     n=req.data.get("name")    
#     a=req.data.get("age")    
#     e=req.data.get("email")    
#     d=req.data.get("dept")   
#     emp=Employees.objects.get(id=__id) 
#     emp.name=n 
#     emp.age=a 
#     emp.email=e
#     emp.dept=d 
#     emp.save()

#     return Response(f"{__id} id emp iupdated successfully")

# @api_view(["DELETE"])
# def delete_emp(req,__id):
#     e= Employees.objects.get(id=__id)
#     e.delete()
#     return Response(f"{__id} id emp delted successfully....")

# @api_view(["GET"])
# def get_employees(req):
#     data=Employees.objects.all().values()
#     # print(data,"data")
#     dataAfterProcessing=[]
#     for i in data:
#         dataAfterProcessing.append(i)
#         # print(,"emp")
#     return Response({"msg":"fetched all data","data":dataAfterProcessing})

# @api_view(["POST"])
# def add_employee(req):
#     n=req.data.get("name")
#     a=req.data.get("age")
#     e=req.data.get("email")
#     d=req.data.get("dept")

#     Employees.objects.create(name=n,age=a,email=e,dept=d)
#     # data=Employees.objects.all()
#     return    Response({"msg":"emp added successfully"})






