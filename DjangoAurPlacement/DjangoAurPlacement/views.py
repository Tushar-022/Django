from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Today is monday")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("Hare Rama")

def contact(request):
    return HttpResponse("Lets call")