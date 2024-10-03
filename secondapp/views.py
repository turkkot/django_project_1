from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def colors(request):
    return HttpResponse('red, green, blue')

def shapes(request):
    return HttpResponse('sphere, cube, pyramid')

def size(request):
    return HttpResponse('small, medium, big')