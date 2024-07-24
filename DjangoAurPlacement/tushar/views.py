from django.shortcuts import render
from .models import ChaiVariety
from .forms import ChaiVarietyForm


def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'tushar/all_chai.html', {'chais': chais})

def store_view(request):
    return render(request,'tushar/chai_stores.html')
