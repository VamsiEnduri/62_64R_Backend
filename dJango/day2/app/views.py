from django.shortcuts import render
# from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def home(request):
    return HttpResponse("home view")

# def about(request):
#     return HttpResponse("about view")

# def contact(req):
#     return HttpResponse("contact view")



# def about(request):
#     return JsonResponse({"name":"vamsi","exp":4.5,"role":"python full stack trainer"})

# def contact(req):
#     return JsonResponse({"contact":'1234567890'})


def about(request):
    return render(request,"about.html")

def contact(req):
    return render(req,"contact.html") # 2 values