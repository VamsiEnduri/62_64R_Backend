from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # logic to retrieve model data
    return HttpResponse("this is home view")