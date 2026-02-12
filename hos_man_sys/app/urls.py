from django.urls import path
from .views import home,register,login,login_validation,doctorsDashboard,patientsDashboard
urlpatterns=[
    path("",home),
    path("register/",register),
    path("login/",login),
    path("login_validation/",login_validation),
    path("doctorsDashboard/",doctorsDashboard),
    path("patientsDashboard/",patientsDashboard),
]