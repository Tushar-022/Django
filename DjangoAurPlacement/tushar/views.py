from django.shortcuts import render
from .models import ChaiVariety

def all_mondays(request):
    return render(request, 'tushar/all_chai.html')

def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'tushar/all_chai.html', {'chais': chais})
