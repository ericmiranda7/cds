from django.shortcuts import render
from .models import Criminal
from django.http import HttpResponse

# Create your views here.
def display(request):
    criminals = Criminal.objects.all()
    return render(request, 'criminals/display.html', {'criminals': criminals})