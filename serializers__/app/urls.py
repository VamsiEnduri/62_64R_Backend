from django.urls import path
from .views import home,add_employee,get_employees,delete_employee,update_employee
urlpatterns=[
    path("",home),
    path("add_employee/",add_employee),
    path("get_employees/",get_employees),
    path("delete_employee/<int:id>/" ,delete_employee),
    path("update_employee/<int:id>/",update_employee)
]