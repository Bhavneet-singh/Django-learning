from django.shortcuts import render
from .models import AppNames
from django.shortcuts import get_object_or_404

# Create your views here.

def app(request):
    apps = AppNames.objects.all()
    return render(request , 'app/app.html' , {'apps' : apps })

def app_description(request , app_id):
    app = get_object_or_404(AppNames , pk= app_id)
    return render(request , 'app/app_description.html' , {'app': app})


