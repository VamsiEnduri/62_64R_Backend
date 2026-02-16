from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Doctor,Patient
# Create your views here.
def home(req):
    return render(req,"registration.html")


def patientsDashboard(req,id):
    patient=Patient.objects.get(id=id) # obj :-- .
    if "appointments" in req.path:
        template="patientsAppointments.html"
    elif "profile" in req.path:
        template="patientsProfile.html"
    else:
        template="patientsDashboard.html"
    return render(req,template,{"user":patient})

def doctorsDashboard(req,id):
    doctor=Doctor.objects.get(id=id) # obj :-- .
    if "appointments" in req.path:
        template="doctorsAppointments.html"
    elif "profile" in req.path:
        template="doctorsProfile.html"
    else:
        template="DoctorsDashboard.html"
    return render(req,template,{"user":doctor})


@api_view(["POST"])
def login_validation(req):
    e=req.data.get("e")
    p=req.data.get("p")
    r=req.data.get("r")
    drs=Doctor.objects.all().values()
    pts=Patient.objects.all().values()
    
    if r == "Doctor":
        print("vamsi     aaaa")
        for i in drs:
            if i["email"] == e and i["password"] == p:
                return Response({"msg":"doctor login done","r_url":"doctorsDashboard","id":i["id"],"role":i["role"]})
    elif r == "Patient":
        for i in pts:
            if i["email"] == e and i["password"] == p:
                return Response({"msg":"patient login done","r_url":"patientsDashboard","id":i["id"],"role":i["role"]})
    else:
        return Response("role doesnt exist")        


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