from django.urls import path
from .views import home,about,contact
urlpatterns = [
    path("",home),
    path("about/",about),
    path("contact/",contact)
    ]

    # http://127.0.0.1:8000/
    # http://127.0.0.1:3306/
    # http://127.0.0.1:5173/