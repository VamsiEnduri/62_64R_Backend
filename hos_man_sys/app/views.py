from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Doctor,Patient
# Create your views here.
def home(req):
    return render(req,"registration.html")

@api_view(["POST"])
def register(req):
    n=req.data.get("n")
    e=req.data.get("e")
    ph=req.data.get("ph")
    p=req.data.get("p")
    cp=req.data.get("cp")
    r=req.data.get("r")
    if p == cp:
        if r == "Doctor":
            Doctor.objects.create(name=n,email=e,phNum=ph,password=p,c_password=cp,role=r)
            return Response({"msg":"doctor added successfully ","d_name":n})
        
        if r == "Patient":
            Patient.objects.create(name=n,email=e,phNum=ph,password=p,c_password=cp,role=r)
            return Response({"msg":"patient added successfully ","p_name":n})

    else:
        return Response("p and cp are not matched")   
    return Response("register")