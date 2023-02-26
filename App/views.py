from django.shortcuts import render

def home(request):
    return  render(request,'Home.html')

def package(request):
    return  render(request,'Package.html')

def about(request):
    return  render(request,'About.html')

def contact(request):
    return  render(request,'Contact.html')

def packkage1(request):
    return render(request, 'Pk1.html')

def packkage2(request):
    return render(request, 'Pk2.html')

def packkage3(request):
    return render(request, 'Pk3.html')
