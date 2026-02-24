from django.urls import path
from .views import home,register,login,dashboard

urlpatterns=[
    path("",home),
path("register/",register),
path("login/",login),
path("dashboard/",dashboard),
]