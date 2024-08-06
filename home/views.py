from django.shortcuts import render, HttpResponse
from django.contrib import messages

# Create your views here.

def about(request):
    return render(request, 'about.html')

def error(request):
    return render(request, 'error.html')

def welcome(request):
    return render(request,'welcome.html')

def signup_page(request):
    return render(request, 'signup_page.html')

def signaction(request):
    return render(request,'signup_page.html')

def my_maps(request):
    return render(request, 'my_maps.html')