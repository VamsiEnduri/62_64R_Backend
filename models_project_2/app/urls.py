from django.urls import path
from .views import home,add_employee,get_employees,get_employee,update_employee,delete_employee

urlpatterns=[
    path("",home),
    path("add_employee/",add_employee),
    path("get_employees/",get_employees),
    path("get_employees/1/",get_employee),
    path("update_employee/<int:__id>/",update_employee),
    path("delete_employee/<int:__id>/",delete_employee)
]