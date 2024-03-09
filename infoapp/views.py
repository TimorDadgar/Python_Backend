from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    response = HttpResponse(calculate_ur_mom())
    response.write("kg yo mama")
    return response 

def calculate_ur_mom():
    return 10+100

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")