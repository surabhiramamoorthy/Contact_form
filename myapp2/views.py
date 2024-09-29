from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def showlist(request):
    fruits=["Mango","Apple","Banana","Jackfruit"]
    student_names=["Tony","Sony","Mony","Bob"]
    return render(request, 'showlist.html', {"fruits": fruits, "student_names": student_names})

def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')

