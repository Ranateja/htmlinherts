from django.shortcuts import render
from django.http import HttpResponse

def child(request):
    return render(request,'child.html')

# Create your views here.
