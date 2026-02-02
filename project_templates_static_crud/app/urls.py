from django.urls import path
from .views import home,add_employee,get_employees,delete_emp,update_emp

urlpatterns=[
    path("",home),
    path("add_employee/",add_employee),
    path("get_employees/",get_employees),
    path("delete_emp/<int:__id>/",delete_emp),
    path("update_emp/<int:__id>/",update_emp)
]