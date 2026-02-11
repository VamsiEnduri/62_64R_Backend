from django.urls import path
from .views import home,register
urlpatterns=[
    path("",home),
    path("register/",register)
]