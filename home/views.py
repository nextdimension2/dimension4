from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from home.models import Apply
from home.models import Data

# Create your views here.
def index(request):
    return render (request,'index.html')

def services(request):
    return render (request,'Services.html')   

def about(request):
    return render (request,'about.html')

def gallery(request):
    return render (request,'gallery.html')   

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')
        contact=Contact(name=name, email=email, subject=subject, desc=desc, date=datetime.today())
        contact.save()
    return render (request,'contact.html')    

 

def bb(request):
    return render (request,'bb.html')   

def get(request):
    return render (request,'get.html')           

def apply(request):
  
  
  return render(request,"apply.html")  