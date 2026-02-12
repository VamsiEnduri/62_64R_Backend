from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Doctor,Patient
# Create your views here.
def home(req):
    return render(req,"registration.html")

   
def patientsDashboard(req):
    c={
        "name":"ramya"
    }
    return render(req,"patientsDashboard.html",c)
   
def doctorsDashboard(req):
    c={
        "name":"ramya"
    }
    return render(req,"DoctorsDashboard.html")


@api_view(["POST"])
def login_validation(req):
    e=req.data.get("e")
    p=req.data.get("p")
    r=req.data.get("r")
    drs=Doctor.objects.all().values()
    pts=Patient.objects.all().values()
    for j in pts:
        if j["email"] == e and j["password"]  == p:
            if  r == "Patient" : 
                return Response({"msg":"login successful patient","r_url":"patientsDashboard"})
        else:
            continue

    for i in drs: #10
        print(type(i))
        if i["email"] == e and i["password"]  == p:
            if  r == "Doctor" : 
                return Response({"msg":"login successful doctor","r_url":"doctorsDashboard"})
        else:
            continue
    return Response({"d":drs})


@api_view(["GET"])
def login(req):
    return render(req,"login.html")


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