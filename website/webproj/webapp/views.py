from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'webapp/homepage.html')

def pic1(request):
    return render(request,'webapp/pic1.html')

def pic2(request):
    return render(request,'webapp/pic2.html')

def pic3(request):
    return render(request,'webapp/pic3.html')
