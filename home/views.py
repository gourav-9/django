from django.shortcuts import render , HttpResponse
from home.models import Contact
    # Create your views here.
def home(request):
    if request.method== "POST":
       name= request.POST.get("name")
       email= request.POST.get("email")
       desc= request.POST.get("desc")
       phone= request.POST.get("phone")
       contact =Contact(name=name,email=email,desc=desc,phone=phone)
       contact.save()
    context={
    "variable": "Welcome in Techno Master GS"
     }
    return render(request,"index.html",context)