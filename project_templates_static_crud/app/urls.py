from django.urls import path
from .views import home,add_employee,get_employees

urlpatterns=[
    path("",home),
    path("add_employee/",add_employee),
    path("get_employees/",get_employees)
]