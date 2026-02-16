from django.urls import path
from .views import home,register,login,login_validation,doctorsDashboard,patientsDashboard
urlpatterns=[
    path("",home),
    path("register/",register),
    path("login/",login),
    path("login_validation/",login_validation),
    path("doctorsDashboard/<int:id>/" ,doctorsDashboard),
    path("doctorsDashboard/<int:id>/appointments" ,doctorsDashboard),
    path("doctorsDashboard/<int:id>/profile" ,doctorsDashboard),
    path("patientsDashboard/<int:id>/" ,patientsDashboard),
    path("patientsDashboard/<int:id>/appointments" ,patientsDashboard),
    path("patientsDashboard/<int:id>/profile" ,patientsDashboard)
]