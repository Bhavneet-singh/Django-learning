from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World")
    return render(request , 'website/index.html')

def about(request):
    # return HttpResponse("Hello World this is request")
    return render(request , 'website/about.html')

def contact(request):
    # return HttpResponse("Hello World this is contact ")
    return render(request , 'website/contact.html')
